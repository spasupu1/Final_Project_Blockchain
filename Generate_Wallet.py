from tkinter import *
import tkinter as tk
import binascii
import os
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5



def generate():
  random_gen = Crypto.Random.new().read
  private_key = RSA.generate(1024, random_gen)
  public_key = private_key.publickey()
  private_key = binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii')
  public_key= binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')

  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Generate keys")
  screen1.geometry("500x600")
  username_info = username.get()
  print ("...............", username_info)
  Label(screen1, text = "Here are your keys "+username_info, bg = "grey", width = "300", height = "2", font = ("Arial", 13)).pack()
  Text(screen1, height=5, width=30)
  Label(screen1, text = "").pack()
  Label(screen1, text = "*** Public key ***").pack()
  T = tk.Text(screen1, height=7, width=63)
  T.pack()
  T.insert(tk.END, public_key)
  Label(screen1, text = "*** Private key ***").pack()
  T = tk.Text(screen1, height=20, width=63)
  T.pack()
  T.insert(tk.END, private_key)
  Label(screen1, text = "").pack()
  Label(screen1, text = "Please do not share your private key with anyone \n It is used to generate a signature to verify that its you", font = ("Calibri", 15)).pack()
  Label(screen1, text = "Your keys are stored in " + username_info + "_Wallet_keys.txt file \n Please keep it safe", font = ("Calibri", 15)).pack()
  f = open(username_info + "_Wallet_keys.txt", "w+")
  f.write("Your Public key \n" + public_key + "\n\n\n" + "Your Private key  \n" + private_key)
  f.close()



def main_screen():
  global screen
  screen = tk.Tk()
  global name
  global username
  name = StringVar()
  screen.geometry("300x350")
  screen.title("Blockchain Wallet Generator")
  Label(text = "Wallet Generator", bg = "grey", width = "300", height = "2", font = ("Arial", 13)).pack()
  Label(text = "Welcome to the blockchain wallet generator").pack()
  Label(text = "Please Enter your name").pack()
  username = Entry(screen, textvariable = name)
  username.pack()
  Label(text = "").pack()
  Button(text = "Generate Wallet keys", height = "6", width = "30", command = generate).pack()
  Label(text = "").pack()
  tk.mainloop()

if __name__ == "__main__":
main_screen()
  
