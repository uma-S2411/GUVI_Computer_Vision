import cv2
import matplotlib.pyplot as plt
img=cv2.imread("img.jpeg")
grayscale= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(grayscale,100,300)
plt.imshow(cv2.cvtColor(grayscale,cv2.COLOR_BGR2RGB))
plt.show()