import cv2

img_path = 'images.jpg'  
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError("Cannot find {img_path}")

cv2.imshow('Original Image', image)
cv2.waitKey(500)  

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray)
cv2.waitKey(500)

new_size = (300, 200)  
resized = cv2.resize(image, new_size)
cv2.imshow('Resized Image', resized)
cv2.waitKey(500)

cv2.imwrite('task1_gray.jpg', gray)
cv2.imwrite('task1_resized.jpg', resized)

cv2.destroyAllWindows()
