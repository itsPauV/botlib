import numpy as np
import cv2

class Detection():
    
    def detect_on_image(img)
        paletten_cascade = cv2.CascadeClassifier('cascade_palette_front_48_16.xml')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        paletten = paletten_cascade.detectMultiScale(gray, 1.4, 3)

        for (x, y, w, h) in wuerfel:
            print("Palette detected")
            print("X: ({:d}/{:d}), Y: ({:d}/{:d}), W: {:d}, H: {:d}".format(x, img.shape[1], y, img.shape[0], w, h))
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
            break

        return img