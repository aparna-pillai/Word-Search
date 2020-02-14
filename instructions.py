from tkinter import *


class Instruction_page(Frame):
    def __init__(self, master, return_home):
        self.return_home = return_home
        super(Instruction_page, self).__init__(master)
        master.title("Instructions Page")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.story_txt = Text()