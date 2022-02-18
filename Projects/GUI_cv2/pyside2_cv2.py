
from PyQt5.QtCore import (QThread, Qt, pyqtSignal)
#from PyQt5.QtGui import (QPixmap, QImage,)
#from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton,QVBoxLayout
from PySide2.QtWidgets import QApplication, QWidget, QLabel,QPushButton,QVBoxLayout
from PySide2.QtCore import QTimer
from PySide2.QtGui import QPixmap
import cv2 # OpenCV
import qimage2ndarray # for a memory leak,see gist
import sys # for exiting
import numpy as np

# Minimal implementation...

img = cv2.imread('example.png')

if __name__ == '__main__':
    def nothing(*arg):
        pass

def create_cv2():
    cv2.namedWindow("result")  # создаем главное окно
    cv2.namedWindow("settings")  # создаем окно настроек
    cv2.resizeWindow('settings', 600, 400) # размер окна

    # создаем 6 бегунков для настройки начального и конечного цвета фильтра
    cv2.createTrackbar('h1', 'settings', 0, 255, nothing)
    cv2.createTrackbar('s1', 'settings', 0, 255, nothing)
    cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
    cv2.createTrackbar('h2', 'settings', 255, 255, nothing)
    cv2.createTrackbar('s2', 'settings', 255, 255, nothing)
    cv2.createTrackbar('v2', 'settings', 255, 255, nothing)
    #return False

def displayFrame():

    create_cv2()

    while True:

       # flag, img = cap.read()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # считываем значения бегунков
        h1 = cv2.getTrackbarPos('h1', 'settings')
        s1 = cv2.getTrackbarPos('s1', 'settings')
        v1 = cv2.getTrackbarPos('v1', 'settings')
        h2 = cv2.getTrackbarPos('h2', 'settings')
        s2 = cv2.getTrackbarPos('s2', 'settings')
        v2 = cv2.getTrackbarPos('v2', 'settings')



        # формируем начальный и конечный цвет фильтра
        h_min = np.array((h1, s1, v1), np.uint8)
        h_max = np.array((h2, s2, v2), np.uint8)

        # накладываем фильтр на кадр в модели HSV
        thresh = cv2.inRange(hsv, h_min, h_max)

        # Custom window
        cv2.namedWindow('result', cv2.WINDOW_KEEPRATIO)
        cv2.imshow('result', thresh)


        ch = cv2.waitKey(5)


        if ch == 27:
            break




   # pass
   # ret, frame = cap.read()
   # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
   # image = qimage2ndarray.array2qimage(frame)
   # label.setPixmap(QPixmap.fromImage(image))

app = QApplication([])
window = QWidget()

# OPENCV

#cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# timer for getting frames

timer = QTimer()
timer.timeout.connect(displayFrame)
timer.start(60)
label = QLabel('No Camera Feed')
button = QPushButton("Quiter")
button.clicked.connect(sys.exit) # quiter button
layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(label)
window.setLayout(layout)
window.show()
app.exec_()

# See also: https://gist.github.com/bsdnoobz/8464000