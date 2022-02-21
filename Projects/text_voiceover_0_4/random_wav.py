from simpleaudio import WaveObject, stop_all
import os
import random
from Projects.text_voiceover_0_3.say import set_opt
import datetime
timer = int(set_opt()['Время повтора'])  # время повтора реплики

def random_wav():

    global now
    global old_sec
    global now_sec

    now = datetime.datetime.now()
    now_sec = now.second
    print(now_sec)
    try:
        sec_raz = (max(old_sec,now_sec) - min(old_sec,now_sec))
       # print('ПРОШЛО ВРЕМЕНИ :', (max(old_sec,now_sec) - min(old_sec,now_sec)))
    except NameError:
        old_sec = 0

    sec_raz = (max(old_sec, now_sec) - min(old_sec, now_sec))

    if sec_raz > timer:

        old_sec = now.second
        stop_all()  # остановить любой звук
        path, dirs, files = next(os.walk("lol")) # количество файлов в папке
        file_count = len(files) # количество файлов в папке
        #print(file_count)
        ranrom_wav_name = random.randint(0, file_count-1) # случайный трек
        wav_name = "lol\\" + str(ranrom_wav_name) + '.wav'
        # print(wav_name)
        # print(words['wav'])
        wave_obj = WaveObject.from_wave_file(wav_name)
        print(wave_obj)
        play_obj = wave_obj.play()
        play_obj.wait_done()