import pyttsx3

import random
import options as opt

tts = pyttsx3.init()  # Инициализировать голосовой движок.


rate = tts.getProperty('rate')  # Скорость произношения
tts.setProperty('rate', rate + opt.random_rate)

volume = tts.getProperty('volume')  # Громкость голоса
tts.setProperty('volume', volume + opt.vol)

voices = tts.getProperty('voices')
tts.setProperty('voice', voices[-1].id)
tts.setProperty('voice', 'ru')

#tts.runAndWait()


def voice(): # Перебрать голоса и вывести параметры каждого
    for voice in voices:

        print('=======')

        print('Имя: %s' % voice.name)

        print('ID: %s' % voice.id)

        print('Язык(и): %s' % voice.languages)

        print('Пол: %s' % voice.gender)

        print('Возраст: %s' % voice.age)