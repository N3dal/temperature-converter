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
        root, bd=0, highlightbackground="black", highlightthickness=1, font=(WIN_FONT, 15), name="temperature_entry")
    temperature_entry.place(x=100, y=40)

    result_label = tkinter.Label(root, textvariable=result_var, font=(
        WIN_FONT, 16, "bold"), bg=WIN_BACKGROUND, fg="gold", name="result_label")
    result_label.place(x=210, y=111)

    convert_btn = tkinter.Button(
        root, text="Convert", bd=0, highlightbackground="black", bg="gray80",  highlightthickness=0,
        activebackground="royalblue", activeforeground="gray90", font=(WIN_FONT, 12),
        command=lambda: convert_btn_event(temperature_entry, result_var, result_label), cursor="hand1", name="convert_btn")
    convert_btn.place(x=324, y=39)

    start_app(root)


def convert_btn_event(temperature_entry: tkinter.Entry, result_var: tkinter.StringVar, result_label: tkinter.Label):
    """btn event/callback when we click on the convert btn."""

    # first we have to get the text from entry.
    text_from_entry = temperature_entry.get()

    result = convert_temperature(text_from_entry)

    center_result_label(result_label, result)

    result_var.set(result)


def center_result_label(result_label: tkinter.Label, text: str):
    """make sure to center the result label, in the center,
    horizontal-center of the window.
    depending on the text len."""

    # make sure to multiply the len by 11 or any int you find good.

    text_len = len(text) * 10

    x_coord = (WIN_WIDTH - text_len) // 2

    result_label.place(x=x_coord, y=111)


def convert_temperature(text: str):
    """convert from Celsius to Kelvin and vice-versa.
    this will convert to Celsius if the text contain a 'k',
    on that text, and it will convert to Kelvin if text contain,
    a 'C' on that text, ex:
    '230c' or '320C' that will convert them to Kelvin.
    '190k' or '120K' that will convert them to Celsius."""

    # first make text lower-case.
    text = text.lower().strip()

    # guard conditions.

    if not text:
        # if we given an empty string.
        return "Enter something Please."

    if text.count('.') > 1:
        return "non-valid syntax."

    if text.isdecimal():
        # if the user don't give us a unit.
        return "Please give a Unit 'C' or 'K'."

    if text.count('k') > 1 or text.count('c') > 1:
        return "There more than one unit."

    if text[-1] not in ('k', 'c'):
        return "Wrong unit position or wrong unit."

    if text.count('-') > 1:
        return "There more than one negative sign."

    if text.find('-') not in (-1, 0):
        return "wrong negative sign."

    if not all(char.isdecimal() or char in ('c', 'k', '-', '.') for char in text):
        return "non-valid syntax."

    # now convert the temperature.

    if 'c' in text:
        "convert from Celsius to Kelvin"
        # + 273.15.

        temperature_in_kelvin = round(float(text.strip('c')) + 273.15, 4)
        return f"{temperature_in_kelvin}K"

    else:
        "convert from Kelvin to Celsius"
        # - 273.15.

        temperature_in_celsius = round(float(text.strip('k')) - 273.15, 4)
        return f"{temperature_in_celsius}C"


def main():
    main_window()


if __name__ == "__main__":
    main()
