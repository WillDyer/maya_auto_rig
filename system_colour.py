import maya.cmds as cmds

class colour():
    def __init__(self):
        self.selection = "WD_Rig_Master"
        self.collect_all_ctrls()
        #print("Coloured!")

    def collect_all_ctrls(self):
        COLOR_CONFIG = {'l': 6, 'r': 13, 'default': 22}
        ctrls = cmds.listRelatives(self.selection, ad=True, typ="transform")
        if ctrls is None:
            ctrls = self.selection
        for ctrl in ctrls:
            try:
                cmds.setAttr(f"{ctrl}.overrideEnabled", 1)
                if ctrl == "ctrl_root_world":
                    cmds.setAttr(f"{ctrl}.overrideColor", 18)
                elif ctrl[:4] == "ctrl":
                    side = ctrl[-1]
                    #print(ctrl)
                    try:
                        cmds.setAttr(f"{ctrl}.overrideColor",
                                    COLOR_CONFIG[side])
                    except KeyError:
                        cmds.setAttr(f"{ctrl}.overrideColor",
                                    COLOR_CONFIG['default'])
                        pass
                else:
                    #cmds.warning("Curve not coloured as does not match 'ctrl' prefix")
                    pass
            except:
                pass
                    
# colour()