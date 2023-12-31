import importlib
import maya.cmds as cmds
import config

importlib.reload(config)

def parent_operation(child, parent):
        cmds.parent(child,parent)

class parenting_created_joints():
    def __init__(self):
        self.ui_data = config.ui_data
        self.system_joints = config.system_joints

        self.parent_joint_to_joint()

    def parent_joint_to_joint(self):
        for sys in ("fk","ik"): #runs the parent system twice for both systems, this should EVENTUALLY PULL DATA FROM THE UI
            try:
                for x in self.system_joints.keys(): #runs the parent system for each join system in the ui data
                    for i in range(len(self.system_joints[x])): #runs the parent system for each joint in joint heirachy
                        try:
                            child = sys + "_jnt" + self.system_joints[x][i+1][7:]
                            parent = sys + "_jnt" + self.system_joints[x][i][7:]
                            parent_operation(child, parent)
                        except IndexError:
                            pass
            except ValueError:
                pass


#parenting_created_joints()