# Welcome to Research Flow

A transparent, open, secure and hack proof Blockchain messenger.


### What is BlockChain?
```
As the name suggests, blockchain is a chain of blocks which stores the data in a decentralised and self regulatory way.
One can open, share, sign  and verify data without the need of any centralised authority.
```

One of the best examples of this technology is Bitcoin.
Money transaction between two users using its own currency has been performed with the encryption using digital signatures and broadcasted to the blockchain network(miners who are like you and me to timestamp and validate the transactions).
Then these transactions are added to the block which is chained to the blockchain.

No one can actually alter the transaction once it is appended to the chain.

Every block is hash linked i.e, the block will have the information of the hash of the previous block.
If the data in the previous block is changed, it changes the hash of it thus invalidates it in the new block and so the chain corrupts.
A new block is added once the miner solves a tough mathematical puzzle and also gets rewarded.
This update is then broadcasted to the network for other miners to update their chain.
As the data is decentralised and all the miners have the data, it is is very unlikely to modify data.


### Problems in the scholastic community?

Research on different aspects is being conducted around the world and communications plays an important role in exchange of ideas, data and also the results.
Currently this exchange of data is not being done properly and is getting modified or manipulated before reaching the next person.
A few problems with the scholastic communication are:

#### Reproducability:
Due to the pressure on researchers to publish, they are more inclined to produce positive results, manipulating some of the data and also using fussy protocols to produce results faster.
Other researchers are unable to reproduce this data because of the above cases.

#### Journal business:
Journals are the primary vehicles to broadcast your research to the world.
They have a lot of bias towards accepting manuscripts and encourage only positive and novel results to maintain their reputation and status amongst other journals.
This even makes researchers to ignore the failed data which is actually important .
This makes the other researchers to perform the same failed experiments as no one reported that this experiment can fail.

#### Peer review:
Journals base their interest to accept of decline a manuscript based on peer review which is an expensive, biased process.
Peer researchers may or may not have expertise in the field of the manuscript and may give an incomplete review or get biased towards a few researchers.

#### Hype on certain area or field:
With time to time, there will be a heightened interest on certain topics which is luring researchers to work only on it for increasing their reputation and attracting top tier journals.

#### Open Access:
A few journals have the concept of open access to the papers but the researcher has to pay a huge sum to make their research reach the masses.

These all problems lead to the success of the websites like Sci-hub which has over 60 million research articles to download infringing the copyrights of the publishers.


### How Blockchain helps?

Blockchain has the capability to make research more transparent, open, accessible and secure.
A researcher can share his data with whomsoever he wants and his transaction is secure in the blockchain.
As each transaction is timestamped ,there won’t be any data infringement and also this can act as a patent on the work.
It is  easy to see how data flows through the scholastic community and thus the original research is being shared without any bias.
As the senders signs the transaction there is no problem of hacking and its theoretically impossible to modify data.
Thus blockchain builds trust, universal access and also credit to your work.
It also allows for anonymity wherever required.


### How my program works:
1.	The program registers the user into the database.

2.	After logging in he can make a new transaction, view his transactions and the messages he received from other users.
3.	If he wants to send a message to another user, he can upload the text file* he want to send and signs it along with his private key.
4.	This authenticates that you are the sender of the message.
5.	This transaction gets added to the open transactions list which is verified by the miner using your public address and adds to the last block of the chain.
6.	He also sends the message to the receiver once the transaction is made.
7.	Ideally each block can only store a few transactions (500 in the case of bitcoin), so it is important to mine and add a new block to the chain.
8.	To mine a block the miner needs to solve a mathematical puzzle which is difficult to solve and easy to verify once it is solved.
9.	So he will be rewarded for adding a new block and also gets a small transaction fee for verifying and adding the transaction.
10.	Once a new transaction or a block is added, he broadcasts the chain to the network which alerts the nodes to update their chain.


* *This program only takes a text file which has charecters and spaces, but not line breaks.
So a few sample text files are included to verify.
