import cv2 as cv

img = cv.imread('./opencv/photo.jpg')
cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('img', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('img', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#contours => is a py list which returns all coordinates of the contours
#hirearchies => is a representation of the hierarchy ex. rectange inside of circle iside of triangle
#cv.RETR_LIST => is a mode in which the findContours finds and returns the contours
#cv.RETR_EXTERNAL => returns only the external contours
#cv.RETR_TREE => returns only hierarchal contours
#  

cv.waitKey(0)