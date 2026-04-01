from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QCheckBox, QTextEdit, QVBoxLayout, QTableWidgetItem, QMessageBox
from PyQt6.QtGui import QTextCursor, QTextDocument, QFont
from PyQt6.QtCore import Qt
import sys, os
from scipy.interpolate import RegularGridInterpolator
import numpy as np
import re
from pathlib import Path

class Ui_Compensate(object):
    def setupUi(self, Compensate):
        Compensate.setObjectName("Compensate")
        Compensate.resize(878, 935)
        self.centralwidget = QtWidgets.QWidget(parent=Compensate)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 861, 901))
        self.tabWidget.setObjectName("tabWidget")
        self.codeTab = QtWidgets.QWidget()
        self.codeTab.setObjectName("codeTab")
        self.saveButton = QtWidgets.QPushButton(parent=self.codeTab)
        self.saveButton.setGeometry(QtCore.QRect(40, 140, 93, 28))
        self.saveButton.setObjectName("saveButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.codeTab)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 180, 761, 640))
        self.plainTextEdit.verticalScrollBar().setFixedWidth(25)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(700)
        font.setKerning(False)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.replaceWithEdit = QtWidgets.QLineEdit(parent=self.codeTab)
        self.replaceWithEdit.setGeometry(QtCore.QRect(580, 80, 113, 31))
        self.replaceWithEdit.setFont(font)
        self.replaceWithEdit.setObjectName("replaceWithEdit")
        self.showlinesCheckBox = QtWidgets.QCheckBox(parent=self.codeTab)
        self.showlinesCheckBox.setGeometry(QtCore.QRect(290, 93, 151, 20))
        self.showlinesCheckBox.setObjectName("showlinesCheckBox")
        self.verifyCheckBox = QtWidgets.QCheckBox(parent=self.codeTab)
        self.verifyCheckBox.setGeometry(QtCore.QRect(150, 93, 151, 20))
        self.verifyCheckBox.setObjectName("verifyCheckBox")
        self.textToFindEdit = QtWidgets.QLineEdit(parent=self.codeTab)
        self.textToFindEdit.setGeometry(QtCore.QRect(580, 41, 113, 31))
        self.textToFindEdit.setFont(font)
        self.textToFindEdit.setObjectName("textToFindEdit")
        self.saveLineEdit = QtWidgets.QLineEdit(parent=self.codeTab)
        self.saveLineEdit.setGeometry(QtCore.QRect(140, 140, 671, 31))
        self.saveLineEdit.setFont(font)
        self.saveLineEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.saveLineEdit.setObjectName("saveLineEdit")
        self.replaceAllButton = QtWidgets.QPushButton(parent=self.codeTab)
        self.replaceAllButton.setGeometry(QtCore.QRect(710, 80, 93, 28))
        self.replaceAllButton.setObjectName("replaceAllButton")
        self.replaceWithButton = QtWidgets.QPushButton(parent=self.codeTab)
        self.replaceWithButton.setGeometry(QtCore.QRect(470, 80, 93, 28))
        self.replaceWithButton.setObjectName("replaceWithButton")
        self.openButton = QtWidgets.QPushButton(parent=self.codeTab)
        self.openButton.setGeometry(QtCore.QRect(40, 50, 93, 28))
        self.openButton.setObjectName("openButton")
        self.findButton = QtWidgets.QPushButton(parent=self.codeTab)
        self.findButton.setGeometry(QtCore.QRect(470, 43, 93, 28))
        self.findButton.setObjectName("findButton")
        self.newButton = QtWidgets.QPushButton(parent=self.codeTab)
        self.newButton.setGeometry(QtCore.QRect(40, 90, 93, 28))
        self.newButton.setObjectName("newButton")
        self.restartButton = QPushButton(parent=self.codeTab)
        self.restartButton.setGeometry(QtCore.QRect(40, 10, 93, 28))
        self.restartButton.setObjectName("restartButton")
        self.restartButton.clicked.connect(self.restart_event_loop)
        self.restartButton.setVisible(False)
        self.autoCompCheckBox = QtWidgets.QCheckBox(parent=self.codeTab)
        self.autoCompCheckBox.setGeometry(QtCore.QRect(150, 53, 201, 20))
        self.autoCompCheckBox.setObjectName("autoCompCheckBox")
        self.tabWidget.addTab(self.codeTab, "")
        self.errorTab = QtWidgets.QWidget()
        self.errorTab.setObjectName("errorTab")
        self.XerrorMapTableWidget = QtWidgets.QTableWidget(parent=self.errorTab)
        self.XerrorMapTableWidget.setGeometry(QtCore.QRect(10, 240, 811, 271))
        self.XerrorMapTableWidget.setStyleSheet("")
        self.XerrorMapTableWidget.setWordWrap(False)
        self.XerrorMapTableWidget.setCornerButtonEnabled(False)
        self.XerrorMapTableWidget.setRowCount(5)
        self.XerrorMapTableWidget.setColumnCount(9)
        self.XerrorMapTableWidget.setObjectName("XerrorMapTableWidget")
        self.XerrorMapTableWidget.horizontalHeader().setVisible(False)
        self.XerrorMapTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.XerrorMapTableWidget.horizontalHeader().setDefaultSectionSize(75)
        self.XerrorMapTableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.XerrorMapTableWidget.horizontalHeader().setStretchLastSection(False)
        self.XerrorMapTableWidget.verticalHeader().setVisible(False)
        self.rowSpinBox = QtWidgets.QSpinBox(parent=self.errorTab)
        self.rowSpinBox.setGeometry(QtCore.QRect(340, 20, 111, 31))
        self.rowSpinBox.setProperty("value", 5)
        self.rowSpinBox.setObjectName("rowSpinBox")
        self.columnSpinBox = QtWidgets.QSpinBox(parent=self.errorTab)
        self.columnSpinBox.setGeometry(QtCore.QRect(120, 20, 111, 31))
        self.columnSpinBox.setProperty("value", 9)
        self.columnSpinBox.setObjectName("columnSpinBox")
        self.rowLabel = QtWidgets.QLabel(parent=self.errorTab)
        self.rowLabel.setGeometry(QtCore.QRect(260, 30, 61, 16))
        self.rowLabel.setObjectName("rowLabel")
        self.columnLabel = QtWidgets.QLabel(parent=self.errorTab)
        self.columnLabel.setGeometry(QtCore.QRect(24, 30, 81, 20))
        self.columnLabel.setObjectName("columnLabel")
        self.YerrorMapTableWidget = QtWidgets.QTableWidget(parent=self.errorTab)
        self.YerrorMapTableWidget.setGeometry(QtCore.QRect(10, 580, 811, 271))
        self.YerrorMapTableWidget.setStyleSheet("")
        self.YerrorMapTableWidget.setWordWrap(False)
        self.YerrorMapTableWidget.setCornerButtonEnabled(False)
        self.YerrorMapTableWidget.setRowCount(5)
        self.YerrorMapTableWidget.setColumnCount(9)
        self.YerrorMapTableWidget.setObjectName("YerrorMapTableWidget")
        self.YerrorMapTableWidget.horizontalHeader().setVisible(False)
        self.YerrorMapTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.YerrorMapTableWidget.horizontalHeader().setDefaultSectionSize(75)
        self.YerrorMapTableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.YerrorMapTableWidget.horizontalHeader().setStretchLastSection(False)
        self.YerrorMapTableWidget.verticalHeader().setVisible(False)
        self.XerrorLabel = QtWidgets.QLabel(parent=self.errorTab)
        self.XerrorLabel.setGeometry(QtCore.QRect(10, 210, 101, 16))
        self.XerrorLabel.setObjectName("XerrorLabel")
        self.Yerrorlabel = QtWidgets.QLabel(parent=self.errorTab)
        self.Yerrorlabel.setGeometry(QtCore.QRect(20, 550, 71, 16))
        self.Yerrorlabel.setObjectName("Yerrorlabel")
        self.rowLabel_2 = QtWidgets.QLabel(parent=self.errorTab)
        self.rowLabel_2.setGeometry(QtCore.QRect(260, 70, 81, 16))
        self.rowLabel_2.setObjectName("rowLabel_2")
        self.maxYlineEdit = QtWidgets.QLineEdit(parent=self.errorTab)
        self.maxYlineEdit.setGeometry(QtCore.QRect(340, 70, 113, 22))
        self.maxYlineEdit.setObjectName("maxYlineEdit")
        self.YstepLineEdit = QtWidgets.QLineEdit(parent=self.errorTab)
        self.YstepLineEdit.setGeometry(QtCore.QRect(340, 100, 113, 22))
        self.YstepLineEdit.setObjectName("YstepLineEdit")
        self.rowLabel_3 = QtWidgets.QLabel(parent=self.errorTab)
        self.rowLabel_3.setGeometry(QtCore.QRect(260, 100, 81, 16))
        self.rowLabel_3.setObjectName("rowLabel_3")
        self.columnLabel_3 = QtWidgets.QLabel(parent=self.errorTab)
        self.columnLabel_3.setGeometry(QtCore.QRect(40, 100, 81, 16))
        self.columnLabel_3.setObjectName("columnLabel_3")
        self.minXlineEdit = QtWidgets.QLineEdit(parent=self.errorTab)
        self.minXlineEdit.setGeometry(QtCore.QRect(120, 68, 113, 22))
        self.minXlineEdit.setObjectName("minXlineEdit")
        self.XstepLineEdit = QtWidgets.QLineEdit(parent=self.errorTab)
        self.XstepLineEdit.setGeometry(QtCore.QRect(120, 100, 113, 22))
        self.XstepLineEdit.setObjectName("XstepLineEdit")
        self.columnLabel_2 = QtWidgets.QLabel(parent=self.errorTab)
        self.columnLabel_2.setGeometry(QtCore.QRect(40, 70, 81, 16))
        self.columnLabel_2.setObjectName("columnLabel_2")
        self.loadMapsButton = QtWidgets.QPushButton(parent=self.errorTab)
        self.loadMapsButton.setGeometry(QtCore.QRect(20, 140, 93, 28))
        self.loadMapsButton.setObjectName("loadMapsButton")
        self.saveMapsButton = QtWidgets.QPushButton(parent=self.errorTab)
        self.saveMapsButton.setGeometry(QtCore.QRect(20, 170, 93, 28))
        self.saveMapsButton.setObjectName("saveMapsButton")
        self.mapFileLineEdit = QtWidgets.QLineEdit(parent=self.errorTab)
        self.mapFileLineEdit.setGeometry(QtCore.QRect(140, 140, 671, 31))
        self.mapFileLineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.mapFileLineEdit.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.mapFileLineEdit.setObjectName("mapFileLineEdit")
        self.mapFileLineEdit.setFont(font)
        self.unitsGroupBox = QtWidgets.QGroupBox(parent=self.errorTab)
        self.unitsGroupBox.setGeometry(QtCore.QRect(480, 20, 171, 41))
        self.unitsGroupBox.setObjectName("unitsGroupBox")
        self.mmRadioButton = QtWidgets.QRadioButton(parent=self.unitsGroupBox)
        self.mmRadioButton.setGeometry(QtCore.QRect(20, 20, 95, 20))
        self.mmRadioButton.setObjectName("mmRadioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(Compensate)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.mmRadioButton)
        self.inRadioButton = QtWidgets.QRadioButton(parent=self.unitsGroupBox)
        self.inRadioButton.setGeometry(QtCore.QRect(100, 20, 95, 20))
        self.inRadioButton.setObjectName("inRadioButton")
        self.buttonGroup.addButton(self.inRadioButton)
        self.tabWidget.addTab(self.errorTab, "")
        Compensate.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Compensate)
        self.statusbar.setObjectName("statusbar")
        Compensate.setStatusBar(self.statusbar)
        self.retranslateUi(Compensate)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Compensate)

    def restart_event_loop(self):
        # Exit the current event loop
        QApplication.exit()
        # Restart the event loop
        # QApplication.exec()

    def retranslateUi(self, Compensate):
        _translate = QtCore.QCoreApplication.translate
        Compensate.setWindowTitle(_translate("Compensate", "2DCompensate"))
        self.saveButton.setText(_translate("Compensate", "Save"))
        self.showlinesCheckBox.setText(_translate("Compensate", "Show line numbers"))
        self.verifyCheckBox.setText(_translate("Compensate", "Verify calculations"))
        self.replaceAllButton.setText(_translate("Compensate", "Replace all"))
        self.replaceWithButton.setText(_translate("Compensate", "Replace with:"))
        self.openButton.setText(_translate("Compensate", "Open"))
        self.findButton.setText(_translate("Compensate", "Find:"))
        self.newButton.setText(_translate("Compensate", "Compensate"))
        self.restartButton.setText(_translate("Compensate", "Restart"))
        self.autoCompCheckBox.setText(_translate("Compensate", "Compensate automatically"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.codeTab), _translate("Compensate", "Code"))
        self.rowLabel.setText(_translate("Compensate", "Rows: (Y)"))
        self.columnLabel.setText(_translate("Compensate", "Coluimns (X)"))
        self.XerrorLabel.setText(_translate("Compensate", "X errors"))
        self.Yerrorlabel.setText(_translate("Compensate", "Y errors"))
        self.rowLabel_2.setText(_translate("Compensate", "Maximum Y:"))
        self.maxYlineEdit.setText(_translate("Compensate", "508"))
        self.YstepLineEdit.setText(_translate("Compensate", "254"))
        self.rowLabel_3.setText(_translate("Compensate", "Y step:"))
        self.columnLabel_3.setText(_translate("Compensate", "X step:"))
        self.minXlineEdit.setText(_translate("Compensate", "-1016"))
        self.XstepLineEdit.setText(_translate("Compensate", "254"))
        self.columnLabel_2.setText(_translate("Compensate", "Minimum X:"))
        self.loadMapsButton.setText(_translate("Compensate", "Load maps"))
        self.saveMapsButton.setText(_translate("Compensate", "Save maps"))
        self.unitsGroupBox.setTitle(_translate("Compensate", "Units:"))
        self.mmRadioButton.setText(_translate("Compensate", "mm"))
        self.inRadioButton.setText(_translate("Compensate", "in"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.errorTab), _translate("Compensate", "Error map"))

