import cv2 as cv

img =cv.imread('C:\\Users\\njugu\\PycharmProjects\\try\\venv\\Scripts\\try_open_cv\\videos and pic\\logo.jpg',1)
cv.imshow('image show',img)
cv.waitKey(0)
# showing edges  in images ,use canny
canny=cv.Canny(img,125,175)
cv.imshow('canny edges',canny)
cv.waitKey(0)

# dilating image
dilated =cv.dilate(canny,(3,3),iterations=1)
cv.imshow('dilated',dilated)
cv.waitKey(0)