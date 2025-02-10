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

        instructions = "Please enter a temperature below and " \
                       "then choose which unit to convert it to."
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=240, width=50,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial","14")
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number that satisfies one of the units"
        self.temp_error = Label(self.temp_frame, text=error,fg="#9C0000")
        self.temp_error.grid(row=3)

        # Conversion, help, history / export buttons
        # (Yet to be updated)
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # Button list (Button Text | Bg Colour | Command | Row | Column)
        button_details_list = [["To Celsius", "#990099", "", 0, 0],
                               ["To Fahrenheiy", "#009900", "", 0, 1],
                               ["Help / Info", "#CC6600", "", 1, 0],
                               ["History / Export", "#004C99", "", 1, 1]]

        self.to_celsius_button = Button(self.button_frame,
                                        text="To Celsius",
                                        bg="#990099",
                                        fg="#ffffff",
                                        font=("Arial","12","bold"), width=12)
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_farenheit_button = Button(self.button_frame,
                                        text="To Farenheit",
                                        bg="#990099",
                                        fg="#ffffff",
                                        font=("Arial", "12", "bold"), width=12)
        self.to_farenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.help_button = Button(self.button_frame,
                                        text="Help / Info",
                                        bg="#990099",
                                        fg="#ffffff",
                                        font=("Arial", "12", "bold"), width=12)
        self.help_button.grid(row=1, column=0, padx=5, pady=5)

        self.history_button = Button(self.button_frame,
                                        text="History / Export",
                                        bg="#990099",
                                        fg="#ffffff",
                                        font=("Arial", "12", "bold"), width=12)
        self.history_button.grid(row=1, column=1, padx=5, pady=5)

# Main routine

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