nc_file = 'c:/data/119/48grid.nc'
new_file = f'compensated_{nc_file}'
text_modified = False
compensate_enabled = False
error_units = 'mm'
win = Ui_Compensate()

# Define grid points for CNC coordinates
x = np.array([-1016,-762,-508,-254,0,254,508,762,1016])  # X-coordinates
y = np.array([-508,-254,0,254,508])  # Y-coordinates
grid_points = (x,y)
# print(grid_points)

x_errors = np.array([[0.000000,0.000000,0.000000,0.000000,0.000000],
                     [0.000000,0.000000,0.000000,0.000000,0.000000],
                     [0.000000,0.000000,0.000000,0.000000,0.000000],
                     [0.000000,0.000000,0.000000,0.000000,0.000000],
                     [0.000000,0.000000,0.000000,0.000000,0.000000],
                     [0.000000,0.000000,0.000000,0.000000,0.000000],
                     [0.000000,0.000000,0.000000,0.000000,0.000000],
                     [0.000000,0.000000,0.000000,0.000000,0.000000],
                     [0.000000,0.000000,0.000000,0.000000,0.000000]])

y_errors = np.array([[0.000000,0.000000,0.000000,0.000000,0.000000],
                     [0.000000,0.000000,0.000000,0.000000,0.000000],
                     [0.000000,0.000000,0.000000,0.000000,0.000000],
                     [0.000000,0.000000,0.000000,0.000000,0.000000],
                     [0.000000,0.000000,0.000000,0.000000,0.000000],
                     [0.000000,0.000000,0.000000,0.000000,0.000000],
                     [0.000000,0.000000,0.000000,0.000000,0.000000],
                     [0.000000,0.000000,0.000000,0.000000,0.000000],
                     [0.000000,0.000000,0.000000,0.000000,0.000000]])

