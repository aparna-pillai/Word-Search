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
       self.letter_list = ["A", "B","C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                      "T", "U", "V", "W", "X", "Y", "Z"]
       lowerr_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

       self.letter_dict = {}

       for pos in range (len(self.letter_list)):
           self.letter_dict[self.letter_list[pos]] = lowerr_list[pos]
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
                   random_char = random.choice(self.letter_list)
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
       self.story_txt = Text(self, width=45, height=17, wrap=WORD)
       self.story_txt.grid(row=0, column=0, columnspan=4)
       self.story_txt.insert(0.0, story)

       Button(self, text="Check", bg="orange2", fg="black",
              font="Courier 10", bd=5, command=self.check
              ).grid(row=9, column=0, sticky=W)

       if self.actual_answer[2] == "P":
           self.word_list = ["phoenix","prophecy","evil","thestral","darkness"]
       if self.actual_answer[17] == "M":
           self.word_list = ["avox","bow and arrow","district twelve","forcefield","hunger games", "jabberjay", "mockingjay", "muttation","nightlock berry","panem"]
       if self.actual_answer[31] == "O":
           self.word_list = ["ashes","inferno","phoenix","blaze","ignite","burn","flame","kindle","spark","smolder","smoke","combust","pyrokinetic","incandescent","heat"]

       Label(self, text=" ", bg="orange2").grid(row=0, column=50, sticky=E)
       row_count = 2
       column_count = 0
       for word in self.word_list:
           if column_count == 6:
               row_count += 1
               column_count = 0
           else:
               Label(self, text=word, bg="orange2",
                     ).grid(row=row_count, column=column_count, sticky=W)
               column_count += 1

   def check(self):
       story = ""

       answer_list = []
       answers = self.story_txt.get(0.0, END)
       for thing in answers:
           if thing != " " and thing != "\n":
                answer_list.append(thing)
       char_count = 0
       for pos in range (len(answer_list)):
           if answer_list[pos] == "*":
               if self.actual_answer[pos] != ".":
                   story += (self.letter_dict[self.actual_answer[pos]])
                   story += " "

               else:
                   story += random.choice(self.letter_list)
                   story += " "

           else:
               story += answer_list[pos]
               story += " "

       self.story_txt.delete(0.0, END)
       self.story_txt.insert(0.0, story)