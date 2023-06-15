from PyQt5 import QtCore, QtGui, QtWidgets
from mapFromCSV import Ui_mapFromCSV 
from selectCOMIcon import Ui_selectCOM
from credits import Ui_Frame
import sys

class Ui_MainWindow(object):
    def openMapFromCSVWindow(self):
        self.window = QtWidgets.QFrame()
        self.ui = Ui_mapFromCSV()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openSelectCOMWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_selectCOM()
        self.ui.setupUi(self.window)
        self.window.show()

    def openCreditsWindow(self):
        self.window = QtWidgets.QFrame()
        self.ui = Ui_Frame()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        if sys.platform == 'win32':
            import ctypes
            app_id = 'mycompany.myapp.subapp.version'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 421)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./data/PipeView_Logo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.welcomeLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcomeLabel.sizePolicy().hasHeightForWidth())
        self.welcomeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(30)
        font.setBold(True)
        self.welcomeLabel.setFont(font)
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.verticalLayout.addWidget(self.welcomeLabel)
        self.chooseLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chooseLabel.sizePolicy().hasHeightForWidth())
        self.chooseLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        self.chooseLabel.setFont(font)
        self.chooseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.chooseLabel.setObjectName("chooseLabel")
        self.verticalLayout.addWidget(self.chooseLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.generateFromCSVButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openMapFromCSVWindow())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generateFromCSVButton.sizePolicy().hasHeightForWidth())
        self.generateFromCSVButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setKerning(True)
        self.generateFromCSVButton.setFont(font)
        self.generateFromCSVButton.setMouseTracking(False)
        self.generateFromCSVButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.generateFromCSVButton.setAutoFillBackground(False)
        self.generateFromCSVButton.setCheckable(False)
        self.generateFromCSVButton.setAutoDefault(True)
        self.generateFromCSVButton.setObjectName("generateFromCSVButton")
        self.horizontalLayout.addWidget(self.generateFromCSVButton)
        self.startMappingButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openSelectCOMWindow())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startMappingButton.sizePolicy().hasHeightForWidth())
        self.startMappingButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setKerning(True)
        self.startMappingButton.setFont(font)
        self.startMappingButton.setObjectName("startMappingButton")
        self.horizontalLayout.addWidget(self.startMappingButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 17))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.creditsButton = QtWidgets.QPushButton(MainWindow, clicked = lambda: self.openCreditsWindow())
        self.creditsButton.setObjectName("creditsButton")
        self.verticalLayout.addWidget(self.creditsButton)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PipeView"))
        self.welcomeLabel.setText(_translate("MainWindow", "Welcome to PipeView!"))
        self.chooseLabel.setText(_translate("MainWindow", "What do you want to do?"))
        self.generateFromCSVButton.setText(_translate("MainWindow", "Generate map\n"
"from .CSV File"))
        self.startMappingButton.setText(_translate("MainWindow", "Start Mapping\n"
"Process"))
        self.creditsButton.setText(_translate("MainWindow", "Credits"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())