# x_errors = np.array([[-1.587500,-1.587500,-1.587500,-2.381250,-0.793750],
#                      [0.000000,-0.793750,0.000000,-2.381250,0.000000],
#                      [0.000000,0.000000,0.000000,-1.587500,-1.587500],
#                      [0.000000,0.000000,0.793750,-1.587500,0.000000],
#                      [0.000000,0.000000,0.000000,0.000000,0.000000],
#                      [0.000000,0.000000,0.000000,1.587500,0.793750],
#                      [0.000000,0.000000,0.000000,1.587500,0.793750],
#                      [0.000000,0.000000,-0.396875,0.793750,0.000000],
#                      [-1.587500,-1.587500,-0.793750,0.793750,0.793750]])

# y_errors = np.array([[-0.793750,0.000000,0.000000,0.000000,-1.587500],
#                      [-1.587500,-0.793750,0.000000,0.000000,-1.587500],
#                      [-3.175000,-1.587500,0.000000,0.000000,-1.587500],
#                      [-3.175000,-1.587500,0.000000,-1.587500,-3.175000],
#                      [-3.175000,-1.587500,0.000000,-0.793750,-3.175000],
#                      [-2.381250,-1.587500,0.000000,-1.587500,-3.175000],
#                      [-3.175000,-1.587500,0.000000,-1.587500,-3.175000],
#                      [-1.587500,0.000000,0.000000,-1.587500,-3.175000],
#                      [-0.793750,0.000000,0.000000,-1.587500,-3.175000]])

