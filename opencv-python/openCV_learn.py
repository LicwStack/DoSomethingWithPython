"""
learn  opencv-python
"""
import cv2
import numpy as np


img1 = cv2.imread('opencv-logo.png')
rows, cols = img1.shape[:2]

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img1, M, (cols, rows))

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# res1 = cv2.resize(img1, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
#
# height, width = img1.shape[:2]
#
# res2 = cv2.resize(img1, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)
#
# while 1:
#     cv2.imshow('res1', res1)
#     cv2.imshow('res2', res2)
#
#     if cv2.waitKey(1) & 0xFF == 27:
#         break
#
# cv2.destroyAllWindows()
