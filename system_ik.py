import importlib
import maya.cmds as cmds
import config
import OPM

importlib.reload(config)
importlib.reload(OPM)

def ik_handle(start_joint,end_joint):
    cmds.ikHandle(n="ikHandle_" + end_joint[7:], solver="ikRPsolver", sj=start_joint, ee=end_joint)
    cmds.parent(f"ikHandle_{end_joint[7:]}","grp_ik_handles")

def create_ctrl(ik_ctrls):
    for i in range(len(ik_ctrls)): #runs the parent system for each joint in joint heirachy    
        cmds.circle(n=f"ik_ctrl_{ik_ctrls[i][7:]}",r=8,nr=(1,0,0))
        cmds.matchTransform("ik_ctrl_" + ik_ctrls[i][7:],ik_ctrls[i])

def ik_system_to_joint(all_ik_ctrls, end_joint):
    #print(all_ik_ctrls[0])
    for item in range(len(all_ik_ctrls[0])):
        #print(all_ik_ctrls[0][item])
        if all_ik_ctrls[0][item] == end_joint:
            cmds.parentConstraint("ik_ctrl_" + all_ik_ctrls[0][item][7:], "ikHandle_" + all_ik_ctrls[0][item][7:],n="pConst_" + all_ik_ctrls[0][item][7:],mo=True)
        else:
            cmds.parentConstraint("ik_ctrl_" + all_ik_ctrls[0][item][7:], "ik_jnt_" + all_ik_ctrls[0][item][7:],n="pConst_" + all_ik_ctrls[0][item][7:],mo=True)

def create_polevector(ui, top, pv_joint, end_joint):
    try:
        cmds.file("C:\Docs\maya\2024\scripts\ctrl_square.abc", i=True)
    except RuntimeError:
        cmds.spaceLocator(n="ctrl_square")

    cmds.matchTransform("ctrl_square", pv_joint, pos=True,scl=True)
    cmds.rename("ctrl_square","pv_ctrl_" + pv_joint[7:])
    cmds.parent(f"pv_ctrl_{pv_joint[7:]}","grp_misc_ctrls")

    #print(f"pvjoint = {pv_joint}")

    if ui[top][4] == "arm": # change this from a value that is got from ui (but make ui presume arm or not)
        cmds.move(-50, "pv_ctrl_" + pv_joint[7:], ws=True, z=True)
    elif ui[top][4] == "leg":
        cmds.move(50, "pv_ctrl_" + pv_joint[7:], ws=True, z=True)
    cmds.poleVectorConstraint("pv_ctrl_" + pv_joint[7:], "ikHandle_" + end_joint[7:], n="pvConst_" + pv_joint[7:])
    
    pv_joint_loc = cmds.xform(pv_joint,q=1,ws=1,rp=1)
    pv_ctrl_loc = cmds.xform("pv_ctrl_" + pv_joint[7:],q=1,ws=1,rp=1)
    cmds.curve( d=1, p=[pv_joint_loc, pv_ctrl_loc], n="pv_curve_" + pv_joint[7:])
    cmds.cluster("pv_curve_" + pv_joint[7:] + ".cv[0]", n="pv_cluster_" + pv_joint[7:] + "_cv0")
    cmds.cluster("pv_curve_" + pv_joint[7:] + ".cv[1]", n="pv_cluster_" + pv_joint[7:] + "_cv1")
    cmds.parent("pv_cluster_" + pv_joint[7:] + "_cv0Handle", pv_joint)
    cmds.parent("pv_cluster_" + pv_joint[7:] + "_cv1Handle", "pv_ctrl_" + pv_joint[7:])
    for x in cmds.ls(typ="cluster"):
        cmds.hide(x+"Handle")
    cmds.setAttr("pv_curve_" + pv_joint[7:] + ".template", 1)
    cmds.parent(f"pv_curve_{pv_joint[7:]}","DO_NOT_TOUCH")
    return "pv_ctrl_" + pv_joint[7:]

