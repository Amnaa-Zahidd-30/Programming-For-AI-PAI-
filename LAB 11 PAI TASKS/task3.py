import cv2

img_path = 'images.jpg' 
image = cv2.imread(img_path)
if image is None:
    raise FileNotFoundError(f"Cannot find {img_path}")

blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imwrite('task3_blurred.jpg', blurred)

y1, y2, x1, x2 = 100, 300, 150, 350
roi = blurred[y1:y2, x1:x2]

cv2.imshow('Blurred', blurred)
cv2.imshow('Cropped ROI', roi)
cv2.waitKey(0)
cv2.imwrite('task3_roi.jpg', roi)
cv2.destroyAllWindows()

print("Interpretation")
print("Blurring reduces high-frequency noise; cropping selects area of interest for further processing.")
