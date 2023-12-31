import maya.cmds as cmds

attrs = {
    'controls_divider': ['CONTROLS','------------',True,False,'not needed'],
    'face': ['Face','Shown:Hidden',False,True,'grp_ctrls_head.visibility'],
    'body': ['Body','Shown:Hidden',False,True,'grp_ctrls_spine.visibility'],
    'arms': ['Arms','Shown:Hidden',False,True,'grp_ctrls_arms.visibility'],
    'legs': ['Legs','Shown:Hidden',False,True,'grp_ctrls_legs.visibility'],
    'visibility_divider': ['VISIBILITY','------------',True,False,'not needed'],
    'vis_geometry': ['Geometry','Shown:Hidden',False,True,'grp_mesh.visibility'],
    'blend_shapes': ['Blendshapes','Shown:Hidden',False,True,'grp_blendshapes.visibility'],
    'lock_divider': ['LOCK','------------',True,False,'not needed'],
    'export_geometry': ['Exoport Geometry','Unlocked:Locked:Wireframe',False,False,'not needed'],
    'debug_divider': ['DEBUG','------------',True,False,'not needed'],
    'rig_system': ['Rig System','Shown:Hidden',False,True,'grp_rig_joints.visibility'],
    'skn_system': ['Skin System','Shown:Hidden',False,True,'grp_skn_joints.visibility'],
    'fk_system': ['FK System','Shown:Hidden',False,True,'grp_fk_joints.visibility'],
    'ik_system': ['IK System','Shown:Hidden',False,True,'grp_ik_joints.visibility'],
    'ik_hndle_system': ['IK Handles','Shown:Hidden',False,True,'grp_ik_handles.visibility']
}

def sys_attr():
    for item in attrs.keys():
        #print(attrs[item][0])
        cmds.addAttr("ctrl_root",sn=item,nn=attrs[item][0],k=True,at="enum",en=attrs[item][1])
        cmds.setAttr(f"ctrl_root.{item}",lock=attrs[item][2])
        if attrs[item][3] == True:
            cmds.createNode('reverse', n=f'reverse_{item}')
            cmds.connectAttr(f"ctrl_root.{item}",f"reverse_{item}.inputX")
            cmds.connectAttr(f"reverse_{item}.outputX",attrs[item][4])
    for xyz in ["X","Y","Z"]:
        cmds.setAttr(f"ctrl_root.scale{xyz}",k=False,lock=True)