
import edit_img as e
from choice_of_voice_engine import choice_of_voice_engine
from play_video_wav import play_wav
from random_wav import random_wav

def Dictor():

    num = 0
    while num < 10: #бесконечный цикл

        if e.edit_img() == True: #Проверка нового кадра
            ##random_wav()# случайный кусок / ФАН
            #play_wav() # воспроизвести живой аудио фрагмент / ВОЗМОЖНОСТЬ
            choice_of_voice_engine() # проверка голосового движка какой выбран



