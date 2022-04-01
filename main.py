#!/usr/bin/python3
# ------------------------------------------------------------------
# simple program for convert Temperature from C to K and vice-versa.
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

    # create widgets.

    convert_btn = tkinter.Button(
        root, text="Convert", bd=0, highlightbackground="black", bg="gray80",  highlightthickness=0,
        activebackground="royalblue", activeforeground="gray90", font=(WIN_FONT, 12), command=None)

    convert_btn.place(x=324, y=39)

    temperature_text = tkinter.Entry(
        root, bd=0, highlightbackground="black", highlightthickness=1, font=(WIN_FONT, 15))

    temperature_text.place(x=100, y=40)

    result_label = tkinter.Label(root, textvariable=None, font=(
        WIN_FONT, 30, "bold"), bg=WIN_BACKGROUND)
    result_label.place(x=210, y=111)

    start_app(root)


def main():
    main_window()


if __name__ == "__main__":
    main()
