from PIL import Image, ImageChops
import cv2

from img_dialog import img_dialog



def difference_images():



    if  img_dialog() == False: # проверка присутвия цвета
        img = Image.new('RGB', (250, 250), (255, 255, 255))
        img.save('old_example.png')
        img.save('example.png')
        #print('Не диалог проверять не нужно')
        return True

    def CalcImageHash(FileName):


        try:
            old_img= Image.open('old_example.png')
        except OSError:
            #print('НОВЫЙ КАДР')
#            old_img = Image.new('RGB', (250, 250), (255, 255, 255))
            old_img = Image.open(FileName)
            old_img.save('old_example.png')
            #old_img.show()


        image = cv2.imread(FileName)
        old_img = cv2.imread('old_example.png')
        # Функция вычисления хэша

        resized = cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA)  # Уменьшим картинку
        gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  # Переведем в черно-белый формат
        avg = gray_image.mean()  # Среднее значение пикселя
        ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)  # Бинаризация по порогу

        # Рассчитаем хэш
        _hash = ""
        for x in range(8):
            for y in range(8):
                val = threshold_image[x, y]
                if val == 255:
                    _hash = _hash + "1"
                else:
                    _hash = _hash + "0"

        return _hash


    def CompareHash(hash1, hash2):
        l = len(hash1)
        i = 0
        count = 0
        while i < l:
            if hash1[i] != hash2[i]:
                count = count + 1
            i = i + 1
        return count


    hash1=CalcImageHash("example.png")
    hash2=CalcImageHash("old_example.png")


    if (CompareHash(hash1, hash2)) > 4:
        img = Image.open('example.png')
        img.save('old_example.png')

    else:

        return True



