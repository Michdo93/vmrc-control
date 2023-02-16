import pyautogui
import os
import time
import subprocess
from pynput.keyboard import Controller
import multiprocessing


keyboard = Controller()

def beamer_shell():
    debug_info = subprocess.call("/usr/bin/vmrc -H "<host>" -U "<username>" -M "<moid>" -X, shell=False)
    print(debug_info)

def vmrc_input():
    time.sleep(6)

    pyautogui.click(x=320, y=295, clicks=1, button='left')

    time.sleep(0.5)

    keyboard.type("<password>")

    time.sleep(2)

    pyautogui.click(x=475, y=340, clicks=1, button='left')


if __name__ == "__main__":
    process1 = multiprocessing.Process(target=beamer_shell)
    process2 = multiprocessing.Process(target=vmrc_input)
    process1.start()
    process2.start()
