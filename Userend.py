'''
Hi, Welcome to the user-end blockchain intrface
This program can be used by the researcher to interact with the blockchain.
The idea was taken from ""
The blockchain is usually maintained in the cloud and servers,
but due to the lack of expertise, I used text files and folders
to simulate database.
A few of the tasks are automised in this program unlike
the real blockchain where in everything is automised.
All the erros were properly handled and might miss a few,
open to suggestions.
I used a few resources from internet to create
this code and make it run successfully.
all the articles whose work was used in this code were
properly cited in the refereces section.
Many thanks to AdilMoujahid, whose idea of code played a
major role in this program.
And also thanks to all those who simplied my work by creating
some amazing modules to import
References:
https://www.python-course.eu/tkinter_labels.php
2. www.stackoverflow.com
3. http://adilmoujahid.com/posts/2018/03/intro-blockchain-bitcoin-python/
4. http://geeksforgeeks.org
'''

from tkinter import *
import tkinter as tk
from tkinter import filedialog
import sys
import yaml
import binascii
import os
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

# gives the path of the directory your python file is in.
dir_path = os.path.dirname(os.path.realpath(__file__))


def generate():

    '''
  The main_function button Generate_keys calls this function
  to generate public and provate keys.
  Using the Crypto module and RSA256 encryption, public key and a private
  is generate for the user
  and saved in the user_database folder.
  A new screen is created and has both public and private keys displayed
    '''

    random_gen = Crypto.Random.new().read
    private_key = RSA.generate(1024, random_gen)
    public_key = private_key.publickey()
    private_key = binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii')
    public_key = binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')

    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Generate keys")
    screen1.geometry("500x610")
    username_info = username.get()
    f = open(dir_path + "/user_database/userkeys.txt", "r+")
    user_key = yaml.load(f.read())

    if username_info in user_key.values():
        your_public_key = list(user_key.keys())[list(user_key.values()).index(username_info)]
        Label(screen1, text="You already generated your keys", fg="red").pack()
        Label(screen1, text="*** Your Public key ***").pack()
        T = tk.Text(screen1, height=7, width=63)
        T.pack()
        T.insert(tk.END, your_public_key)
    else:
        Label(screen1, text="Here are your keys " + username_info,
              bg="grey", width="300", height="2",
              font=("Times New Roman", 15)).pack()
        Label(screen1, text="").pack()
        Label(screen1, text="*** Public key ***").pack()
        T = tk.Text(screen1, height=7, width=63)
        T.pack()
        T.insert(tk.END, public_key)
        Label(screen1, text="*** Private key ***").pack()
        T = tk.Text(screen1, height=20, width=63)
        T.pack()
        T.insert(tk.END, private_key)
        Label(screen1, text="").pack()

        Label(screen1, text="**Please do not share your private key with anyone \n It is used to generate a signature to verify that its you**",
              fg="red", font=("Calibri", 15)).pack()
        Label(screen1, text="Your keys are stored in " + username_info + "_Wallet.txt in user_database folder \n Please keep it safe",fg="blue", 
              font=("Calibri", 15)).pack()
        Label(screen1, text="All the public keys generated are stored in userkeys.txt file",
              fg="orange", font=("Calibri", 15)).pack()

        # creates a wallet file on your name to store your keys
        f = open(dir_path + "/user_database/" +
                 username_info + "_Wallet.txt", "w")
        f.write("Your Public key \n" + public_key +
                "\n\n\n" + "Your Private key  \n" + private_key +
                "\n\n\n\n\n\nYour Transaction signatures\n\n")
        f.close()

        # Now creates a file user_messages which stores
        # the messages you recieved.
        f = open(dir_path + "/user_messages/" +
                 username_info + "_messages.txt", "w+")
        f.close()

        # adds your public key to the database
        new_key = {public_key: username_info}
        user_key.update(new_key)
        f.close()
        f = open(dir_path + "/user_database/userkeys.txt", "w")
        f.write(str(user_key))
        f.close()


def make_transaction():
    '''
    This function is called when the "Make a transcation" button
    is clicked on the main screen.
    It takes your pulbic and private key, reciever's public key.
    It also asks you to upload your text file to be sent for creating a
    signature using your provate key.

    A new screen is created which shows the transaction signature and
    this is saved to your file user_Wallet.txt in user_database folder.
    '''
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Make a new transaction")
    screen2.geometry("500x600")
    global sender_public_address
    global sender_private_address
    global reciever_public_address
    global sender_public_address_entry
    global sender_private_address_entry
    global reciever_public_address_entry

    sender_public_address = StringVar()
    sender_private_address = StringVar()
    reciever_public_address = StringVar()
    username_info = username.get()
    Label(screen2, text="Whom do you want to send your work " +
          username_info, bg="grey", width="300", height="2",
          fg="white", font=("Arial", 15)).pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Please enter your wallet_public address:",
          font=("Times New Roman", 15)).pack()
    sender_public_address_entry = Entry(screen2,
                                        textvariable=sender_public_address)
    sender_public_address_entry.pack()
    Label(screen2, text="Please enter your wallet_private address:",
          font=("Times New Roman", 15)).pack()
    sender_private_address_entry = Entry(screen2,
                                         textvariable=sender_private_address)
    sender_private_address_entry.pack()
    Label(screen2, text="Please enter the Reciever's wallet_public address:",
          font=("Times New Roman", 15)).pack()
    reciever_public_address_entry = Entry(screen2,
                                          textvariable=reciever_public_address)
    reciever_public_address_entry.pack()
    Label(screen2, text="").pack()
    Button(screen2, text='Upload and Submit', height="4", width="20",
           command=upload_and_submit).pack()
    Label(screen2, text="").pack()


