from tkinter import Tk
from tkinter import Button, Frame, Label, Entry, Text
from axle import *


class StartWindows():
    def __init__(self):
        self.root = Tk()
        self.root.title(u"Start Windows")
        self.root.geometry("1300x350+200+50")
        self.window_create()

    def window_create(self):
        # frame
        self.frame_upset = Frame(self.root, bg='green', borderwidth=1)
        self.frame_downset = Frame(self.root, bg='red', borderwidth=1)
        self.frame_text_input = Frame(self.frame_upset, bg='grey', bd=1)
        self.frame_button = Frame(self.frame_downset, height=50, bg='grey')

        # frame pack
        self.frame_upset.pack(side='top', fill='both')
        self.frame_downset.pack(side='top', fill='both')
        self.frame_text_input.pack(side='top', fill='both')
        self.frame_button.pack(side='top', fill='both')

        # button in frame_button

        self.button_quit = Button(self.frame_button, text="Выход", width=12, height=2, bg='black', fg='red',
                                  font='arial 12')
        # button bind

        self.button_quit.bind('<Button-1>', self.close_window)

        # button pack

        self.button_quit.grid(row=0, column=11, )

        self.root.mainloop()

    def close_window(self, event):
        self.root.quit()