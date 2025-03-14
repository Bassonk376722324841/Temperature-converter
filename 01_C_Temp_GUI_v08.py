# Imports
from tkinter import *
import all_constants as c
import conversion_rounding as cr


class Converter:
    """
    Temperature conversion tool
    (C to F) or (F to C)
    """

    def __init__(self):
        """
        Temperature Converter GUI
        """

        self.all_calculations_list = []

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Arial", "16", "bold")
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
                                font=("Arial", "14")
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.answer_error = Label(self.temp_frame, text=error, fg="#004C99")
        self.answer_error.grid(row=3)

        # Conversion, help, history / export buttons
        # (Yet to be updated)
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # Button list (Button Text | Bg Colour | Command | Row | Column)
        button_details_list = [
            ["To Celsius", "#990099", lambda: self.check_temp(c.ABS_ZERO_FAHRENHEIT), 0, 0],
            ["To Fahrenheit", "#009900", lambda: self.check_temp(c.ABS_ZERO_CELSIUS), 0, 1],
            ["Help / Info", "#CC6600", "", 1, 0],
            ["History / Export", "#004C99", "", 1, 1]
        ]

        # List to hold buttons once they're made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial", "13", "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        # Retrieve "History / Export" button and disable it at the start.
        self.history_button = self.button_ref_list[3].config(state=DISABLED)

    def check_temp(self, min_temp):
        '''
        Checks if the input (Temperature) is valid and either invokes
        a calculation function or shows a custom error to the GUI.
        '''

        # Retrieve temperature to be converted
        to_convert = self.temp_entry.get()

        # Reset label and entry box if an error is found
        self.answer_error.config(fg="#004C99", font=("Arial","13","bold"))
        self.temp_entry.config(bg="#FFFFFF")

        # Checks that a user enters a valid input.
        # (Being an integer and not a string)
        try:
            to_convert = float(to_convert)
            if to_convert >= min_temp:
                error = ""
                self.convert(min_temp,to_convert)
            else:
                error = f"Please enter a number above {min_temp}"

        except ValueError:
            error = "Please enter temperature with no characters"

        # Display Error if necessary
        if error != "":
            self.answer_error.config(text=error, fg="#9C0000")
            self.temp_entry.config(bg="#F4CCCC")
            self.temp_entry.delete(0, END)

    def convert(self, min_temp,to_convert):
        '''
        Converts temperatures and updates answer label.
        Also stores calculations for export or for
        History feature.
        '''

        if min_temp == c.ABS_ZERO_CELSIUS:
            answer = cr.to_fahrenheit(to_convert)
            answer_statement = f"{to_convert} C is {answer} F"
        else:
            answer = cr.to_celsius(to_convert)
            answer_statement = f"{to_convert} F is {answer} C"

        self.answer_error.config(text=answer_statement)

        self.all_calculations_list.append(answer)


# Main routine

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
