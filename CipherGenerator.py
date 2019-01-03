from tkinter import *
from CipherFunctions import *

DEFAULT_FONT = ("courier", 20)
CIPHER_TYPES = {'Atbash', 'Baconian', 'Caesar', 'ROT13', 'Substitution', }
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
        self.cipher = DEFAULT_CIPHER
        popupMenu = OptionMenu(self.master, tkvar, *CIPHER_TYPES, 
                               command = self.get_cipher)
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
    
    def get_cipher(self, value):
        self.cipher = value
    
    def encrypt_message(self):
        plain_text = self.plain_entry.get("1.0", 'end-1c')
        self.cipher_entry.delete("1.0", 'end-1c')
    
        if self.cipher == "Caesar":
            cipher_text = Caesar_encrypt(plain_text)
        elif self.cipher == "Substitution":
            cipher_text = Substitution_encrypt(plain_text)
        elif self.cipher == "Atbash":
            cipher_text = Atbash_encrypt(plain_text)
        elif self.cipher == "ROT13":
            cipher_text = Rot13_encrypt(plain_text)
        elif self.cipher == "Baconian":
            cipher_text = Baconian_encrypt(plain_text)
        else:
            cipher_text = "ERROR: ENCRIPTION CIPHER NOT RECOGNIZED!" 

        self.cipher_entry.insert("1.0", cipher_text)
        
    
    def decrypt_message(self):
        cipher_text = self.cipher_entry.get("1.0", 'end-1c')
        self.plain_entry.delete("1.0", 'end-1c')
        
        if self.cipher == "Caesar":
            plain_text = Caesar_decrypt(cipher_text)
        elif self.cipher == "Substitution":
            plain_text = Substitution_decrypt(cipher_text)
        elif self.cipher == "Atbash":
            plain_text = Atbash_decrypt(cipher_text)
        elif self.cipher == "ROT13":
            plain_text = Rot13_decrypt(cipher_text)
        elif self.cipher == "Baconian":
            plain_text = Baconian_decrypt(cipher_text)
        else:
            plain_text = "ERROR: DECRYPTION CIPHER NOT RECOGNIZED!"
            
        self.plain_entry.insert("1.0", plain_text)
        
    
    def clear_plain_entry(self):
        self.plain_entry.delete("1.0", 'end-1c')
    
    def clear_cipher_entry(self):
        self.cipher_entry.delete("1.0", 'end-1c')
        
        

root = Tk()
my_gui = CipherGenerator(root)
root.mainloop()