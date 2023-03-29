import cv2 as cv

img = cv.imread('images/flower.jpg')
#converting to rgb(optional)
image = cv.cvtColor(img,cv.COLOR_BGR2RGB)

#blur img using blur() function
blur = cv.blur(img,(20,20))
cv.imshow('blurred image',blur)

cv.waitKey(0)
cv.destroyAllWindows()