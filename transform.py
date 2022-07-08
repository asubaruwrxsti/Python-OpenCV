import cv2 as cv
import numpy as np

img = cv.imread('./opencv/photo.jpg')
cv.imshow('img', img)

#translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0]) #shape 1 = width; shape 0 = height
    return cv.warpAffine(img, transMat, dimensions)
    # -x => left
    # -y = up
    # x => right
    # y => down

translated = translate(img, 100,100) #down, right
cv.imshow('img', translated)

#rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv. warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 50)
cv.imshow('img', rotated)

#resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('img', resized)

#flipping
flip = cv.flip(resized, 0) #1=> vertically; 0=> horizontally; -1 =>both
cv.imshow('img', flip)

#cropping
cropped = img[200:300, 300:400]
cv.imshow('img', cropped)

cv.waitKey(0)