# print(f'X errors:\n{x_errors.T}')
# print(f'Y errors:\n{y_errors.T}')

def compensate(nc_file, new_file):
    global text_modified, error_units
    # , interp_func_x, interp_func_y
    ui.plainTextEdit.clear()
    ui.plainTextEdit.insertPlainText(f'({new_file})\n')
    line_index = 0
    with open(nc_file) as ncfile:
        with open(new_file, 'w') as newfile:
            newfile.write(f'({new_file})\n')
            current_x = None
            current_y = None
            for line in ncfile:
                if 'G21' in line:
                    # print('gcode is in mm')
                    code_units = 'mm'
                    if code_units != error_units:
                        r = QMessageBox.information(ui.saveMapsButton, 'Info', 'unit mismatch detected! Aborting!', buttons = QMessageBox.StandardButton.Ok)
                        # print("unit mismatch detected! Aborting!")
                        r = ''
                        break
                elif 'G20' in line:
                    # print('gcode is in inches')
                    code_units = 'in'
                    if code_units != error_units:
                        r = QMessageBox.information(ui.saveMapsButton, 'Info', 'unit mismatch detected! Aborting!', buttons = QMessageBox.StandardButton.Ok)
                        r = ''
                        break
                line_index += 1
                new_line = line
                # print(line)
                matchx = re.search(r'X([-+]?\d*\.\d+|\d+)', line)
                matchy = re.search(r'Y([-+]?\d*\.\d+|\d+)', line)
                if matchx:
                    current_x = float(matchx.group(1))
                    cx = 'X' + f'{current_x:.3f}'
                if matchy:
                    current_y = float(matchy.group(1))
                    cy = 'Y' + f'{current_y:.3f}'
                if matchx:
                    coordinate = np.array([float(current_x), float(current_y)])
                    x_error = interp_func_x(coordinate).item()
                    # x_error = x_error[0]
                    if current_x <= 0:
                        compensated_x = (current_x + x_error)
                        x_line = f'X {compensated_x:.3f} = {current_x:.3f} + {x_error:.3f}'
                    else:
                        compensated_x = (current_x - x_error)
                        x_line = f'X {compensated_x:.3f} = {current_x:.3f} - {x_error:.3f}'
                    # print(x_line)
                    comped_x = compensated_x
                    new_line = new_line.replace(cx, f'X{comped_x:.3f}')
                    if ui.verifyCheckBox.isChecked():
                        new_line = f'{new_line.rstrip()}\n( --> {x_line})\r'
                if matchy:
                    coordinate = np.array([float(current_x), float(current_y)])
                    y_error = interp_func_y(coordinate).item()
                    if current_y <= 0:
                        compensated_y = (current_y + y_error)
                        y_line = f'Y {compensated_y:.3f} = {current_y:.3f} + {y_error:.3f}'
                    else:
                        compensated_y = (current_y - y_error)                    
                        y_line = f'Y {compensated_y:.3f} = {current_y:.3f} - {y_error:.3f}'
                    # print(y_line)
                    comped_y = compensated_y
                    new_line = new_line.replace(cy, f'Y{comped_y:.3f}')
                    if ui.verifyCheckBox.isChecked():
                        new_line = f'{new_line.rstrip()}\n( --> {y_line})\r'
                if ui.showlinesCheckBox.isChecked():
                   numbered_line = f'{line_index}: {new_line}'
                   # ui.plainTextEdit.insertPlainText(new_line.rstrip())
                   ui.plainTextEdit.insertPlainText(numbered_line)
                else:
                    ui.plainTextEdit.insertPlainText(new_line)
                newfile.write(new_line)
            ui.saveLineEdit.setText(new_file)
            text_modified = False
            ui.saveButton.setEnabled(False)

