from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtSerialPort import QSerialPortInfo
from mappingProcessNew import Ui_mappingProcess
import sys

class Ui_selectCOM(object):
    def scan_ports(self):
        ports = QSerialPortInfo.availablePorts()
        self.listWidget.clear()

        for port in ports:
            item = QListWidgetItem(port.portName())
            self.listWidget.addItem(item)
    
    def connectCOM(self):
        item = self.listWidget.currentItem()
        if item:
            self.window = QtWidgets.QFrame()
            self.ui = Ui_mappingProcess()
            self.ui.connectCOMPort(str(item.text()))
            self.ui.setupUi(self.window)
            self.ui.COMLabel.setText(str(item.text()))
            self.window.show()

    def setupUi(self, selectCOM):
        if sys.platform == 'win32':
            import ctypes
            app_id = 'mycompany.myapp.subapp.version'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

        selectCOM.setObjectName("selectCOM")
        selectCOM.resize(800, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./data/PipeView_Logo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        selectCOM.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(selectCOM)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.refreshCOMButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.scan_ports())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshCOMButton.sizePolicy().hasHeightForWidth())
        self.refreshCOMButton.setSizePolicy(sizePolicy)
        self.refreshCOMButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refreshCOMButton.setObjectName("refreshCOMButton")
        self.verticalLayout.addWidget(self.refreshCOMButton)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.connectCOMButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.connectCOM())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectCOMButton.sizePolicy().hasHeightForWidth())
        self.connectCOMButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.connectCOMButton.setFont(font)
        self.connectCOMButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.connectCOMButton.setObjectName("connectCOMButton")
        self.verticalLayout.addWidget(self.connectCOMButton)
        selectCOM.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(selectCOM)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menubar.setObjectName("menubar")
        selectCOM.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(selectCOM)
        self.statusbar.setObjectName("statusbar")
        selectCOM.setStatusBar(self.statusbar)

        self.retranslateUi(selectCOM)
        QtCore.QMetaObject.connectSlotsByName(selectCOM)

    def retranslateUi(self, selectCOM):
        _translate = QtCore.QCoreApplication.translate
        selectCOM.setWindowTitle(_translate("selectCOM", "PipeView"))
        self.label.setText(_translate("selectCOM", "Select the COM port where the device is connected to:"))
        self.refreshCOMButton.setText(_translate("selectCOM", "Refresh"))
        self.connectCOMButton.setText(_translate("selectCOM", "Connect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selectCOM = QtWidgets.QMainWindow()
    ui = Ui_selectCOM()
    ui.setupUi(selectCOM)
    selectCOM.show()
    sys.exit(app.exec_())