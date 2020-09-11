# -----------------------------------------------------------
# Creating a webcam face-detector using python.
#
# (C) 2020 Sandra VS Nair, Trivandrum
# email sandravsnair@gmail.com
# -----------------------------------------------------------

import cv2

#Haar cascade classifier file for detecting face.
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("photo.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Converting colored image to gray.

faces=face_cascade.detectMultiScale(gray_img,
                                    scaleFactor=1.05,
                                    minNeighbors=5)

#Drawing rectangles in detected faces.
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
    
#Preview of the image.
cv2.imshow("Face Detection",img)
cv2.waitKey(0)