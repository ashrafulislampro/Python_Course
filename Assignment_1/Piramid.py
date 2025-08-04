import pyautogui
from time import sleep
num = int(input("Enter number of pyramid rows: "))

print("Click on your text editor or notepad in the next 5 seconds...")


for i in range(1, num+1):
    pyautogui.write("#" * i)
    pyautogui.press("enter")