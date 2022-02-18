import pyttsx3
from pyttsx3.drivers import sapi5

from PyQt5 import QtTextToSpeech # Модуль текст в голос





import random
from options import set_opt

tts = pyttsx3.init()  # Инициализировать голосовой движок.

random_rate = random.uniform(float(set_opt()['Минималья скорость']),float(set_opt()['Максимальная скорость'])) # Скорость произношения
random_rate *= random_rate
vol = random.uniform(float(set_opt()['Минимальная громкость']),float(set_opt()['Максимальная громкость'])) # Громкость голоса

rate = tts.getProperty('rate')  # Скорость произношения
tts.setProperty('rate', rate + random_rate)

volume = tts.getProperty('volume')  # Громкость голоса
tts.setProperty('volume', volume + vol)

voices = tts.getProperty('voices')
tts.setProperty('voice', voices[-1].id)
tts.setProperty('voice', 'ru')

#tts.runAndWait()

speakers = ['aidar', 'baya', 'kseniya', 'irina', 'ruslan', 'natasha',
            'thorsten', 'tux', 'gilles', 'lj', 'dilyara']


def find_voice_noy_silero():
    voices_detect = []
    for voice in voices:
         song = ('Имя: %s' % voice.name)
         song = song.replace("Имя: ", "")
         voices_detect.append(song)
    print(voices_detect)
   # print(type(voices_detect))
    return voices_detect



def find_voice():
    voices_detect = []
    for voice in voices:
         song = ('Имя: %s' % voice.name)
         song = song.replace("Имя: ", "")
         voices_detect.append(song)
    print(voices_detect)
   # print(type(voices_detect))
    return voices_detect + speakers


def voice(): # Перебрать голоса и вывести параметры каждого
    for voice in voices:

        print('=======')

        print('Имя: %s' % voice.name)

        print('ID: %s' % voice.id)

        print('Язык(и): %s' % voice.languages)

        print('Пол: %s' % voice.gender)

        print('Возраст: %s' % voice.age)

