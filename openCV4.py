import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

px = img[55, 55]

print(px)

# img[55, 55] = [255, 255, 255]

roi = img[100:150, 100:150]


# img[100:150, 150:250] = [255, 255, 255]

watch_face = img[150:300, 90:350]
img[0:150, 0:260] = watch_face

cv2.imshow('Frame', img)

cv2.waitKey(0)
cv2.destroyAllWindows()