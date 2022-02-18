import cv2
from show_img import show

def smart_cut():
    img = cv2.imread('border.png', -1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gray.png",gray)
    gray_img = cv2.imread('gray.png')
    show('gray', gray_img)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imwrite("hsv.png",hsv)
    hsv_img = cv2.imread('hsv.png')
    show('hsv', hsv_img)

    mask = cv2.inRange(hsv, (0, 160, 100), (255, 255, 255))
    cv2.imwrite("mask.png",mask)
    mask_img = cv2.imread('mask.png')
    show('mask', mask_img)
    binary = cv2.bitwise_not(mask)
    (contours,hierarchy) = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if y < 10:
            #print('y :', y)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), cv2.FILLED)

    vis = img.copy()
    cv2.imwrite('for_tesseract.png', vis)
    show('for_tesseract.png', vis)