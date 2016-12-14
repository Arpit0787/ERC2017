"""
Exercise-2

In our last example, we drew filled rectangle. You modify the code to draw an unfilled rectangle.

Example:
import cv2
import numpy as np
drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv2.destroyAllWindows()
"""
import cv2
import numpy as np
drawing = False # true if mouse is pressed
ix,iy = -1,-1
# mouse callback function
def draw_rectangle(event,x,y,flags,param):
    global ix,iy,drawing,mode,img,img1
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
                img1=np.copy(img)
                cv2.rectangle(img1,(ix,iy),(x,y),(255,255,255),1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
        img1=np.copy(img)
            
img = np.zeros((512,512,3), np.uint8)
img1 = img
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_rectangle)
print("Press Esc to exit")
while(1):
    if drawing==False:            
        cv2.imshow('image',img)
    else:
        cv2.imshow('image',img1)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()