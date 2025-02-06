import customtkinter
import time

class ClickButton(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.button = customtkinter.CTkButton(self, text="Start Clicking!", command=self.startClicking)
        self.button.grid(row=0, column=0, padx=10, pady=(0,10), sticky="s")

    def startClicking(self):
        counter = 0
        while True:
            print(f"Click: {counter}")
            counter += 1
            time.sleep(0.1)