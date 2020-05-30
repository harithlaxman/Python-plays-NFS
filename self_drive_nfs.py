import numpy as np
import cv2 as cv
from PIL import ImageGrab
import time
from directxkeys import ReleaseKey, PressKey, W, A, S, D
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from grabscreen import grab_screen

# for i in list(range(4))[::-1]:
#     print(i+1)
#     time.sleep(1)
#
# print('down')
# PressKey(W)
# time.sleep(3)
# print('up')
# PressKey(W)
# ReleaseKey(W)

def draw_lines(img, lines):
    try:
        for line in lines:
            coord = line[0]
            cv.line(img, (coord[0], coord[1]), (coord[2], coord[3]), [255, 255, 255], 2)
    except:
        pass

def roi(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = (255,) *3
    cv.fillPoly(mask, vertices, match_mask_color)
    masked = cv.bitwise_and(img, mask)
    return masked

def process_img(ori_image):

    hsv = cv.cvtColor(ori_image, cv.COLOR_BGR2HSV)
    lower_white = np.array([0,0,142], dtype=np.uint8)
    upper_white = np.array([255,51,255], dtype=np.uint8)
    lower_yellow = np.array([70,0,0], dtype=np.uint8)
    upper_yellow = np.array([111,255,255], dtype=np.uint8)
    #Masking White and Yellow
    mask_white = cv.inRange(hsv, lower_white, upper_white)
    mask_yellow = cv.inRange(hsv, lower_yellow, upper_yellow)
    processed_img = cv.bitwise_or(mask_white, mask_yellow)
    #ROI
    vertices = np.array([[300,343],[380,290],[420,290],[500,343]], np.int32)
    processed_img = roi(processed_img, [vertices])
    #Canny edge detection
    processed_img = cv.Canny(processed_img, threshold1 = 200, threshold2 = 300)
    #Gaussian Blur
    processed_img = cv.GaussianBlur(processed_img, (5,5), 0)
    #Draw Lines
    lines = cv.HoughLinesP(processed_img, 1, np.pi/180, 180, np.array([]), 100, 5)
    draw_lines(processed_img, lines)

    return processed_img


last_time = time.time()
while(True):
    screen = grab_screen(region=(0,40,800,600))
    print('The loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    processed_screen = process_img(screen)
    cv.imshow('window', processed_screen)
    if cv.waitKey(25) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break
