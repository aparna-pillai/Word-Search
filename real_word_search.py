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
        letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                       "T", "U", "V", "W", "X", "Y", "Z"]
        line_list = []
        self.actual_answer = []
        story = ""
        for line in self.text_file:
            for char in line:
                if char != " " and char != "\n":
                    self.actual_answer.append(char)
            self.char_per_line = 0
            for char in line:
                if char == ".":
                    random_char = random.choice(letter_list)
                    line_list.append(random_char)
                    self.char_per_line += 1
                elif char == " ":
                    line_list.append(char)
                else:
                    line_list.append(char)
                    self.char_per_line += 1
            for char in line_list:
                story += char
            line_list = []
        self.story_txt = Text(self, width=45, height=25, wrap=WORD)
        self.story_txt.grid(row=0, column=0, columnspan=4)
        self.story_txt.insert(0.0, story)

        Button(self, text="Check", bg="orange2", fg="black",
               font="Courier 10", bd=5, command=self.check
               ).grid(row=5, column=0, sticky=W)

    def check(self):
        answer_list = []
        actual_answer_list = []
        answers = self.story_txt.get(0.0, END)
        for thing in answers:
            if thing != " " and thing != "\n":
                 answer_list.append(thing)

