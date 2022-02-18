import os
import cv2
import numpy as np
from options import set_opt
from show_img import show



def detect_line():

#    print(1)

    img_orig = cv2.imread('example.png')
    img = cv2.imread('example.png')

    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imwrite("hsv.png",img)
    hsv_img = cv2.imread('hsv.png')
    show('hsv', hsv_img)

    img = cv2.inRange(img,(int(set_opt()['mb_h1']), int(set_opt()['mb_s1']), int(set_opt()['mb_v1'])) ,(int(set_opt()['mb_h2']), int(set_opt()['mb_s2']), int(set_opt()['mb_v2'])) )#(0, 160, 100), (255, 255, 255) # выделение линий
    cv2.imwrite("mask.png", img)
    mask_img = cv2.imread('mask.png')
    show('mask', mask_img)
    binary = cv2.bitwise_not(img)

    img = cv2.Canny(img, 50, 50,  apertureSize=3)  # инвентирует изображение выделяя контуры, Обнаружение хитрого края
    cv2.imwrite("edges.png", img)
    edges_img = cv2.imread('edges.png')
    show('edges ', edges_img)

    minLineLength = img.shape[1] - 1900  # что-то о линиях важно находит прямые линии



    lines = cv2.HoughLinesP(image=img, rho=1, theta=np.pi / 180, threshold=100, lines=np.array([]), minLineLength=minLineLength, maxLineGap=2)  # threshold - минимальная длина линии


    try:
        a, b, c = lines.shape  # значение в матрице lines
    except AttributeError:
        #print('ОШИБКА НЕТ ТЕКСТА')
        if os.path.isfile('result.png') == True:
            os.remove('result.png')
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

            cv2.line(img_orig , (lines[i][0][0] + x1, lines[i][0][1] + y1), (lines[i][0][2] + x2, lines[i][0][3] + y2),
                     (0, 255, 255), 1, cv2.LINE_AA)  # подсветка линий


            N += 1

    cv2.imwrite('result.png', img_orig)
    result_img = cv2.imread('result.png')
    show('result ', result_img)

    return 0


