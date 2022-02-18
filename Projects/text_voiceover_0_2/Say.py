import voise as v
import pytesseract
import show_img as s
import pitch_voise as p
import datetime
from fuzzywuzzy import fuzz
from options import set_voise
from options import set_opt

timer = int(set_opt()['Время повтора'])  # время повтора реплики



def say():


    global now
    global old_sec
    global now_sec

    now = datetime.datetime.now()
    now_sec = now.second



    #print('ПРОШЛО ВРЕМЕНИ :', (max(old_sec,now_sec) - min(old_sec,now_sec)))
    #global timer # отщитывать время

    now = datetime.datetime.now()
   # print('now.second ',now.second )
    global old_text # глобальная переменная



    #timer -= 1 # отсчет времени между речью
#    print('timer' , timer)
    img = s.cv.imread("tesseract_mask.png")

    ### РАСПОЗНАНИЕ ###
    #'tessedit_char_whitelist=абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ --oem 3 --psm 6 '
    # Будет выведен весь текст с картинки
    config = r'--oem 3  --psm 4 tessedit_char_whitelist=абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    text = pytesseract.image_to_string(img, config= config , lang='rus')  # распознание текста


    try:
        text_raz = fuzz.ratio(text, old_text)
    except NameError:

        old_text=' '


    text_raz = fuzz.ratio(text, old_text)
    #print('text_raz :',text_raz)


    try:
        sec_raz = (max(old_sec,now_sec) - min(old_sec,now_sec))
       # print('ПРОШЛО ВРЕМЕНИ :', (max(old_sec,now_sec) - min(old_sec,now_sec)))
    except NameError:
        old_sec = 0

    sec_raz = (max(old_sec,now_sec) - min(old_sec,now_sec))

    if text_raz < 95 or  sec_raz > timer: #or timer <= 0:
        old_sec = now.second
        #pass
        #print('СТРОКИ ИДЕНТИЧНЫ! НЕ ПОВТОРЯТЬ', text_raz,old_text,'\p', text)
        #return False
    #else:
        #timer = 10
        old_text = text
       # print('old_text :',old_text)

        # Попробовать установить предпочтительный голос
        for voice in v.voices:

           # print('opt.voise_name :', opt.voise_name)

            if voice.name == set_voise():
                v.tts.setProperty('voice', voice.id)

        v.tts.save_to_file(str(text), 'text.wav')


        # v.tts.say(text)
        v.tts.runAndWait()

        p.pitch_voise()
