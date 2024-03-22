import maya.cmds as cmds
import config

class ikfk_switch():
    def __init__(self):
        self.system_joints = config.all_systems
        self.create_ikfk_switch()
        
    def create_ikfk_switch(self):
        object = "ctrl_COG"
        cmds.addAttr(object,ln="ikfk_switch_dvdr",nn="------------", k=1,at="enum",en="IKFK Switch")
        cmds.setAttr(f"{object}.ikfk_switch_dvdr", l=True)
        for obj in self.system_joints:
            print("onj" + obj)

            # check for ik an fk jnts
            ik_jnt = obj.replace("rig", "ik")
            ik = cmds.ls(ik_jnt)
            fk_jnt = obj.replace("rig", "fk")
            fk = cmds.ls(fk_jnt)

            ik_exists = True
            fk_exists = True

            if not ik:
                ik_exists = False
            if not fk:
                fk_exists = False
            
            if fk_exists and ik_exists == True:
                cmds.addAttr(object,ln=f"ikfk_switch_{obj[8:]}",nn=f"IKFK Switch {obj[8:]}",k=1,at="float",min=0,max=1)
                cmds.createNode('reverse', n=f'IKFK_Reverse_{obj[8:]}')
                cmds.connectAttr(f"{object}.ikfk_switch_{obj[8:]}",f'IKFK_Reverse_{obj[8:]}.inputX')

                # connect ik fk ctrls
                for joint in self.system_joints[obj]:
                    fk_ctrl = joint.replace("jnt_rig","ctrl_fk")
                    ik_ctrl = joint.replace("jnt_rig","ctrl_ik")
                    pv_ctrl = joint.replace("jnt_rig","ctrl_pv")
                    pv_crv = joint.replace("jnt_rig","pv_curve")

                    # parent constraint joints
                    cmds.parentConstraint(f"jnt_fk_{joint[8:]}",f"jnt_ik_{joint[8:]}",joint, n=f"pConst_{joint[8:]}")

                    # constraint connection
                    try:
                        cmds.connectAttr(f"{object}.ikfk_switch_{obj[8:]}",f"pConst_{joint[8:]}.jnt_fk_{joint[8:]}W0")
                        cmds.connectAttr(f'IKFK_Reverse_{obj[8:]}.outputX',f"pConst_{joint[8:]}.jnt_ik_{joint[8:]}W1")
                    except RuntimeError:
                        pass

                    # visability connection
                    try:
                        cmds.connectAttr(f"{object}.ikfk_switch_{obj[8:]}",f"{fk_ctrl}.visibility")
                        cmds.connectAttr(f'IKFK_Reverse_{obj[8:]}.outputX',f"{ik_ctrl}.visibility")
                    except RuntimeError:
                        pass

                    try:
                        cmds.connectAttr(f'IKFK_Reverse_{obj[8:]}.outputX',f"{pv_ctrl}.visibility")
                        cmds.connectAttr(f'IKFK_Reverse_{obj[8:]}.outputX',f"{pv_crv}.visibility")
                    except RuntimeError:
                        pass


                