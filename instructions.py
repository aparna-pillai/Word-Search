from tkinter import *

class Instruction_page(Frame):
   def __init__(self, master, return_home):
       """Initialize Frame."""
       self.return_home = return_home
       super(Instruction_page, self).__init__(master)
       master.title("Instructions Page")
       self.grid()
       self.create_widgets()

   def create_widgets(self):
       Label(self,text="").grid(row=0,column=0)

       self.story_txt = Text(self, font= "Courier 20", fg="Crimson", width=100, height=11, wrap=WORD)
       self.story_txt.grid(row=0, column=1, columnspan=4)

       instructions = ("Welcome to Phoenix Puzzles: Fun Brain Games!!!\n\n"
                       "Here you can challenge your brain by playing Word Search.\n\n"
                       "For Word Search, you can choose from three levels -- easy, medium, and hard.\n"
                       "Bonus! All three word searches have a theme of phoenixes and fire!\n\n"
                       "When you're ready, click the 'home page' button to return to the home screen and "
                       "start your puzzle!\n\n"
                       "Can you solve them all?"
                       )

       self.story_txt.delete(0.0, END)
       self.story_txt.insert(0.0, instructions)

       self.home_bttn = Button(self, text="home page", command=self.back_to_home)

       Button(self, text="Home Page",
              font="Courier 20",
              fg="Orangered",
              command=self.back_to_home
              ).grid(row=4, column=1, sticky=W)

   def back_to_home(self):
       self.return_home()