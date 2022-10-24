import cv2


image = cv2.imread("bitcoin.webp")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

adap_thresh = cv2.adaptiveThreshold(
    blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 65, -2)

cv2.imshow("Original image", image)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", adap_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()


image = cv2.imread("letter.webp")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

adap_thresh = cv2.adaptiveThreshold(
    blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3)
cv2.imshow("Original image", image)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", adap_thresh)
cv2.waitKey(0)
