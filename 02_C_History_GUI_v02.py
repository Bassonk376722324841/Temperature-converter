from tkinter import *

# Prevents unwanted windows
from functools import partial

class Converter:
    """
    Temperature conversion tool
    (C to F) or (F to C)
    """

    def __init__(self):

        self.temp_frame = Frame(padx=10,pady=10)
        self.temp_frame.grid()

        self.history_button = Button(self.temp_frame,
                                     text="History / Export",
                                     bg="#CC6600",
                                     fg="#FFFFFF",
                                     font=("Arial", "14", "bold"), width=12,
                                     command=self.to_history)
        self.history_button.config(row=1, padx=5, pady=5)

    def to_history(self):
        HistoryExport(self)


class HistoryExport:
    '''
    Displays history dialogue box
    '''

    def __int__(self, partner):
        # Set up Dialogue box and background colour

        green_back = "#05E804"
        peach_back = "#ffe6cc"

        self.history_box = Toplevel()

        # Disable history button
        partner.history_buttom.config(state=DISABLED)

        # If users press x at top, close history and
        # releases history button
        self.history_box.protocol("WM_DELETE_WINDOW",
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # Strings for 'long' labels...
        recent_intro_txt = ("Below are your recent calculations - showing"
                            "3 / 3 calculations. All calculations are"
                            "Shown to the nearest degree.")

        export_instruction_txt = ("Please press 'Export' to save your calculations in a"
                                  "file. If the filename already exists, it will be sent"
                                  "to a new file.")

        calculations = ""

        # Label list (label text | format | bg)
        history_labels_list = [
            ["History / Export", ("Arial","16","bold"), None],
            [recent_intro_txt, ("Arial","11"), None],
            ["Calculation list", ("Arial", "14"), green_back],
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
        self.hist_button_frame

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
