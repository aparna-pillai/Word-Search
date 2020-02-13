from tkinter import *

class Word_Search(Frame):
   def __init__(self, master,next_screen):
       """Initialize Frame."""
       self.next_screen=next_screen
       super(Word_Search, self).__init__(master,background="orange2")
       self.grid()
       self.choosing_widgets()

   def choosing_widgets(self):
       Label(self,text="Choose your level!").grid(row=1,column=0,sticky=W)

       Label(self,text="Easy: wordsearch_level1.txt"
             ).grid(row=2, column=0, columnspan= 4, sticky=W)

       Label(self, text="Medium: wordsearch_level2.txt"
             ).grid(row=3, column=0, columnspan= 4,sticky=W)

       Label(self, text="Hard: wordsearch_level3.txt"
             ).grid(row=4, column=0, columnspan= 4, sticky=W)

       Label(self,text="Load Cipher File:"
             ).grid(row=6,column=0,sticky=W)

       self.file_ent=Entry(self)
       self.file_ent.grid(row=6,column=1,sticky=W)

       self.load_file_bttn=Button(self,text="Load", command=self.load_file
                                  ).grid(row=6,column=2,sticky=E)

   def load_file(self):
       file_name=self.file_ent.get()
       text_file = open(file_name, "r")
       self.next_screen(text_file)

