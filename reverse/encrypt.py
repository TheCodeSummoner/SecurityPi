import binascii


def encrypt(message, key="t0T@l1y_S3cURe"):
    # Initialise an iterator to xor the message with key
    i = 0

    # Initialise a list to store xor-ed values
    encr = []

    # Xor asciis of each character in the message and the key
    for char in message:

        # Add the xor to the list
        encr.append(str(ord(char) ^ ord(key[i])))

        # Increase the iterator
        i += 1

        # Reset the iterator if there is no next character in the key
        if i == len(key):
            i = 0

    # Add the length of message 3 times to each value, subtract length of the key once
    encr = [int(xor) + 3*len(message) - len(key) for xor in encr]

    # Perform some easy mathematical operations to mess the values up
    encr = [(xor//3 + 10)*3 if xor % 3 == 0 else xor for xor in encr]

    # Populate the list with more values to look more scary
    encr = [encr[i//2] if i % 2 == 0 else encr[(i//2)] + 5 for i in range(0, len(encr)*2)]

    # Convert the ascii codes to characters
    encr = "".join(chr(xor) for xor in encr)

    # Reformat the values
    encr = binascii.hexlify(bytes(encr, encoding="utf-8"))

    # Return the values
    return encr