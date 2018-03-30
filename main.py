import time
import calendar
from tkinter import *

root = Tk()
bt1 = Button(self, fg = "red", bg = "blue")
root.mainloop()
print("If you want show calendar press 1")
cheese = int(input("1[calendar]"))

if cheese == 1:
    import cal
    print("Is works!")
else:
    print("Error!")
    
