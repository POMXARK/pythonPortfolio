import cv2
import numpy as np
from show_img import show
from options import set_opt



def npc():
    img = cv2.imread("for_tesseract.png")
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([int(set_opt()['h1']), int(set_opt()['s1']), int(set_opt()['v1'])], np.uint8)
    upper = np.array([int(set_opt()['h2']), int(set_opt()['s2']), int(set_opt()['v2'])], np.uint8)
    #upper = np.array([60,225,245],np.uint8)
    mask = cv2.inRange(imghsv, lower, upper)
    im = np.copy(mask)
    #cv2.drawContours(im, contours, -1, (0, 255, 0), 0)
    cv2.imwrite("text_npc.png", im)
    text_npc = cv2.imread('text_npc.png')
    show('text_npc',  text_npc)




