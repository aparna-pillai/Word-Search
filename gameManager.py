import tkinter
from homePage import Home_page
from instructions import Instruction_page
from wordSearch import Word_Search
from real_word_search import Word_Search2
from Timer import ExampleApp
from endScreen import End_Screen


class Game_Manager(object):
  def __init__(self):
      self.root = tkinter.Tk()
      self.current_screen = None

  def load_page(self):
      self.root.title("Phoenix Puzzles")
      self.current_screen = Home_page(self.root, self.instructions, self.word_search)

  def instructions(self):
      self.current_screen.destroy()
      self.hedwig = Instruction_page(self.root, self.return_to_home)

  def return_to_home(self):
      self.hedwig.destroy()
      self.current_screen = Home_page(self.root, self.instructions, self.word_search)

  def word_search(self):
      self.current_screen.destroy()
      self.harry = Word_Search(self.root, self.word_search2)

  def word_search2(self, text_file):
      self.harry.destroy()
      self.albus = Word_Search2(self.root, text_file)
      self.nagini = ExampleApp(self.end_screen)

  def end_screen(self):
      self.albus.destroy()
      self.nagini.destroy()
      self.fawkes = End_Screen(self.root,self.exit_screen)

  def exit_screen(self):
      self.root.destroy()

def main():
  game = Game_Manager()
  game.load_page()
  game.root.mainloop()


main()

