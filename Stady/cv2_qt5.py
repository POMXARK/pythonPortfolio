# -*- coding: utf-8 -*-

# Реализация формы сгенерирована при чтении файла пользовательского интерфейса 'process.ui'
#
# Создано: PyQt5 UI code generator 5.11.3
#
# ПРЕДУПРЕЖДЕНИЕ! Все изменения, внесенные в этот файл, будут потеряны!
#
# Подпишитесь на канал PyShine Youtube, чтобы узнать подробности!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2, imutils




class Ui_MainWindow(object):

    print(object.__dict__)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(536, 571) # размеры окна

        self.centralwidget = QtWidgets.QWidget(MainWindow) # присвоить класс главного окна
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        # self.label.setPixmap(QtGui.QPixmap("images/2.jpg"))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout.addWidget(self.verticalSlider)
        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget) # слайдер
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical) # орентация слайдера
        self.verticalSlider_2.setObjectName("verticalSlider_2") # добавить слайдер
        self.horizontalLayout.addWidget(self.verticalSlider_2) # добавить виджет
        self.horizontalLayout_3.addLayout(self.horizontalLayout)  # добавить лайаут
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)  # добавление лайаута
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.verticalSlider.valueChanged['int'].connect(self.brightness_value)
        self.verticalSlider_2.valueChanged['int'].connect(self.blur_value)
        self.pushButton_2.clicked.connect(self.loadImage)
        self.pushButton.clicked.connect(self.savePhoto)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Добавлен код сюда
        self.filename = None  # Будет содержать адрес изображения
        self.tmp = None  # Будет удерживать временное изображение для отображения
        self.brightness_value_now = 0  # Обновлено значение яркости
        self.blur_value_now = 0  # Обновлено значение размытия

    def loadImage(self):
        """ Эта функция загрузит выбранное пользователем изображение
             и установите для него метку с помощью функции setPhoto
        """
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image)

    def setPhoto(self, image):
        """ Эта функция принимает изображение и изменяет его размер.
             только для отображения и преобразовать его в QImage
             установить на этикетке.
        """
        self.tmp = image
        image = imutils.resize(image, width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def brightness_value(self, value):
        """ Эта функция будет принимать значение от ползунка
             для яркости от 0 до 99
        """
        self.brightness_value_now = value
        print('Brightness: ', value)
        self.update()

    def blur_value(self, value):
        """ Эта функция будет принимать значение от ползунка
             для размытия от 0 до 99 """
        self.blur_value_now = value
        print('Blur: ', value)
        self.update()

    def changeBrightness(self, img, value):
        """ Эта функция принимает изображение (img) и яркость
             ценить. Он выполнит изменение яркости с помощью OpenCv
             и после разделения объединит img и вернет его.
        """
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        lim = 255 - value
        v[v > lim] = 255
        v[v <= lim] += value
        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        return img

    def changeBlur(self, img, value):
        """ Эта функция принимает в качестве входных данных изображение img и значения размытия.
             После выполнения операции размытия с использованием функции opencv он возвращает
             изображение img.
        """
        kernel_size = (value + 1, value + 1)  # +1 is to avoid 0
        img = cv2.blur(img, kernel_size)
        return img

    def update(self):
        """ Эта функция обновит фото в соответствии с
             текущие значения размытия и яркости и установите для фото метки.
        """
        img = self.changeBrightness(self.image, self.brightness_value_now)
        img = self.changeBlur(img, self.blur_value_now)
        self.setPhoto(img)

    def savePhoto(self):
        """Эта функция сохранит изображение"""
        # здесь укажите имя выходного файла
        # допустим, мы хотим сохранить вывод как отметку времени
        # раскомментируйте две строки ниже

        # время импорта
        # filename = 'Snapshot' + str (time.strftime ("% Y-% b-% d at% H.% M.% S% p")) + '. png'

        # Или мы можем дать любое имя, например output.jpg или output.png
        # filename = 'Snapshot.png'

        # Или гораздо лучший вариант - позволить пользователю определять местоположение и расширение
        # используя файловый диалог.

        filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]

        cv2.imwrite(filename, self.tmp)
        print('Изображение сохранено как:', self.filename)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyshine photo editor"))
        self.pushButton_2.setText(_translate("MainWindow", "Open"))
        self.pushButton.setText(_translate("MainWindow", "Save"))


# Подпишитесь на канал PyShine Youtube, чтобы узнать подробности!

# САЙТ: www.pyshine.com


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
