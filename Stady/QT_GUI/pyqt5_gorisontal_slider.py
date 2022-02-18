#!/usr/bin/python


from PyQt5.QtWidgets import (QWidget, QSlider, QHBoxLayout, QGridLayout,
                             QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI() # - функция записанна в инит класса QWidget

    def initUI(self):

        hbox = QHBoxLayout()
        #hbox = QGridLayout() # 0 - выбор лайаута
        sld = QSlider(Qt.Horizontal, self) # = - 1 присваеваем ЭкземпляруКласса? виджет
        print(dir(sld)) # посмотреть аргументы ЭкземпляраКласа и всех наследуемые атрибуты
        print(sld.__dict__) # локальные атрибуты ЭкземпляраКласса
        sld.setRange(0, 100)  # дипазон значений слайдера
        #sld.setFocusPolicy(Qt.NoFocus) # необязательно
        #sld.setPageStep(5) # необязательно

        self.label = QLabel('0', self) # 3 - присваивает изначальное  , задает тип виджета метка базовый класс  QLabel
        sld.valueChanged.connect(self.updateLabel) # 4 - отдает значение из изменяет sld.valueChanged, в функцию , значение ( вызов функции)


        #self.label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter) # 5 лишнее
        #self.label.setMinimumWidth(80) # 6 лишнее

        hbox.addWidget(sld) # 6.5 добовляет виджети в правильном месте и актевирует его ( на выбранный Layout, ЭкземплярКласса QWidget
       # hbox.addSpacing(15) # добовляет отступ - не основное
        hbox.addWidget(self.label)  # 7 # добовляет виджети в правильном месте - не основное

        self.setLayout(hbox) # -0.5 обязательно

       # self.setGeometry(300, 300, 350, 250) # размер окна - необязательно
       # self.setWindowTitle('QSlider') # название окна - необязательно
        self.show() # показ окна обязательно

    def updateLabel(self, value): # 1 - главная функция

        self.label.setText(str(value)) # 2 - изменяет значение ползунка





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
