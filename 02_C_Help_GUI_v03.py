# Imports
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

        self.help_button = Button(self.temp_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg="#FFFFFF",
                                     font=("Arial", "14", "bold"), width=12,
                                     command=self.to_help)
        self.help_button.grid(row=1, padx=5, pady=5)

    def to_help(self):
        '''
        Opens the help dialogue box and disables help button
        to prevent users from opening multiple help boxes.
        '''
        DisplayHelp(self)


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
