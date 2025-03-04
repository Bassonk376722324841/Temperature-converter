from datetime import date

all_calculations_list = ['45.0 C is 113 F','45.0 F is 7 C',
                         '0.0 F is -18 C','0.0 C is 32 F',
                         '-111.0 F is -79 C','-111.0 C is -168 F']

# **** Get current date for heading and filename
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

filename = f"temperatures_{year}_{month}_{day}"
write_to = f"{filename}.txt"

with open(write_to, "w") as text_file:

    text_file.write("**** Temperature calculations ****\n")
    text_file.write(f"Generated: {day}/{month}/{year}\n\n")
    text_file.write("Here is your calculation history from oldest to newest.\n\n")

    # Write the items to file
    for item in all_calculations_list:
        text_file.write("~~~ ")
        text_file.write(item)
        text_file.write("\n")