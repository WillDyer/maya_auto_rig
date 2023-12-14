import importlib
import maya.cmds as cmds
import offset_parent_matrix as opm

import joints_select as js

importlib.reload(opm)
importlib.reload(js)

print(js.get_joints())
print(js.ik_rename())
print(js.ik_rename())

'''def parent_joints():

    for i in range(AMOUNT):
        cmds.select(FK_JOINTS_LIST[i], r=True)
        opm.offset_parent_matrix()
    
    #IK_JOINTS_LIST.reverse()
    FK_JOINTS_LIST.reverse()

    
    amount_parent = AMOUNT - 1
    
    for i in range(amount_parent):
        cmds.parent(IK_JOINTS_LIST[i],IK_JOINTS_LIST[i+1])
        cmds.parent(FK_JOINTS_LIST[i],FK_JOINTS_LIST[i+1])'''