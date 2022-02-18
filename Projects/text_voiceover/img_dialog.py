#!/usr/local/bin/python3
import numpy as np
from PIL import Image

def img_dialog():

    # Открываем изображение и превращаем его в массив numpy
    im=np.array(Image.open("example.png").convert('RGB'))

    # Разберитесь, что мы ищем
    sought = [36, 50, 80] # искомый цвет

    # Найдите все пиксели, в которых 3 значения RGB совпадают с "искомыми", и посчитайте их
    result = np.count_nonzero(np.all(im==sought,axis=2))
    #print('синего цвета :',result)
    if  result > 90:
        #print('ЭТО КАДР ДИАЛОГА')
        return True
    else:
        #print('ЭТО НЕ ДИАЛОГ')
        return False