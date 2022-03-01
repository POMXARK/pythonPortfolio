import edit_img as e
from Projects.text_voiceover_0_4.Say import ConvertTextToVoice


class RunApp():
    def __init__(self, speakers: list, voice_file: str, voice_opt_file: str, time_replay: str, img, pytesseract_config: str, lang: str,  min_speed: str, max_speed: str, min_volume: str, max_volume: str):
        num = 0
        while num < 10: #бесконечный цикл
            convert = ConvertTextToVoice(img=img, lang=lang, min_speed=min_speed, max_speed=max_speed,
                                         min_volume=min_volume, max_volume=max_volume,
                                         pytesseract_config=pytesseract_config, speakers=speakers,
                                         voice_file=voice_file,
                                         voice_opt_file=voice_opt_file, time_replay=time_replay)
            obj_edit_img = e.MainHandler(speakers=speakers,voice_file=voice_file,voice_opt_file=voice_opt_file)
            if obj_edit_img.edit_img() == True: #Проверка нового кадра
                ##random_wav()# случайный кусок / ФАН
                #play_wav() # воспроизвести живой аудио фрагмент / ВОЗМОЖНОСТЬ
                convert.choice_of_voice_engine() # проверка голосового движка какой выбран



