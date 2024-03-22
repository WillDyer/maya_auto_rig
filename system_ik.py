import importlib
import maya.cmds as cmds
import config
import OPM
import system_get_file_location
import system_polevector

importlib.reload(config)
importlib.reload(OPM)
importlib.reload(system_polevector)

class create_ik_system():
    def __init__(self):
        self.ui_data = config.ui_data
        self.system_joints = config.system_joints
        self.all_ctrls_ik = []
        print(f"UIDAATA: {self.ui_data}")

        self.ik_system()
        #self.system_to_heirachy()

    def ctrls_ik_to_heirachy(self,x, ctrls_ik):
        for item in ctrls_ik: # eventually ik spine will be added here
            try:
                if self.ui_data[x][2] == "arm":
                    cmds.parent(f"ctrl_ik{item[6:]}", "grp_ik_arm")
                elif self.ui_data[x][2] == "leg":
                    cmds.parent(f"ctrl_ik{item[6:]}", "grp_ik_leg")
            except ValueError:
                pass
            

    def ik_system(self):
        for x in self.system_joints.keys(): #runs the parent system for each join system in the ui data
            ctrls_ik = []
            all_ctrls_ik = []
            #print(len(self.system_joints[x]))             
            if len(self.system_joints[x]) == 4:
                ui = self.ui_data # temp whilst i work on rest of script
                top = self.system_joints[x][-1] # temp whilst i work on rest of script
                # print("4 joints in system presuming clavicles included")
                if self.ui_data[top][2] == "arm":
                    start_joint = "jnt_ik" + self.system_joints[x][2][7:]
                    end_joint = "jnt_ik" + self.system_joints[x][0][7:]
                    pv_joint = "jnt_ik" + self.system_joints[x][1][7:]
                    ctrls_ik = ["jnt_ik" + self.system_joints[x][-1][7:], start_joint, end_joint]
                elif self.ui_data[top][2] == "leg":
                    start_joint = "jnt_ik" + self.system_joints[x][2][7:]
                    end_joint = "jnt_ik" + self.system_joints[x][0][7:]
                    pv_joint = "jnt_ik" + self.system_joints[x][1][7:]
                    ctrls_ik = ["jnt_ik" + self.system_joints[x][-1][7:], start_joint, end_joint]
                # print(f"start joint: {start_joint}, end joint: {end_joint}")
                
            elif len(self.system_joints[x]) == 3:
                ui = self.ui_data # temp whilst i work on rest of script
                top = self.system_joints[x][-1] # temp whilst i work on rest of script
                # print("3 joints in system presuming clavicles not included")
                start_joint = "jnt_ik" + self.system_joints[x][2][7:]
                end_joint = "jnt_ik" + self.system_joints[x][0][7:]
                pv_joint = "jnt_ik" + self.system_joints[x][1][7:]
                ctrls_ik = [start_joint, end_joint]
                
            elif len(self.system_joints[x]) < 3:
                cmds.error("less than 3 joints in system cant create IK sys")

            cmds.ikHandle(n=f"hdl_ik_{end_joint[7:]}", solver="ikRPsolver", sj=start_joint, ee=end_joint)


            ik_handle_name = f"hdl_ik_{end_joint[7:]}"
            all_ctrls_ik.append(ctrls_ik)
            self.create_ctrl(ctrls_ik)
            self.ctrls_ik_to_heirachy(x, ctrls_ik)
            pv_ctrl = self.create_polevector(ui,top ,pv_joint, end_joint)
            self.offset_parent_matrix(all_ctrls_ik)

            self.ik_system_to_joint(all_ctrls_ik, end_joint)
            self.populate_to_group(top, x, pv_ctrl, ctrls_ik, ik_handle_name)
            cmds.select(x)

    def system_to_heirachy(self):
        for item in self.system_joints.keys():
            cmds.parent(f"jnt_ik{item[7:]}","grp_ik_joints")
    
    def create_ctrl(self, ctrls_ik):
        for i in range(len(ctrls_ik)): #runs the parent system for each joint in joint heirachy    
            cmds.circle(n=f"ctrl_ik_{ctrls_ik[i][7:]}",r=8,nr=(1,0,0))
            cmds.matchTransform("ctrl_ik_" + ctrls_ik[i][7:],ctrls_ik[i])

    def ik_system_to_joint(self, all_ctrls_ik, end_joint):
        #print(all_ctrls_ik[0])
        for item in range(len(all_ctrls_ik[0])):
            #print(all_ctrls_ik[0][item])
            if all_ctrls_ik[0][item] == end_joint:
                cmds.parentConstraint("ctrl_ik_" + all_ctrls_ik[0][item][7:], "hdl_ik_" + all_ctrls_ik[0][item][7:],n="pConst_" + all_ctrls_ik[0][item][7:],mo=True)
            else:
                cmds.parentConstraint("ctrl_ik_" + all_ctrls_ik[0][item][7:], "jnt_ik_" + all_ctrls_ik[0][item][7:],n="pConst_" + all_ctrls_ik[0][item][7:],mo=True)

    def create_polevector(self, ui, top, pv_joint, end_joint):
        path = system_get_file_location.get_loc()
        CURVE_FILE = path + "/file_imports/ctrl_square.abc"
        try:
            cmds.file(CURVE_FILE, i=True)
        except RuntimeError:
            cmds.spaceLocator(n="ctrl_square")
        pv = "ctrl_square"
        system_polevector.get_pole_vector_position(top, pv_joint, end_joint, pv)
        cmds.rename("ctrl_square","ctrl_pv_" + pv_joint[7:])
        cmds.select("ctrl_pv_" + pv_joint[7:])
        OPM.offsetParentMatrix()
        cmds.poleVectorConstraint("ctrl_pv_" + pv_joint[7:], "hdl_ik_" + end_joint[7:], n="pvConst_" + pv_joint[7:])
        
        pv_joint_loc = cmds.xform(pv_joint,q=1,ws=1,rp=1)
        ctrl_pv_loc = cmds.xform("ctrl_pv_" + pv_joint[7:],q=1,ws=1,rp=1)
        cmds.curve( d=1, p=[pv_joint_loc, ctrl_pv_loc], n="pv_curve_" + pv_joint[7:])
        cmds.cluster("pv_curve_" + pv_joint[7:] + ".cv[0]", n="cluster_pv_" + pv_joint[7:] + "_cv0")
        cmds.cluster("pv_curve_" + pv_joint[7:] + ".cv[1]", n="cluster_pv_" + pv_joint[7:] + "_cv1")
        cmds.parent("cluster_pv_" + pv_joint[7:] + "_cv0Handle", pv_joint)
        cmds.parent("cluster_pv_" + pv_joint[7:] + "_cv1Handle", "ctrl_pv_" + pv_joint[7:])
        for x in cmds.ls(typ="cluster"):
            cmds.hide(x+"Handle")
        cmds.setAttr("pv_curve_" + pv_joint[7:] + ".template", 1)

        return "ctrl_pv_" + pv_joint[7:]

    def offset_parent_matrix(self, all_ctrls_ik):
        for ctrl in all_ctrls_ik[0]:
            cmds.select("ctrl_ik" + ctrl[6:])
            OPM.offsetParentMatrix()

    def populate_to_group(self, top, x, pv_ctrl, ctrls_ik, ik_handle_name):
        cmds.group(n=f"autorig_ik_{self.ui_data[top][2]}{x[7:]}",w=True,em=True)
        cmds.group(f"jnt_ik{x[7:]}", n=f"ik_joints{x[7:]}",p=f"autorig_ik_{self.ui_data[top][2]}{x[7:]}")
        cmds.group(ik_handle_name, n=f"ik_hdl{x[7:]}",p=f"autorig_ik_{self.ui_data[top][2]}{x[7:]}")
        cmds.group(f"pv_curve{pv_ctrl[7:]}",n=f"ik_misc{x[7:]}",p=f"autorig_ik_{self.ui_data[top][2]}{x[7:]}")
        cmds.group(pv_ctrl, n=f"ik_controls{x[7:]}",p=f"autorig_ik_{self.ui_data[top][2]}{x[7:]}")
        for ctrl in ctrls_ik:
            cmds.parent(f"ctrl_ik_{ctrl[7:]}",f"ik_controls{x[7:]}")
                
                     
#create_ik_system()