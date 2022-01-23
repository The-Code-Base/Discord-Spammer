import random
import time
import pyautogui

number = int(input('How many messages do you want to send? :'))
time.sleep(5)  # Delay
a = 0
while True:
    with open("text.txt", "r") as file:  # Open the file in read mode
        allText = file.read()
        words = list(map(str, allText.split()))

        pyautogui.typewrite((random.choice(words)))
        pyautogui.press("enter")
        print(f'Successfully send the message {a}')

    a += 1
    if a == number:  # Automatically exits after sending messages
        exit()
