import cv2
import numpy as np
from PIL import Image
import os

def face_training():

    # Path for face image database
    path = '.\\dataset\\'

    recognizer = cv2.face.LBPHFaceRecognizer_create()#for images recognizing
    detector = cv2.CascadeClassifier(".\\trainer\\haarcascade_frontalface_default.xml") #for images crop

    # function to get the images and label data
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
        faceSamples=[]
        ids = []
        ''' input the pictures and put ids (from picture names) and pictures in two lists'''
        for imagePath in imagePaths:

            PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
            img_numpy = np.array(PIL_img,'uint8')

            id = int(os.path.split(imagePath)[-1].split(".")[0])
            faces = detector.detectMultiScale(img_numpy)

            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)
        return faceSamples,ids
    

    print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    faces,ids = getImagesAndLabels(path)

    
    ## Show the image from dataset
    # while True:
    #     cv2.imshow('camera',faces[0]) 
    #     k = cv2.waitKey(10000) & 0xff # Press 'ESC' for exiting video
    #     if k == 27:
    #         break

    recognizer.train(faces, np.array(ids))

    # Save the model into trainer/trainer.yml
    recognizer.write('.\\trainer\\trainer.yml')

    # Print the numer of faces trained and end program
    print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
    
    return True

