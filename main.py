#!/usr/bin/python3
# -----------------------------------------------------------------
#
#
#
#
# Author:N84.
#
# Create Date:
# ///
# ///
# ///
# -----------------------------------------------------------------

import tkinter
from os import system
from os import name as OS_NAME


# set the defaults.
WIN_WIDTH = 500
WIN_HEIGHT = 350
WIN_BACKGROUND = "gray35"
WIN_TITLE = "N3dal"
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

    start_app(root)


def main():
    main_window()


if __name__ == "__main__":
    main()
