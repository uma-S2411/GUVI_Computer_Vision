import cv2
import numpy as np
import matplotlib.pyplot as plt


img = np.zeros((500,500),dtype=np.uint8)
circle = cv2.circle(img,(250,250),250,(255,255,255),-1)
rect = cv2.rectangle(img.copy(),(50,50),(250,250),(255,255,255),-1)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()