import cv2
import numpy as np

img_path = 'images.jpg'  
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Cannot find {img_path}")

image = cv2.resize(image, (800, 600))

text = "This is Computer Vision Lab"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, text, (50, 150), font, 1.2, (0, 0, 255), 2, cv2.LINE_AA)
cv2.imwrite('task4_image_text.jpg', image)

blank = np.zeros((300, 800, 3), dtype=np.uint8)
cv2.putText(blank, "This is Computer Vision Lab", (20, 150), font, 1.0, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imwrite('task4_blank_text.jpg', blank)

cv2.imshow('Image with Text', image)
cv2.imshow('Blank with Text', blank)
cv2.waitKey(0)
cv2.destroyAllWindows()
