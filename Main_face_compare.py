import cv2
import numpy as np
from VGGnet import verifyFace
import os

def main(pname,tershold=35):

    cascadePath = os.path.dirname(os.path.abspath(__file__)) + "\\trainer\\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)

    font = cv2.FONT_HERSHEY_SIMPLEX


    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height

    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    dir = os.path.dirname(os.path.abspath(__file__)) + '\\img\\live.jpg'
    count = 0

    while count<100:
        
        ret, img =cam.read()
        count+=1
        print(count)

        faces = faceCascade.detectMultiScale( 
            img,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )

        
        if count== 99:
            cv2.imwrite(dir, img)
        else:
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            
        cv2.imshow('camera',img) 

        k = cv2.waitKey(1) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        
    cv2.destroyAllWindows()

    cosine,euclidean = verifyFace("passenger.jpg", 'live.jpg')
    
    out_confidence = round(100 - euclidean , 5)
    out =False
    if out_confidence>tershold:
        print('they are same!')
        out = True
        cv2.putText(img, pname , (x+5,y-5), font, 1, (0,0,255), 2)
        cv2.putText(img, str(out_confidence), (x+5,y+h-5), font, 1, (255,0,0), 2)  
    else:
        cv2.putText(img, "unKnown!" , (x+5,y-5), font, 1, (0,0,255), 2)
        cv2.putText(img, str(out_confidence), (x+5,y+h-5), font, 1, (255,0,0), 2)
        

    while True:
        cv2.imshow('output',img)
        k = cv2.waitKey(1) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
    
    
     
    cam.release()
    cv2.destroyAllWindows()
    
    return out,out_confidence

if __name__ == '__main__':
    out,confidence = main('sajjad')
    print(f' output percentage and final condition is : {out} , {confidence}')