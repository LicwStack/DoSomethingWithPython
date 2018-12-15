import cv2
import numpy as np

img = cv2.imread('3.jpg')
img=cv2.resize(img,None,fx=0.4,fy=0.4)
cv2.imshow('img', img)

rows, cols, channels = img.shape

# 转换hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([150, 43, 43])
upper_blue = np.array([180, 255, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)
cv2.imshow('Mask', mask)

# 腐蚀膨胀
erode = cv2.erode(mask, None, iterations=1)
# cv2.imshow('erode', erode)
dilate = cv2.dilate(erode, None, iterations=1)
# cv2.imshow('dilate', dilate)

# 遍历替换
for i in range(rows):
    for j in range(cols):
        if dilate[i, j] == 255:
            img[i, j] = (0, 0, 0)  # 此处替换颜色，为BGR通道

cv2.imshow('res', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
