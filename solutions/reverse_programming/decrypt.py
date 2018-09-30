import binascii


def decrypt(message, key="t0T@l1y_S3cURe"):

    # Unhexlify the message
    decr = str(binascii.b2a_hex(binascii.unhexlify(message)))[2:-1]

    # Rebuild the string
    decr = bytes.fromhex(decr).decode('utf-8')

    # Remove the artificial values from the given message
    decr = [decr[i] for i in range(0, len(decr), 2)]

    # Reverse the mathematical operations
    decr = [(ord(ascii) // 3 - 10) * 3 if ord(ascii) % 3 == 0 else ord(ascii) for ascii in decr]

    # Reverse the subtraction and addition
    decr = [xor - 3*len(decr) + len(key) for xor in decr]

    # Initialise an iterator to xor the message with key (xor is reversible)
    i = 0

    # Initialise a list to store asciis of characters after reversing the xor
    asciis = []

    # Xor asciis of each character in the message and the key
    for value in decr:

        # Add the xor to the list
        asciis.append(value ^ ord(key[i]))

        # Increase the iterator
        i += 1

        # Reset the iterator if there is no next character
        if i == len(key):
            i = 0

    # Convert the ascii codes back to characters
    decr = "".join(chr(ascii) for ascii in asciis)

    # Return the string
    return decr
