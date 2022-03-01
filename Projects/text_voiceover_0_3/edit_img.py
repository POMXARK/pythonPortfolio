from win32api import GetSystemMetrics
from pyautogui import screenshot
from cv2 import imread

from Projects.text_voiceover_0_3.voise import BaseVoiceOptions
from MakeBorder import make_border
from Smart_cut import smart_cut
from For_tesseract import tesserack_mask
from Detect_text import clear_text

import os

import numpy as np

from Projects.text_voiceover_0_3.Say import show

from PIL import Image
import cv2


class MainHandler(BaseVoiceOptions):
    global resources_path
    resources_path = 'resources/'


    def edit_img(self):

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
        img = screenshot(region=(
        int(self._opt_1['X']), int(self._opt_1['Y']), Width - int(self._opt_1['отсуп с краев экрана по ширине']),
        int(self._opt_1['высота'])))  # обрезка изображения
        img.save(resources_path + "example.png")
        im1_img = imread(resources_path + "example.png")
        show('"example.png"', im1_img)

        # перед этим img_dialog() == False: # проверка присутствия цвета
        if self.difference_images() == True:  # дубликат приведущей сцены - пропуск
            # print('ЛИШНИЙ КАДР')
            return False
        else:
            print('else')
            self.detect_line()  # ищет прямые линии на img
            make_border()  # создает рамку вокруг img
            smart_cut()  # закрашивает лишнее на img
            self.npc()  # только текст npc
            clear_text()  # чистка img от графических артефактов
            tesserack_mask()  # обрабока для понимая tesserack
            # sil.say_silero()

            return True

    def detect_line(self):

        #    print(1)

        img_orig = cv2.imread(resources_path + 'example.png')
        img = cv2.imread(resources_path + 'example.png')

        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        cv2.imwrite(resources_path + "hsv.png", img)
        hsv_img = cv2.imread(resources_path + 'hsv.png')
        show('hsv', hsv_img)

        img = cv2.inRange(img, (int(self._opt_1['mb_h1']), int(self._opt_1['mb_s1']), int(self._opt_1['mb_v1'])), (
            int(self._opt_1['mb_h2']), int(self._opt_1['mb_s2']),
            int(self._opt_1['mb_v2'])))  # (0, 160, 100), (255, 255, 255) # выделение линий
        cv2.imwrite(resources_path + "mask.png", img)
        mask_img = cv2.imread(resources_path + 'mask.png')
        show(resources_path + 'mask', mask_img)
        binary = cv2.bitwise_not(img)

        img = cv2.Canny(img, 50, 50,
                        apertureSize=3)  # инвентирует изображение выделяя контуры, Обнаружение хитрого края
        cv2.imwrite(resources_path + "edges.png", img)
        edges_img = cv2.imread(resources_path + 'edges.png')
        show('edges ', edges_img)

        minLineLength = img.shape[1] - 1900  # что-то о линиях важно находит прямые линии

        lines = cv2.HoughLinesP(image=img, rho=1, theta=np.pi / 180, threshold=100, lines=np.array([]),
                                minLineLength=minLineLength, maxLineGap=2)  # threshold - минимальная длина линии

        try:
            a, b, c = lines.shape  # значение в матрице lines
        except AttributeError:
            # print('ОШИБКА НЕТ ТЕКСТА')
            if os.path.isfile('result.png') == True:
                os.remove(resources_path + 'result.png')
            return False

        a, b, c = lines.shape  # значение в матрице lines

        N = 0

        for i in range(a):
            # print(N)
            if N < 3:

                rho = 1
                theta = np.pi / 180
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho

                raz_x = lines[i][0][1] - lines[i][0][3]
                raz_y = lines[i][0][0] - lines[i][0][2]

                if raz_x == 0:
                    x1 = int((x0 + 100000 * (-b)))
                    x2 = int(x0 - 100000 * (-b))
                else:
                    x1 = 0
                    x2 = 0

                if raz_y == 0:
                    y1 = int(y0 + 10000 * (a))
                    y2 = int(y0 - 10000 * (a))
                else:
                    y1 = 0
                    y2 = 0

                cv2.line(img_orig, (lines[i][0][0] + x1, lines[i][0][1] + y1),
                         (lines[i][0][2] + x2, lines[i][0][3] + y2),
                         (0, 255, 255), 1, cv2.LINE_AA)  # подсветка линий

                N += 1

        cv2.imwrite(resources_path + 'result.png', img_orig)
        result_img = cv2.imread(resources_path + 'result.png')
        show('result ', result_img)

        return 0

    def npc(self):
        img = cv2.imread(resources_path + "for_tesseract.png")
        imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower = np.array([int(self._opt_1['h1']), int(self._opt_1['s1']), int(self._opt_1['v1'])], np.uint8)
        upper = np.array([int(self._opt_1['h2']), int(self._opt_1['s2']), int(self._opt_1['v2'])], np.uint8)
        # upper = np.array([60,225,245],np.uint8)
        mask = cv2.inRange(imghsv, lower, upper)
        im = np.copy(mask)
        # cv2.drawContours(im, contours, -1, (0, 255, 0), 0)
        cv2.imwrite(resources_path + "text_npc.png", im)
        text_npc = cv2.imread(resources_path + 'text_npc.png')
        show('text_npc', text_npc)

    def img_dialog(self):

        # Открываем изображение и превращаем его в массив numpy
        im = np.array(Image.open(resources_path + "example.png").convert('RGB'))

        # Разберитесь, что мы ищем
        sought = [int(self._opt_1['rgb1']), int(self._opt_1['rgb2']), int(self._opt_1['rgb3'])]  # искомый цвет

        # Найдите все пиксели, в которых 3 значения RGB совпадают с "искомыми", и посчитайте их
        # ПРОВЕРКА СЛОМАНА!!!
        result = np.count_nonzero(np.all(im == sought, axis=2))
        # print('искомого цвета :',result)
        if result > 90:
            # print('ЭТО КАДР ДИАЛОГА')
            return True
        else:
            # print('ЭТО НЕ ДИАЛОГ')
            return False  # True #False

    def difference_images(self):

        if self.img_dialog() == False:  # проверка присутвия цвета
            img = Image.new('RGB', (250, 250), (255, 255, 255))
            img.save(resources_path + 'old_example.png')
            img.save(resources_path + 'example.png')
            # print('Не диалог проверять не нужно')
            return True

        def CalcImageHash(FileName):

            try:
                old_img = Image.open(resources_path + 'old_example.png')
            except OSError:
                # print('НОВЫЙ КАДР')
                #            old_img = Image.new('RGB', (250, 250), (255, 255, 255))
                old_img = Image.open(FileName)
                old_img.save(resources_path + 'old_example.png')
                # old_img.show()

            image = cv2.imread(FileName)
            old_img = cv2.imread(resources_path + 'old_example.png')
            # Функция вычисления хэша

            resized = cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA)  # Уменьшим картинку
            gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  # Переведем в черно-белый формат
            avg = gray_image.mean()  # Среднее значение пикселя
            ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)  # Бинаризация по порогу

            # Рассчитаем хэш
            _hash = ""
            for x in range(8):
                for y in range(8):
                    val = threshold_image[x, y]
                    if val == 255:
                        _hash = _hash + "1"
                    else:
                        _hash = _hash + "0"

            return _hash

        def CompareHash(hash1, hash2):
            l = len(hash1)
            i = 0
            count = 0
            while i < l:
                if hash1[i] != hash2[i]:
                    count = count + 1
                i = i + 1
            return count

        hash1 = CalcImageHash(resources_path + "example.png")
        hash2 = CalcImageHash(resources_path + "old_example.png")

        if (CompareHash(hash1, hash2)) > 4:
            img = Image.open(resources_path + 'example.png')
            img.save(resources_path + 'old_example.png')

        else:

            return True
