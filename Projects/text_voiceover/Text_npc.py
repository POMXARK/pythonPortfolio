import cv2
import numpy as np
import show_img as s



def npc():

    img = cv2.imread("for_tesseract.png")
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 0, 130], np.uint8)
    #lower = np.array([0,70,135],np.uint8)
    #upper = np.array([61, 225, 240], np.uint8)
    upper = np.array([60,225,245],np.uint8)
    mask = cv2.inRange(imghsv, lower, upper)
    #contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    im = np.copy(mask)
    #cv2.drawContours(im, contours, -1, (0, 255, 0), 0)
    cv2.imwrite("text_npc.png", im)
    text_npc = s.cv.imread('text_npc.png')
    s.show('text_npc',  text_npc)
   # pc = (40,0,165),(255,255,255) # голубой текст
   # npc = (0,70,135),(61,225,240) # желтый текст



