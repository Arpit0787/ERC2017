"""
Exercise 3

Create a Paint application with adjustable colors and brush radius using trackbars. For drawing, refer previous
tutorial on mouse handling.
"""

import cv2
import numpy as np

drawing=False

def nothing(x):
    pass

def brush(event,x,y,flags,param):
    r=cv2.getTrackbarPos('R','Paint')
    g=cv2.getTrackbarPos('G','Paint')
    b=cv2.getTrackbarPos('B','Paint')
    radius=cv2.getTrackbarPos('Brush size','Paint')
    global img,drawing
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            cv2.circle(img,(x,y),radius,(b,g,r),-1)
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
    
img=np.zeros((400,512,3),np.uint8)
cv2.namedWindow('Paint')
cv2.createTrackbar('R','Paint',0,255,nothing)
cv2.createTrackbar('G','Paint',0,255,nothing)
cv2.createTrackbar('B','Paint',0,255,nothing)
cv2.createTrackbar('Brush size','Paint',1,20,nothing)

cv2.setMouseCallback('Paint',brush)
print("Press Q to exit")

while(1):
    cv2.imshow('Paint',img)
    k=cv2.waitKey(1)&0xFF
    if(k==ord('q')):
        break
cv2.destroyAllWindows()