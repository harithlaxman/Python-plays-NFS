import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

def nothing(x):
    pass

cv.namedWindow("Trackbar")

cv.createTrackbar("L-TH", "Trackbar", 0, 1000, nothing)
cv.createTrackbar("L-S", "Trackbar", 0, 255, nothing)
cv.createTrackbar("L-V", "Trackbar", 0, 255, nothing)
cv.createTrackbar("U-TH", "Trackbar", 0, 1000, nothing)
cv.createTrackbar("U-S", "Trackbar", 0, 255, nothing)
cv.createTrackbar("U-V", "Trackbar", 0, 255, nothing)

def roi(img, vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = (255,)*3
    cv.fillPoly(mask, vertices, match_mask_color)
    masked = cv.bitwise_and(img, mask)
    return masked

while True:
    l_th = cv.getTrackbarPos("L-TH", "Trackbar")
    l_s = cv.getTrackbarPos("L-S", "Trackbar")
    l_v = cv.getTrackbarPos("L-V", "Trackbar")
    u_th = cv.getTrackbarPos("U-TH", "Trackbar")
    u_s = cv.getTrackbarPos("U-S", "Trackbar")
    u_v = cv.getTrackbarPos("U-V", "Trackbar")

    image = mpimg.imread('roi.jpg')
    plt.imshow(image)
    plt.show()
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    #lower_white = np.array([l_h, l_s, l_v], dtype=np.uint8)
    #upper_white = np.array([u_h, u_s, u_v], dtype=np.uint8)

    lower_white = np.array([0,0,142], dtype=np.uint8)
    upper_white = np.array([255,51,255], dtype=np.uint8)
    lower_yellow = np.array([70,0,0], dtype=np.uint8)
    upper_yellow = np.array([111,255,255], dtype=np.uint8)

    mask_white = cv.inRange(hsv, lower_white, upper_white)
    mask_yellow = cv.inRange(hsv, lower_yellow, upper_yellow)

    comb_mask = cv.bitwise_or(mask_white, mask_yellow)
    
    vertices = np.array([[300,343],[380,290],[420,290],[500,343]], np.int32)
    cropped_image = roi(comb_mask, [vertices])
    processed_img = cv.GaussianBlur(cropped_image, (5,5), 0)
    processed_img = cv.Canny(processed_img, 200, 300)
    #cv.imshow("White Mask", mask_white)
    #cv.imshow("Yellow Mask", mask_yellow)
    #cv.imshow("Combined", comb_mask)
    cv.imshow("Final", cropped_image)

    key = cv.waitKey(1)
    if key == 27:
        break
        cv.destroyAllWindows()
    
    


