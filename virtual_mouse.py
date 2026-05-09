import pyautogui
import numpy as np

pyautogui.FAILSAFE = False

def move_mouse(cx, cy, wCam=640, hCam=480):
    screenW, screenH = pyautogui.size()

    x = np.interp(cx, [0, wCam], [0, screenW])
    y = np.interp(cy, [0, hCam], [0, screenH])
    pyautogui.moveTo(int(x), int(y))

def click_mouse():
    pyautogui.click()
    