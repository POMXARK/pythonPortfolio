import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication

application = QApplication(sys.argv)

i=0
timer = QtCore.QTimer()

def num():
    global i, timer
    if i <999:
        print ( i )
        i += 1
    else:
        timer.stop()

timer.timeout.connect(num)
timer.start(2000)

sys.exit(application.exec_())