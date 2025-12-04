import cv2
import numpy as np

img_path = 'task1_gray.jpg' 
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Cannot find {img_path}")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.imwrite('task5_threshold.jpg', thresh)

angle = 600
(h, w) = thresh.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

rotated = cv2.warpAffine(thresh, rotation_matrix, (w, h))
cv2.imwrite('task5_rotated_600.jpg', rotated)

cv2.imshow('Thresholded', thresh)
cv2.imshow('Rotated (600 deg)', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
