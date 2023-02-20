import datetime
from hashlib import sha256
import random

class BlockChain:

    blockNo=0
    nonce=0
    transaction=None
    previous_hash=None
    hash=None
    timestamp=str(datetime.datetime.now())

    blockchainList=[]

    def __init__(self):
        self.blockNo=1
        self.nonce=random.randint(0,100)
        self.previous_hash="0000000000000000000"
        self.timestamp=str(datetime.datetime.now())

    def hashblock(self):
        newNonce=random.randint(1,1000000000)
        hashtext=str(self.blockNo)+str(newNonce)+str(self.transaction)+str(self.previous_hash)+self.timestamp
        blockhash=sha256(hashtext.encode()).hexdigest()

        self.hash=blockhash
        self.nonce=newNonce

    def addToBlockchain(self):
        block={
            'blockNo':self.blockNo,
            'nonce':self.nonce,
            'previous_hash':self.previous_hash,
            'transaction':self.transaction,
            'timestamp':self.timestamp,
            'hash':self.hash
        }
        self.blockchainList.append(block)

## เริ่มสร้าง blockchain.

block=BlockChain()

# print(block.blockNo)
# print(block.nonce)
# print(block.transaction)
# print(block.previous_hash)
# print(block.hash)
# print(block.timestamp)
# print(block.blockchainList)


block.hashblock()
# print(block.blockNo)
# print(block.nonce)
# print(block.transaction)
# print(block.previous_hash)
# print(block.hash)
# print(block.timestamp)
# print(block.blockchainList)

# print("=============เพิ่ม block เข้าไปใน blockchain=============")
block.addToBlockchain()
# print(block.blockNo)
# print(block.nonce)
# print(block.transaction)
# print(block.previous_hash)
# print(block.hash)
# print(block.timestamp)
# print(block.blockchainList)

print("=============แสดงข้อมูลของ block ใน blockchain=============")
print("หมายเลข block: ",block.blockchainList[0]['blockNo'])
print("ค่า Nonce: ",block.blockchainList[0]['nonce'])
print("ข้อมูลใน block: ",block.blockchainList[0]['transaction'])
print("previous_hash: ",block.blockchainList[0]['previous_hash'])
print("hash ของ block: ",block.blockchainList[0]['hash'])
print("เวลาที่สร้าง block: ",block.blockchainList[0]['timestamp'])
