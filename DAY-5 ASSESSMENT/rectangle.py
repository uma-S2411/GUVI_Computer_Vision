import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img.jpeg")
print(img.shape)

cv2.rectangle(img,(10,10),(100,100),(255,0,0),2)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()
