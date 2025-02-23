from tkinter import *


class Converter:
    """
    Temperature conversion tool
    (C to F) or (F to C)
    """

    def __init__(self):

        self.temp_frame = Frame(padx=10,pady=10)
        self.temp_frame.grid()

    def to_help(self):
        print("You pressed the help button")


# Main routine

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
