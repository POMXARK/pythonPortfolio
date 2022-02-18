from PyQt5 import QtWidgets # для создания элементов
from PyQt5.QtWidgets import QApplication, QMainWindow # для создания приложения и окна
import sys # обязательно для PyQt5


def add_label():
    print(1)


def application():
    app = QApplication(sys.argv)
    window = QMainWindow() # создать окно

    window.setWindowTitle("Простая программа")
    window.setGeometry(300,250,350,200) # смещение и размеры окна

    main_text = QtWidgets.QLabel(window) # создать надпись в окне
    main_text.setText("Это базовая надпись")
    main_text.move(100,100)
    main_text.adjustSize() # адаптивный размер обьекта



    btn = QtWidgets.QPushButton(window)
    btn.move(70,150)
    btn.setText('Нажми на меня')
    btn.setFixedWidth(200)
    btn.clicked.connect(add_label) # выполнить действие!!!

    window.show() # показать окно
    sys.exit(app.exec_()) # закрыть программу

if __name__ == "__main__":
    application()