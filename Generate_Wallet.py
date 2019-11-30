import binascii
import os
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

def Generate_keys():
    random_gen = Crypto.Random.new().read
    private_key = RSA.generate(1024, random_gen)
    public_key = private_key.publickey()
    private_key = binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii')
    public_key= binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
    print ("Your public key is :", public_key)
    print ("Your Private key is :", private_key)
    
    
def upload_data():
    all_files = os.listdir("uploads/")   # imagine you're one directory above test dir
    print(all_files)
    for i in all_files:
        if i[-4:] == ".txt":
            f = open(i, "r")
            contents = f.read()
            print (contents)
    
    
if __name__ == "__main__":
    Generate_keys()
    upload_data()