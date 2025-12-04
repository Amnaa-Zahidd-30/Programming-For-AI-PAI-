import cv2

img1_path = 'images.jpg'  
img2_path = 'honey-bee.jpg'  

img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)
if img1 is None or img2 is None:
    raise FileNotFoundError("Check image1.jpg and image2.jpg paths")

img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

alpha = 0.6
beta = 0.4
blended = cv2.addWeighted(img1, alpha, img2, beta, 0.0)
cv2.imwrite('task6_blended.jpg', blended)

gray_blend = cv2.cvtColor(blended, cv2.COLOR_BGR2GRAY)
cv2.imwrite('task6_gray_blend.jpg', gray_blend)

equalized = cv2.equalizeHist(gray_blend)
cv2.imwrite('task6_equalized.jpg', equalized)

cv2.imshow('Blended', blended)
cv2.imshow('Gray Blended', gray_blend)
cv2.imshow('Equalized', equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()

