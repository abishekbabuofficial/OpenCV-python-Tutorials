import cv2 as cv

'''Haar Cascade is a feature-based object detection algorithm to detect objects from images.
A cascade function is trained on lots of positive and negative images for detection. 
The algorithm does not require extensive computation and can run in real-time.'''

#inputing the pre-trained classifier annotations which is in the .xml file
haar_cascade = cv.CascadeClassifier('haar_face.xml')

#uncomment following lines to detect faces from an imagae
'''img = cv.imread('images/hang.jpg')
faces_rect = haar_cascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=3)
for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(230,50,150),2)
cv.imshow("Detected Face",img)
cv.waitKey(0)
cv.destroyAllWindows()'''

#detecting the faces live through webcam
cap = cv.VideoCapture(0)
while True:
    ret,frame = cap.read()
    #converting the frame to gray as opencv classifies only on grayscaled data
    image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #detecting faces in frame using detectMultiScale()
    faces_rect = haar_cascade.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=3)

    #drawing bounding boxes around the faces
    for (x,y,w,h) in faces_rect:
        #(230,50,150) is the colour of boxes which is in RGB format and 2 indicates thickness of box
        cv.rectangle(frame,(x,y),(x+w,y+h),(230,50,150),2)

    cv.imshow("Detected Face",frame)

    if cv.waitKey(27) & 0xFF==ord('d'):
        break

cap.release()
cv.destroyAllWindows()
