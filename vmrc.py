import pyautogui
import os
import time
import subprocess
from pynput.keyboard import Controller
import multiprocessing


keyboard = Controller()

def beamer_shell():
    debug_info = subprocess.run('/usr/bin/vmrc -H "<host>" -U "<username>" -M "<moid>" -X', shell=True)
    print(debug_info)

def vmrc_input():
    time.sleep(6)

    #pyautogui.click(x=320, y=295, clicks=1, button='left')
    password_input = pyautogui.locateOnScreen('/home/<user>/Pictures/vmrcpassword.png')
    password_input2 = pyautogui.locateOnScreen('/home/<user>/Bilder/vmrcpassword2.png')

    while True:
        if password_input is not None:
            password_input_center = pyautogui.center(password_input)
            pyautogui.click(password_input_center)
            break
        elif password_input2 is not None:
            password_input_center = pyautogui.center(password_input2)
            pyautogui.click(password_input_center)
            break
        time.sleep(1)

    debug = subprocess.run('setxkbmap de', shell=True)
    print(debug.returncode)

    time.sleep(2)

    if debug.returncode == 0:
        keyboard.type("<password>")
    else:
        return 0

    time.sleep(3)

    #pyautogui.click(x=475, y=340, clicks=1, button='left')
    connect_button = pyautogui.locateOnScreen('/home/<user>/Pictures/vmrcconnect.png')

    if connect_button is not None:
        connect_button_center = pyautogui.center(connect_button)
        pyautogui.click(connect_button_center)
    else:
        pyautogui.click(x=475, y=340, clicks=1, button='left')


if __name__ == "__main__":
    process1 = multiprocessing.Process(target=beamer_shell)
    process2 = multiprocessing.Process(target=vmrc_input)
    process1.start()
    process2.start()
