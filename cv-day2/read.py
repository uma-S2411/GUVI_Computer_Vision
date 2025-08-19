import cv
import matplotlib.pyplot as plt

img = cv.imread("img.jpg")
rows,cols=img.shape[:2]
(h, w) = img.shape[:2]

print(img.shape)

rect = cv.rectangle(img,(300,300),(100,750),(50,50,50),2)
circle = cv.circle(img,(30,30),50,(0,0,255),1)

RM = cv.getRotationMatrix2D((w//2,h//2),45,1.0)
rotated = cv.warpAffine(img, RM, (w,h))

plt.imshow(cv.cvtColor(rotated,cv.COLOR_BGR2RGB))
plt.axis("off")
plt.show()