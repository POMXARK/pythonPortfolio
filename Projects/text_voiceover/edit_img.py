from win32api import GetSystemMetrics
import pyautogui
import cv2
import show_img as s
import Detect_line as l
import MakeBorder as m
import Smart_cut as c
import For_tesseract as t
import Text_npc as npc
import Detect_text as clear
import Detect_dooble_img as d

def edit_img():


    global old_text

    Width = GetSystemMetrics(0)
    Height = GetSystemMetrics(1)

    # скриншоты и нахождение отдельных элементов
    img = pyautogui.screenshot(region=(100,600, Width-160, 410)) # обрезка изображения
    #img = pyautogui.screenshot(region=(100, 300, Width - 160, 710))  # обрезка изображения лучше распознавания нового кадра
    img.save("example.png")
    im1_img = cv2.imread("example.png")
    s.show('"example.png"', im1_img )

    if d.difference_images() == True:# дубликат приведущей сцены - пропуск
        #print('ЛИШНИЙ КАДР')
        return False
    else:
        l.detect_line() # ищет прямые линии на img
        m.make_border() # создает рамку вокруг img
        c.smart_cut() # закрашивает лишнее на img
        npc.npc() # только текст npc
        clear.clear_text() # чистка img от графических артефактов
        t.tesserack_mask() # обрабока для понимая tesserack


        return True