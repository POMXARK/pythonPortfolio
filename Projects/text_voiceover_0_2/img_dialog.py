#!/usr/local/bin/python3
import numpy as np
from PIL import Image
from options import set_opt

def img_dialog():

    # Открываем изображение и превращаем его в массив numpy
    im=np.array(Image.open("example.png").convert('RGB'))

    # Разберитесь, что мы ищем
    sought = [int(set_opt()['rgb1']), int(set_opt()['rgb2']), int(set_opt()['rgb3'])] # искомый цвет

    # Найдите все пиксели, в которых 3 значения RGB совпадают с "искомыми", и посчитайте их
    # ПРОВЕРКА СЛОМАНА!!!
    result = np.count_nonzero(np.all(im==sought,axis=2))
    #print('искомого цвета :',result)
    if  result > 90:
        #print('ЭТО КАДР ДИАЛОГА')
        return True
    else:
        #print('ЭТО НЕ ДИАЛОГ')
        return  False# True #False