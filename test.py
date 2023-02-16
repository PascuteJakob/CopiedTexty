from pynput import mouse
import keyboard
from pynput.mouse import Button, Controller

def on_scroll(x, y, dx, dy):
    keyboard.write("aaaaaaaaaaaa",0,False)

# Collect events until released
with mouse.Listener(
        on_scroll=on_scroll) as listener:
    listener.join()
