import importlib

#command files
import grp_1 as grp
import joints_select
import system_parent_created_joints
import system_fk
import system_ik
import system_combined
import system_fingers

import system_colour #last thing ran

#reload
importlib.reload(grp)
importlib.reload(joints_select)
importlib.reload(system_parent_created_joints)
importlib.reload(system_fk)
importlib.reload(system_ik)
importlib.reload(system_combined)
importlib.reload(system_fingers)

importlib.reload(system_colour) # last thing loaded

#execute in order
def run_auto_rigger():
    import config
    importlib.reload(config)
    print(f"Config: {config.ui_data}")
    grp.grpSetup()
    joints_select.systems()
    system_parent_created_joints.parenting_created_joints()
    system_fk.create_fk_system()
    system_ik.create_ik_system()
    system_combined.combine_systems()
    system_fingers.create_fingers()

    system_colour.colour() # last thing ran

    print("run")