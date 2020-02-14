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
      Label(self, text="").grid(row=0, column=0)

      self.story_txt = Text(self, font="Verdana 20 bold", fg="Crimson", width=100, height=22, wrap=WORD)
      self.story_txt.grid(row=0, column=1, columnspan=5)

      instructions = ("Welcome to Phoenix Word Search!!!\n\n"
                      "Here you can challenge your brain by playing word search.\n\n\n"
                      "For Word Search, you can choose from three levels -- easy, medium, and hard.\n\n"
                      "When you find a word, replace all the letters of the word in the word search with an "
                      "\nasterisk [*]. Then press the check button to see if you've found a word!\n\n"
                      "Bonus! All three word searches have a theme of phoenixes and fire!\n\n"
                      "If you change a letter that's not part of a word to an asterisk, then when \nthe word search "
                      "resets, it will change to a different random letter. \n\nDon't get confused!\n\n"
                      "When you're ready, click the 'home page' button to return to the home screen \nand "
                      "start your puzzle!\n\n"
                      "Can you beat the clock and solve them all?"
                      )

      self.story_txt.delete(0.0, END)
      self.story_txt.insert(0.0, instructions)

      self.home_bttn = Button(self, text="home page", command=self.back_to_home)

      Button(self, text="Home Page",
             font="fixedsys 20",              fg="light gray",
             bg="maroon",
             command=self.back_to_home
             ).grid(row=4, column=1, sticky=W)

  def back_to_home(self):
      self.return_home()