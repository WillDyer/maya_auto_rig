import importlib
import maya.cmds as cmds
import config

importlib.reload(config)

def duplicate_system_joints(item):
        cmds.select(item, r=True)
        cmds.joint()
        cmds.parent(w=True)

class systems():
    def __init__(self):
        self.joints_list_split = []
        self.temporary_list = []
        self.joints_list_split_temp = []
        self.ui_data = config.ui_data
        self.system_joints = config.system_joints

        self.split_joints()
        self.split_systems_to_world()
        for x in self.ui_data.keys():
            if self.ui_data[x][3] == "ik":
                self.create_ik_joints(x)
            elif self.ui_data[x][3] == "fk":
                self.create_fk_joints(x)
            else:
                cmds.error("No system joints made")
        self.rig_joints_back_together()

    def split_joints(self):
        for x in self.ui_data.keys():
            self.temporary_list = []
            for i in self.system_joints[x]:
                joints = str(i)
                self.joints_list_split_temp = joints.split("_")[2]
                self.temporary_list.append(self.joints_list_split_temp)
            self.joints_list_split.append(self.temporary_list)
        
    def split_systems_to_world(self):
        for x in self.ui_data.keys():
            cmds.select(x)
            cmds.parent(w=True)
        
    def create_ik_joints(self,x):
        print("ik joints made")
        for item in self.system_joints[x]:
            duplicate_system_joints(item)
            new_joint = cmds.ls(sl=True, typ='joint')
            cmds.rename(new_joint, f"jnt_ik{item[7:]}")
        for item in range(len(self.system_joints[x])):
            try:
                cmds.parent(f"jnt_ik{self.system_joints[x][item][7:]}",f"jnt_ik{self.system_joints[x][item+1][7:]}")
            except IndexError:
                pass
        
    def create_fk_joints(self,x):
        print("fk joints made")
        for item in self.system_joints[x]:
            duplicate_system_joints(item)
            new_joint = cmds.ls(sl=True, typ='joint')
            cmds.rename(new_joint, f"jnt_fk{item[7:]}")
        for item in range(len(self.system_joints[x])):
            try:
                cmds.parent(f"jnt_fk{self.system_joints[x][item][7:]}",f"jnt_fk{self.system_joints[x][item+1][7:]}")
            except IndexError:
                pass

    def rig_joints_back_together(self):
        for x in self.ui_data.keys():
            cmds.parent(x,self.ui_data[x][1])


#systems()