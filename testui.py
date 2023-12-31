import maya.cmds as cmds
import system_get_file_location #This is needed as if code is run inside of maya the __file__ attr is not created
from maya import OpenMayaUI as omui
import PySide2.QtCore as QtCore 
import PySide2.QtGui as QtGui 
import PySide2.QtWidgets as QtWidgets
from shiboken2 import wrapInstance 
import os.path
import math
import copy

#module imports
import importlib
import maya.cmds as cmds
import modules_setup

importlib.reload(modules_setup)

combo_box_values = []
saved_combo_box_values = []

saved_pressed = 0

ui_data = {
        }

def saved_values(self):
    if joint_dropdown_value in ui_data:
        self.ui.amount_of_joints.setValue(int(ui_data[joint_dropdown_value][0]))
        if ui_data[joint_dropdown_value][1] == "True":
            self.ui.twistJoints.setChecked(True)
        else:
            self.ui.twistJoints.setChecked(False)
        if ui_data[joint_dropdown_value][2] == "True":
            self.ui.ik_handle.setChecked(True)
        else:
            self.ui.ik_handle.setChecked(False)
    elif saved_pressed == 1:
        if joint_dropdown_value not in ui_data:
            self.ui.amount_of_joints.setValue(4)
            self.ui.twistJoints.setChecked(False)
            self.ui.ik_handle.setChecked(False)
    else:
        pass

mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QWidget)

