import maya.cmds as cmds


class polish_rig():
    def __init__(self):
        self.get_autorig_groups()

    def get_autorig_groups(self):
        autorig_groups = cmds.ls("autorig_*")
        # print(autorig_groups)

        for groups in autorig_groups:
            try:
                for sub_group in cmds.listRelatives(groups, c=True):
                    # print(f"{cmds.listRelatives(sub_group,p=True)[0]}: {sub_group}")
                    items_to_parent = cmds.listRelatives(sub_group, c=True)
                    # print(items_to_parent)

                    if cmds.listRelatives(sub_group, p=True)[0][:10] == "autorig_fk":
                        if sub_group[:9] == "fk_joints":
                            cmds.parent(items_to_parent, "grp_fk_joints")
                    if cmds.listRelatives(sub_group, p=True)[0][:14] == "autorig_fk_arm":
                        if sub_group[:11] == "fk_controls":
                            cmds.parent(items_to_parent, "grp_fk_arm")
                    if cmds.listRelatives(sub_group, p=True)[0][:14] == "autorig_fk_leg":
                        if sub_group[:11] == "fk_controls":
                            cmds.parent(items_to_parent, "grp_fk_leg")
                    if cmds.listRelatives(sub_group, p=True)[0][:16] == "autorig_fk_spine":
                        if sub_group[:11] == "fk_controls":
                            cmds.parent(items_to_parent, "grp_fk_spine")

                    if cmds.listRelatives(sub_group, p=True)[0][:10] == "autorig_ik":
                        if sub_group[:9] == "ik_joints":
                            cmds.parent(items_to_parent, "grp_ik_joints")
                        if sub_group[:6] == "ik_hdl":
                            cmds.parent(items_to_parent, "grp_ik_handles")
                        if sub_group[:7] == "ik_misc":
                            cmds.parent(items_to_parent, "DO_NOT_TOUCH")
                    if cmds.listRelatives(sub_group, p=True)[0][:14] == "autorig_ik_arm":
                        if sub_group[:11] == "ik_controls":
                            print(items_to_parent)
                            cmds.parent(items_to_parent, "grp_ik_arm")
                    if cmds.listRelatives(sub_group, p=True)[0][:14] == "autorig_ik_leg":
                        if sub_group[:11] == "ik_controls":
                            cmds.parent(items_to_parent, "grp_ik_leg")
                    if cmds.listRelatives(sub_group, p=True)[0][:16] == "autorig_ik_spine":
                        if sub_group[:13] == "ikctrl_joints":
                            cmds.parent(sub_group, "grp_ik_spine")
                        if sub_group[:11] == "ik_controls":
                            cmds.parent(sub_group, "grp_ik_spine")
                cmds.delete(groups)
            except TypeError:  # if a group is empty
                cmds.delete(groups)
                pass