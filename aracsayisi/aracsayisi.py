import cv2
import numpy as np
cam=cv2.VideoCapture("video1.avi")
backsub=cv2.createBackgroundSubtractorMOG2()
c=0

while True:
    ret,frame=cam.read()
    if ret==1:
        fgmask=backsub.apply(frame)
        
        cv2.line(frame,(0,50),(300,50),(0,255,0),2)
        cv2.line(frame,(0,50),(300,70),(0,255,0),2)
        
        contours,hiers=cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        try:hiers=hiers[0]
        except:hiers=[]
        
        for contour,hier in zip(contours,hiers):
            (x,y,w,h)=cv2.boundingRect(contour)
            if w>40 and h>40:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
                if x>50 and x<70:
                    c=c+1
        font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        cv2.putText(frame,"car"+str(c),(90,100),font,2,(0,0,255),2,cv2.LINE_AA)
        cv2.imshow("vid",fgmask )
        cv2.imshow("vid1", frame)
       
        
    if cv2.waitKey(40)==ord("q"):
        break



cam.release()
cv2.destroyAllWindows()