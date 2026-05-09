import cv2
import math
import numpy as np
import time

from hand_tracker import HandTracker
from volume_controller import volume, volMin, volMax
from brightness_control import set_brightness
from virtual_mouse import move_mouse, click_mouse
from gesture_actions import take_screenshot

cap = cv2.VideoCapture(0)
wCam, hCam = 640, 480
cap.set(3, wCam)
cap.set(4, hCam)

tracker = HandTracker()
pTime = 0
mode = "volume" # Mode awal

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1) 
    
    img = tracker.findHands(img)
    lmList = tracker.findPosition(img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('v'):
        mode = "volume"
    elif key == ord('b'):
        mode = "brightness"
    elif key == ord('m'):
        mode = "mouse"
    elif key == ord('s'):
        take_screenshot()
    elif key == ord('q'):
        break

    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)

        if mode == "volume":
            vol = np.interp(length, [30, 200], [volMin, volMax])
            volPer = np.interp(length, [30, 200], [0, 100])
            volume.SetMasterVolumeLevel(vol, None)
            cv2.putText(img, f'Vol: {int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

        elif mode == "brightness":
            brightPer = np.interp(length, [30, 200], [0, 100])
            set_brightness(brightPer)
            cv2.putText(img, f'Brt: {int(brightPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 3)

        elif mode == "mouse":

            move_mouse(x2, y2, wCam, hCam)
            
            if length < 30:
                cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
                click_mouse()
                time.sleep(0.2) 

    cv2.putText(img, f'MODE: {mode.upper()}', (40, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Gesture Control AI", img)

cap.release()
cv2.destroyAllWindows()