def load_file(f):
    global text_modified
    ui.plainTextEdit.clear()
    ui.plainTextEdit.insertPlainText(f'({f})\n')
    line_index = 0
    with open(f) as ncfile:
        for line in ncfile:
            line_index += 1
            if ui.showlinesCheckBox.isChecked():
                line = f'{line_index}: {line}'
            ui.plainTextEdit.insertPlainText(line)
    ui.saveLineEdit.setText(f)
    text_modified = False
    ui.saveButton.setEnabled(False)

def get_file():
    global nc_file, new_file
    file_name, _ = QFileDialog.getOpenFileName(ui.openButton, 'Open File', '', 'CNC Files ( *.gcode *.nc *.txt)')
    if file_name:
        ui.plainTextEdit.textChanged.disconnect(set_modified_flag)
        load_file(file_name)
        if ui.autoCompCheckBox.isChecked():
            n1 = Path(file_name)
            n1 = n1.stem
            n2 = n1 + '_compensated'
            nc_file = file_name
            new_file = nc_file.replace(n1, n2)
            compensate(file_name, new_file)
        ui.plainTextEdit.textChanged.connect(set_modified_flag)

def save_file():
    global new_file, text_modified
    save_name = ui.saveLineEdit.text()
    if save_name:
        with open(save_name, 'w') as f:
            f.write(ui.plainTextEdit.toPlainText())
        print(f'File saved as: {save_name}')
        ui.saveButton.setEnabled(False)
        text_modified = False

