## Reverse programming

When browsing your target's deleted data you have managed to recover an interesting source file, called *encrypt.py*, here are the contents:

```
import binascii

# New encryption algorithm, will be used to encrypt secret messages. Keys are going to consist of 5 letters, lowercase.
def encrypt(message, key="t0T@l1y_S3cURe"):
    i = 0
    encr = []
    for char in message:
        encr.append(str(ord(char) ^ ord(key[i])))
        i += 1
        if i == len(key):
            i = 0
    encr = [int(xor) + 3*len(message) - len(key) for xor in encr]
    encr = [(xor//3 + 10)*3 if xor % 3 == 0 else xor for xor in encr]
    encr = [encr[i//2] if i % 2 == 0 else encr[(i//2)] + 5 for i in range(0, len(encr)*2)]
    encr = "".join(chr(xor) for xor in encr)
    encr = binascii.hexlify(bytes(encr, encoding="utf-8"))
    return encr
```

Based on the comment you believe breaking the encryption will be crucial in proving the insecurity of your target. In order to achieve that, you must create a decryption algorithm.

#### Tasks

Your first task is to decrypt messages encrypted with the default key. Your next task is to decrypt messages with a randomly generated key, using the hint given in the comment.

#### Example solution

Message *b'7378c383c388676ce2829fe282a46469c29ac29fc2bdc382c2a2c2a7c284c289595e7ec283c280c2856d726f74595e565bc299c29e797ec292c297c28ec2935c617075c2b9c2bec29bc2a04c51767bc2a2c2a7c291c296'* encrypted with the default key should be decrypted to *You’re as young as you feel.*. The decrypted sentence is the answer.

Message 
*b'c394c399c2adc2b2c2a6c2abe284aae284afc2b5c2bac298c29dc48ec493c389c38ec2a0c2a5c38fc394c298c29dc380c385c3b1c3b6c2a1c2a6c2b0c2b5c2bdc382c2acc2b1c29ac29fc3a3c3a8c2bdc382c2adc2b2c2b3c2b8c2a0c2a5c2b6c2bbc2a0c2a5c297c29cc48ec493c2a4c2a9c2bac2bfc2afc2b4c2a3c2a8c2adc2b2c2a6c2abc2afc2b4c3a3c3a8c2bac2bfc48ec493c2a0c2a5c298c29dc2bac2bfc2bdc382c2b3c2b8c3abc3b0c3a3c3a8c3b9c3bec384c389c38dc392c3b3c3b8c39ec3a3c2b9c2bec387c38cc485c48a'* encrypted with a random key should be deciphered with the key *dyzll*. The key is the answer.

#### Author

Kacper Florianski