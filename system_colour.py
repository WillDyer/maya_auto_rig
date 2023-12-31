import maya.cmds as cmds

class colour():
    def __init__(self):
        self.collect_all_ctrls()

    def collect_all_ctrls(self):
        ctrls = cmds.listRelatives("WD_Rig_Master",ad=True,typ="transform")
        print(ctrls)
        for ctrl in ctrls:
            if ctrl == "ctrl_root_world":
                cmds.setAttr(f"ctrl_root_worldShape.overrideEnabled", 1)
                cmds.setAttr(f"ctrl_root_worldShape.overrideColor", 18)
            
            elif ctrl[3:7] == "ctrl":
                if ctrl[-1] == "l":
                    try:
                        cmds.setAttr(f"{ctrl}.overrideEnabled", 1)
                        cmds.setAttr(f"{ctrl}.overrideColor", 6)
                    except RuntimeError:
                        pass
                elif ctrl[-1] == "r":
                    try:
                        cmds.setAttr(f"{ctrl}.overrideEnabled", 1)
                        cmds.setAttr(f"{ctrl}.overrideColor", 13)
                    except RuntimeError:
                        pass
            elif ctrl[:4] == "ctrl":
                try:
                    cmds.setAttr(f"{ctrl}.overrideEnabled", 1)
                    cmds.setAttr(f"{ctrl}.overrideColor", 22)
                except RuntimeError:
                    pass
            else:
                pass
            

#colour()