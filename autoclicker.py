from pynput.keyboard import Listener, Key
import pyautogui
import time

# Settings
delay = 0.1  # in seconds
start_key = Key.f1
stop_key = Key.f2
exit_key = Key.f3

running = True
clicking = False

def on_press(key):
    global running, clicking

    if key == start_key:
        clicking = True
        print("[Clicking started]")
    elif key == stop_key:
        clicking = False
        print("[Clicking stopped]")
    elif key == exit_key:
        running = False
        print("[Exit]")

def display_controls():
    print("// AutoClicker by iSayChris")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t F1 = Start Clicking")
    print("\t F2 = Stop Clicking")
    print("\t F3 = Exit")
    print("-----------------------------------------------------")
    print('Press F1 to start ...')

def main():
    global clicking
    lis = Listener(on_press=on_press)
    lis.start()
    display_controls()
    while running:
        if clicking:
            pyautogui.click(pyautogui.position())
            time.sleep(delay)
    lis.stop()

if __name__ == "__main__":
    main()
