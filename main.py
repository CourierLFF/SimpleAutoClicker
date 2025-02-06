import customtkinter
from clickButton import ClickButton
            

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("SimpleAutoClicker")
        self.geometry("400x400")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.clickButtonFrame = ClickButton(self)
        self.clickButtonFrame.grid(row=0, column=0, padx=10, pady=(10, 0))


app = App()
app.mainloop()