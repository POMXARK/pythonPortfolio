import matplotlib.pyplot as plt
import cv2 as cv

def show(title, img, color=True):
    if color:
       pass
        #mng = plt.get_current_fig_manager()
#        mng.window.state("zoomed")
        #plt.imshow(img[:, :, ::-1]), plt.title(title), plt.show() # для диагностики
    else:
        pass
        #mng = plt.get_current_fig_manager()
#        mng.window.state("zoomed")
        #plt.imshow(img, cmap='gray'), plt.title(title), plt.show() # для диагностики

def show_img(title,img_obj):
    img_obj = img_obj
    title_img = str(title + ".png")
    print('title: ', title_img)
    cv.imwrite(title_img, img_obj)
    img_obj = cv.imread(title_img)
    show(title_img, img_obj)