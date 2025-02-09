import customtkinter
import time
import threading
from pynput import keyboard
import pyautogui

class ClickButton(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.hotkey = keyboard.Key.f9
        self.clicking = False
        self.clickDelay = 0.1

        self.startButton = customtkinter.CTkButton(self, text=f"Start Clicking! ({str(self.hotkey).replace("Key.", "")})", command=self.startClickingButton)
        self.startButton.grid(row=0, column=0, padx=10, pady=10)
        self.recordButton = customtkinter.CTkButton(self, text="Record Hotkey", command=self.recordHotkey)
        self.recordButton.grid(row=1, column=0, padx=10, pady=10)
        self.delayLabel = customtkinter.CTkLabel(self, text="Click Delay (Seconds)", fg_color="transparent")
        self.delayLabel.grid(row=0, column=1, padx=10)
        self.delayEntry = customtkinter.CTkEntry(self, placeholder_text="0.1")
        self.delayEntry.grid(row=1, column=1, padx=10)
        self.clickListener = keyboard.Listener(on_press=self.hotkeyCheck)
        self.clickListener.start()

    def startClicking(self):
        counter = 0
        print(self.delayEntry.get())
        self.delayLabel.focus_set()
        self.focus()
        try: 
            self.clickDelay = float(self.delayEntry.get())
        except:
            self.clickDelay = 0.1
        while self.clicking:
            print(f"Click: {counter}")
            counter += 1
            pyautogui.click()
            time.sleep(self.clickDelay)
    
    #Setup the hotkey record to run in it's own thread because if I don't it's gonna cause the whole program to freeze when it tries to update the button text.
    def recordHotkey(self):
        threading.Thread(target=self._recordHotkeyThread, daemon=True).start()

    def _recordHotkeyThread(self):
        def on_press(key):
            self.delayLabel.focus_set()
            self.focus()
            self.hotkey = key
            print(self.hotkey)
            self.after(0, self.updateButtonText)
            return False
        
        with keyboard.Listener(on_press=on_press) as recordListener:
            recordListener.join()

    def updateButtonText(self):
        self.startButton.configure(text=f"Start Clicking! ({str(self.hotkey).replace('Key.', '')})")

    
    def hotkeyCheck(self, key):
        if key == self.hotkey:
            self.clicking = not self.clicking
            if self.clicking:
                threading.Thread(target=self.startClicking, daemon=True).start()

    #This could probably be included in the startClicking function if I just check to see if the hotkey or button started the click but I can't be bothered to do that and this function is small enough that I don't mind repeating it.
    def startClickingButton(self):
        self.clicking = not self.clicking
        if self.clicking:
            time.sleep(0.5)
            threading.Thread(target=self.startClicking, daemon=True).start()