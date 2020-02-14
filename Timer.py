import tkinter as tk


class ExampleApp(tk.Tk):
    def __init__(self, end_screen):
        tk.Tk.__init__(self)
        self.end_screen = end_screen
        self.label = tk.Label(self, text="", font="Courier 30", width=30)
        self.label.pack()
        self.remaining = 0
        self.countdown(10)

    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="Time's up!", fg="orange")
        else:
            self.label.configure(text="Time Remaining: %d seconds" % self.remaining, fg="orange")
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

        if self.remaining <= 0:
            self.end_screen()
