from tkinter import *

# Prevents unwanted windows
from functools import partial

import all_constants as c
from datetime import date


class Converter:
    """
    Temperature conversion tool
    (C to F) or (F to C)
    """

    def __init__(self):

        # self.all_calculations_list = ['45.0 C is 113 F','45.0 F is 7 C',
        #                               '0.0 F is -18 C','0.0 C is 32 F',
        #                               '-111.0 F is -79 C','-111.0 C is -168 F']
        #

        self.all_calculations_list = ['45.0 C is 113 F', '45.0 F is 7 C',
                                      '0.0 F is -18 C', '0.0 C is 32 F',
                                      '-111.0 F is -79 C', "This is a test"]

        self.temp_frame = Frame(padx=10,pady=10)
        self.temp_frame.grid()

        self.history_button = Button(self.temp_frame,
                                     text="History / Export",
                                     bg="#CC6600",
                                     fg="#FFFFFF",
                                     font=("Arial", "14", "bold"), width=12,
                                     command=self.to_history)
        self.history_button.grid(row=1, padx=5, pady=5)

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
                               bg=item[2], wraplength=300, justify="left", padx=20, pady=10)
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
            ["Export", "#004C99", lambda: self.export_data(calculations), 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1],

        ]

        for btn in button_details_list:
            self.make_button = Button(self.hist_button_frame,
                                      font=("Arial", "12", "bold"),
                                      text=btn[0], bg=btn[1],
                                      fg="#FFFFFF", width=12,
                                      command=btn[2])
            self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)


    def export_data(self, calculations):
        # **** Get current date for heading and filename
        today = date.today()

        # Get day, month and year as individual strings
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%y")

        filename = f"temperatures_{year}_{month}_{day}"

        success_string = ("Export Successful! The file is named "
                          f"{filename}.txt")

        write_to = f"{filename}.txt"

        with open(write_to, "w") as text_file:
            text_file.write("**** Temperature calculations ****\n")
            text_file.write(f"Generated: {day}/{month}/{year}\n\n")
            text_file.write("Here is your calculation history from oldest to newest.\n\n")

            # Write the items to file
            for item in calculations:
                text_file.write("~~~ ")
                text_file.write(item)
                text_file.write("\n")

    def close_history(self, partner):
        '''
        Closes history dialogue box and enables history button
        '''

        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

# Main routine

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
