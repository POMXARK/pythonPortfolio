from simpleaudio import WaveObject, stop_all
from Projects.text_voiceover_0_3.say import show_img as s
import pytesseract
import rapidfuzz.fuzz


def load_dict_from_file():
    f = open('dict.txt','r')
    data=f.read()
    f.close()
   # print(data)
    return eval(data)



def play_wav():
    stop_all()  # остановить любой звук
    img = s.cv.imread("tesseract_mask.png")

    config = r'--oem 3  --psm 4 tessedit_char_whitelist=абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    text = pytesseract.image_to_string(img, config=config, lang='rus')

    load_dict_wav = load_dict_from_file()

    for words in load_dict_wav:
        all_wav = range(int(words['start_wav']),int(words['end_wav']))
        #print(all_wav)
        #print(words['Dialogs'])
        for it in range(int(words['start_wav']),int(words['end_wav'])+1):
            if it <= int(words['end_wav'])+1:
                #print(all_wav)
                if rapidfuzz.fuzz.ratio(str(words['Dialogs']), text) > 60:
                   # print(it)
                    wav_name = "wav\\"  + str(it-1) + '.wav'
                    #print(wav_name)
                    #print(words['wav'])
                    wave_obj = WaveObject.from_wave_file(wav_name)
                    play_obj = wave_obj.play()
                    play_obj.wait_done()




        #print(text,load_dict_wav)