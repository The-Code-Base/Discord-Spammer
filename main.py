import random
import time
import pyautogui

time.sleep(5)#Delay
while True:
    with open("text.txt", "r") as file:# Open the file in read mode
        allText = file.read()
        words = list(map(str, allText.split()))

        pyautogui.typewrite((random.choice(words)))
        pyautogui.press("enter")