import cv2 as cv


def rescaleFrame(frame, scale=0.5):
    #support for both webcam and video file
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height, capture):
    #only webcam video capture
    capture.set(3, width)
    capture.set(4, height)


img = cv.imread('photo.jpg')
cv.imshow('image', rescaleFrame(img))

video = cv.VideoCapture('sample.mp4')

while True:
    isTrue, frame = video.read()
    cv.imshow('video', rescaleFrame(frame))

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()

cv.waitKey(0)
