import numpy as np
import cv2
while True:
    image1 = cv2.imread("1.jpg")
    image2 = cv2.imread("2.png")
    cv2.imshow("2", image2)
    image2 = cv2.resize(image2, (640, 480))
    image1 = cv2.resize(image1, (640,480))
    hsv = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
    cv2.imshow("Image1", image1)

    l_g = np.array([50,100,100])
    u_g = np.array([70,255,255])
    mask=cv2.inRange(hsv,l_g,u_g)
    res= cv2.bitwise_and(image1, image1, mask=mask)
    f=image1-res
    final =np.where(f==0, image2, f) #where condition is true, replace new variable by old
    cv2.imshow("Final", f)







