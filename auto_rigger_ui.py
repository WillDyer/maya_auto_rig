import maya.cmds as cmds
from maya import OpenMayaUI as omui

from PySide2.QtCore import *
from PySide2.QtGui import *
#suggested fix from PySide2.QtWidgets import QWidget, QUiLoader, QApplication, QPushButton, QVBoxLayout, QFileDialog, QLabel, QSpinBox
#class main_ui(QWidget):
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *
from shiboken2 import wrapInstance
import system_get_file_location
import os.path
import importlib

#command files
import config
import system_group
import system_joints
import system_parent_created_joints
import system_fk
import system_ik
import system_ik_spline
import system_polish_rig
import system_finalise
import system_ikfk

import system_colour #last thing ran

#reload
importlib.reload(system_group)
importlib.reload(system_joints)
importlib.reload(system_parent_created_joints)
importlib.reload(system_fk)
importlib.reload(system_ik)
importlib.reload(system_ik_spline)
importlib.reload(system_polish_rig)
importlib.reload(system_finalise)
importlib.reload(system_ikfk)


importlib.reload(system_colour) # last thing loaded


mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QWidget)


class QtSampler(QWidget):
    def __init__(self, *args, **kwargs):
        self.path = system_get_file_location.get_loc()
        super(QtSampler,self).__init__(*args, **kwargs)
        self.setParent(mayaMainWindow)
        self.setWindowTitle("Will's Auto Rigger :)")
        self.setWindowFlags(Qt.Window)
        self.initUI()
        
        self.ui.leg_setup_button.clicked.connect(self.load_leg_setup)
        self.ui.arm_setup_button.clicked.connect(self.load_arm_setup)
        self.ui.spine_setup_button.clicked.connect(self.load_spine_setup)
        self.ui.finger_setup_button.clicked.connect(self.load_finger_setup)
        self.ui.human_setup_button.clicked.connect(self.load_human_setup)

        self.ui.ik_arm_button.clicked.connect(self.ik_arm_setup)
        self.ui.fk_arm_button.clicked.connect(self.fk_arm_setup)
        self.ui.ik_leg_button.clicked.connect(self.ik_leg_setup)
        self.ui.fk_leg_button.clicked.connect(self.fk_leg_setup)
        self.ui.ik_spine_button.clicked.connect(self.ik_spine_setup)
        self.ui.fk_spine_button.clicked.connect(self.fk_spine_setup)
        self.ui.polish_rig_button.clicked.connect(self.polish_rig)

        self.all_systems = {}
        
    def initUI(self):
        loader = QUiLoader()
        UI_FILE = self.path +"/file_imports/AutoRigger_main_window.ui"
        file = QFile(UI_FILE)
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, parentWidget=self)
        file.close()
        
    def load_leg_setup(self):
        # print("load arm pressed")
        try:
            cmds.file(f"{self.path}/file_imports/leg_setup.ma",i=True)
        except RuntimeError:
            cmds.error("Could not find file path")

    def load_arm_setup(self):
        # print("load arm pressed")
        try:
            cmds.file(f"{self.path}/file_imports/arm_setup.ma",i=True)
        except RuntimeError:
            cmds.error("Could not find file path")

    def load_spine_setup(self):
        # print("load arm pressed")
        try:
            cmds.file(f"{self.path}/file_imports/spine_setup.ma",i=True)
        except RuntimeError:
            cmds.error("Could not find file path")

    def load_finger_setup(self):
        # print("load arm pressed")
        try:
            cmds.file(f"{self.path}/file_imports/fingers_setup.ma",i=True)
        except RuntimeError:
            cmds.error("Could not find file path")

    def load_human_setup(self):
        # print("load arm pressed")
        try:
            cmds.file(f"{self.path}/file_imports/skeleton.ma",i=True)
        except RuntimeError:
            cmds.error("Could not find file path")
        
    def fk_arm_setup(self):
        selected_joints = cmds.ls(sl=True,r=True)
        amount_of_joints = 4
        body_area = "arm"
        ik_or_fk = "fk"
        list_relatives_or_while_loop = "list_relatives"

        self.update_config(amount_of_joints,selected_joints,body_area,ik_or_fk,list_relatives_or_while_loop)
        importlib.reload(config)
        system_joints.systems()
        system_fk.CreateFkSystems()

    def ik_arm_setup(self):
        # print("ik setup")
        selected_joints = cmds.ls(sl=True,r=True)
        amount_of_joints = 4
        body_area = "arm"
        ik_or_fk = "ik"
        list_relatives_or_while_loop = "list_relatives"

        self.update_config(amount_of_joints,selected_joints,body_area,ik_or_fk,list_relatives_or_while_loop)
        importlib.reload(config)
        system_joints.systems()
        system_ik.create_ik_system()

    def fk_leg_setup(self):
        selected_joints = cmds.ls(sl=True,r=True)
        amount_of_joints = 5
        body_area = "leg"
        ik_or_fk = "fk"
        list_relatives_or_while_loop = "list_relatives"

        self.update_config(amount_of_joints,selected_joints,body_area,ik_or_fk,list_relatives_or_while_loop)
        importlib.reload(config)
        system_joints.systems()
        system_fk.CreateFkSystems()

    def ik_leg_setup(self):
        selected_joints = cmds.ls(sl=True,r=True)
        amount_of_joints = 3
        body_area = "leg"
        ik_or_fk = "ik"
        list_relatives_or_while_loop = "list_relatives"

        self.update_config(amount_of_joints,selected_joints,body_area,ik_or_fk,list_relatives_or_while_loop)
        importlib.reload(config)
        system_joints.systems()
        system_ik.create_ik_system()

    def fk_spine_setup(self):
        selected_joints = cmds.ls(sl=True,r=True)
        amount_of_joints = len(cmds.listRelatives(ad=True,typ="joint"))
        body_area = "spine"
        ik_or_fk = "fk"
        list_relatives_or_while_loop = "while_loop"

        self.update_config(amount_of_joints,selected_joints,body_area,ik_or_fk,list_relatives_or_while_loop)
        importlib.reload(config)
        system_joints.systems()
        system_fk.CreateFkSystems()

    def ik_spine_setup(self):
        selected_joints = cmds.ls(sl=True,r=True)
        amount_of_joints = len(cmds.listRelatives(ad=True,typ="joint"))
        body_area = "spine"
        ik_or_fk = "ik"
        list_relatives_or_while_loop = "while_loop"

        self.update_config(amount_of_joints,selected_joints,body_area,ik_or_fk,list_relatives_or_while_loop)
        importlib.reload(config)
        system_joints.systems()
        system_ik_spline.create_ik_spline()

    def polish_rig(self):
        system_group.grpSetup()
        system_polish_rig.polish_rig()
        system_finalise.finalise_rig()
        system_ikfk.ikfk_switch()
        system_colour.colour()

    def update_config(self, amount_of_joints, selected_joints,body_area,ik_or_fk,list_relatives_or_while_loop):
        system_joints = {}
        ui_data = {}
        jnt_true = True
        joint_list = []
        joint_name = ""
        test_amt = 0

        for joint in selected_joints:
            parent_joint = cmds.listRelatives(joint,p=True)
            if list_relatives_or_while_loop == "list_relatives":
                joint_list = cmds.listRelatives(joint, ad=True,typ="joint")
                joint_list.append(joint)
                joint_list = joint_list[-amount_of_joints:]

            elif list_relatives_or_while_loop == "while_loop":
                joint_name = joint
                joint_list.append(joint)
                while jnt_true == True:
                    jnt = cmds.listRelatives(joint_name, c=True,typ="joint")
                    test_amt = test_amt + 1

                    if jnt == None:
                        joint_list.reverse()
                        jnt_true = False
                    elif test_amt == 5:
                        joint_list.reverse()
                        jnt_true = False
                    else:
                        joint_name = jnt[0]
                        joint_list.append(jnt[0])
                amount_of_joints = len(joint_list)

            else:
                cmds.error("List_relatives_or_while_loop variable does not match statements")

            system_joints |= {joint: joint_list}

            try:
                ui_data_temp = [amount_of_joints, parent_joint[0], body_area,ik_or_fk]
            except TypeError:
                cmds.error("joint does not have a parent, please give a parent joint.")
            ui_data |= {joint: ui_data_temp}

        self.all_systems.update({joint: joint_list})

        z = "\nall_systems = " + str(self.all_systems)
        y = "\nsystem_joints = " + str(system_joints)        
        x = "ui_data = "+str(ui_data)
        lines = [x,y,z]

        path = self.path +"/config.py"
        assert os.path.isfile(path)
        with open(path, "w") as f:
            for line in lines:
                f.write(str(line))
            f.close()


def main():
    ui = QtSampler()
    ui.show()
    return ui
    
if __name__ == '__main__':
    main()