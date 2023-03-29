import cv2 as cv

img=cv.imread('images/tony.jpg')

#resizing
re_img = cv.resize(img,(500,500))

#rotating the image using the matrix of image with specific angle of rotation
#below the var stores the dim of rows and cols
rows,cols = re_img.shape[:2]
m = cv.getRotationMatrix2D((cols/2,rows/2),90,1)

#The warpAffine() used to correct for geometric distortions or deformations that occur while rotating
res= cv.warpAffine(re_img, m, (cols, rows))

#alternate method using simply rotate function
rez = cv.rotate(re_img,cv.ROTATE_180)

#show the image
#getrotation output
cv.imshow('tony',res)
#rotate output
cv.imshow('updown img',rez)

cv.waitKey(0)
cv.destroyAllWindows()
