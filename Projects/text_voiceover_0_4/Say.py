import datetime
from fuzzywuzzy import fuzz
import pytesseract
from torch import device as torch_device,package,set_num_threads
from simpleaudio import WaveObject, stop_all
from pydub import AudioSegment
import random
import simpleaudio as sa
import os

import cv2 as cv

from Projects.text_voiceover_0_4.src.options import VoiceOptions


def show(title, img, color=True):
    if color:
       pass
        #mng = plt.get_current_fig_manager()
#        mng.window.state("zoomed")
        #plt.imshow(img[:, :, ::-1]), plt.title(title), plt.show() # для диагностики
    else:
        pass
        #mng = plt.get_current_fig_manager()
#        mng.window.state("zoomed")
        #plt.imshow(img, cmap='gray'), plt.title(title), plt.show() # для диагностики

def show_img(title,img_obj):
    img_obj = img_obj
    title_img = str(title + ".png")
    print('title: ', title_img)
    cv.imwrite(title_img, img_obj)
    img_obj = cv.imread(title_img)
    show(title_img, img_obj)


class ConvertTextToVoice(VoiceOptions):
    def __init__(self, time_replay: str, img, pytesseract_config: str, lang: str, speakers: list, voice_file: str,
                 voice_opt_file: str, min_speed: str, max_speed: str, min_volume: str, max_volume: str):

        super().__init__(min_speed, max_speed, min_volume, max_volume, speakers, voice_file, voice_opt_file)
        self.speakers = speakers
        ### self._text = pytesseract.image_to_string(img, config=pytesseract_config, lang=lang)  # распознание текста
        self._timer = int(self._opt_1[time_replay])  # время повтора реплики
        self._old_text = ''
        self.img = img
        self.pytesseract_config = pytesseract_config

    def choice_of_voice_engine(self):
        self._text = pytesseract.image_to_string(self.img, config=self.pytesseract_config, lang='rus')  # распознание текста
        no_silero = self.find_voice_noy_silero()
        voise = self._voice_name

        for speaker in no_silero:
            if voise == speaker:
                self._say()

        for silero_speaker in self.speakers:
            if voise == silero_speaker:
                pass
                ####self.say_silero()

    def _say(self):

        global now
        global old_sec
        global now_sec
        global old_text  # глобальная переменная

        now = datetime.datetime.now()
        now_sec = now.second
        now = datetime.datetime.now()

        ### РАСПОЗНАНИЕ ###
        # Будет выведен весь текст с картинки

        try:
            text_raz = fuzz.ratio(self._text, self._old_text)
        except :
            self._old_text = ' '


        try:
            sec_raz = (max(old_sec, now_sec) - min(old_sec, now_sec))
        except NameError:
            old_sec = 0

        sec_raz = (max(old_sec, now_sec) - min(old_sec, now_sec))

        if text_raz < 95 or sec_raz > self._timer:  # or timer <= 0:
            old_sec = now.second
            old_text = self._text

            # Попробовать установить предпочтительный голос
            for voice in self._voices:
                if voice.name == self._voice_name:
                    self._tts.setProperty('voice', voice.id)

            self._tts.save_to_file(str(self._text), 'text.wav')

            self._tts.runAndWait()

            self.pitch_voise()

    def say_silero(self):
        stop_all()  # остановить любой звук
        device = torch_device('cpu')
        set_num_threads(16)
        local_file = 'model_multi.pt'

        img = cv.imread("tesseract_mask.png")

        example_speakers = self._voice_name
        sample_rate = 16000
        model = package.PackageImporter(local_file).load_pickle("tts_models", "model")
        model.to(device)
        print('silero mod :', example_speakers)

        config = r'--oem 3  --psm 4 tessedit_char_whitelist=абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

        text = pytesseract.image_to_string(img, config=config, lang='rus')

        old_text = text

        try:
            audio_paths = model.save_wav(texts=text,
                                         speakers=example_speakers,
                                         sample_rate=sample_rate)

        except IndexError:
            return False
        audio_paths = model.save_wav(texts=text,
                                     speakers=example_speakers,
                                     sample_rate=sample_rate)

        wave_obj = WaveObject.from_wave_file('test_000.wav')
        play_obj = wave_obj.play()
        play_obj.wait_done()

    def pitch_voise(self):


        try_wav = os.path.getsize("text.wav") # проверка голосового файла

        #if try_wav < 50 or self._say() == False:
        #    #print(try_wav,'Звука НЕТ')
        #    return False


        sound = AudioSegment.from_file('text.wav', format="wav")

        # сдвинуть высоту тона на половину октавы (скорость увеличится пропорционально)
        octaves = random.uniform(-0.2,-0.1)

        new_sample_rate = int(sound.frame_rate * (2.0 ** octaves))

        # сохраните те же образцы, но скажите компьютеру, что в них следует играть
        # новый, более высокая частота дискретизации. Этот файл похож на бурундука, но имеет странную частоту дискретизации.
        hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})

        # теперь мы просто преобразуем его в обычную частоту дискретизации (44,1k - стандартный аудио CD) в
        # убедитесь, что он работает в обычных аудиоплеерах. Кроме потенциально потери качества звука (если
        # вы установили слишком низкое значение - 44,1k вполне достаточно) теперь это должно заметно изменить звучание звука.
        hipitch_sound = hipitch_sound.set_frame_rate(44100)

        #export / save звук изменен.
        hipitch_sound.export("out.wav", format="wav")

        sa.stop_all()
        wave_obj = sa.WaveObject.from_wave_file('out.wav')
        play_obj = wave_obj.play()



        #path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'out.wav')
        #os.remove(path)
