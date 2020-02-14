from tkinter import *
import random

class Word_Search2(Frame):
    def __init__(self, master, text_file):
        """Initialize Frame."""
        self.text_file = text_file
        super(Word_Search2, self).__init__(master, background="orange2")
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        letter_list = ["A" ,"B" ,"C" ,"D" ,"E" ,"F" ,"G" ,"H" ,"I" ,"J" ,"K" ,"L" ,"M" ,"N" ,"O" ,"P" ,"Q" ,"R" ,"S" ,"T","U" ,"V" ,"W" ,"X" ,"Y" ,"Z"]
        line_list = []
        story = ""
        for line in self.text_file:
            for char in line:
                if char == ".":
                    random_char = random.choice(letter_list)
                    line_list.append(random_char)
                else:
                    line_list.append(char)

            for char in line_list:
                story += char
            line_list = []

            story += "\n"

        self.story_txt = Text(self, width = 45, height = 25, wrap = WORD)
        self.story_txt.grid(row = 0, column = 0, columnspan = 4)
        self.story_txt.insert(0.0, story)

        Button(self, text="Word Search", bg="orange2", fg="black",
               font="Courier 25", bd=5, command=self.check
               ).grid(row=5, column=0, sticky=N)

    def check(self):
        pass