def upload_and_submit():
    '''
    This function is called when the upload and submit button is clicked
    on the 'make a transaction' screen
    It reads the file you upload, takes only text file, gives an error mesage
     if any other filetype os uploaded.
    The Hex Keys generated are even length strings and the program gives an
    error message if the string lengths are odd.
    Using the RSA encryption and Crypto module, the private key along with
    message is signed and the signature is returned.
    '''
    filename = filedialog.askopenfilename()
    if filename[-4:] == '.txt':
        f = open(filename, "r")
        message = f.read()
        username_info = username.get()
        sender_public_address = sender_public_address_entry.get()
        sender_private_address = sender_private_address_entry.get()
        reciever_public_address = reciever_public_address_entry.get()
        if len(sender_private_address) % 2 == 0 and len(reciever_public_address) % 2 == 0 and len(sender_public_address) % 2 == 0:
            private_key = RSA.importKey(binascii.unhexlify(sender_private_address))
            signer = PKCS1_v1_5.new(private_key)
            a = SHA.new(str(message).encode('utf8'))
            signature = binascii.hexlify(signer.sign(a)).decode('ascii')
            Label(screen2, text="*** Transaction signature ***").pack()
            T = tk.Text(screen2, height=7, width=50)
            T.pack()
            T.insert(tk.END, signature)
            Label(screen2, text="*Your message along with the Transaction signature is added to your Wallet file*").pack()
            f = open(dir_path + "/user_database/" + username_info +
                     "_Wallet.txt", "a+")
            f.write("Message to be verified: \n" + message +
                    "\n\n" + "Transaction signature:  \n" + signature +
                    "\n\nReciever's address\n" + reciever_public_address +
                    "\n\n\n")
            f.close()
            Button(screen2, text='**Quit**',
                   height="4", width="20", command=exit).pack()
        else:
            Label(screen2, text="Please check your address, one of them might be wrong",
                  fg="red", font=("Arial", 15)).pack()
    else:
        Label(screen2, text="Please upload a text file",
              bg="grey", fg="white").pack()


def exit():
    '''
    This function is called when you are done
    with your transaction and want to quit the program.
    '''
    sys.exit(0)


def view_transaction():
    '''
    This functions is called when you click 'View your trasactions'
    button on the main screen.
    It asks for your public address and retrieves all the transactions
    from the blockchain to show on the screen.

    '''
    global screen3
    global user_public_address
    global user_public_address_entry

    user_public_address = StringVar()
    screen3 = Toplevel(screen)
    screen3.title("View your transactions")
    screen3.geometry("500x600")
    Label(screen3, text="Please enter your public address").pack()
    user_public_address_entry = Entry(screen3,
                                      textvariable=user_public_address)
    user_public_address_entry.pack()
    Label(screen3, text="").pack()
    Button(screen3, text='Submit', height="4",
           width="20", command=get_transactions).pack()


def get_transactions():
    '''
    This function is called when you click on submit after
    entering your public address.
    It checks the blockchain for transactions having your
    public address as sender address.
    '''
    user_public_address = user_public_address_entry.get()
    f = open("blockchain.txt", "r")
    chain = yaml.load(f.read())
    print (chain)
    get_transactions = []
    for index, block in enumerate(chain):
        for i, transactions in enumerate(block['transactions']):
            if transactions['sender_public_address'] == user_public_address:
                get_transactions.append((("block-",index+1, "transaction-",i+1), transactions))
    Label(screen3, text="*** Transactions ***").pack()
    T = tk.Text(screen3, height=20, width=60)
    T.pack()
    T.insert(tk.END, str(get_transactions))


def view_message():
    '''
    This function is called when you click on 'View your messages'
    button on the main screen.
    It askes your name and then shos you all the messages
    you recieved from different public addresses.
    '''
    screen4 = Toplevel(screen)
    screen4.title("View your messages")
    screen4.geometry("500x600")
    username_info = username.get()
    f = open(dir_path + "/user_messages/" + username_info +
             "_messages.txt", "w+")
    contents = f.read()
    Label(screen4, text="*** Messages ***").pack()
    if contents == "":
        Label(screen4, text="___No Messages found___\n Please build your scholastic network",
              fg="red", font=("Georgia", 19)).pack()
    else:
        T = tk.Text(screen4, height=40, width=60)
        T.pack()
        T.insert(tk.END, contents)


def main_screen():

    '''
The main function calls the main_screen function first.
It defines the screen attributes and also the Labels
(the text to be displayed on screen) and Buttons(buttons associated with
calling an other function)
It takes the user name and use it in the remaining functions
'''

    global screen
    global name
    global username
    screen = tk.Tk()
    name = StringVar()
    screen.geometry("400x550")
    screen.title("Research Flow")

    Label(text="Research Flow", bg="#787878",
          width="300", height="2", font=("Luminari", 17),
          fg="white").pack()
    Label(text="Welcome to the blockchain wallet generator",
          bg="#787878", fg="white", font=("Arial", 14)).pack()
    Label(text="**Please enter your name**", bg="#787878",
          fg="white", font=("Arial", 14)).pack()
    Label(text="").pack()
    username = Entry(screen, textvariable=name)
    username.pack()
    Label(text="").pack()
    Button(text="Generate Wallet keys", height="4", width="30",
           font=("Times New Roman", 14), command=generate).pack()
    Label(text="").pack()
    Button(text='Make a transaction', height="4", width="30",
           font=("Times New Roman", 14), command=make_transaction).pack()
    Label(text="").pack()
    Button(text='View your transactions', height="4", width="30",
           font=("Times New Roman", 14), command=view_transaction).pack()
    Label(text="").pack()
    Button(text='View your messages', height="4", width="30",
           font=("Times New Roman", 14), command=view_message).pack()

    tk.mainloop()


if __name__ == '__main__':
    main_screen()
