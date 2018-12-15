import cv2

e1 = cv2.getTickCount()
img1 = cv2.imread('bg.jpg')
img2 = cv2.imread('opencv-logo.png')

rows1, cols1, channels1 = img1.shape
rows2, cols2, channels2 = img2.shape

roi = img1[0:rows2, 0:cols2]
# cv2.imshow('roi', roi)

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # 灰度处理

ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)  # 二值化处理
mask_inv = cv2.bitwise_not(mask)  # 颜色取反

# cv2.imshow('mask', mask)
# cv2.imshow('mask_inv', mask_inv)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
# cv2.imshow('img1_bg', img1_bg)

img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)
# cv2.imshow('img2_fg', img2_fg)

dst = cv2.add(img1_bg, img2_fg)
# cv2.imshow('dst', dst)

img1[0:rows2, 0:cols2] = dst

cv2.imshow('res', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

e2 = cv2.getTickCount()
time = (e2 - e1)/cv2.getTickFrequency()
print(time)

