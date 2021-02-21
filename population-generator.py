import tkinter as tk
import sys
import csv

def pull_data(state, year):
    file = open(sys.argv[1], "r")
    data_table = []
    for x in file:
        if state in x and year in x:
            addition = x
            addition = addition.replace("\n", "")
            addition = addition.split(",")
            spot_1 = addition[0]
            spot_2 = addition[1]
            addition[0] = spot_2
            addition[1] = spot_1
            data_table.append(addition)
    file.close()
    return data_table

def write_data(data):
    header = ["input_year", "input_state", "output_population_size"]
    with open("output.csv", "w", newline="") as x:
        writer = csv.writer(x, delimiter=",")
        writer.writerow(header)

        for y in data:
            writer.writerow(y)

def submit_check():
    checker = True
    year_check = year_entry.get()
    if int(year_check) >= 2010 and int(year_check) < 2020:
        message_year["text"] = ""
        year = year_check
    else:
        message_year["text"] = "This is not a valid year"
        checker = False

    state_list = {"AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID","IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "WA", "WV", "WI", "WY"}
    state_check = state_entry.get()
    if state_check.upper() in state_list:
        message_state["text"] = ""
        state = state_check.upper()
    else:
        message_state["text"] = "This is not a valid state abbreviation"
        checker = False

    if checker == True:
        data = pull_data(state, year)
        write_data(data)
        message_submit["text"] = "Data Pulled Successfully"

window = tk.Tk()
window.title("Population Generator")

title_frame = tk.Frame(master=window)
title_label = tk.Label(master=title_frame, text = "Welcom to the Population Generator", background = "black", foreground = "white", height=2)

title_label.grid(row=0, column=0)

title_frame.grid(row=0, column=0, padx=10)

year_frame = tk.Frame(master=window)
year_entry = tk.Entry(master=year_frame, width = 4, )
year_text = tk.Label(master=year_frame, anchor ="w", text = "Enter a US Census Year (2010 to 2019)", height = 2)

year_entry.grid(row=0, column=0)
year_text.grid(row=0, column=1)

state_frame = tk.Frame(master=window)
state_entry = tk.Entry(master=state_frame, width = 4)
state_text = tk.Label(master=state_frame, text = "Enter a US State Abbreviation", height = 2)

state_entry.grid(row=0, column=0)
state_text.grid(row=0, column=1)

btn_convert = tk.Button(
    master=window,
    text="Submit",
    command = submit_check
)

message_year = tk.Label(master=window, text="", foreground = "red")
message_state = tk.Label(master=window, text="", foreground = "red")
message_submit = tk.Label(master=window, text="", foreground = "red")

title_frame.grid(row=0, column=0)
year_frame.grid(row=1, column=0, sticky ="w")
message_year.grid(row=1, column=1)
state_frame.grid(row=2, column=0, sticky ="w")
message_state.grid(row=2, column=1)
btn_convert.grid(row=3, column =0, sticky ="w")
message_submit.grid(row=3, column=1, sticky="w")

window.mainloop()