import importlib

import maya.cmds as cmds
import config
importlib.reload(config)

class combine_systems():
    def __init__(self):
        self.ui_data = config.ui_data
        self.system_joints = config.system_joints

        self.setup_ikfK_switch()
        self.parent_system_to_rig()
        self.ikfk_weights()
    
    def get_top_heirachy_joint(self, joints):
        parent = None
        stop = False
        
        while not stop:
            p = cmds.listRelatives(parent or joints, parent=True)
            if p is None:
                stop = True
            else:
                parent = p[0]
            
        if parent:
            #print(f"{joints} has top-level parent {parent}")
            return parent
        else:
            #print(f"{joints} is top-level object")
            return self.joints
        
    def ikfk_weights(self):
        for key in self.system_joints.keys():
            cmds.createNode('reverse', n=f"{key[8:]}_ikfk_reverse")
            cmds.connectAttr(f"ctrl_COG.ikfk_switch_{key[8:]}", f"{key[8:]}_ikfk_reverse.inputX")
            for item in self.system_joints[key]:
                print(item)
                cmds.connectAttr(f"ctrl_COG.ikfk_switch_{key[8:]}", f"pConst{item[7:]}.jnt_fk{item[7:]}W0")
                cmds.connectAttr(f"{key[8:]}_ikfk_reverse.outputX", f"pConst{item[7:]}.jnt_ik{item[7:]}W1")

                if not cmds.ls("ctrl_ik"+item[7:]):
                    print("false")
                elif cmds.ls("ctrl_ik"+item[7:])[0] == "ctrl_ik"+item[7:]:
                    cmds.connectAttr(f"{key[8:]}_ikfk_reverse.outputX", f"ctrl_ik{item[7:]}.visibility")

                if not cmds.ls("ctrl_fk"+item[7:]):
                    print("false")
                elif cmds.ls("ctrl_fk"+item[7:])[0] == "ctrl_fk"+item[7:]:
                    cmds.connectAttr(f"ctrl_COG.ikfk_switch_{key[8:]}", f"ctrl_fk{item[7:]}.visibility")

    def parent_system_to_rig(self):
        joints_list = []

        joints = list(self.ui_data.keys())[0]
        top_of_heirachy = self.get_top_heirachy_joint(joints)
        print(top_of_heirachy)

        joints_list = cmds.listRelatives(top_of_heirachy,ad=True, typ='joint')
        joints_list.append(top_of_heirachy)
        joints_list.reverse()
        #print(joints_list)

        for item in (joints_list):
            #print(item)
            try:
                cmds.parentConstraint(f"jnt_fk{item[7:]}",f"jnt_ik{item[7:]}",item, n=f"pConst{item[7:]}")
            except ValueError:
                #print(f"{item} does not have ik fk equivalent")        #for testing
                pass


    def setup_ikfK_switch(self):
        for x in self.system_joints.keys():
            cmds.addAttr("ctrl_COG",nn=f"IKFK Switch: {x[8:]}",sn=f"ikfk_switch_{x[8:]}",k=True,min=0,max=1)


#combine_systems()
