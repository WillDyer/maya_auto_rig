import maya.cmds as cmds
global ik_joints_list
global fk_joints_list
joints_list = []
ik_joints_list = []
fk_joints_list = []
nameList = []

def get_joints():
    global joints_list
    top_joint = cmds.ls(sl=True, typ='joint')
    joints_list = cmds.listRelatives(top_joint,ad=True, typ='joint')
    joints_list.append(top_joint[0])
    joints_list.reverse()
    print(joints_list)

def duplicate_ik_fk_joints():
    
    for item in joints_list:
        cmds.select(item, r=True)
        cmds.joint()
        cmds.parent(w=True)
        new_joint = cmds.ls(sl=True, typ='joint')
        ik_joints_list.append(new_joint[0])

        cmds.select(item, r=True)
        cmds.joint()
        cmds.parent(w=True)
        new_joint = cmds.ls(sl=True, typ='joint')
        fk_joints_list.append(new_joint[0])

    global amount
    amount = len(joints_list)
    return amount

def ik_rename():
    #renaming joints & creates list for each set of joints
    for i in range(amount):
        try:
            left_or_right = "_" + joints_list[i].split("_")[3]
        except IndexError:
            left_or_right = ""
        cmds.rename(ik_joints_list[i], 'jnt_ik_' + joints_list[i].split("_")[2] + left_or_right)
        ik_joint_temp = 'jnt_ik_' + joints_list[i].split("_")[2] + left_or_right
        ik_joints_list.append(ik_joint_temp)
    print(fk_joints_list)
    return ik_joints_list

def fk_rename():
    #renaming joints & creates list for each set of joints
    for i in range(amount):
        try:
            left_or_right = "_" + joints_list[i].split("_")[3]
        except IndexError:
            left_or_right = ""
        cmds.rename(fk_joints_list[i], 'jnt_fk_' + joints_list[i].split("_")[2] + left_or_right)
        
        fk_joint_temp = 'jnt_fk_' + joints_list[i].split("_")[2] + left_or_right
        fk_joints_list.append(fk_joint_temp)
    print(fk_joints_list)
    return fk_joints_list
#list is not appending