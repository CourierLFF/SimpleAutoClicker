import customtkinter
import time
from pynput import keyboard

class ClickButton(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.hotkey = None

        self.button = customtkinter.CTkButton(self, text="Start Clicking!", command=self.startClicking)
        self.button.grid(row=0, column=0, padx=10, pady=10)
        self.button = customtkinter.CTkButton(self, text="Record Hotkey", command=self.recordHotkey)
        self.button.grid(row=1, column=0, padx=10, pady=10)

    def startClicking(self):
        counter = 0
        while True:
            print(f"Click: {counter}")
            counter += 1
            time.sleep(0.1)
    
    def recordHotkey(self):
        def on_press(key):
            self.hotkey = key
            print(self.hotkey)
        
        def on_release(key):
            keyboard.Listener.stop(recordListener)

        recordListener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release)
        recordListener.start()
