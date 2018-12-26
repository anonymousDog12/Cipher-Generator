from tkinter import *

DEFAULT_FONT = ("courier", 20)
CIPHER_TYPES = {'Caesar', 'Substitution'}
DEFAULT_CIPHER = ('Caesar')

class CipherGenerator:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x600")
        self.master.title("Cipher Generator")


        # ============== Cipher Selection ===============
        instruction1 = Label(master = master, font=DEFAULT_FONT,
                           text="SELECT YOUR CIPHER: ")
        instruction1.grid(row=0, sticky="W")
        
        tkvar = StringVar(self.master)
        tkvar.set(DEFAULT_CIPHER)
        
        popupMenu = OptionMenu(self.master, tkvar, *CIPHER_TYPES)
        popupMenu.grid(row = 1, sticky = "W")
        
        # ============== User Input Plaintext =============
        instruction2 = Label(master = master, font=DEFAULT_FONT,
                           text="PLAINTEXT: ")
        instruction2.grid(row=2, sticky="W")
        self.plain_entry = Text(master = master, height = 13, 
                               font="Courier")
        self.plain_entry.config(width = 74, highlightbackground = "#f6f6f6")
        self.plain_entry.grid(row = 3)
        
        # ============ Encrypt Button and Clear ============
        encrypt_button = Button(master = master, font = DEFAULT_FONT,
                               width = 10, text = "↓ENCRYPT↓", 
                               command = self.encrypt_message)
        encrypt_button.grid(row = 4, padx=(0, 300))
        
        clear_plain_button = Button(master = master, font = DEFAULT_FONT,
                              width = 17, command = self.clear_plain_entry,
                              text = "CLEAR PLAIN TEXT")
        clear_plain_button.grid(row = 4, padx=(200, 0))
        
        Label(master, text = "").grid(row = 5)
        Label(master, text = "").grid(row = 6)
        
        # ============== User Input Ciphertext =============
        instruction3 = Label(master = master, font=DEFAULT_FONT,
                           text="CIPHERTEXT: ")
        instruction3.grid(row=7, sticky="W")
        self.cipher_entry = Text(master = master, height = 13, 
                               font="Courier")
        self.cipher_entry.config(width = 74, highlightbackground = "#f6f6f6")
        self.cipher_entry.grid(row = 8)
        
        # ============ Decrypt Button and Clear ============
        encrypt_button = Button(master = master, font = DEFAULT_FONT,
                               width = 10, text = "↑DECRYPT↑", 
                               command = self.decrypt_message)
        encrypt_button.grid(row = 9, padx=(0, 300))
        
        clear_cipher_button = Button(master = master, font = DEFAULT_FONT,
                              width = 17, command = self.clear_cipher_entry,
                              text = "CLEAR CIPHER TEXT")
        clear_cipher_button.grid(row = 9, padx=(200, 0))
        
        
    def encrypt_message(self):
        plain_text = self.plain_entry.get("1.0", 'end-1c')
    
    def decrypt_message(self):
        print("TODO")
    
    def set_plain_entry(self, text):
        pass
    
    def set_cipher_entry(self, text):
        pass
    
    def clear_plain_entry(self):
        self.plain_entry.delete("1.0", 'end-1c')
    
    def clear_cipher_entry(self):
        self.cipher_entry.delete("1.0", 'end-1c')
        
        

root = Tk()
my_gui = CipherGenerator(root)
root.mainloop()