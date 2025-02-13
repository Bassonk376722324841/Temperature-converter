from tkinter import *


class Converter:
    """
    Temperature conversion tool
    (C to F) or (F to C)
    """

    def __init__(self):
        """
        Temperature Converter GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Arial","16","bold")
                                  )
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and" \
                       "then choose which unit to convert it to."
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=240, width=50,
                                       justify="left")
        self.temp_instructions.grid(row=1)

# Main routine

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