def offset_parent_matrix(all_ik_ctrls):
    for ctrl in all_ik_ctrls[0]:
        cmds.select("ik_ctrl" + ctrl[6:])
        OPM.offsetParentMatrix()


class create_ik_system():
    def __init__(self):
        self.ui_data = config.ui_data
        self.system_joints = config.system_joints
        self.all_ik_ctrls = []
        print(f"UIDAATA: {self.ui_data}")

        self.ik_system()
        self.system_to_heirachy()

    def ik_ctrls_to_heirachy(self,x, ik_ctrls):
        for item in ik_ctrls: # eventually ik spine will be added here
            try:
                if self.ui_data[x][4] == "arm":
                    cmds.parent(f"ik_ctrl{item[6:]}", "grp_ik_arm")
                elif self.ui_data[x][4] == "leg":
                    cmds.parent(f"ik_ctrl{item[6:]}", "grp_ik_leg")
            except ValueError:
                pass
            

    def ik_system(self):
        for x in self.system_joints.keys(): #runs the parent system for each join system in the ui data
            ik_ctrls = []
            all_ik_ctrls = []
            #print(len(self.system_joints[x]))             
            if len(self.system_joints[x]) == 4:
                ui = self.ui_data # temp whilst i work on rest of script
                top = self.system_joints[x][0] # temp whilst i work on rest of script
                print("4 joints in system presuming clavicles included")
                if self.ui_data[top][4] == "arm":
                    start_joint = "ik_jnt" + self.system_joints[x][1][7:]
                    end_joint = "ik_jnt" + self.system_joints[x][3][7:]
                    pv_joint = "ik_jnt" + self.system_joints[x][2][7:]
                    ik_ctrls = ["ik_jnt" + self.system_joints[x][0][7:], start_joint, end_joint]
                elif self.ui_data[top][4] == "leg":
                    start_joint = "ik_jnt" + self.system_joints[x][0][7:]
                    end_joint = "ik_jnt" + self.system_joints[x][2][7:]
                    pv_joint = "ik_jnt" + self.system_joints[x][1][7:]
                    ik_ctrls = [start_joint, end_joint]
                ik_handle(start_joint, end_joint)
                all_ik_ctrls.append(ik_ctrls)
                create_ctrl(ik_ctrls)
                self.ik_ctrls_to_heirachy(x, ik_ctrls)
                create_polevector(ui,top ,pv_joint, end_joint)
                offset_parent_matrix(all_ik_ctrls)
                
                #print(f"SJ: {start_joint}, EJ: {end_joint}")
                
            elif len(self.system_joints[x]) == 3:
                #print("3 joints in system presuming clavicles not included")
                start_joint = "ik_jnt" + self.system_joints[x][0][7:]
                end_joint = "ik_jnt" + self.system_joints[x][2][7:]
                pv_joint = "ik_jnt" + self.system_joints[x][1][7:]
                ik_handle(start_joint, end_joint)
                ik_ctrls= [start_joint, end_joint]
                all_ik_ctrls.append(ik_ctrls)
                create_ctrl(ik_ctrls)
                ui = self.ui_data # temp whilst i work on rest of script
                top = self.system_joints[x][0] # temp whilst i work on rest of script
                create_polevector(ui, top, pv_joint, end_joint)
                offset_parent_matrix(all_ik_ctrls)

                #print(f"SJ: {start_joint}, EJ: {end_joint}")
                
            elif len(self.system_joints[x]) < 3:
                print("less than 3 joints in system cant create IK sys")

            ik_system_to_joint(all_ik_ctrls, end_joint)

    def system_to_heirachy(self):
        for item in self.system_joints.keys():
            cmds.parent(f"ik_jnt{item[7:]}","grp_ik_joints")
            #cmds.parent(f"{item[7:]}","grp_misc_ctrls")
                
                     
#create_ik_system()