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
        self.create_ik_joints()
        self.create_fk_joints()
        self.rig_joints_back_together()

    def split_joints(self):
        for x in self.ui_data.keys():
            self.temporary_list = []
            for i in self.system_joints[x]:
                joints = str(i)
                self.joints_list_split_temp = joints.split("_")[2]
                self.temporary_list.append(self.joints_list_split_temp)
            self.joints_list_split.append(self.temporary_list)
            #print(self.joints_list_split)
            
        #print(f"Split Joint List: {self.joints_list_split}")
        
    def split_systems_to_world(self):
        for x in self.ui_data.keys():
            cmds.select(x)
            cmds.parent(w=True)
        
    def create_ik_joints(self):
        for x in self.ui_data.keys():
            for item in self.system_joints[x]:
                duplicate_system_joints(item)
                new_joint = cmds.ls(sl=True, typ='joint')
                new_name = "ik_jnt"+item[7:]
                cmds.rename(new_joint, new_name)
                #print(f"IK: New Joint: {new_joint}, New Joint Name: {new_name}")
        
    def create_fk_joints(self):
        for x in self.ui_data.keys():
            for item in self.system_joints[x]:
                duplicate_system_joints(item)
                new_joint = cmds.ls(sl=True, typ='joint')
                new_name = "fk_jnt"+item[7:]
                cmds.rename(new_joint, new_name)
                #print(f"FK: New Joint: {new_joint}, New Joint Name: {new_name}")

    def rig_joints_back_together(self):
        for x in self.ui_data.keys():
            cmds.parent(x,self.ui_data[x][3])
            #print(f"Child: {x}, Parent: {self.ui_data[x][3]}")
        #-cmds.parent("rig_jnt_root","grp_rig_joints")

#systems()