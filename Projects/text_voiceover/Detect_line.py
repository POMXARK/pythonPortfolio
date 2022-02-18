import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import show_img as s

def detect_line():



    img_orig = cv2.imread('example.png')
    img = cv2.imread('example.png')

    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imwrite("hsv.png",img)
    hsv_img = cv2.imread('hsv.png')
    s.show('hsv', hsv_img)

    img = cv2.inRange(img, (0, 160, 100), (255, 255, 255))
    cv2.imwrite("mask.png", img)
    mask_img = cv2.imread('mask.png')
    s.show('mask', mask_img)
    binary = cv2.bitwise_not(img)

    img = cv2.Canny(img, 50, 50,  apertureSize=3)  # инвентирует изображение выделяя контуры, Обнаружение хитрого края
    cv2.imwrite("edges.png", img)
    edges_img = cv2.imread('edges.png')
    s.show('edges ', edges_img)

    minLineLength = img.shape[1] - 1900  # что-то о линиях важно находит прямые линии

    #lines = np.zeros(shape=(1,1))
    #print('lines : ',len(lines))

    lines = cv2.HoughLinesP(image=img, rho=1, theta=np.pi / 180, threshold=100, lines=np.array([]), minLineLength=minLineLength, maxLineGap=2)  # threshold - минимальная длина линии


    try:
        a, b, c = lines.shape  # значение в матрице lines
    except AttributeError:
        #print('ОШИБКА НЕТ ТЕКСТА')
        if os.path.isfile('result.png') == True:
            os.remove('result.png')
        return False





    # lines =[[]]
    # [[  72   56 1845   56]]
    # lines=np.array([[[60,56,1850,56]]]) #(x1,y1,x2(len),y2)      y1,y2 - чем меньше, тем ближе к верхниму краю (len) - длина линии (вправо) x1,x2- горизонтальный отступ от левого края , чем меньше тем ближе
    # lines=np.array([[[0,56,2000,56]]]) #(x1,y1,x2(len),y2)      y1,y2 - чем меньше, тем ближе к верхниму краю (len) - длина линии (вправо) x1,x2- горизонтальный отступ от левого края , чем меньше тем ближе
    #print('shape :', len(lines.shape))
    #if len(lines) < 1:
    #     print('ОШИБКА НЕТ ТЕКСТА')


    a, b, c = lines.shape  # значение в матрице lines

    # print('a: ',a)
    # print('b :',b)
    # print('c :',c)

    # lines =[[  72  ,56,1845  ,56]]


    # print(lines)

    N = 0

    for i in range(a):
        # print(N)
        if N < 3:
            #print(lines[i])
            # print(lines[i][0][0])
            # print(lines[i][0][1])
            # print(lines[i][0][2])
            # print(lines[i][0][3])
            rho = 1
            theta = np.pi / 180
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho

            raz_x = lines[i][0][1] - lines[i][0][3]
            raz_y = lines[i][0][0] - lines[i][0][2]

            #print(raz_x, ' - raz - ', raz_y)

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

            # if i < 1:
            # print('lines[i] :',lines[i])
            # print('a :',a)
            # print('i :',i)
            # rho, theta = i[0]
            # x0 = a * rho
            # x1 = lines[i][0][0]
            # cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.line(img_orig , (lines[i][0][0] + x1, lines[i][0][1] + y1), (lines[i][0][2] + x2, lines[i][0][3] + y2),
                     (0, 255, 255), 1, cv2.LINE_AA)  # подсветка линий
            #print((lines[i][0][0] + x1, lines[i][0][1] + y1), (lines[i][0][2] + x2, lines[i][0][3] + y2))

            N += 1

    cv2.imwrite('result.png', img_orig)
    result_img = cv2.imread('result.png')
    s.show('result ', result_img)

    return 0