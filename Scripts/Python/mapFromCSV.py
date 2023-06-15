from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import MapeoDireccionRegistro
import sys

class Ui_mapFromCSV(object):
    def open_explorer(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("CSV files (*.csv)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            file_path = selected_files[0]
            self.filePathLineEdit.setText(file_path)
    
    def generateMap(self):
        try:
            MapeoDireccionRegistro.mapFromCSV(self.filePathLineEdit.text())
        except:
            pass

    def setupUi(self, mapFromCSV):
        if sys.platform == 'win32':
            import ctypes
            app_id = 'mycompany.myapp.subapp.version'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
        
        mapFromCSV.setObjectName("mapFromCSV")
        mapFromCSV.resize(498, 171)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./data/PipeView_Logo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mapFromCSV.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(mapFromCSV)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(mapFromCSV)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setTextFormat(QtCore.Qt.AutoText)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filePathLineEdit = QtWidgets.QLineEdit(mapFromCSV)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filePathLineEdit.sizePolicy().hasHeightForWidth())
        self.filePathLineEdit.setSizePolicy(sizePolicy)
        self.filePathLineEdit.setObjectName("filePathLineEdit")
        self.horizontalLayout.addWidget(self.filePathLineEdit)
        self.fileExplorerButton = QtWidgets.QPushButton(mapFromCSV, clicked = lambda: self.open_explorer())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileExplorerButton.sizePolicy().hasHeightForWidth())
        self.fileExplorerButton.setSizePolicy(sizePolicy)
        self.fileExplorerButton.setObjectName("fileExplorerButton")
        self.horizontalLayout.addWidget(self.fileExplorerButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.generateMapButton = QtWidgets.QPushButton(mapFromCSV, clicked = lambda: self.generateMap())
        self.generateMapButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generateMapButton.sizePolicy().hasHeightForWidth())
        self.generateMapButton.setSizePolicy(sizePolicy)
        self.generateMapButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.generateMapButton.setIconSize(QtCore.QSize(12, 12))
        self.generateMapButton.setObjectName("generateMapButton")
        self.verticalLayout.addWidget(self.generateMapButton)

        self.retranslateUi(mapFromCSV)
        QtCore.QMetaObject.connectSlotsByName(mapFromCSV)

    def retranslateUi(self, mapFromCSV):
        _translate = QtCore.QCoreApplication.translate
        mapFromCSV.setWindowTitle(_translate("mapFromCSV", "PipeView"))
        self.titleLabel.setText(_translate("mapFromCSV", "Map Generation (*.CSV)"))
        self.filePathLineEdit.setText(_translate("mapFromCSV", "File Path"))
        self.fileExplorerButton.setText(_translate("mapFromCSV", "Open"))
        self.generateMapButton.setText(_translate("mapFromCSV", "Generate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mapFromCSV = QtWidgets.QFrame()
    ui = Ui_mapFromCSV()
    ui.setupUi(mapFromCSV)
    mapFromCSV.show()
    sys.exit(app.exec_())