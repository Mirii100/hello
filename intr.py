import  cv2 as cv
img=cv.imread('C:\\Users\\njugu\\PycharmProjects\\try\\venv\\Scripts\\try_open_cv\\videos and pic\\logo.jpg',1)
cv.imshow('image',img)
cv.waitKey(0)
cv .destroyAllWindows()

capture= cv.videoCapture('C:\\Users\\njugu\\PycharmProjects\\try\\venv\\Scripts\\activate')
while True:
    isTrue,frame=capture.read()
    cv.imshow('video',frame)