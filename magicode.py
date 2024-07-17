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
    
    mask1 = mask1+ mask2

    mask1  = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations = 2 )
    mask1 =  cv2.dilate(mask1, np.ones ((3,3), np.uint8),iterations = 1)

    mask2 = cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(background, background, mask = mask1)
    res2 = cv2.bitwise_and(img, img, mask = mask2)

    final_output = cv2.addWeighted(res1,1,  res2,1, 0 )
    cv2.imshow("Invisible Man", final_output)

    k =  cv2.waitKey(10)
    #27 - Escape key
    if k == 27:
        break

    



    
