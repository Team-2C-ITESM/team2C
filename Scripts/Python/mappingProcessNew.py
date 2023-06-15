from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import os
from PyQt5.QtCore import QObject
from DireccionCSV import generateDirectionCSV
import serial
import sys
import DireccionCSV
from DireccionCSV import *

class Worker(QObject):
    finished = pyqtSignal()

    def __init__(self, ser):
        super().__init__()
        self.ser = ser

    def do_work(self):
        DireccionCSV.run = True
        generateDirectionCSV(self.ser)

        self.finished.emit()  # emit the finished signal when the loop is done
    
    def stop(self):
        DireccionCSV.run = False  # set the run condition to false on stop
        DireccionCSV.distance = 0.0

class Ui_mappingProcess(QtWidgets.QMainWindow):
    stop_signal = pyqtSignal()

    def openCamApp(self):
        cwd = os.getcwd()
        cwd += '\data\FSC_player_en.exe'
        os.popen(cwd)

    def connectCOMPort(self,serialPort):
        self.ser = serial.Serial(serialPort, 115200)

    def moveServos(self,command):
        self.ser.write(command.encode())
    
    def changeAngleServoTwo(self,angle):
        if 60 >= int(self.currentDegreesLabel.text()) + angle >= -60:
            self.currentDegreesLabel.setText(str(int(self.currentDegreesLabel.text())+angle))
            self.moveServos('2'+','+self.currentDegreesLabel.text()+'\n')
    
    def changeMovement(self,val):
        if DireccionCSV.run:
            DireccionCSV.distance = val

    def start_loop(self):
        self.worker_thread.start()

    def stop_loop(self):
        self.worker_thread.requestInterruption()

    def closeWindow(self,mappingProcess):
        self.ser.close()
        mappingProcess.close()

    def setupUi(self, mappingProcess):
        mappingProcess.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        
        if sys.platform == 'win32':
            import ctypes
            app_id = 'mycompany.myapp.subapp.version'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

        mappingProcess.setObjectName("mappingProcess")
        mappingProcess.resize(582, 508)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./data/PipeView_Logo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mappingProcess.setWindowIcon(icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mappingProcess.sizePolicy().hasHeightForWidth())
        mappingProcess.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(mappingProcess)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(mappingProcess)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.COMLabel = QtWidgets.QLabel(mappingProcess)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        self.COMLabel.setFont(font)
        self.COMLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.COMLabel.setObjectName("COMLabel")
        self.verticalLayout.addWidget(self.COMLabel)
        self.openCamButton = QtWidgets.QPushButton(mappingProcess, clicked = lambda: self.openCamApp())
        self.openCamButton.setObjectName("openCamButton")
        self.verticalLayout.addWidget(self.openCamButton)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        # self.startLogButton = QtWidgets.QPushButton(mappingProcess, clicked = lambda: self.start_loop())
        self.startLogButton = QtWidgets.QPushButton(mappingProcess)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startLogButton.sizePolicy().hasHeightForWidth())
        self.startLogButton.setSizePolicy(sizePolicy)
        self.startLogButton.setObjectName("startLogButton")
        self.horizontalLayout_5.addWidget(self.startLogButton)
        self.stopLogButton = QtWidgets.QPushButton(mappingProcess)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopLogButton.sizePolicy().hasHeightForWidth())
        self.stopLogButton.setSizePolicy(sizePolicy)
        self.stopLogButton.setObjectName("stopLogButton")
        self.horizontalLayout_5.addWidget(self.stopLogButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startMovButton = QtWidgets.QPushButton(mappingProcess, clicked = lambda: self.changeMovement(0.1))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startMovButton.sizePolicy().hasHeightForWidth())
        self.startMovButton.setSizePolicy(sizePolicy)
        self.startMovButton.setObjectName("startMovButton")
        self.horizontalLayout.addWidget(self.startMovButton)
        self.stopMovButton = QtWidgets.QPushButton(mappingProcess, clicked = lambda: self.changeMovement(0.0))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopMovButton.sizePolicy().hasHeightForWidth())
        self.stopMovButton.setSizePolicy(sizePolicy)
        self.stopMovButton.setObjectName("stopMovButton")
        self.horizontalLayout.addWidget(self.stopMovButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lessDegreesButton = QtWidgets.QPushButton(mappingProcess, clicked = lambda: self.changeAngleServoTwo(-15))
        self.lessDegreesButton.setObjectName("lessDegreesButton")
        self.horizontalLayout_2.addWidget(self.lessDegreesButton)
        self.currentDegreesLabel = QtWidgets.QLabel(mappingProcess)
        self.currentDegreesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentDegreesLabel.setObjectName("currentDegreesLabel")
        self.horizontalLayout_2.addWidget(self.currentDegreesLabel)
        self.moreDegreesButton = QtWidgets.QPushButton(mappingProcess, clicked = lambda: self.changeAngleServoTwo(+15))
        self.moreDegreesButton.setObjectName("moreDegreesButton")
        self.horizontalLayout_2.addWidget(self.moreDegreesButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(180, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.horizontalLayout_4.addItem(spacerItem)
        self.prototypeImageLabel = QtWidgets.QLabel(mappingProcess)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prototypeImageLabel.sizePolicy().hasHeightForWidth())
        self.prototypeImageLabel.setSizePolicy(sizePolicy)
        self.prototypeImageLabel.setText("")
        self.prototypeImageLabel.setPixmap(QtGui.QPixmap("./data/PrototypeCrop.png"))
        self.prototypeImageLabel.setScaledContents(True)
        self.prototypeImageLabel.setObjectName("prototypeImageLabel")
        self.horizontalLayout_4.addWidget(self.prototypeImageLabel)
        spacerItem1 = QtWidgets.QSpacerItem(180, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.minusNinetyDegreesButton = QtWidgets.QPushButton(mappingProcess, clicked = lambda: self.moveServos("1,-90\n"))
        self.minusNinetyDegreesButton.setObjectName("minusNinetyDegreesButton")
        self.horizontalLayout_3.addWidget(self.minusNinetyDegreesButton)
        self.minusFourtyFiveDegreesButton = QtWidgets.QPushButton(mappingProcess, clicked = lambda: self.moveServos("1,-45\n"))
        self.minusFourtyFiveDegreesButton.setObjectName("minusFourtyFiveDegreesButton")
        self.horizontalLayout_3.addWidget(self.minusFourtyFiveDegreesButton)
        self.zeroDegreesButton = QtWidgets.QPushButton(mappingProcess, clicked = lambda: self.moveServos("1,0\n"))
        self.zeroDegreesButton.setObjectName("zeroDegreesButton")
        self.horizontalLayout_3.addWidget(self.zeroDegreesButton)
        self.fourtyFiveDegreesButton = QtWidgets.QPushButton(mappingProcess, clicked = lambda: self.moveServos("1,45\n"))
        self.fourtyFiveDegreesButton.setObjectName("fourtyFiveDegreesButton")
        self.horizontalLayout_3.addWidget(self.fourtyFiveDegreesButton)
        self.ninetyDegreesButton = QtWidgets.QPushButton(mappingProcess, clicked = lambda: self.moveServos("1,90\n"))
        self.ninetyDegreesButton.setObjectName("ninetyDegreesButton")
        self.horizontalLayout_3.addWidget(self.ninetyDegreesButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.closeWindowButton = QtWidgets.QPushButton(mappingProcess, clicked = lambda: self.closeWindow(mappingProcess))
        self.closeWindowButton.setObjectName("closeWindowButton")
        self.verticalLayout.addWidget(self.closeWindowButton)

        self.retranslateUi(mappingProcess)
        QtCore.QMetaObject.connectSlotsByName(mappingProcess)

        # Thread:
        self.thread = QThread()
        self.worker = Worker(self.ser)
        self.stop_signal.connect(self.worker.stop)  # connect stop signal to worker stop method
        self.worker.moveToThread(self.thread)

        self.worker.finished.connect(self.thread.quit)  # connect the workers finished signal to stop thread

        self.thread.started.connect(self.worker.do_work)
        self.thread.finished.connect(self.worker.stop)

        # Start Button action:
        self.startLogButton.clicked.connect(self.thread.start)

        # Stop Button action:
        self.stopLogButton.clicked.connect(self.stop_thread)

    def retranslateUi(self, mappingProcess):
        _translate = QtCore.QCoreApplication.translate
        mappingProcess.setWindowTitle(_translate("mappingProcess", "PipeView"))
        self.titleLabel.setText(_translate("mappingProcess", "Mapping"))
        self.COMLabel.setText(_translate("mappingProcess", "COM"))
        self.openCamButton.setText(_translate("mappingProcess", "Open Realtime Camera App"))
        self.startLogButton.setText(_translate("mappingProcess", "Start logging"))
        self.stopLogButton.setText(_translate("mappingProcess", "Stop logging"))
        self.startMovButton.setText(_translate("mappingProcess", "Start movement"))
        self.stopMovButton.setText(_translate("mappingProcess", "Stop movement"))
        self.lessDegreesButton.setText(_translate("mappingProcess", "-15°"))
        self.currentDegreesLabel.setText(_translate("mappingProcess", "0"))
        self.moreDegreesButton.setText(_translate("mappingProcess", "+15°"))
        self.minusNinetyDegreesButton.setText(_translate("mappingProcess", "-90°"))
        self.minusFourtyFiveDegreesButton.setText(_translate("mappingProcess", "-45°"))
        self.zeroDegreesButton.setText(_translate("mappingProcess", "0°"))
        self.fourtyFiveDegreesButton.setText(_translate("mappingProcess", "45°"))
        self.ninetyDegreesButton.setText(_translate("mappingProcess", "90°"))
        self.closeWindowButton.setText(_translate("mappingProcess", "Close"))

    # When stop_btn is clicked this runs. Terminates the worker and the thread.
    def stop_thread(self):
        self.stop_signal.emit()  # emit the finished signal on stop

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mappingProcess = QtWidgets.QFrame()
    ui = Ui_mappingProcess()
    ui.setupUi(mappingProcess)
    mappingProcess.show()
    sys.exit(app.exec_())