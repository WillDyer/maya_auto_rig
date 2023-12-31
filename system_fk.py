import importlib
import maya.cmds as cmds
import config
import OPM

importlib.reload(config)
importlib.reload(OPM)

class create_fk_system():
    def __init__(self):
        self.ui_data = config.ui_data
        self.system_joints = config.system_joints
        self.fk_ctrls = []
        self.all_fk_ctrls = []
        
        self.fk_system()
        self.fk_system_to_joint()
        self.system_to_heirachy()

    def fk_system(self):
        for x in self.system_joints.keys(): #runs the parent system for each join system in the ui data
                self.fk_ctrls = []
                for i in range(len(self.system_joints[x])): #runs the parent system for each joint in joint heirachy
                    cmds.circle(n=f"fk_ctrl{self.system_joints[x][i][7:]}",r=8,nr=(1,0,0))
                    cmds.matchTransform(f"fk_ctrl{self.system_joints[x][i][7:]}",self.system_joints[x][i])
                    self.fk_ctrls.append(f"fk_ctrl{self.system_joints[x][i][7:]}")
                    self.all_fk_ctrls.append(f"fk_ctrl{self.system_joints[x][i][7:]}")
                #print(self.all_fk_ctrls)

                for ctrl in range(len(self.fk_ctrls)):
                    try:
                        cmds.parent(self.fk_ctrls[ctrl+1],self.fk_ctrls[ctrl])
                    except IndexError:
                        pass

                for ctrl in self.fk_ctrls:
                    cmds.select(ctrl)
                    OPM.offsetParentMatrix()
                     
    def fk_system_to_joint(self):
        #print(self.all_fk_ctrls)
        for item in range(len(self.all_fk_ctrls)):
            cmds.parentConstraint(self.all_fk_ctrls[item], f"fk_jnt{self.all_fk_ctrls[item][7:]}",n=f"pConst{self.all_fk_ctrls[item][7:]}")

    def system_to_heirachy(self):
        for item in self.system_joints.keys():
            cmds.parent(f"fk_jnt{item[7:]}","grp_fk_joints")
            if self.ui_data[item][4] == "arm":
                cmds.parent(f"fk_ctrl{item[7:]}","grp_fk_arm")
            if self.ui_data[item][4] == "leg":
                cmds.parent(f"fk_ctrl{item[7:]}","grp_fk_leg")
                
                     
#create_fk_system()