def set_modified_flag():
    global text_modified
    text_modified = True
    ui.saveButton.setEnabled(True)
    # print("Text modified flag set to True")  

def set_cursor_to_end():
    cursor = ui.plainTextEdit.textCursor()
    # cursor.moveCursor(QTextCursor.End)
    # print(cursor)

def set_error_map_column_headers():
    header_start = float(ui.minXlineEdit.text())
    header_step = float(ui.XstepLineEdit.text())
    for i in range(ui.XerrorMapTableWidget.columnCount()):
        header_value = header_start + i * header_step
        header_item = QTableWidgetItem(str(header_value))
        ui.XerrorMapTableWidget.setHorizontalHeaderItem(i, header_item)
    for i in range(ui.YerrorMapTableWidget.columnCount()):
        header_value = header_start + i * header_step
        header_item = QTableWidgetItem(str(header_value))
        ui.YerrorMapTableWidget.setHorizontalHeaderItem(i, header_item)
    header_start = float(ui.maxYlineEdit.text())
    header_step = -float(ui.YstepLineEdit.text())
    for i in range(ui.XerrorMapTableWidget.rowCount()):
        header_value = header_start + i * header_step
        header_item = QTableWidgetItem(str(header_value))
        ui.XerrorMapTableWidget.setVerticalHeaderItem(i, header_item)
    for i in range(ui.YerrorMapTableWidget.rowCount()):
        header_value = header_start + i * header_step
        header_item = QTableWidgetItem(str(header_value))
        ui.YerrorMapTableWidget.setVerticalHeaderItem(i, header_item)

def set_error_map_table_sizes():
    ui.XerrorMapTableWidget.setRowCount(ui.rowSpinBox.value())
    ui.XerrorMapTableWidget.setColumnCount(ui.columnSpinBox.value())
    ui.YerrorMapTableWidget.setRowCount(ui.rowSpinBox.value())
    ui.YerrorMapTableWidget.setColumnCount(ui.columnSpinBox.value())
    set_error_map_column_headers()

