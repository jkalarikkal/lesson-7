import cv2 
import numpy as np
import time

raw_video = cv2.VideoCapture (0) #0 refers to inbuilt cam

time.sleep(0)

count  = 0

background  = 0

#capturing bg

for i in range(60):
    return_val, background = raw_video.read()
    #return value will return true (tcapturing image) or false (video capture has stopped or not happening)
    if return_val == False:
        continue

#flipping img to flip to fit vid Cam

background = np.flip(background, axis = 1)


while(raw_video.isOpened()):
    return_val, img = raw_video.read()
    if not return_val:
        break
    count = count + 1
    img = np.flip(img, axis  = 1)
    #output from here down
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #mask 1
    lower_red = np.array([100,40,40])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    
    #mask 2
    lower_red = np.array([155,40,40])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    


    
