import sys
#from PySide import QtCore, QtGui
from PyQt5 import QtCore, QtGui, QtWidgets

from ui_start import Ui_Start
from ui_inst  import Ui_Inst


class StartWindow(QtWidgets.QWidget, Ui_Start):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        self.pushButton.clicked.connect( self.but_1 )

    def but_1(self): # открытие 2-го окна

        self.inst = QtWidgets.QWidget()
        ui_ins = Ui_Inst()
        ui_ins.setupUi(self.inst)
        self.inst.show()
        #ui_ins.textEdit.setText("12546")
        print(1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = StartWindow()
    w.show()
    sys.exit(app.exec_())