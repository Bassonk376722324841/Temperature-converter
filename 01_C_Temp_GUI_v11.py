# Imports
from tkinter import *
import all_constants as c
import conversion_rounding as cr

# Prevents unwanted windows
from functools import partial


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
            ["Help / Info", "#CC6600", self.to_help, 1, 0],
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
        self.history_button = self.button_ref_list[3]
        self.history_button.config(state=DISABLED)

        self.help_button = self.button_ref_list[2]

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
            error = "Please enter a valid temperature"

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

        # enable history / export button the moment we get a valid calculation
        self.history_button.config(state=NORMAL)

        self.answer_error.config(text=answer_statement)
        self.all_calculations_list.append(answer_statement)
        print(self.all_calculations_list)

    def to_help(self):
        '''
        Opens the help dialogue box and disables help button
        to prevent users from opening multiple help boxes.
        '''
        DisplayHelp(self)


    def to_history(self):
        '''
        Opens history dialogue box and disables history button
        so that users can't create multiple history boxes.
        '''
        HistoryExport(self, self.all_calculations_list)


class HistoryExport:
    '''
    Displays history dialogue box
    '''

    def __init__(self, partner, calculations):
        # Set up Dialogue box and background colour

        green_back = "#05E804"
        peach_back = "#ffe6cc"

        self.history_box = Toplevel()

        # Disable history button
        partner.history_button.config(state=DISABLED)

        # If users press x at top, close history and
        # releases history button
        self.history_box.protocol("WM_DELETE_WINDOW",
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # Background colour and text for calculations area
        if len(calculations) <= c.MAX_CALCS:
            calc_back = "#05E804"
            calc_amount = "all your"
        else:
            calc_back = "#ffe6cc"
            calc_amount = f"Showing {c.MAX_CALCS} / {len(calculations)}"

        # Create string from calculations list (newest to oldest)
        newest_first_string = ""
        newest_first_list = list(reversed(calculations))

        if len(newest_first_list) <= c.MAX_CALCS:

            for item in newest_first_list[:-1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[-1]

        else:
            for item in newest_first_list[:c.MAX_CALCS-1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[c.MAX_CALCS-1]

        # Strings for 'long' labels...
        recent_intro_txt = ("Below are your recent calculations - showing"
                            " 3 / 3 calculations. All calculations are"
                            "Shown to the nearest degree.")

        export_instruction_txt = ("Please press 'Export' to save your calculations in a"
                                  "file. If the filename already exists, it will be sent"
                                  "to a new file.")

        calculations = ""

        # Label list (label text | format | bg)
        history_labels_list = [
            ["History / Export", ("Arial","16","bold"), None],
            [recent_intro_txt, ("Arial","11"), None],
            [newest_first_string, ("Arial", "14"), calc_back],
            [export_instruction_txt, ("Arial", "11"), None]
        ]

        history_label_ref = []
        for count, item in enumerate(history_labels_list):
            new_label = Label(self.history_box, text=item[0], font=item[1],
                               bg=item[2], wraplength=500, justify="left", padx=20, pady=10)
            new_label.grid(row=count)

            history_label_ref.append(new_label)

        # Retrieve export instruction label to configure it for
        # showing the filename if the user exports the file
        self.export_filename_label = history_label_ref[3]

        # Make frame to hold buttons (2 columns)
        self.hist_button_frame = Frame(self.history_box)
        self.hist_button_frame.grid(row=4)

        button_ref_list = []

        # Button list (button text | bg colour| command | row | colour)
        button_details_list = [
            ["Export", "#004C99", "", 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1],

        ]

        for btn in button_details_list:
            self.make_button = Button(self.hist_button_frame,
                                      font=("Arial", "12", "bold"),
                                      text=btn[0], bg=btn[1],
                                      fg="#FFFFFF", width=12,
                                      command=btn[2])
            self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)

    def close_history(self, partner):
        '''
        Closes history dialogue box and enables history button
        '''

        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


class DisplayHelp:

    def __init__(self, partner):

        # Setup dialogue box and background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # If users press x at top, close help and
        # 'release' the help button
        self.help_box.protocol("WM_DELETE_WINDOW",
                               partial(self.close_help, partner))

        # Disable help button
        partner.help_button.config(state=DISABLED)

        self.help_frame = Frame(self.help_box, width=300,
                              height=200, bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To use this program, enter a temperature that you" \
                    "want to convert and choose which unit of measrement" \
                    "to convert it into. The options available are degrees" \
                    "Celsius (Centigrade) or Fahrenheit. \n\n" \
                    "Note that -273 degrees C (-459 F) is absolute zero" \
                    "(the lowest possible temperature)"

        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF", command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner):
        '''
        Closes help dialogue box and enables help button
        '''

        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# Main routine

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
