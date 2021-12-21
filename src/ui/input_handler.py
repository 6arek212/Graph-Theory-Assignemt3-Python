from tkinter import *
from tkinter import simpledialog

from tkinter import messagebox
from tkinter import Text


def show_message(message):
    Tk().wm_withdraw()
    USER_INP = simpledialog.askstring(title="Q",
                                      prompt=message)
    return USER_INP


class InputHandler:

    def __init__(self, q):
        self.value = ''
        self.question = q

    def ask_for_value(self, handler):
        return handler(show_message(self.question))
