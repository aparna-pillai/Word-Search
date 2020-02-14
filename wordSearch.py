from tkinter import *


class Word_Search(Frame):
  def __init__(self, master, next_screen):
      """Initialize Frame."""
      self.next_screen = next_screen
      super(Word_Search, self).__init__(master, background="black")
      self.grid()
      self.choosing_widgets()

  def choosing_widgets(self):
      Label(self, text="Choose your level!", font="Courier 28", fg="crimson", bg="black").grid(row=1, column=0,
                                                                                               sticky=W)
      Label(self, text="", bg="black"
            ).grid(row=2, column=0, sticky=W)

      Label(self, text="Easy: level1.txt", bg="black", fg="red", font="Courier 22"
            ).grid(row=3, column=0, columnspan=4, sticky=W)

      Label(self, text="Medium: level2.txt", bg="black", fg="orangered", font="Courier 22"
            ).grid(row=4, column=0, columnspan=4, sticky=W)

      Label(self, text="Hard: level3.txt", bg="black", fg="tomato", font="Courier 22"
            ).grid(row=5, column=0, columnspan=4, sticky=W)

      Label(self, text="", bg="black"
            ).grid(row=6, column=0, sticky=W)

      Label(self, text="Load Word Search File:", bg="black", font="Courier 18", fg="orange"
            ).grid(row=7, column=0, sticky=W)

      self.file_ent = Entry(self, bg="black", fg="white")
      self.file_ent.grid(row=8, column=0, sticky=W)

      Label(self, text="", bg="black"
            ).grid(row=9, column=0, sticky=W)

      self.load_file_bttn = Button(self, text="Load", command=self.load_file,
                                   bg="black", fg="gold", font="Courier 18"
                                   ).grid(row=10, column=0, sticky=W)

  def load_file(self):
      file_name = self.file_ent.get()
      if file_name != "level1.txt" and file_name != "level2.txt" and file_name != "level3.txt":
          Label(self, text="Error: Not a valid file\nPlease re-enter file!", fg="white", bg="black"
                ).grid(row=11, column=0, sticky=W)
      else:
          text_file = open(file_name, "r")
          self.next_screen(text_file)