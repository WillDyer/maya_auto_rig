import maya.cmds as cmds
import importlib
import OPM

import config
importlib.reload(config)

class create_ik_spline():
    def __init__(self):
        self.ui_data = config.ui_data
        self.system_joints = config.system_joints

        self.create_handle()
    
    def create_handle(self):
        location_list = []
        jnt_ikctrl_list = []
        ctrl_list = []

        for key in self.system_joints.keys():
            self.system_joints[key].reverse()
            for jnt in self.system_joints[key]:
                loc = cmds.xform(f"jnt_ik{jnt[7:]}",q=1,ws=1,rp=1)
                location_list.append(loc)
            for jnt in range(0, len(self.system_joints[key]), 2):
                loc = location_list[jnt]
                jnt_ikctrl = cmds.joint(n=f"jnt_ikctrl{self.system_joints[key][jnt][7:]}", p=loc, rad=3)
                jnt_ikctrl_list.append(jnt_ikctrl)
                try:
                    cmds.parent(jnt_ikctrl, w=True)
                except RuntimeError:
                    pass
            
            cmds.curve(n=f"crv_ik{key[7:]}",p=location_list,d=1)
            cmds.ikHandle(n=f"hdl_ik{key[7:]}",
                        startJoint=f"jnt_ik{self.system_joints[key][0][7:]}", 
                        endEffector=f"jnt_ik{self.system_joints[key][-1][7:]}", 
                        solver='ikSplineSolver', 
                        ccv=False, 
                        scv=False, 
                        curve=f"crv_ik{key[7:]}")
            
            for ikctrl in jnt_ikctrl_list:
                cmds.circle(n=f"ctrl_ik{ikctrl[10:]}",
                            r=8, nr=(1, 0, 0))

                cmds.matchTransform(f"ctrl_ik{ikctrl[10:]}", ikctrl)
                cmds.select(f"ctrl_ik{ikctrl[10:]}")
                OPM.offsetParentMatrix()
                cmds.parentConstraint(f"ctrl_ik{ikctrl[10:]}", ikctrl)
                ctrl_list.append(f"ctrl_ik{ikctrl[10:]}")
            
            jnt_ikctrl_list.append(f"crv_ik{key[7:]}")
            ik_spline_crv = f"crv_ik{key[7:]}"
            cmds.skinCluster(jnt_ikctrl_list,tsb=True, bm=0, sm=0, nw=1)

            ik_handle_name = f"hdl_ik{key[7:]}"
            self.populate_to_group(jnt_ikctrl_list,ik_handle_name,key,ik_spline_crv,ctrl_list)
            cmds.select(key)

    def populate_to_group(self,jnt_ikctrl_list,ik_handle_name,key,ik_spline_crv,ctrl_list):
        cmds.group(n=f"autorig_ik_spine{key[7:]}",w=True,em=True)
        cmds.group(f"jnt_ik{key[7:]}", n=f"ik_joints{key[7:]}",p=f"autorig_ik_spine{key[7:]}")
        cmds.group(ik_handle_name, jnt_ikctrl_list, n=f"ikctrl_joints{key[7:]}",p=f"autorig_ik_spine{key[7:]}")
        cmds.group(ctrl_list, n=f"ik_controls{key[7:]}",p=f"autorig_ik_spine{key[7:]}")
        cmds.group(ik_spline_crv,n=f"ik_misc{key[7:]}",p=f"autorig_ik_spine{key[7:]}")