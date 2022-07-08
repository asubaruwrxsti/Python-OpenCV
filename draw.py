import cv2 as cv
import numpy as np

blank = np.zeros((512,512,3), dtype=np.uint8)
cv.imshow('blank', blank)

#paint img to ceratin color
blank[200:300, 300:400] = 213, 255, 0
cv.imshow('blank', blank)

#draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), thickness=-1, color=(0,255,0))
cv.imshow('blank', blank)

#draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), radius=40, thickness=40, color=(0,0,255))
cv.imshow('blank', blank)

#draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), thickness=40, color=(0,255,255))
cv.imshow('blank', blank)

#write text
cv.putText(blank, 'OpenCV', (225,225), cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), thickness=2)
cv.imshow('blank', blank)

cv.waitKey(0)

