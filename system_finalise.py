import maya.cmds as cmds


class finalise_rig():
    def __init__(self):
        self.root_jnt = "jnt_rig_root"
        self.rig_joints_suffix()
        self.parent_rig_skn()
        self.put_joints_in_group()

    def rig_joints_suffix(self):
        rig_joints_suffix = []
        
        # replace name
        all_rig_joints = cmds.listRelatives(self.root_jnt, ad=True, type="joint")
        all_rig_joints.append(self.root_jnt)
        
        for rig_joint in all_rig_joints:
            rig_joint = rig_joint[8:]
            rig_joints_suffix.append(rig_joint)

        self.skn_joints(rig_joints_suffix)

    def skn_joints(self, rig_joints_suffix):
        cmds.duplicate(self.root_jnt,rc=True)

        all_skn_joints = cmds.listRelatives(f"{self.root_jnt}1", ad=True, type="joint")
        all_skn_joints.append(f"{self.root_jnt}1")

        # rig and skn replaced
        for joint in range(len(all_skn_joints)):
            joint_renamed = all_skn_joints[joint].replace("rig", "skn")

            joint_renamed = joint_renamed[:8:] + rig_joints_suffix[joint]
            cmds.rename(all_skn_joints[joint], joint_renamed)

    def parent_rig_skn(self):
        all_rig_joints = cmds.listRelatives(self.root_jnt, ad=True, type="joint")
        all_rig_joints.append(self.root_jnt)

        for joint in all_rig_joints:
            cmds.parentConstraint(joint, f"jnt_skn_{joint[8:]}", n=f"pConst_{joint[8:]}")

        # parent cog to joint
        try:
            cmds.parentConstraint("ctrl_COG","jnt_rig_COG", n="pConst_COG")
        except:
            cmds.error("ERROR: COG joint not named as: jnt_rig_COG")

    def put_joints_in_group(self):
        cmds.parent(self.root_jnt, "grp_rig_joints")
        cmds.parent(f"jnt_skn{self.root_jnt[7:]}", "grp_skn_joints")
