import cv2


image = cv2.imread("bitcoin.webp")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

ret, thresh_binary = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)

cv2.imshow("Original image", image)
cv2.imshow("THRESH_BINARY", thresh_binary)
cv2.waitKey(0)
