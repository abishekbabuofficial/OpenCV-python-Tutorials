import cv2 as cv

#reading image directly as grayscaled using 0 parameter
#gray = cv.imread('images/scenory.jpg',0)

img = cv.imread('images\scenory.jpg')
#to view normal original image uncommand below line
#cv.imshow('Image',img)

#converting the img into gray 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#displaying the output
cv.imshow('Gray img',gray)

cv.waitKey(0)
cv.destroyAllWindows()