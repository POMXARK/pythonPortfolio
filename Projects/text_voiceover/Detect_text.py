import numpy as np
import cv2 as cv
import show_img as s

def clear_text():
    img = cv.imread('text_npc.png')
    lower = np.array([0, 0, 0], np.uint8)
    upper = np.array([0, 0, 0], np.uint8)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
    thresh = cv.inRange(hsv, lower, upper)  # применяем цветовой фильтр
    contours0, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #cv.imshow('filter', thresh)

    ## Проецировать на ось
    H, W = img.shape[:2]
    xx = np.sum(hierarchy, axis=0) / H
    yy = np.sum(hierarchy, axis=1) / W

    ## Порог и найдите ноль
    xx[xx < 60] = 0
    yy[yy < 100] = 0

    ixx = xx.nonzero()
    iyy = yy.nonzero()

    # перебираем все найденные контуры в цикле
    N = 0
    for cnt in contours0:
        (x, y, w, h) = cv.boundingRect(cnt)
        if N < 101:
            rect = cv.minAreaRect(cnt)  # пытаемся вписать прямоугольник
            box = cv.boxPoints(rect)  # поиск четырех вершин прямоугольника
            box = np.int0(box)  # округление координат
            if N < 101:
            #if box[1][0] < 500 and box[0][0] < 500 :
                '''
                print('box :', box)
                print('box[0] :', box[0])
                print('box[1] :', box[1])
                print('box[0][0] :', box[0][0])
                print('box[0][1] :', box[0][1])
                print('box[1][0] :', box[1][0])
                print('box[1][1] :', box[1][1])
                print('max :', max(box[0][0], box[1][0]))
                print('min :', min(box[0][0], box[1][0]))
                print('raz box[0]: ', max(box[0][0], box[1][0]) - min(box[0][0], box[1][0]))
                print('raz box[1]: ', max(box[0][1], box[1][1]) - min(box[0][1], box[1][1]))
                print('raz bag: ',max(box[0][0], box[1][0]) - min(box[0][0],box[1][0]))
                #cv.drawContours(img, [box], -1, (255, 0, 0), 10)  # рисуем ошибки
                '''
                if max(box[0][0], box[1][0]) - min(box[0][0], box[1][0]) > 1 or \
                         max(box[0][1], box[1][1]) - min(box[0][1],box[1][1]) > 3: # проверка линии на точку (устранение неточности алгоритма)
                    print()
                    #cv.drawContours(img, [box], -1, (0, 255, 0), 2)  # рисуем прямоугольник
                else:

                    cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), cv.FILLED)
                    #cv.drawContours(img, [box], -1, (0, 0, 255 ), 0)  # рисуем ошибки
            # else:
            #   cv.drawContours(img, [box], -1, (0, 0, 255), 0)
            N+= 1
#            print('N :',N)



    cv.imwrite('clear_text.png', img)
    clear_text_img = cv.imread('clear_text.png')
    s.show('clear_text', clear_text_img)


#clear_text()

cv.waitKey()