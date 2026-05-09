import pyautogui
import time

def take_screenshot():
    nama_file = f"screenshot_{int(time.time())}.png"
    pyautogui.screenshot(nama_file)
    print(f"Screenshot disimpan: {nama_file}")
    