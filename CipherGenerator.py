from tkinter import *

DEFAULT_FONT = ("courier", 20)
CIPHER_TYPES = {'Caesar', 'Substitution'}
DEFAULT_CIPHER = ('Caesar')

class CipherGenerator:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Cipher Generator")

        self.instruction = Label(master = master, font=DEFAULT_FONT,
                           text="SELECT YOUR CIPHER: ")
        self.instruction.grid(row=0, sticky="W")
        
        tkvar = StringVar(self.master)
        tkvar.set(DEFAULT_CIPHER)
        
        popupMenu = OptionMenu(self.master, tkvar, *CIPHER_TYPES)
        popupMenu.grid(row = 1, sticky = "W")
        
        

        



root = Tk()
my_gui = CipherGenerator(root)
root.mainloop()