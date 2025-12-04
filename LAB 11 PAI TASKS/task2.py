
import cv2
import numpy as np

images = np.zeros((300, 400, 3), dtype=np.uint8)

cv2.rectangle(images, (50, 50), (200, 150), (0, 0, 255), -1)
cv2.circle(images, (300, 200), 50, (0, 255, 0), -1)
cv2.rectangle(images, (220, 30), (370, 90), (255, 0, 0), 3)

cv2.imshow('Shapes', images)
cv2.waitKey(0)
cv2.imwrite('task2_shapes.png', images)
cv2.destroyAllWindows()
