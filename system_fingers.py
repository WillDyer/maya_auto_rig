import importlib
import maya.cmds as cmds

import config
import OPM

importlib.reload(config)
importlib.reload(OPM)

class create_fingers():
    def __init__(self):
        self.ui_data = config.ui_data
        self.system_joints = config.system_joints

        self.ctrl_finger_dict = {}
        
        self.create_controls()
        print(self.ctrl_finger_dict)


    def create_controls(self):
        ctrl_list = []

        for x in self.ui_data.keys():
            if self.ui_data[x][4] == "arm":
                cmds.group(n=f"grp_ctrl_fingers{self.system_joints[x][-1][7:]}",em=True)
                end_joint_arm = self.system_joints[x][-1][7:]
                top_joint_arm = self.system_joints[x][0][7:]
                cmds.matchTransform(f"grp_ctrl_fingers{self.system_joints[x][-1][7:]}",self.system_joints[x][-1])
                
                finger_joints = cmds.listRelatives(self.system_joints[x][-1],ad=True, typ='joint')
                
                for joint in finger_joints:
                    cmds.circle(n=f"ctrl_fk{joint[7:]}",r=1,nr=(1,0,0))
                    cmds.matchTransform(f"ctrl_fk{joint[7:]}",joint)
                    
                    ctrl = f"ctrl_fk{joint[7:]}"
                    ctrl_list.append(ctrl)
                    
                    self.ctrl_finger_dict |= {f"{ctrl.split('_')[2]}{ctrl[-2:]}": []}

                for ctrl in ctrl_list:
                    for key in self.ctrl_finger_dict.keys():
                        if key == f"{ctrl.split('_')[2]}{ctrl[-2:]}":
                            self.ctrl_finger_dict[key].append(ctrl)
                        else:
                            pass

                self.child_parent_setup()
                self.parent_constranit()
                self.parent_back_to_heirachy(end_joint_arm,top_joint_arm)
                self.offset_parent_matrix()
            
            self.ctrl_finger_dict = {}
        


    def child_parent_setup(self):
        for key in self.ctrl_finger_dict.keys():
            for item in range(len(self.ctrl_finger_dict[key])):
                try:
                    child = self.ctrl_finger_dict[key][item]
                    parent = self.ctrl_finger_dict[key][item+1]
                    cmds.parent(child, parent)
                except IndexError:
                    pass

    def parent_constranit(self):
        for key in self.ctrl_finger_dict.keys():
            for item in self.ctrl_finger_dict[key]:
                cmds.parentConstraint(item, f"jnt_rig{item[7:]}")

    def offset_parent_matrix(self):
        for key in self.ctrl_finger_dict.keys():
            for item in self.ctrl_finger_dict[key]:
                cmds.select(item)
                OPM.offsetParentMatrix()

    def parent_back_to_heirachy(self, end_joint_arm, top_joint_arm):
        for key in self.ctrl_finger_dict.keys():
            cmds.parent(self.ctrl_finger_dict[key][-1], f"grp_ctrl_fingers{end_joint_arm}")
        cmds.parent(f"grp_ctrl_fingers{end_joint_arm}", "grp_clav_rotate")
        cmds.parentConstraint(f"ctrl_fk{end_joint_arm}", f"ctrl_ik{end_joint_arm}", f"grp_ctrl_fingers{end_joint_arm}",n=f"pConst_grp_ctrl_fingers{end_joint_arm}")
        cmds.connectAttr(f"ctrl_COG.ikfk_switch{top_joint_arm}",f"pConst_grp_ctrl_fingers{end_joint_arm}.ctrl_fk{end_joint_arm}W0")
        cmds.connectAttr(f"{top_joint_arm[1:]}_ikfk_reverse.outputX",f"pConst_grp_ctrl_fingers{end_joint_arm}.ctrl_ik{end_joint_arm}W1")
        

#create_fingers()