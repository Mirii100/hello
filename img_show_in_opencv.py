import cv2 as cv
import  numpy as np


blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)
blank[:]= 0,255,0
cv.imshow('green',blank)
# drawing a rectangle in the blank space
cv.rectangle(blank,(0,0),(250,250),(0,255,255),thickness=cv.FILLED)
# showing  rectangle on the screen
cv.imshow('rectangle',blank)
cv.circle(blank,(250,250),40,(blank.shape[1]//2,blank.shape[1]//2),thickness=3)
cv.imshow('circle',blank)
cv.putText(blank,'Alexander njuguna is practising opencv and numpy code',(0,225),cv.FONT_HERSHEY_TRIPLEX,
           1.0,(0,2,255),2)
cv.imshow('text',blank)
#img =cv.imread('C:\\Users\\njugu\\PycharmProjects\\try\\venv\\Scripts\\try_open_cv\\videos and pic\\logo.jpg',1)
#cv.imshow('image show',img)
cv.waitKey(0)
cv .destroyAllWindows()