"""
Exercise-1

Try to create the logo of OpenCV using drawing functions available in OpenCV
"""
import numpy as np
import cv2
img=np.ones((600,600,3),np.uint8)
font=cv2.FONT_HERSHEY_PLAIN
cv2.circle(img, (300,135), 100, (0,0,255),-1)
cv2.circle(img, (300,135), 40, (0,0,0),-1)
cv2.circle(img, (180,375), 100, (0,255,0),-1)
cv2.circle(img, (180,375), 40, (0,0,0),-1)
cv2.circle(img, (420,375), 100, (255,0,0),-1)
cv2.circle(img, (420,375), 40, (0,0,0),-1)
pts1 = np.array([[300,135],[250,235],[350,235]], np.int32)
pts1 = pts1.reshape((-1,1,2))
cv2.fillPoly(img,[pts1],(0,0,0))
pts2 = np.array([[180,375],[290,375],[250,235]], np.int32)
pts2 = pts2.reshape((-1,1,2))
cv2.fillPoly(img,[pts2],(0,0,0))
pts3 = np.array([[420,375],[350,235],[490,235]], np.int32)
pts3 = pts3.reshape((-1,1,2))
cv2.fillPoly(img,[pts3],(0,0,0))
cv2.putText(img,'OpenCV',(180,550),font,4,(255,255,255),2)
cv2.imshow('exercise-1',img)
print("Press Q to exit")
k=cv2.waitKey(0) & 0xFF
if k==ord('q'):
    cv2.destroyAllWindows()