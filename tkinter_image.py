from tkinter import *

root=Tk()

photo=PhotoImage(file="e1f11c68f493c36538593420538bf451.png")
w=Label(root,image=photo)
w.pack()
ent=Entry(root)
ent.pack()
ent.focus_set()

root.mainloop()

root.configure(background="AntiqueWhite1")