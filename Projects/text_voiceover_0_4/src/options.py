from xml.etree import ElementTree

import pyttsx3
import random


class BaseVoiceOptions:

    def __init__(self, speakers: list, voice_file: str,voice_opt_file: str):
        self._speakers = speakers
        _voice_name = open(voice_file)  # открыть файл
        self._voice_name = _voice_name.read()  # прочитать
        self._voice_opt_file = voice_opt_file
        self._set_opt()

    def _set_opt(self):
        try:
            _options = []
            self._opt = open(self._voice_opt_file)  # открыть файл
            self._opt = self._opt.read()  # прочитать
            with open(self._opt) as f:
                tree = ElementTree.parse(self._opt)
                root = tree.getroot()
                for i in root:
                    _options.append(i.text)


            #with open(self._opt) as f:
            #    _options = f.read().splitlines()
            #print(type(_options))

            #tree = ElementTree.parse(self._voice_opt_file)
            #root = tree.getroot()
            #for i in root:
            #    _options.append(i.text)

        except FileNotFoundError:
            _options = []
        try:
            self._opt_1 = {
                'Минималья скорость': _options[0],
                'Максимальная скорость': _options[1],
                'Минимальная громкость': _options[2],
                'Максимальная громкость': _options[3],
                'Время повтора': _options[4],
                'X': _options[5],
                'Y': _options[6],
                'отсуп с краев экрана по ширине': _options[7],
                'высота': _options[8],
                'h1': _options[9],
                's1': _options[10],
                'v1': _options[11],
                'h2': _options[12],
                's2': _options[13],
                'v2': _options[14],
                'rgb1': _options[15],
                'rgb2': _options[16],
                'rgb3': _options[17],
                'mb_h1': _options[18],
                'mb_s1': _options[19],
                'mb_v1': _options[20],
                'mb_h2': _options[21],
                'mb_s2': _options[22],
                'mb_v2': _options[23]}
        except IndexError:
            self._opt_1 = {
                'Минималья скорость': 0,
                'Максимальная скорость': 0,
                'Минимальная громкость': 0,
                'Максимальная громкость': 0,
                'Время повтора': 0,
                'X': 0,
                'Y': 0,
                'отсуп с краев экрана по ширине': 0,
                'высота': 0,
                'h1': 0,
                's1': 0,
                'v1': 0,
                'h2': 0,
                's2': 0,
                'v2': 0,
                'rgb1': 0,
                'rgb2': 0,
                'rgb3': 0,
                'mb_h1': 0,
                'mb_s1': 0,
                'mb_v1': 0,
                'mb_h2': 0,
                'mb_s2': 0,
                'mb_v2': 0, }
            return self._opt_1


class VoiceOptions(BaseVoiceOptions):
    def __init__(self, min_speed: str = '', max_speed: str= '', min_volume: str= '', max_volume: str= '', speakers: list= [],
                 voice_file: str= '', voice_opt_file: str= ''):

        super().__init__(speakers, voice_file, voice_opt_file)
        self._tts = pyttsx3.init()  # Инициализировать голосовой движок.
        self._random_rate = random.uniform(float(self._opt_1[min_speed]),
                                           float(self._opt_1[max_speed]))  # Скорость произношения
        self._random_rate *= self._random_rate
        self._vol = random.uniform(float(self._opt_1[min_volume]),
                                   float(self._opt_1[max_volume]))  # Громкость голоса
        self._rate = self._tts.getProperty('rate')  # Скорость произношения
        self._tts.setProperty('rate', self._rate + self._random_rate)
        self._volume = self._tts.getProperty('volume')  # Громкость голоса
        self._tts.setProperty('volume', self._volume + self._vol)
        self._voices = self._tts.getProperty('voices')
        self._tts.setProperty('voice', self._voices[-1].id)
        self._tts.setProperty('voice', 'ru')



    def find_voice_noy_silero(self):
        voices_detect = []
        for voice in self._voices:
            song = ('Имя: %s' % voice.name)
            song = song.replace("Имя: ", "")
            voices_detect.append(song)
        return voices_detect


    def voice(self):  # Перебрать голоса и вывести параметры каждого
        for voice in self._voices:
            print('=======')

            print('Имя: %s' % voice.name)

            print('ID: %s' % voice.id)

            print('Язык(и): %s' % voice.languages)

            print('Пол: %s' % voice.gender)

            print('Возраст: %s' % voice.age)


class Speakers:

    @staticmethod
    def find_voice():
        _tts = pyttsx3.init()
        _voices = _tts.getProperty('voices')
        voices_detect = []
        for voice in _voices:
            song = ('Имя: %s' % voice.name)
            song = song.replace("Имя: ", "")
            voices_detect.append(song)
        return voices_detect