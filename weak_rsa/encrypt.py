from math import pow
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.construct((128002755223454646198073965340894060371445991066613494720122727544008615411871891096844097898661194591655302143326237919569747921814908576549065399104457717799143751183406752650325048257476598274890218678473868119028796397050641629556437191648323652004493511036039102735115075825117431749292058415814982067341, 3))

encryptor = PKCS1_OAEP.new(key.publickey())
encrypted = encryptor.encrypt(bytes("hi", encoding="utf-8"))

for i in encrypted:
    print(pow(i, 1/3))


# Works nice, figure out how to decrypt a message exploting the m^e (mod n) = m^e
# Figure out how does cracking a p, q contribute to deciphering a message?

'''
f = key.export_key()
print(f)
'''