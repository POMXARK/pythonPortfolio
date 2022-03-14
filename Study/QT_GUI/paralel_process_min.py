import sys
import traceback
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import  *
from time import sleep



class WorkerSignals(QObject):
    ''' Определяет сигналы, доступные из рабочего рабочего потока Worker(QRunnable).'''

    finish   = pyqtSignal()
    error    = pyqtSignal(tuple)
    result   = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    ''' Наследует от QRunnable, настройки рабочего потока обработчика, сигналов и wrap-up. '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Хранить аргументы конструктора (повторно используемые для обработки)
        self.fn      = fn
        self.args    = args
        self.kwargs  = kwargs
        self.signals = WorkerSignals()

        #== Добавьте обратный вызов в наши kwargs ====================================###
        kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        # Получите args/kwargs здесь; и обработка с их использованием
        try:                       # выполняем метод `some_func` переданный из Main
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:  # если ошибок не была, испускаем сигнал .result и передаем результат `result`
            self.signals.result.emit(result)      # Вернуть результат обработки
        finally:
            self.signals.finish.emit()            # Done / Готово



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Name')

        self.inp = QLineEdit()
        self.btn = QPushButton('Действие')
        self.btn.clicked.connect(lambda x: self.some_func(self.inp.text()))

        self.lay = QVBoxLayout(self)
        self.lay.addWidget(self.btn)
        self.lay.addWidget(self.inp)


        self.threadpool = QThreadPool() # основное


# ---- Worker(QRunnable) ------------------------#
    def some_func(self, n):
#        sleep(int(n))  # Любое действие, требующее существенного времени на выполнение
        # Передайте функцию для выполнения
        # Любые другие аргументы, kwargs передаются функции run
        worker = Worker(self.parall_process) # обязательно

        self.threadpool.start(worker)


    def parall_process(self, progress_callback):
        i = 0
        while i < 1:
            print(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())