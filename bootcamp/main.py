#This project is my first python program of sorts. This is extremely cool and fun-to-play with project. There are multiple
#There are multiple possibilities to play with this. 
import numpy as np                     
import cv2
#Here both NumPy and OpenCV in short cv2 are python libraries. NumPy helps us to play with different mathematical functions
#on matrices and arrays. OpenCV is used for image, videos and other visual stuff to program upon. Computer Vision stuff.

video1 = cv2.VideoCapture("green.mp4")  
#Method for video capturing from video files, image sequences or cameras. Video capturing means allocating it resources.
#video is another datatype itself comprising of matrices, combo of lists, comprising of different frames.
                                                         
image1 = cv2.imread("image.jpg")       
#cv2.imread() method loads an image from the specified file. Allocates resources 
image = cv2.resize(image1, (640,480))
while True:
    ret, frame1 = video1.read()           #checks the video, if it is broken, ret will return false and out of loop ;if video is right, video is stored inside frame
    frame1 = cv2.resize(frame1, (640,480))
    hsv_cvted=cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    cv2.imshow("Frame", frame1)

    l_g = np.array([50, 100, 100])
    u_g = np.array([70, 255, 255])
    #range for red values. mask will contain white areas for those where red is present while black areas for those where red is not
    mask=cv2.inRange(hsv_cvted, l_g, u_g)
    cv2.imshow("Mask", mask)
    res=cv2.bitwise_and(frame1, frame1, mask=mask)
    cv2.imshow("Result", res)
    f=frame1-res
    green_screen=np.where(f==0, image, f)
    cv2.imshow("Green Screen", green_screen)

    k=cv2.waitKey(1)                   #checks for key press, puts its unicode value in k
    if k == ord('q'):                  #ord gives its unicode value
        break 
    print(k)

video1.release
cv2.destroyAllWindows()



                                


                    

