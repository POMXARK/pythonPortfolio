#import keyboard
import Say as say
import time

import edit_img as e
from kivy.properties import ObjectProperty
import sys
## Kivy ##
from kivy.app import App # окно
from kivy.uix.boxlayout import BoxLayout # разметка элементов нужно для запуска
import threading # поралельное выполнение - требуется для бесконечного цикла и циклов for
from kivy.clock import Clock # для цикличного исполнения функций
from kivy.uix.widget import Widget
from kivy.uix.button import Button # кнопка
from kivy.uix.togglebutton import ToggleButton # кнопка-переключатель
from kivy.uix.label import Label #н надпись
from kivy.lang import Builder # для загрузки дизайна
from kivy.uix.gridlayout import GridLayout # разметка в виде
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.image import Image
# Назначьте наш файл дизайна .kv (для запуска имя класса должно совподать)
#Builder.load_file('SmaRT_Dictor.kv') # нужен если класс App(App) имеет отличающиеся название от kv файла, иначе вызывает баги
import simpleaudio as sa

from class_run import Class_run as c


print(" Class - atribut run  : ",c().run_def)

global script_run
global start
start = False

'''
print(
    'Для работы необходимо установить \ntesseract \nffmpeg-2021-08-22-git-d905af0c24-full_build (есть в архиве) \nи любой голос (в архиве есть RHVoice-voice-Kyrgyz-Azamat-v4.0.9-setup.exe) '
    '\nприятного тестирования :) \nверсия для Sea Dogs 2 - Pirates Of The Caribbean.v 1.03 \nрекомендую в папке с игрой engine.ini выставить : \nmodules path = modules\ '
    '\nfull_screen = 0\nscreen_x = 1920\nscreen_y = 1080')
    
    
     "b" + "r" * 60
brrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr

    
'''

#print(v.voice())


def print_def():
    print(1)


def Dictor(script_run):


        if e.edit_img() == True: #Проверка нового кадра
            say.say() # говорение с проверкой на повтор
             #continue




class SmaRTLayout(GridLayout):
    #Это мой новый экран
    def __init__(self, **kwargs): # выполняется при вызове класса , можно добовлять свои аргументы (переменные)
        super(SmaRTLayout, self).__init__(**kwargs) # обязательно


        try:
            self.app_start
        except AttributeError:
            self.app_start = False

        self.app_start # Свой аргумент ( переменная) вызываемая из класса (запуска_приложения)



    def add_new_screen(self):
        #удаляет все виджеты принадлежащие классу MainScreen и создает сделанный мной виджет MyNewScreen
        self.clear_widgets()
        self.add_widget(MyNewScreen())





    def on_start(self):

       # if SmaRTLayout().app_start == True:
        Clock.schedule_interval(self.update_Dictor, 1)  # Бесконечное исполнение
        print(2334)



    def on_state(self): # СОБЫТИЕ ПЕРЕКЛЮЧАТЕЛЬ!
       # SmaRTLayout.app_start = False
        self.lbl_1 = "Корсары 2"
        self.lbl_2 = "Выбранно : Корсары 2"


        for child in [child for child in self.children if child._text == self.lbl_1 or child._text == self.lbl_2]:
            if child.state == 'down' or child.state == 'normal':
                pass
                #child.text = self.lbl_2



            for child in [child for child in self.children if child._text == self.lbl_1]:
                if child.state == 'down':
                    child._text = self.lbl_2
                    SmaRTLayout.app_start = True # возвращает значение аргументва в класс


            for child in [child for child in self.children if child._text == self.lbl_2]:
                if child.state == 'normal':
                    child._text = self.lbl_1
                    print('stop')
                    SmaRTLayout.app_start = False # возвращает значение аргументва в класс


    def on_state_2(self):  # СОБЫТИЕ ПЕРЕКЛЮЧАТЕЛЬ!

        self.lbl_1 = "Корсары 3"
        self.lbl_2 = "Выбранно : Корсары 3"

        for child in [child for child in self.children if child._text == self.lbl_1 or child._text == self.lbl_2]:
            if child.state == 'down' or child.state == 'normal':
                pass
                #child.text = self.lbl_2

            for child in [child for child in self.children if child._text == self.lbl_1]:
                if child.state == 'down':
                    child._text = self.lbl_2

            for child in [child for child in self.children if child._text == self.lbl_2]:
                if child.state == 'normal':
                    child._text = self.lbl_1



    def update_Dictor(self, *args): # реализуемое действие
        print(SmaRTLayout().app_start) # возвращает значение аргумента из класса
        if SmaRTLayout().app_start == True:
            print('update')
            Dictor(True)
        else:
            sa.stop_all() # остановить любой звук

            App.on_stop(SmaRTLayout())



class MyButton(ToggleButton):
    button_id = ObjectProperty(None)




class MyNewScreen(BoxLayout):
    #Это мой новый экран
    def __init__(self,**kwargs):
        super().__init__(**kwargs)




class SmaRT_DictorApp(App): # вызывает окно приложения
    def build(self):
        SmaRTLayout().on_start() # вызывает метод(фунцию) из другого класса!
        return SmaRTLayout()




if __name__ == "__main__":  # Запуск приложения
    SmaRT_DictorApp().run()