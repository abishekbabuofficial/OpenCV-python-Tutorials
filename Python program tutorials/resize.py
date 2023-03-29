import cv2 as cv

img=cv.imread('images/tony.jpg')
#resizing
re_img = cv.resize(img,(500,500))
#show the image
cv.imshow('tony',re_img)

#uncomment following lines to work with video input
'''
#creating a user defined func to resize each frame of video, the scale indicating 75% of original dimension
def rescale(frame,scale=0.75):
    #shape[1] gets width of each frame and shape[0] gets height of each frame
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dim=(width,height)
    return cv.resize(frame,dim,interpolation=cv.INTER_AREA)
cap=cv.VideoCapture('images/video1.mp4')
while True:
    ret,frame = cap.read()
    rez= rescale(frame)
    cv.imshow("resized vdo",rez)
    
    if cv.waitKey(27) & 0xFF==ord('d'):
        break'''

#cv.waitKey(0)
cv.destroyAllWindows()
