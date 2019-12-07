'''
Hi, Welcome to the user-end blockchain interface
This program can be used by the researcher to interact with the blockchain.
The idea was taken from "Daniel Van Flymen" who made me confident that
it is not super difficult to work on blockchain.

The blockchain is usually maintained in the cloud and servers,
but due to the lack of expertise, I used text files and folders
to simulate database.
A few of the tasks are automised in this program unlike
the real blockchain where in everything is automised.
All the erros were properly handled and might miss a few,
open to suggestions.
I used a few resources from internet to create
this code and make it run successfully.
All the articles used in this code were
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
5. https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
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


def register():
    '''
    Asks the user to input his usernale and password to create an account.
    '''
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("500x550")
    Label(screen1, text="Research Flow", bg="#787878",
          width="300", height="2", font=("Luminari", 17),
          fg="white").pack()

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter your details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10,
           height=1, command=register_user).pack()


def register_user():
    '''
    Regsisters the user into the database and creates a Wallet file for him.
    it also adds the user name and his public key to the userkeys folder.
    Randomly generates a public and a private key for the user.
    Uses Crypto modules to generate keys.
    '''
    username_info = username.get()
    password_info = password.get()
    if os.path.isfile(dir_path + "/user_database/" +
                      username_info + "_Wallet.txt"):
        Label(screen1, text="You are already registered, please login",
              fg="green", font=("calibri", 11)).pack()
    else:
        random_gen = Crypto.Random.new().read
        private_key = RSA.generate(1024, random_gen)
        public_key = private_key.publickey()
        private_key = binascii.hexlify(private_key.exportKey(
                                       format='DER')).decode('ascii')
        public_key = binascii.hexlify(public_key.exportKey(
                                      format='DER')).decode('ascii')

        f1 = open(dir_path + "/user_database/userkeys.txt", "r")
        userkeys = yaml.load(f1.read())
        f1.close()
        new_keys = {public_key: username_info}
        userkeys.update(new_keys)
        f1 = open(dir_path + "/user_database/userkeys.txt", "w")
        f1.write(str(userkeys))
        f1.close()

        f = open(dir_path + "/user_database/" +
                 username_info + "_Wallet.txt", "w+")
        data = {'username': username_info, 'password': password_info,
                'public_key': public_key, 'private_key': private_key,
                'recieved_messages': []}
        f.write(str(data))
        f.close()
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        Label(screen1, text="Registration Sucess \n"
                            "Your Public and private key generated.",
              fg="green", font=("calibri", 11)).pack()


def login():
    '''
    This function asks the user to login using his credentials.
    '''
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("500x550")
    Label(screen2, text="Research Flow", bg="#787878",
          width="300", height="2", font=("Luminari", 17),
          fg="white").pack()

    global login_user
    global login_password
    global login_user_entry
    global login_password_entry
    login_user = StringVar()
    login_password = StringVar()
    Label(screen2, text="Please enter your details below").pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Username * ").pack()
    login_user_entry = Entry(screen2, textvariable=login_user)
    login_user_entry.pack()
    Label(screen2, text="Password * ").pack()
    login_password_entry = Entry(screen2, textvariable=login_password)
    login_password_entry.pack()

    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10,
           height=1, command=login_check).pack()


def login_check():
    '''
    Verify login credentials.
    yaml converts the string into its respective datatype.
    uses isfile function of os to check whether the file is present or not.
    '''
    login_user_entry = login_user.get()
    login_password_entry = login_password.get()
    if os.path.isfile(dir_path + "/user_database/" +
                      login_user_entry + "_Wallet.txt"):
        f = open(dir_path + "/user_database/" +
                 login_user_entry + "_Wallet.txt", "r")
        data = yaml.load(f.read())
        f.close()
        if data['password'] == login_password_entry:
            main_screen()
        else:
            Label(screen2, text="Username or password incorrect",
                  fg="red").pack()
    else:
        Label(screen2, text="You are not registered, please register",
              fg="green", font=("calibri", 11)).pack()


def view_keys():
    '''
    SHows your public and private keys retrieved from your wallet file.
    '''
    global screen7
    screen7 = Toplevel(screen)
    screen7.geometry("400x550")
    screen7.title("Research Flow")
    login_user_entry = login_user.get()

    f = open(dir_path + "/user_database/" +
             login_user_entry + "_Wallet.txt", "r")
    data = yaml.load(f.read())
    f.close()
    Label(screen7, text="Your public key:",
          font=("Times New Roman", 15)).pack()
    Label(screen7, text="").pack()
    T = tk.Text(screen7, height=8, width=40)
    T.pack()
    T.insert(tk.END, str(data['public_key']))
    Label(screen7, text="Your private key:",
          font=("Times New Roman", 15)).pack()
    Label(screen7, text="").pack()
    T = tk.Text(screen7, height=30, width=40)
    T.pack()
    T.insert(tk.END, str(data['private_key']))


def make_transaction():
    '''
    This function is called when the "Make a transcation" button
    is clicked on the main screen.
    It takes your pulbic and private key, reciever's public key.
    It also asks you to upload your text file to be sent for creating a
    signature using your private key.
    Upon submitting the text file, it calls the upload_and_sumbit function.
    '''
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Make a new transaction")
    screen4.geometry("500x600")
    global sender_public_address
    global sender_private_address
    global reciever_public_address
    global reciever_public_address_entry

    login_user_entry = login_user.get()
    reciever_public_address = StringVar()

    Label(screen4, text="Whom do you want to send your work " +
          login_user_entry, bg="grey", width="300", height="2",
          fg="white", font=("Arial", 15)).pack()
    Label(screen4, text="").pack()

    Label(screen4, text="Please enter the Reciever's wallet_public address:",
          font=("Times New Roman", 15)).pack()
    reciever_public_address_entry = Entry(screen4,
                                          textvariable=reciever_public_address)
    reciever_public_address_entry.pack()
    Label(screen4, text="").pack()

    Button(screen4, text='Upload and Submit', height="4", width="20",
           command=upload_and_submit).pack()
    Label(screen4, text="").pack()


def upload_and_submit():
    '''
    It reads the file you upload, takes only text file, gives an error mesage
    if any other filetype os uploaded.
    The Hex Keys generated are even length strings and the program gives an
    error message if the string lengths are odd.
    Using the RSA encryption and Crypto module, the private key along with
    message is signed and the signature is returned.
    Can open any text file from your computer.
    '''
    filename = filedialog.askopenfilename()
    if filename[-4:] == '.txt':
        f = open(filename, "r")
        message = f.read()
        login_user_entry = login_user.get()
        f = open(dir_path + "/user_database/" +
                 login_user_entry + "_Wallet.txt", "r")
        data = yaml.load(f.read())
        f.close()
        sender_public_address = data['public_key']
        sender_private_address = data['private_key']
        reciever_public_address = reciever_public_address_entry.get()

        if len(reciever_public_address) % 2 == 0:
            private_key = RSA.importKey(binascii.
                                        unhexlify(sender_private_address))
            signer = PKCS1_v1_5.new(private_key)
            a = SHA.new(str(message).encode('utf8'))
            signature = binascii.hexlify(signer.sign(a)).decode('ascii')

            Label(screen4, text="Your message successfully signed and "
                                "ready to be verified").pack()

            f = open('open_transactions.txt', "r")
            open_list = yaml.load(f.read())
            open_list.append({'sender_name': login_user_entry,
                              'sender_public_address': sender_public_address,
                              'reciever_public_address': reciever_public_address,
                              'transaction_signature': signature,
                              'message': message})

            f = open('open_transactions.txt', "w")
            f.write(str(open_list))
            f.close()
            Button(screen4, text='**Quit**',
                   height="4", width="20", command=exit).pack()
        else:
            Label(screen4, text="Please check your address, it might be wrong",
                  fg="red", font=("Arial", 15)).pack()
    else:
        Label(screen4, text="Please upload a text file",
              bg="grey", fg="white").pack()


def exit():
    '''
    This function is called when you are done
    with your transaction and want to quit the program.
    Uses sys module.
    '''
    sys.exit(0)


def view_transactions():
    '''
    This function is uses to view your transactions
    It checks the blockchain for transactions having your
    public address as sender address and retrieved those transactions
    with the block and transaction numeber
    '''
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("View your transactions")
    screen5.geometry("500x600")
    Label(screen5, text="Here are your transactions").pack()
    Label(screen5, text="").pack()
    login_user_entry = login_user.get()

    f = open(dir_path + "/user_database/" +
             login_user_entry + "_Wallet.txt", "r")
    data = yaml.load(f.read())
    f.close()
    sender_public_address = data['public_key']

    f = open("blockchain.txt", "r")
    chain = yaml.load(f.read())
    get_transactions = []
    for index, block in enumerate(chain):
        for i, transactions in enumerate(block['transactions']):
            if transactions['sender_public_address'] == sender_public_address:
                get_transactions.append((("block-", index + 1,
                                          "transaction-",
                                          i + 1), transactions))
    T = tk.Text(screen5, height=20, width=60)
    T.pack()
    T.insert(tk.END, str(get_transactions))


def view_message():
    '''
    This function is called when you click on 'View your messages'
    button on the main screen.
    it shows the messages you recieved from different users.
    Retrieves data from your wallet file.
    '''
    screen6 = Toplevel(screen)
    screen6.title("View your messages")
    screen6.geometry("500x600")
    login_user_entry = login_user.get()

    f = open(dir_path + "/user_database/" +
             login_user_entry + "_Wallet.txt", "r")
    data = yaml.load(f.read())
    f.close()
    messages = data['recieved_messages']
    Label(screen6, text="*** Messages ***").pack()
    if messages == []:
        Label(screen6, text="___No Messages found___\n"
                            "Please build your scholastic network",
              fg="red", font=("Georgia", 19)).pack()
    else:
        T = tk.Text(screen6, height=40, width=60)
        T.pack()
        T.insert(tk.END, messages)


def main_screen():

    '''
