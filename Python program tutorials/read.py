#import the cv2 with/without reference obj
import cv2 as cv

#uncomment following lines for reading an image
'''
#read the image
img=cv.imread('images/apples.jpg')
#show the image
cv.imshow('tony',img)'''

#reading video input
vdo=cv.VideoCapture('images/video1.mp4')

#reading frame by frame of the video
while True:
    isTrue,frame = vdo.read()
    cv.imshow('video',frame)
    
    #quit the window by pressing 'e' key on keyboard
    if cv.waitKey(27)& 0xFF==ord('e'):
        break

#release the captured frames
vdo.release()
#waitKey is used to assign how long time the img/video should display
cv.waitKey(0)
cv.destroyAllWindows()