class main_ui(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(main_ui,self).__init__(*args, **kwargs)
        self.setParent(mayaMainWindow)
        self.setWindowFlags(Qt.Window)
        self.initUI()
        
        self.ui.add_joint.clicked.connect(self.addPressed)
        self.ui.save_joint_profile.clicked.connect(self.savePressed)
        self.ui.create_rig.clicked.connect(self.createrigPressed)
        self.ui.use_autorig.clicked.connect(self.use_autorig_pressed)
        self.ui.load_autorig.clicked.connect(self.load_autorig_pressed)

        self.ui.twistJoints.stateChanged.connect(self.update_twist_joints_checkbox)
        self.ui.ik_handle.stateChanged.connect(self.update_ik_handle_checkbox)

        self.ui.amount_of_joints.valueChanged.connect(self.update_amount_of_joints)

        self.ui.joint_field.textChanged.connect(self.updateTextEdit)

        self.ui.joint_dropdown.currentIndexChanged.connect(self.combobox)

        self.ui.body_area.currentIndexChanged.connect(self.body_area)
        
    def initUI(self):
        loader = QUiLoader()
        path = system_get_file_location.get_loc()
        print(f"file path {path}")
        UI_FILE = path + "/test.ui"
        file = QFile(UI_FILE)
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, parentWidget=self)
        file.close()

    def addPressed(self):
        try:
            cmds.select(Value, r=True)
            combo_box_values.append(Value)

            for x in range(len(combo_box_values)):
                if not saved_combo_box_values:
                    saved_combo_box_values.append(combo_box_values[x])
                    self.ui.joint_dropdown.addItem(saved_combo_box_values[x])
                    print("no values ran")
    
                elif Value in combo_box_values[x]:
                    print("already exists")
                    pass
    
                elif Value not in saved_combo_box_values:
                    saved_combo_box_values.append(combo_box_values[-1])
                    self.ui.joint_dropdown.addItem(saved_combo_box_values[-1])
                    
                else:
                    print("alredy exists ignored")
            print("input value",Value)
            print("saved_values",saved_combo_box_values)

            possible_arm = ['rig_jnt_clavicle','rig_jnt_shoulder','rig_jnt_arm']
            possible_leg = ['rig_jnt_hip','rig_jnt_fema','rig_jnt_pelvis']

            if Value[:-2] in possible_arm:
                self.ui.body_area.setCurrentIndex(0)
            elif Value[:-2] in possible_leg:
                self.ui.body_area.setCurrentIndex(1)
            else:
                pass
            
        except ValueError:
            self.ui.object_name_found.setText(f"Joint: {Value} not found.")

    def use_autorig_pressed(self):
        global ui_data
        ui_data = {'rig_jnt_clavicle_r': [4, 'False', 'False', 'rig_jnt_chest', 'arm'],
                   'rig_jnt_clavicle_l': [4, 'False', 'False', 'rig_jnt_chest', 'arm'],
                   'rig_jnt_hip_r': [4, 'False', 'False', 'rig_jnt_pelvis', 'leg'],
                   'rig_jnt_hip_l': [4, 'False', 'False', 'rig_jnt_pelvis', 'leg'],
                   #'rig_jnt_pelvis': [5, 'False', 'False', 'rig_jnt_COG', 'spine']
                   }
        return ui_data

    def load_autorig_pressed(self):
        path = system_get_file_location.get_loc()
        print(f"file path {path}")
        SKELETON_FILE = path + "/skeleton.ma"
        try:
            cmds.file(SKELETON_FILE,i=True)
            cmds.warning("rig joints loaded")
        except RuntimeError:
            cmds.warning(f"Cannont Find: {SKELETON_FILE}")

    def savePressed(self):
        global ui_data
        global saved_pressed
        parent_joint = cmds.listRelatives(p=True,typ="joint")
        print("parent "+parent_joint[0])
        parent_joint = str(parent_joint[0])
        
        ui_data_temp = [self.update_amount_of_joints(), self.update_twist_joints_checkbox(), self.update_ik_handle_checkbox(), parent_joint, self.body_area()]

        data_to_be_merged = {self.combobox(): ui_data_temp}
        print(f"data merging: {data_to_be_merged}")

        ui_data |= data_to_be_merged
        print(f"updated ui data: {ui_data}")

        saved_pressed = 1

        saved_values(self)        

    def updateTextEdit(self):
        global Value
        Value = self.ui.joint_field.text()
        Value = str(Value)
        self.ui.object_name_found.setText("")
        return Value
    
    def combobox(self):
        global joint_dropdown_value
        joint_dropdown_value = self.ui.joint_dropdown.currentText()
        joint_dropdown_value = str(joint_dropdown_value)

        combo_box_index = self.ui.joint_dropdown.currentIndex()
        #print(f"combox index: {combo_box_index}")

        saved_values(self)

        return joint_dropdown_value
    
    def body_area(self):
        body_area_dropdown_value = self.ui.body_area.currentText()
        body_area_dropdown_value = str(body_area_dropdown_value)

        print(body_area_dropdown_value)
        return body_area_dropdown_value
         
    
    def update_amount_of_joints(self):
        global amount_of_joints
        amount_of_joints = self.ui.amount_of_joints.value()
        #print(f"joints: {amount_of_joints}")

        return amount_of_joints
    
    def update_twist_joints_checkbox(self):
        twist_joints_value = self.ui.twistJoints.isChecked()
        twist_joints_value = str(twist_joints_value)

        #print(f"twist joint value: {twist_joints_value}")
        return twist_joints_value

    def update_ik_handle_checkbox(self):
        ik_handle_value = self.ui.ik_handle.isChecked()
        ik_handle_value = str(ik_handle_value)

        #print(f"ik hndle value: {ik_handle_value}")
        return ik_handle_value
    
    def createrigPressed(self):
        system_joints = {}
        print("Button Pressed")

        for x in ui_data.keys():
            joints_list = cmds.listRelatives(x,ad=True,typ='joint')
            joints_list.append(x)
            joints_list.reverse()
            joints_list = joints_list[:ui_data[x][0]]
            
            data_to_be_merged = {x: joints_list}

            system_joints |= data_to_be_merged

        y = "\nsystem_joints = " + str(system_joints)        
        x = "ui_data = "+str(ui_data)
        lines = [x,y]

        path = r"C:\Docs\maya\2024\scripts\config.py"
        assert os.path.isfile(path)
        with open(path, "w") as f:
            for line in lines:
                f.write(str(line))
            f.close()
        modules_setup.run_auto_rigger()
        print(f"Saved config: {lines}")
    

def main():
    ui = main_ui()
    ui.show()
    return ui
    
'''if __name__ == '__main__':
    main()'''
