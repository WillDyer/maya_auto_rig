import importlib
import maya.cmds as cmds
import offset_parent_matrix as opm

import joints_select as js

importlib.reload(opm)
importlib.reload(js)

fk_joint_split_temp = []
fk_joint_split = []

def unparent_joints():
    AMOUNT = js.get_joints()
    FK_JOINTS_LIST = js.fk_list()
    IK_JOINTS_LIST = js.ik_list()
    print(AMOUNT)
    print("fk",FK_JOINTS_LIST)
    print("ik",IK_JOINTS_LIST)
    
    for i in range(AMOUNT):
        #print(FK_JOINTS_LIST[i])
        fk_joint_split_temp = FK_JOINTS_LIST[i].split("_")[2]
        fk_joint_split.append(fk_joint_split_temp)
    print(fk_joint_split)
    
    '''for x in range(AMOUNT):
        cmds.parent(FK_JOINTS_LIST[fk_joint_split.index("shoulder")], w=True)'''
    '''for i in range(AMOUNT):
        cmds.select(FK_JOINTS_LIST[i], r=True)
        print(FK_JOINTS_LIST[i])
        opm.offsetParentMatrix()'''
    
    
    '''for i in range(amount_parent):
        #cmds.parent(IK_JOINTS_LIST[i],IK_JOINTS_LIST[i+1])
        cmds.parent(FK_JOINTS_LIST[i],FK_JOINTS_LIST[i+1])'''