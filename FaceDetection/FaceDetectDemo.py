# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 00:48:52 2018

@author: PrashantTrainer

Computer Vision Hands-on Exercise - 1

Enabling Camera and performing Face Detection using Viola-Jones Face Detection Algo

1. Install OpenCV
    pip install opencv-python
2. Download OpenCV package for CascadeClassifier
    https://github.com/opencv/opencv/tree/3.4.1 (Download ZIP)
3. Import CV
4. Enable Video Capture
5. Initialize Face Detection Classifier 
6. Writing the following logic
    a. Convert the image into grayscale
    b. Detect face with scale factor as 1.3 and minimum-neighbours as 5
    c. Draw a green rectangle surrounding the face based on edges (BGR format)
    d. Quit the program if pressed 'q' key
7. Release the camera
8. CLear and destroy all windows created by the program

"""

#Part 1 ---> Understanding how to enable camera and see live feeds

import cv2

#Enabling the camera for video capture 
camera = cv2.VideoCapture(0)

#Show the camera feed
while(True):
    # Capture frame-by-frame
    ret, frame = camera.read()

    # Display the resulting frame
    cv2.imshow('Face Detection by Prashant N',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()

#Part 2 ---> Performing Face Detection

import cv2

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)



while(True):
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) #BGR
    cv2.imshow("Face Detection By Prashant",img)
    if(cv2.waitKey(1) == ord('q')):
        break#millisecond
    
cam.release()
cv2.destroyAllWindows()            
