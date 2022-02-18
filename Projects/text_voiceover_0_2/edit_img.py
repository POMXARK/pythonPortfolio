from win32api import GetSystemMetrics
from pyautogui import screenshot
from cv2 import imread
from show_img import show
from Detect_line import detect_line
from MakeBorder import make_border
from Smart_cut import smart_cut
from For_tesseract import tesserack_mask
from Npc_text import npc
from Detect_text import clear_text
from Detect_dooble_img import difference_images
from options import set_opt
#import silero as sil

def edit_img():


    global old_text

    Width = GetSystemMetrics(0)
    Height = GetSystemMetrics(1)

    """
    Существует также необязательный region
    аргумент ключевого слова, если вы не хотите снимать весь экран. 
    Вы можете передать кортеж из четырех целых чисел слева, сверху, ширины и высоты области для захвата:
    
    screenshot('screenshot.png',region=(0,0, 300, 400))
    Здесь в свойстве region мы указали что у нас будет снят левый верхний угол размером 300x400 пикселей. 
    То есть первые две координаты(0,0) отвечают за левый верхний угол, а вторые(300, 400) за размер области экрана.
    """

    # скриншоты и нахождение отдельных элементов
    img = screenshot(region=(int(set_opt()['X']),int(set_opt()['Y']), Width-int(set_opt()['отсуп с краев экрана по ширине']),
                             int(set_opt()['высота']))) # обрезка изображения
    #img = screenshot(region=(100, 300, Width - 160, 710))  # обрезка изображения лучше распознавания нового кадра
    img.save("example.png")
    im1_img = imread("example.png")
    show('"example.png"', im1_img )

    # перед этим img_dialog() == False: # проверка присутствия цвета
    if difference_images() == True:# дубликат приведущей сцены - пропуск
        #print('ЛИШНИЙ КАДР')
        return False
    else:
        print('else')
        detect_line() # ищет прямые линии на img
        make_border() # создает рамку вокруг img
        smart_cut() # закрашивает лишнее на img
        npc() # только текст npc
        clear_text() # чистка img от графических артефактов
        tesserack_mask() # обрабока для понимая tesserack
        #sil.say_silero()

        return True