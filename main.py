import os
import pyautogui
import time


discordPath = os.path.expanduser("~") + "//AppData//Local//Discord//app-0.0.308//Discord.exe"
os.startfile(discordPath)
time.sleep(0.5)
while True:
    x, y = pyautogui.locateCenterOnScreen("main_menu.png")
    pyautogui.click(x, y)
    x, y = pyautogui.locateCenterOnScreen("settings.png")
    pyautogui.click(x, y)
    x, y = pyautogui.locateCenterOnScreen("edit1.png")
    pyautogui.click(x, y)
    x, y = pyautogui.locateCenterOnScreen("pp.png")
    pyautogui.click(x, y)
    x, y = pyautogui.locateCenterOnScreen("desktop.png")
    pyautogui.click(x, y)
    x, y = pyautogui.locateCenterOnScreen("file0.png")
    pyautogui.click(x, y)
    x, y = pyautogui.locateCenterOnScreen("file.png")
    pyautogui.click(x, y)
    x, y = pyautogui.locateCenterOnScreen("file2.png")
    pyautogui.click(x, y)
    x, y = pyautogui.locateCenterOnScreen("file3.png")
    pyautogui.click(x, y)
    x, y = pyautogui.locateCenterOnScreen("file4.png")
    pyautogui.click(x, y)