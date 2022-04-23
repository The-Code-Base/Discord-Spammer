import time
import pyautogui

message=str(input('Enter the message you want to Send : '))
number = int(input('How many messages do you want to Send? :'))
number+=1
time.sleep(5)  # Delay to start the spammer
a = 1
while True:
        pyautogui.typewrite(message)
        pyautogui.press("enter")
        print(f'Successfully send the message {a}')
        a += 1
        if a == number:  # Automatically exits after sending messages
            exit()
