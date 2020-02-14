from tkinter import *


class End_Screen(Frame):
    def __init__(self, master, exit_screen):
        """Initialize Frame."""
        self.exit_screen = exit_screen
        super(End_Screen, self).__init__(master, background="lemon chiffon")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="We hope you", font="Courier 40 bold", bg="lemon chiffon",
              fg="dark goldenrod").grid(row=0, column=1, sticky=N)

        Label(self, text="enjoyed playing", font="Courier 40 bold", bg="lemon chiffon",
              fg="dark goldenrod").grid(row=1, column=1, sticky=N)

        Label(self, text="Phoenix Word Search!\n", font="Courier 45 bold", bg="lemon chiffon",
              fg="dark goldenrod").grid(row=2, column=1, sticky=N)

        Button(self, text="Exit", bg="gold", fg="black",
               font="Courier 14 bold", bd=5, command=self.exit
               ).grid(row=3, column=1, sticky=N)

        imageSmall = PhotoImage(file="smallerPhoenix.gif")
        w = Label(self,
                  image=imageSmall
                  ).grid(row=4, column=1, sticky=N)
        w.photo = imageSmall

    def exit(self):
        self.exit_screen()
