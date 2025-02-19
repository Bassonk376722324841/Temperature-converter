from tkinter import *
import all_constants as c
import conversion_rounding as ct


class Converter:
    '''
    Temperature conversion tool (C to F / F to C)
    '''

    def convert(self, min_temp,to_convert):
        '''
        Converts temperatures and updates answer label.
        Also stores calculations for export or for
        History feature.
        '''

        if min_temp == c.ABS_ZERO_CELSIUS:
            self.answer_error.config(text=f"Converting {to_convert} C to F")
        else:
            self.answer_error.config(text=f"Converting {to_convert} F to C")