import customtkinter
import time
import threading
from pynput import keyboard
import pyautogui

class ClickButton(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.hotkey = None
        self.clicking = False

        self.button = customtkinter.CTkButton(self, text="Start Clicking!", command=self.startClickingButton)
        self.button.grid(row=0, column=0, padx=10, pady=10)
        self.button = customtkinter.CTkButton(self, text="Record Hotkey", command=self.recordHotkey)
        self.button.grid(row=1, column=0, padx=10, pady=10)

        self.clickListener = keyboard.Listener(on_press=self.hotkeyCheck)
        self.clickListener.start()

    def startClicking(self):
        counter = 0
        while self.clicking:
            print(f"Click: {counter}")
            counter += 1
            pyautogui.click()
            time.sleep(0.1)
    
    def recordHotkey(self):
        def on_press(key):
            self.hotkey = key
            print(self.hotkey)
            return False
        
        with keyboard.Listener(on_press=on_press) as recordListener:
            recordListener.join()
    
    def hotkeyCheck(self, key):
        if key == self.hotkey:
            self.clicking = not self.clicking
            if self.clicking:
                threading.Thread(target=self.startClicking, daemon=True).start()

    def startClickingButton(self):
        self.clicking = not self.clicking
        if self.clicking:
            time.sleep(0.5)
            threading.Thread(target=self.startClicking, daemon=True).start()