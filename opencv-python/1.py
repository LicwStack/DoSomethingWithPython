import cv2

for i in dir(cv2):
    if i.startswith('COLOR_'):
        print(i)

# flags=[i for in dir(cv2) if i startswith('COLOR_')]
# print(flags)