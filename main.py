#!/usr/bin/python3
# ------------------------------------------------------------------
# simple program for convert Temperature from Celsius to Kelvin and vice-versa.
#
#
#
# Author:N84.
#
# Create Date:
# ///
# ///
# ///
# ------------------------------------------------------------------

import tkinter
from os import system
from os import name as OS_NAME

# TODO: add help pop-up window that explain how to use the program.


# set the defaults.
WIN_WIDTH = 500
WIN_HEIGHT = 200
WIN_BACKGROUND = "gray55"
WIN_TITLE = "Temperature Converter"
WIN_FONT = "Ubuntu"


def clear():
    """wipe the terminal screen."""

    if OS_NAME == "posix":
        # *nix machines.
        system("clear")

    else:
        # windows machines.
        system("cls")


def start_app(root: tkinter.Tk):
    """"""
    root.mainloop()


def main_window():
    """"""
    root = tkinter.Tk()

    root.title(WIN_TITLE)

    # set the start postion and window size.
    root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")

    # make the window un-resizeable.
    root.resizable(False, False)

    # to remove the title bar uncomment this:
    # root.overrideredirect(1)

    # change the window background=>bg.
    root.configure(bg=WIN_BACKGROUND)

    # create special var.
    result_var = tkinter.StringVar()

    # create widgets.

    temperature_entry = tkinter.Entry(
        root, bd=0, highlightbackground="black", highlightthickness=1, font=(WIN_FONT, 15))
    temperature_entry.place(x=100, y=40)

    convert_btn = tkinter.Button(
        root, text="Convert", bd=0, highlightbackground="black", bg="gray80",  highlightthickness=0,
        activebackground="royalblue", activeforeground="gray90", font=(WIN_FONT, 12), command=lambda: convert_btn_event(temperature_entry, result_var))
    convert_btn.place(x=324, y=39)

    result_label = tkinter.Label(root, textvariable=result_var, font=(
        WIN_FONT, 16, "bold"), bg=WIN_BACKGROUND)
    result_label.place(x=210, y=111)

    start_app(root)


def convert_btn_event(temperature_entry: tkinter.Entry, result_var: tkinter.StringVar):
    """btn event/callback when we click on the convert btn."""

    # first we have to get the text from entry.
    text_from_entry = temperature_entry.get()

    result = convert_temperature(text_from_entry)

    result_var.set(result)


def convert_temperature(text: str):
    """convert from Celsius to Kelvin and vice-versa.
    this will convert to Celsius if the text contain a 'k',
    on that text, and it will convert to Kelvin if text contain,
    a 'C' on that text, ex:
    '230c' or '320C' that will convert them to Kelvin.
    '190k' or '120K' that will convert them to Celsius."""

    # first make text lower-case.
    # and make sure to replace all dashs.
    # ex: '320-k' => '320k'.
    text = text.lower().strip().replace('-', '')

    # guard conditions.

    if not text:
        # if we given an empty string.
        return "Enter something Please."

    if text.isdecimal():
        # if the user don't give us a unit.
        return "Please give a Unit 'C' or 'K'."

    if text.count('k') > 1 or text.count('c') > 1:
        return "There more than one unit."

    if not all(char.isdecimal() or char in ('c', 'k') for char in text):
        return "non-valid syntax."

    # now convert the temperature.

    if 'c' in text:
        "convert from Celsius to Kelvin"
        # + 273.15.

        temperature_in_kelvin = round(int(text.strip('c')) + 273.15, 4)
        return f"{temperature_in_kelvin}K"

    else:
        "convert from Kelvin to Celsius"
        # - 273.15.

        temperature_in_celsius = round(int(text.strip('k')) - 273.15, 4)
        return f"{temperature_in_celsius}C"


def main():
    main_window()


if __name__ == "__main__":
    main()
