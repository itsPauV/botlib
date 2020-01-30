import numpy as np
import cv2

class LineTracking():
    def track_line(self):
        # Capture the frames
        #video_capture = cv2.VideoCapture(0)
        video_capture.set(3, 160)
        video_capture.set(4, 120)

        ret, frame = video_capture.read()

        # Crop the image
        crop_img = frame[60:120, 0:160]

        # Convert to grayscale
        gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

        # Gaussian blur
        blur = cv2.GaussianBlur(gray,(5,5),0)

        # Color thresholding
        ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)

        # Find the contours of the frame
        _, contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)

        # Find the biggest contour (if detected)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)

            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            cv2.line(crop_img,(cx,0),(cx,720),(255,0,0),1)
            cv2.line(crop_img,(0,cy),(1280,cy),(255,0,0),1)

            cv2.drawContours(crop_img, contours, -1, (0,255,0), 1)

            #if cx >= 100:
            #    print("Turn Left!")
            #if cx < 100 and cx > 70:
            #    print("On Track!")
            #if cx <= 90:
            #    print("Turn Right")
            #print(cx)
            return cx

if __name__ == "__main__":
    video_capture = cv2.VideoCapture(0)
    while True:
        lt = LineTracking()
        print(lt.track_line())
