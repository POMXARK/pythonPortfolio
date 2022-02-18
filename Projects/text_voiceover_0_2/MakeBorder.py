
from show_img import show
import cv2 as cv




def make_border():

    try:
        if open('result.png') == False:
            return False
    except OSError:
        return False

    if open('result.png') == False:
        return False

    borderType = cv.BORDER_CONSTANT
    # Loads an image


    src = cv.imread(cv.samples.findFile('result.png'), cv.IMREAD_COLOR)
    border = 5


    # value = [randint(0, 255), randint(0, 255), randint(0, 255)] # моргание цвета
    value = (0, 255, 255)
    # dst = cv.copyMakeBorder(src, top, bottom, left, right, borderType, None, value)
    dst = cv.copyMakeBorder(src, border, border, border, border, borderType, None, value)
    cv.imwrite('border.png', dst)
    show('border', dst)

    return 0