After you successfully logged in this function is called.
It defines the screen attributes and also the Labels
(the text to be displayed on screen) and Buttons(buttons associated with
calling an other function)
It gives you soem choices to choose from.
'''

    global screen3
    screen3 = Toplevel(screen)
    screen3.geometry("400x550")
    screen3.title("Research Flow")

    Label(screen3, text="Research Flow", bg="#787878",
          width="300", height="2", font=("Luminari", 17),
          fg="white").pack()

    Label(screen3, text="").pack()
    Button(screen3, text='View your keys', height="4", width="30",
           font=("Times New Roman", 14), command=view_keys).pack()

    Label(screen3, text="").pack()
    Button(screen3, text='Make a transaction', height="4", width="30",
           font=("Times New Roman", 14), command=make_transaction).pack()

    Label(screen3, text="").pack()
    Button(screen3, text='View your transactions', height="4", width="30",
           font=("Times New Roman", 14), command=view_transactions).pack()

    Label(screen3, text="").pack()
    Button(screen3, text='View your messages', height="4", width="30",
           font=("Times New Roman", 14), command=view_message).pack()


def first_screen():
    '''
    This function is called by the main function.
    It aks the user to register or login.
    '''
    global screen
    screen = tk.Tk()
    screen.geometry("400x550")
    screen.title("Research Flow")
    Label(text="Research Flow", bg="#787878",
          width="300", height="2", font=("Luminari", 17),
          fg="white").pack()
    Label(text="Good Morning, Welcome to Research Flow",
          bg="#787878", fg="white", font=("Arial", 14)).pack()
    Label(text="Our service is transparent, open, secure and hack proof.",
          bg="#787878", fg="white", font=("Arial", 14)).pack()
    Label(text="Please login or register.",
          bg="#787878", fg="white", font=("Arial", 14)).pack()
    Label(text="").pack()
    Button(text='Login', height="4", width="30",
           font=("Times New Roman", 14), command=login).pack()
    Label(text="").pack()
    Button(text='Register', height="4", width="30",
           font=("Times New Roman", 14), command=register).pack()
    tk.mainloop()


if __name__ == '__main__':
    '''
    THis is the main function which only calls the first screen function.
    '''
    first_screen()
