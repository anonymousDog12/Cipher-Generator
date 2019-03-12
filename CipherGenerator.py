from tkinter import *
from CipherFunctions import *


DEFAULT_FONT = ("courier", 10)
CIPHER_TYPES = {'RSA' }
DEFAULT_CIPHER = ('RSA')
PARA_HEIGHT=4
TEXT_HEIGHT=4
K=1024 #RSA_cipher bit upbound 


class CipherGenerator:
    def __init__(self, master):
        self.master = master
        #self.master.geometry("600x600")
        self.master.title("Cipher Generator")
        


        # ============== Cipher Selection ===============
        instruction1 = Label(master = master, font=DEFAULT_FONT,
                           text="SELECT YOUR CIPHER: ")
        instruction1.grid(row=0, sticky="W")
    
        tkvar = StringVar()
        tkvar.set(DEFAULT_CIPHER)
        self.cipher = DEFAULT_CIPHER
        self.cipher_para=[]
        popupMenu = OptionMenu(self.master, tkvar, *CIPHER_TYPES, 
                               command = self.get_cipher)
        popupMenu.grid(row = 0,sticky="W",padx=200)
        
        
        #============= key generater ============
        encrypt_button = Button(master = master, font = DEFAULT_FONT,
                               width = 10, height=1,text = "GENERATE",command=self.para_display)
        encrypt_button.grid(row = 1,sticky="W", padx=10)
        
        #================ parameter for ciphor =====================
        self.label_e = Label(master = master, font=DEFAULT_FONT,
                           text = "PUBLIC KEY:")
        self.label_e.grid(row = 2, sticky = "W")
        
        self.text_e = Text(master = master,  
                               font="Courier",height=PARA_HEIGHT)
        self.text_e.grid(row = 2,padx=(200,10))
        
        
        self.label_n = Label(master = master, font=DEFAULT_FONT,
                           text = "MODULUS:")
        self.label_n.grid(row = 3, sticky = "W")
        
        self.text_n = Text(master = master,  
                               font="Courier",height=PARA_HEIGHT)
        self.text_n.grid(row = 3,padx=(200,10))
        
        
        self.label_d = Label(master = master, font=DEFAULT_FONT,
                           text = "PRIVATEKEY:")
        self.label_d.grid(row = 4, sticky = "W")
        
        self.text_d = Text(master = master,  
                               font="Courier",height=PARA_HEIGHT)
        self.text_d.grid(row = 4,padx=(200,10))
  
    
        
        # ============== User Input Plaintext =============
        self.ins2_var=StringVar()
        self.instruction2 = Label(master = master, font=DEFAULT_FONT,
                           textvariable=self.ins2_var)
        self.ins2_var.set("PLAINTEXT: ")
        if self.cipher=="RSA":
            self.ins2_var.set("PLAINTEXT: "+str(CH_BOUND)+" character left")
        self.instruction2.grid(row=5, sticky="W")
        self.plain_entry = Text(master = master, height =TEXT_HEIGHT, 
                               font="Courier")
        self.plain_entry.config(highlightbackground = "#f6f6f6")
        self.plain_entry.grid(row = 6,padx=(200,10))
        self.plain_entry.bind('<KeyRelease>',self.plain_entry_callback) 
        
        # ============ Encrypt Button and Clear ============
        encrypt_button = Button(master = master, font = DEFAULT_FONT,
                               width = 10, text = "↓ENCRYPT↓", 
                               command = self.encrypt_message)
        encrypt_button.grid(row = 7, padx=(0, 300))
        
        clear_plain_button = Button(master = master, font = DEFAULT_FONT,
                              width = 17, command = self.clear_plain_entry,
                              text = "CLEAR PLAIN TEXT")
        clear_plain_button.grid(row = 7, padx=(200, 0))
        
        #Label(master, text = "").grid(row = 8)
        #Label(master, text = "").grid(row = 9)
        
        # ============== User Input Ciphertext =============
        self.instruction3 = Label(master = master, font=DEFAULT_FONT,
                           text="CIPHERTEXT: ")
        self.instruction3.grid(row=7, sticky="W")
        self.cipher_entry = Text(master = master, height = TEXT_HEIGHT, 
                               font="Courier")
        self.cipher_entry.config( highlightbackground = "#f6f6f6")
        self.cipher_entry.grid(row = 11,padx=(200,10))
        
        # ============ Decrypt Button and Clear ============
        encrypt_button = Button(master = master, font = DEFAULT_FONT,
                               width = 10, text = "↑DECRYPT↑", 
                               command = self.decrypt_message)
        encrypt_button.grid(row = 12, padx=(0, 300))
        
        clear_cipher_button = Button(master = master, font = DEFAULT_FONT,
                              width = 17, command = self.clear_cipher_entry,
                              text = "CLEAR CIPHER TEXT")
        clear_cipher_button.grid(row = 12, padx=(200, 0))
    
    def run(self):
        self.master.mainloop()
        
    def para_display(self):
        self.text_d.delete("1.0", 'end-1c')
        self.text_n.delete("1.0", 'end-1c')
        self.text_e.delete("1.0", 'end-1c')
        if self.cipher=="RSA":
            
            n,e,d=RSA(K+1)
            self.text_d.insert("1.0", str(d))
            self.text_n.insert("1.0", str(n))
            self.text_e.insert("1.0", str(e))
    def plain_entry_callback(self,e):
         if self.cipher=="RSA":
                plain_text = self.plain_entry.get("1.0", 'end-1c')
                self.ins2_var.set("PLAINTEXT: "+str(CH_BOUND-len(plain_text))+ " character left")
        
        

        
        
    
    def get_cipher(self, value):
        self.cipher = value
        
        if value=="RSA":
            self.ins2_var.set("PLAINTEXT: PLAINTEXT: ")
        else:
            self.ins2_var.set("PLAINTEXT: "+str(CH_BOUND)+" character left")
                
    
    def encrypt_message(self):
        plain_text = self.plain_entry.get("1.0", 'end-1c')
        self.cipher_entry.delete("1.0", 'end-1c')
        if self.cipher =="RSA":
            e=int(self.text_e.get("1.0", 'end-1c'))
            n=int(self.text_n.get("1.0", 'end-1c'))
            cipher_text = RSA_encrypt(plain_text,e=e,n=n)
        elif self.cipher == "Caesar":
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
        if self.cipher == "RSA":
            d=int(self.text_d.get("1.0", 'end-1c'))
            n=int(self.text_n.get("1.0", 'end-1c'))
            plain_text = RSA_decrypt(cipher_text,d=d,n=n)
            
        elif self.cipher == "Caesar":
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
        
        
my_gui = CipherGenerator(Tk())
my_gui.run()