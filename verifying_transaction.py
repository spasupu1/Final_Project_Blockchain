from collections import OrderedDict
import binascii
import os
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5



def verify_transaction_signature(sender_public_address, signature, message):
        public_key = RSA.importKey(binascii.unhexlify(sender_public_address))
        verifier = PKCS1_v1_5.new(public_key)
        h = SHA.new(str(message).encode('utf8'))
        return verifier.verify(h, binascii.unhexlify(signature))

def get_message():
	message = []
	all_files = os.listdir("./")
	print (all_files)
	for i in all_files:
		if i[-4:] == ".txt":
			f = open(i, "r")
			contents = f.read()
			message.append(contents)
			print (message)
	return message


if __name__ == "__main__":
	sender_public_address = "30819f300d06092a864886f70d010101050003818d0030818902818100d24d3507e87f995dfff4cc16b5a0b2c807e73646e19e248b177054619e5fb2e3733bf26ff22bdcc1f6e5044cbbea929199673bd51c8a32faa846e8e2d7195081e2e03a761f09047114071bd19a0289e4239319e123912f9a70a9a0fa4d5802673a9960d7c40d1acbea6e59fbac0d36c57a5464a57ff1db44764986b6d161c8870203010001"
	signature = "41a8170f6c12229c6686994d1928a8645281b3defde260438e2688f87eb07a4a6d8c90c3f64a30edc2574e46249c33cb6a17638a40b9b08ca8069f0daf4318b8a56aa183cdc88d961af247a2caa85ae5a5bb332e42b59ab867b3ab6dfccee086d6a82e9b6b0f6301f7d5d7f62198e4c235cddba012d585d0fdbb072a467c3a75"
	message = get_message()
	a = verify_transaction_signature(sender_public_address, signature, message)
	if a == True:
		print("congrats")