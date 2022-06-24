import cv2
import numpy as np
from PIL import Image
import os

from face_recognition import face_recognition
from face_training import face_training

def main(pname,treshold):
    finalCon = False

    face_detector = cv2.CascadeClassifier('.\\trainer\\haarcascade_frontalface_default.xml')

    imagePath = '.\\img\\passenger.jpg'

    PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
    gray = np.array(PIL_img,'uint8')

    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:

        cv2.rectangle(gray, (x,y), (x+w,y+h), (255,0,0), 2)     

        dir = '.\\dataset\\0.1.jpg'
        cv2.imwrite(dir, gray[y:y+h,x:x+w])
        
        # cv2.namedWindow("image", cv2.WINDOW_NORMAL)    # Create window with freedom of dimensions
        # imS = cv2.resize(gray, (200, 300))    
        # cv2.imshow('image', imS)

    face_training()
    outPer = face_recognition(pname)
    if(outPer>treshold):
        finalCon = True
    
    # os.remove('.\\img\\passenger.jpg')
    # os.remove('.\\dataset\\0.1.jpg')
    return outPer , finalCon

if __name__=='__main__':
    outPer , finalCon =main('negin',50)
    print(f' output percentage and final condition is : {outPer} , {finalCon}')