import cv2 as cv

img = cv.imread('./opencv/photo.jpg')
cv.imshow('Original', img)

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Original', gray)

#blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Original', blur)

#edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Original', canny)

#dilate image
dilated = cv.dilate(canny, (7,7), iterations=1)
cv.imshow('Original', dilated)

#eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Original', eroded)

#resize
resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA) #cubic, linear
cv.imshow('Original', resize)

#cropping
cropped = img[50:200, 200:400]
cv.imshow('Original', cropped)

cv.waitKey(0)