def save_error_maps():
    global error_units
    if ui.mmRadioButton.isDown():
        error_units = 'mm'
    else:
        error_units = 'in'
    out_file = ui.mapFileLineEdit.text()
    if os.path.exists(out_file) == True:
        reply = QMessageBox.question(ui.saveMapsButton, 'File exists', f'The file "{out_file}" already exists. Do you want to overwrite it?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.No:
            return
    with open(out_file, 'w') as map_file:
        map_file.write(f'X error map: {error_units}\n')
        columns = ui.XerrorMapTableWidget.columnCount()
        rows = ui.XerrorMapTableWidget.rowCount()
        header = '          '
        for column in range(columns):
            header += f' {ui.XerrorMapTableWidget.horizontalHeaderItem(column).text():>10}'
        # print(header)
        map_file.write(f'{header}\n')
        for row in range(rows):
            row_data = f'{ui.XerrorMapTableWidget.verticalHeaderItem(row).text():>10}'
            for column in range(columns):            
                item = ui.XerrorMapTableWidget.item(row, column)
                cell_value = item.text() if item else ' '
                row_data += f' {str(cell_value):>10}'
            # print(row_data)
            map_file.write(f'{row_data}\n')

        map_file.write(f'\nY error map: {error_units}\n')
        columns = ui.YerrorMapTableWidget.columnCount()
        rows = ui.YerrorMapTableWidget.rowCount()
        header = '          '
        for column in range(columns):
            header += f' {ui.YerrorMapTableWidget.horizontalHeaderItem(column).text():>10}'
        # print(header)
        map_file.write(f'{header}\n')
        for row in range(rows):
            row_data = f'{ui.YerrorMapTableWidget.verticalHeaderItem(row).text():>10}'
            for column in range(columns):            
                item = ui.YerrorMapTableWidget.item(row, column)
                cell_value = item.text() if item else ' '
                row_data += f' {str(cell_value):>10}'
            # print(row_data)
            map_file.write(f'{row_data}\n')

def load_error_maps():
    global grid_points, x_errors, y_errors, error_units
    in_file = ui.mapFileLineEdit.text()
    if os.path.exists(in_file) == False:
        in_file = 'error_maps.txt'
        ui.mapFileLineEdit.setText('error_maps.txt')
        reply = QMessageBox.information(ui.saveMapsButton, 'Info', 'Error map file set to default: error_maps.txt', buttons = QMessageBox.StandardButton.Ok)
    with open(in_file, 'r') as map_file:
        rows = map_file.readlines()
        # print(rows)
        test_line = rows[0].strip()
        if 'mm' in test_line:
            error_units = 'mm'
            ui.mmRadioButton.setChecked(True)
        else:
            error_units = 'in'
            ui.inRadioButton.setChecked(True)
        # print(f'First line: {test_line}')
        if 'X error map:' in test_line:
            # print('Loading X error map...')
            x_error_list = []
            # Process X error map
            num_columns = ui.XerrorMapTableWidget.columnCount()
            num_rows = ui.XerrorMapTableWidget.rowCount()
            horizontal_header = rows[1].strip().split()
            ui.XerrorMapTableWidget.setHorizontalHeaderLabels(horizontal_header)
            for i in range(num_rows):
                row_data = rows[i + 2].strip().split()
                x_error_list.append(row_data[1:num_columns+2])
                ui.XerrorMapTableWidget.setVerticalHeaderItem(i, QTableWidgetItem(row_data[0]))
                for j in range(num_columns):
                    ui.XerrorMapTableWidget.setItem(i, j, QTableWidgetItem(row_data[j + 1]))
                    x_error_list[i][j] = float(row_data[j + 1])
                # add column for sorting:
                x_error_list[i].append(i)
            ui.XerrorMapTableWidget.horizontalHeader().setVisible(True)
            ui.XerrorMapTableWidget.verticalHeader().setVisible(True)
            ui.XerrorMapTableWidget.setCurrentCell(0, 0)
            x_np = np.array(x_error_list)
            sorted_index = np.argsort(-x_np[:, num_columns])
            sorted_x_np = x_np[sorted_index]
            # delete sorting column:
            sorted_x_np = np.delete(sorted_x_np, -1, axis=1)
            # print(f'Sorted X error map:\n{sorted_x_np.T}')
            x_errors = sorted_x_np.T

            test_line = rows[num_rows + 3].strip()
            # print(test_line)
            y_error_list = []
            ui.YerrorMapTableWidget.setHorizontalHeaderLabels(horizontal_header)
            for i in range(num_rows):
                row_data = rows[i + 5 + num_rows].strip().split()
                y_error_list.append(row_data[1:num_columns+2])
                # print(f'Row {i} data: {row_data}')
                ui.YerrorMapTableWidget.setVerticalHeaderItem(i, QTableWidgetItem(row_data[0]))
                for j in range(num_columns):
                    ui.YerrorMapTableWidget.setItem(i, j, QTableWidgetItem(row_data[j + 1]))
                    y_error_list[i][j] = float(row_data[j + 1])
                # add column for sorting:
                y_error_list[i].append(i)                  
            ui.YerrorMapTableWidget.horizontalHeader().setVisible(True)
            ui.YerrorMapTableWidget.verticalHeader().setVisible(True)
            y_np = np.array(y_error_list)
            sorted_index = np.argsort(-y_np[:, num_columns])
            sorted_y_np = y_np[sorted_index]
            # delete sorting column:
            sorted_y_np = np.delete(sorted_y_np, -1, axis=1)
            # print(f'Sorted Y error map:\n{sorted_y_np.T}')
            y_errors = sorted_y_np.T
    ui.restartButton.click()

def do_compensate():
    ui.autoCompCheckBox.setChecked(True)
    get_file()
    ui.autoCompCheckBox.setChecked(False)

def find_text():
    text_to_find = ui.textToFindEdit.text()
    if not text_to_find:
        return
    cursor = ui.plainTextEdit.textCursor()
    found = ui.plainTextEdit.document().find(text_to_find, cursor)
    if found.isNull():
        # If not found, start from the beginning
        cursor.setPosition(0)
        print('Wrapping search to the beginning of the document.')
        found = ui.plainTextEdit.document().find(text_to_find, cursor)
    if not found.isNull():
        ui.plainTextEdit.setTextCursor(found)

def replace_text():
    replace_string = ui.replaceWithEdit.text()
    if not replace_string:
        return
    ui.plainTextEdit.insertPlainText(replace_string)  

def replace_all():
    count = 0
    text_to_find = ui.textToFindEdit.text()
    replace_string = ui.replaceWithEdit.text()
    if not text_to_find or not replace_string:
        reply = QMessageBox.information(ui.replaceAllButton, 'Info', 'Need both text to find and replace with', buttons = QMessageBox.StandardButton.Ok)
        return reply
    cursor = ui.plainTextEdit.textCursor()
    cursor.setPosition(0)
    cursor.beginEditBlock()
    flags = QTextDocument.FindFlag.FindCaseSensitively
    doc_cursor = ui.plainTextEdit.document().find(text_to_find, cursor, flags)
    while not doc_cursor.isNull():
        doc_cursor.insertText(replace_string)
        count += 1
        doc_cursor = ui.plainTextEdit.document().find(text_to_find, doc_cursor, flags)
    cursor.endEditBlock()
    reply = QMessageBox.information(ui.replaceAllButton, 'Info', f'Replaced {count} occurrences of "{text_to_find}" with "{replace_string}".', buttons = QMessageBox.StandardButton.Ok)

def get_map_file():
    global nc_file, new_file
    file_name, _ = QFileDialog.getOpenFileName(ui.openButton, 'Open File', '', 'Map Files (*.txt)')
    if file_name:
        ui.mapFileLineEdit.setText(file_name)
        load_error_maps()

def create_interpolator(grid, values):
    interp_func = RegularGridInterpolator(grid, values, method='linear', bounds_error=False, fill_value=None)
    return interp_func

app = QtWidgets.QApplication(sys.argv)
Compensate = QtWidgets.QMainWindow()
ui = Ui_Compensate()
ui.setupUi(Compensate)
ui.openButton.clicked.connect(get_file)
ui.saveButton.clicked.connect(save_file)
ui.newButton.clicked.connect(do_compensate)
ui.findButton.clicked.connect(find_text)
ui.replaceWithButton.clicked.connect(replace_text)
ui.replaceAllButton.clicked.connect(replace_all)

ui.rowSpinBox.valueChanged.connect(set_error_map_table_sizes)
ui.columnSpinBox.valueChanged.connect(set_error_map_table_sizes)

ui.minXlineEdit.textChanged.connect(set_error_map_table_sizes)
ui.XstepLineEdit.textChanged.connect(set_error_map_table_sizes)

ui.maxYlineEdit.textChanged.connect(set_error_map_table_sizes)
ui.YstepLineEdit.textChanged.connect(set_error_map_table_sizes)

ui.autoCompCheckBox.setChecked(True)

ui.saveMapsButton.clicked.connect(save_error_maps)
ui.loadMapsButton.clicked.connect(get_map_file)

ui.saveLineEdit.textChanged.connect(set_modified_flag)
ui.plainTextEdit.textChanged.connect(set_modified_flag)

ui.mapFileLineEdit.setText('error_maps.txt')

load_error_maps()

interp_func_x = create_interpolator(grid_points, x_errors)
interp_func_y = create_interpolator(grid_points, y_errors)

# Define new CNC coordinates to test compensation values
# test_coords = np.array([-254, 254])
# y_compensation_values = interp_func_y(test_coords)
# x_compensation_values = interp_func_x(test_coords)
# compensation_values = list(zip(x_compensation_values, y_compensation_values))
# print("Compensation values:", compensation_values)

Compensate.show()

keep_running = True
while keep_running:
    app.exec()
    # print('Coming up for air...')
    interp_func_x = create_interpolator(grid_points, x_errors)
    interp_func_y = create_interpolator(grid_points, y_errors)
    # print('Interpolators reset.')
