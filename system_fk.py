import importlib
import maya.cmds as cmds
import config
import OPM

importlib.reload(config)
importlib.reload(OPM)


class CreateFkSystems():
    def __init__(self):
        self.ui_data = config.ui_data
        self.system_joints = config.system_joints

        self.fk_system()
        # self.fk_system_to_joint()
        # self.system_to_heirachy()

    def fk_system(self):
        # runs the parent system for each join system in the ui data
        for x in self.system_joints.keys():
            ctrls_fk = []
            # runs the parent system for each joint in joint heirachy
            for i in range(len(self.system_joints[x])):
                cmds.circle(n=f"ctrl_fk{self.system_joints[x][i][7:]}",
                            r=8, nr=(1, 0, 0))
                cmds.matchTransform(f"ctrl_fk{self.system_joints[x][i][7:]}",
                                    self.system_joints[x][i])

                # check for child end joint and if so delete
                if cmds.listRelatives(self.system_joints[x][i], c=True) is None:
                    cmds.delete(f"ctrl_fk{self.system_joints[x][i][7:]}")
                else:
                    ctrls_fk.append(f"ctrl_fk{self.system_joints[x][i][7:]}")

            for ctrl in range(len(ctrls_fk)):
                try:
                    cmds.parent(ctrls_fk[ctrl], ctrls_fk[ctrl+1])
                except IndexError:
                    pass

            for ctrl in ctrls_fk:
                cmds.select(ctrl)
                OPM.offsetParentMatrix()

            self.fk_system_to_joint(ctrls_fk)
            self.populate_to_group(x, ctrls_fk)
            cmds.select(x)

    def fk_system_to_joint(self, ctrls_fk):
        for item in range(len(ctrls_fk)):
            cmds.parentConstraint(ctrls_fk[item],
                                  f"jnt_fk{ctrls_fk[item][7:]}",
                                  n=f"pConst{ctrls_fk[item][7:]}")

    def populate_to_group(self, x, ctrls_fk):
        cmds.group(n=f"autorig_fk_{self.ui_data[x][2]}{x[7:]}",
                   w=True, em=True)
        cmds.group(ctrls_fk[-1],
                   n=f"fk_controls{x[7:]}",
                   p=f"autorig_fk_{self.ui_data[x][2]}{x[7:]}")
        cmds.group(f"jnt_fk{self.system_joints[x][-1][7:]}",
                   n=f"fk_joints{x[7:]}",
                   p=f"autorig_fk_{self.ui_data[x][2]}{x[7:]}")

# create_fk_system()
