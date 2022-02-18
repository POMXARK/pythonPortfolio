import sys
import traceback
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import  *
from time import sleep


# Если при ошибке в слотах приложение просто падает без стека,
# есть хороший способ ловить такие ошибки:
def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    #import traceback
    text += ''.join(traceback.format_tb(tb))
    QMessageBox.critical(None, 'Error', text)
    quit()
sys.excepthook = log_uncaught_exceptions


class MsgBoxWorker(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(900, 300, 400, 80)
        self.setWindowTitle('MsgBox Worker(QRunnable)')
        layout     = QVBoxLayout(self)
        self.label = QLabel("")
        layout.addWidget(self.label)
        close_btn  = QPushButton("Close Окно")
        layout.addWidget(close_btn)
        # ------- Сигнал   это только закроет окно, поток как работал, так и работает
        close_btn.clicked.connect(self.close)


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

        self.progressBar = QProgressBar()
        self.progressBar.setProperty("value", 0)

        self.lay = QVBoxLayout(self)
        self.lay.addWidget(self.btn)
        self.lay.addWidget(self.inp)
        self.lay.addWidget(self.progressBar)

        self.threadpool = QThreadPool()
        print("Max потоков, кот. будут использоваться=`%d`" % self.threadpool.maxThreadCount())
        self.msgWorker = MsgBoxWorker()

# ---- Worker(QRunnable) ------------------------#
    def some_func(self, n):
#        sleep(int(n))  # Любое действие, требующее существенного времени на выполнение
        # Передайте функцию для выполнения
        # Любые другие аргументы, kwargs передаются функции run
        worker = Worker(self.execute_this_fn)
        worker.signals.result.connect(self.print_output)
        worker.signals.finish.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)
        self.threadpool.start(worker)

    def progress_fn(self, n):
        self.progressBar.setValue(n)
        self.msgWorker.label.setText(str(n))
        # Восстанавливаем визуализацию потокового окна, если его закрыли. Поток работает.
        if not self.msgWorker.isVisible():
            self.msgWorker.show()

    def execute_this_fn(self, progress_callback):
        for n in range(0, 11):
            QThread.msleep(600)
            progress_callback.emit(n*100/10)
        return "Готово."

    def print_output(self, s):
        print("\ndef print_output(self, s):", s)

    def thread_complete(self):
        print("\nTHREAD ЗАВЕРШЕН!, self->", self)

# --END-- Worker QRunnable) -------------------#

    #==============================================###
    # потоки или процессы должны быть завершены    ###
    def closeEvent(self, event):
        reply = QMessageBox.question\
        (self, 'Информация',
            "Вы уверены, что хотите закрыть приложение?",
             QMessageBox.Yes,
             QMessageBox.No)
        if reply == QMessageBox.Yes:
            # закрыть поток Worker(QRunnable)
            self.msgWorker.close()
            super(Window, self).closeEvent(event)
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())