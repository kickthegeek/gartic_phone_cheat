import cv2
import numpy as np
import pyautogui as pag
import time
import ctypes




posx = 450
posy = 224
fx = 1090
fy = 585

# posx = 297
# posy = 146
# fx = 555
# fy = 300


w = fx-posx
h = fy-posy

img = cv2.imread('naruto.jpg')
img = cv2.resize(img , (w,h))


image_arr = np.asarray(img)
image_arr.shape
gray = cv2.cvtColor(image_arr,cv2.COLOR_BGR2GRAY)
c1=2 #sobel
c2=1 # prewitt

# kernel1 = np.array([[-1,-c1,-1],[0,0,0],[1,c1,1]])
# kernel2 = np.array([[-1,0,1],[-c1,0,c1],[-1,0,1]])

# filtre1 = cv2.filter2D(gray,-1,kernel1)
# filtre2 = cv2.filter2D(gray,-1,kernel2)

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	# return the edged image
	return edged


blurred = cv2.GaussianBlur(gray, (3, 3), 0)
# apply Canny edge detection using a wide threshold, tight
# threshold, and automatically determined threshold
wide = cv2.Canny(blurred, 10, 200)
tight = cv2.Canny(blurred, 225, 250)
auto = auto_canny(blurred)

# cv2.imwrite("result_wide.jpg",wide)
# cv2.imwrite("result_tight.jpg",tight)
# cv2.imwrite("result_auto.jpg",auto)

def click_mouse():
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
    time.sleep(0.004)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
#mouse controlling now 
time.sleep(3)
lines,cols = auto.shape
seuil= np.max(auto)/2
for i in range(lines):
    for j in range(cols):
        #pag.moveTo(j+posx, i+posy)
        # pag.moveTo(x=j+posx, y=i+posy,duration=0.0,_pause=False)
        # if filtre2[i][j]>0:
        #     pag.click()
        if auto[i][j]>seuil:
            ctypes.windll.user32.SetCursorPos(j+posx,i+posy)
            click_mouse()
    

            