import cv2

img = cv2.imread("building.jpeg")

cv2.imread("compressed_image_30.jpeg",img,[int (cv2.IMWRITE_JPEG_QUALITY),30])

cv2.imread("compressed_image_90.jpeg",img,[int (cv2.IMWRITE_JPEG_QUALITY),90])
