import numpy as np
import show_img as s
def tesserack_mask():
    img = s.cv.imread("clear_text.png")
    s.show('for_tesseract', img)
    img = s.cv.cvtColor(img, s.cv.COLOR_BGR2HSV)

    # формируем начальный и конечный цвет фильтра
    h_min = np.array((0, 0, 102), np.uint8)
    h_max = np.array((255, 180, 255), np.uint8)

    # накладываем фильтр на кадр в модели HSV
    img= s.cv.inRange(img, h_min, h_max)
    s.cv.imwrite('tesseract_mask.png', img)
    tesseract_mask = s.cv.imread('tesseract_mask.png')
    s.show('tesseract_mask', tesseract_mask)