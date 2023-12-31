import importlib
import maya.cmds as cmds

import system_attr
importlib.reload(system_attr)

#import ikfk_const_setup as switch
#importlib.reload(switch)

ik_joints_to_parent = ["jnt_ik_clavicle_r","jnt_ik_clavicle_l","jnt_ik_hip_r","jnt_ik_hip_l"]
fk_joints_to_parent = ["jnt_fk_clavicle_r","jnt_fk_clavicle_l","jnt_fk_hip_r","jnt_fk_hip_l"]
grp_controls = ['ctrl_root','ctrl_COG','ctrl_root_world']


def grpSetup():
    selection = cmds.ls(sl=True, typ='joint')
    path_abc = "C:/Docs/maya/024/scripts/curve_import.abc"
    path_ma = "C:/Docs/maya/2024/scripts/curve_import.ma"

    try:
        cmds.file(path_abc, i=True)
    except RuntimeError:
        print("Couldnt load file using basic shapes instead")
        cmds.file(path_ma, i=True)
        #cmds.circle(n='ctrl_root',r= 70,nr=(0,1,0))
        #cmds.circle(n='ctrl_COG',r= 40,nr=(0,1,0))
        #cmds.circle(n='ctrl_root_world',r=85,nr=(0,1,0))

    try:
        grpList = ['grp_mesh','grp_controls','grp_joints','grp_locators','grp_blendshapes']
        jntList = ['grp_ik_handles','grp_ik_joints','grp_fk_joints','grp_rig_joints','grp_skn_joints']
        ctrlList = ['grp_ctrls_head','grp_ctrls_spine','grp_ctrls_arms','grp_ctrls_legs']
    
        cmds.group(n='WD_Rig_Master',w=True,em=True)
        cmds.parent("ctrl_root_world","WD_Rig_Master")
        cmds.group(n='DO_NOT_TOUCH',p='WD_Rig_Master',em=True)
    
        for x in range(len(grpList)):
            cmds.group(n=grpList[x],p="ctrl_root_world",em=True)
        for x in range(len(jntList)):
            cmds.group(n=jntList[x],p=grpList[2],em=True)
        
        cmds.group(n='grp_root',p='grp_controls',em=True)
        cmds.parent('ctrl_root','grp_root')
        cmds.group(n='grp_COG',p='ctrl_root',em=True)
        cmds.matchTransform('grp_COG','rig_jnt_COG',pos=True,rot=True)

        cmds.matchTransform('ctrl_COG','grp_COG',pos=True,rot=True)
        cmds.parent('ctrl_COG','grp_COG')

        cmds.group(n='grp_misc_ctrls',p='ctrl_COG',em=True)

        for x in range(len(ctrlList)):
            cmds.group(n=ctrlList[x],p='ctrl_COG',em=True)
        #spine grps
        cmds.group(n='grp_ik_spine',p='grp_ctrls_spine',em=True)
        cmds.group(n='grp_fk_spine',p='grp_ctrls_spine',em=True)
    
        #arm groups
        cmds.group(n='grp_clav_rotate',p='grp_ctrls_arms',em=True)
        cmds.group(n='grp_ik_arm',p='grp_clav_rotate',em=True)
        cmds.group(n='grp_fk_arm',p='grp_clav_rotate',em=True)
    
        #leg groups
        cmds.group(n='grp_ik_leg',p='grp_ctrls_legs',em=True)
        cmds.group(n='grp_fk_leg',p='grp_ctrls_legs',em=True)

        system_attr.sys_attr()

    except RuntimeError:
        cmds.error("Groups exists already that matches name, grps might be missing in file structure")
    
    '''for x in range(len(grp_controls)):
        cmds.setAttr(grp_controls[x]+".overrideEnabled", 1)
        cmds.setAttr(grp_controls[x]+".overrideColor", 17)'''

    #switch.create_attr()
        
    return selection
