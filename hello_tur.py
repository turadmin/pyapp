import os
import time

def print_hello():
    for _ in range(5):
        print("Hello Tur")
        time.sleep(1)

def clear_screen():
    os.system('clear')  # Используйте 'cls' вместо 'clear', если вы работаете на Windows

while True:
    print_hello()
    clear_screen()
