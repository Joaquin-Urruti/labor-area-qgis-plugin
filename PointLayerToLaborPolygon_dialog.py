# -*- coding: utf-8 -*-
from qgis.PyQt import QtGui, QtWidgets, QtCore
from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt import uic
import os

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'PointLayerToLaborPolygon_dialog_base.ui'))

class PointLayerToLaborPolygonDialog(QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(PointLayerToLaborPolygonDialog, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, PointLayerToLaborPolygonDialogBase):
        PointLayerToLaborPolygonDialogBase.setObjectName("PointLayerToLaborPolygonDialogBase")
        PointLayerToLaborPolygonDialogBase.resize(532, 419)
        self.button_box = QtWidgets.QDialogButtonBox(PointLayerToLaborPolygonDialogBase)
        self.button_box.setGeometry(QtCore.QRect(340, 380, 161, 32))
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.button_box.setObjectName("button_box")
        self.comboBox = QtWidgets.QComboBox(PointLayerToLaborPolygonDialogBase)
        self.comboBox.setGeometry(QtCore.QRect(20, 40, 471, 21))
        self.comboBox.setObjectName("input_layer")
        self.lineEdit = QtWidgets.QLineEdit(PointLayerToLaborPolygonDialogBase)
        self.lineEdit.setGeometry(QtCore.QRect(30, 330, 351, 31))
        self.lineEdit.setObjectName("output_layer")
        self.pushButton = QtWidgets.QPushButton(PointLayerToLaborPolygonDialogBase)
        self.pushButton.setGeometry(QtCore.QRect(400, 330, 100, 32))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(PointLayerToLaborPolygonDialogBase)
        self.label.setGeometry(QtCore.QRect(30, 10, 451, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(PointLayerToLaborPolygonDialogBase)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 161, 31))
        self.label_2.setObjectName("label_2")
        self.labor_width = QtWidgets.QDoubleSpinBox(PointLayerToLaborPolygonDialogBase)
        self.labor_width.setGeometry(QtCore.QRect(30, 100, 151, 31))
        self.labor_width.setObjectName("labor_width")
        self.label_3 = QtWidgets.QLabel(PointLayerToLaborPolygonDialogBase)
        self.label_3.setGeometry(QtCore.QRect(30, 300, 181, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(PointLayerToLaborPolygonDialogBase)
        self.label_4.setGeometry(QtCore.QRect(30, 140, 161, 31))
        self.label_4.setObjectName("label_4")
        self.extra_distance = QtWidgets.QDoubleSpinBox(PointLayerToLaborPolygonDialogBase)
        self.extra_distance.setGeometry(QtCore.QRect(30, 170, 151, 31))
        self.extra_distance.setObjectName("extra_distance")
        self.label_5 = QtWidgets.QLabel(PointLayerToLaborPolygonDialogBase)
        self.label_5.setGeometry(QtCore.QRect(30, 210, 181, 31))
        self.label_5.setObjectName("label_5")
        self.simplification_level = QtWidgets.QSpinBox(PointLayerToLaborPolygonDialogBase)
        self.simplification_level.setGeometry(QtCore.QRect(30, 240, 151, 31))
        self.simplification_level.setObjectName("simplification_level")

        self.retranslateUi(PointLayerToLaborPolygonDialogBase)
        self.button_box.accepted.connect(PointLayerToLaborPolygonDialogBase.accept)
        self.button_box.rejected.connect(PointLayerToLaborPolygonDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(PointLayerToLaborPolygonDialogBase)

    def retranslateUi(self, PointLayerToLaborPolygonDialogBase):
        _translate = QtCore.QCoreApplication.translate
        PointLayerToLaborPolygonDialogBase.setWindowTitle(_translate("PointLayerToLaborPolygonDialogBase", "Convert points to labor area"))
        self.pushButton.setText(_translate("PointLayerToLaborPolygonDialogBase", "PushButton"))
        self.label.setText(_translate("PointLayerToLaborPolygonDialogBase", "Select labor point layer"))
        self.label_2.setText(_translate("PointLayerToLaborPolygonDialogBase", "Select the working width"))
        self.label_3.setText(_translate("PointLayerToLaborPolygonDialogBase", "Select output layer name"))
        self.label_4.setText(_translate("PointLayerToLaborPolygonDialogBase", "Select extra distance"))
        self.label_5.setText(_translate("PointLayerToLaborPolygonDialogBase", "Select simplification level"))
