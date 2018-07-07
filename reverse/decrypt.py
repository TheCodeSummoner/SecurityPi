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

if __name__ == "__main__":
    a = decrypt(b'c3a6c3abc481c486c38ec393c391c396c38ac38fc39bc3a0c2b9c2bec488c48dc3abc3b0c484c489c3afc3b4c3a8c3adc3abc3b0c381c386c387c38cc3aec3b3c3aac3afc38dc392c38cc391c3b1c3b6c4a3c4a8c3bcc481c3bcc481c491c496c3a1c3a6c39cc3a1c3aac3afc382c387c480c485c491c496c3a8c3adc391c396c38ac38fc480c485c4a3c4a8c3b0c3b5c3a8c3adc3b2c3b7c3afc3b4c3a2c3a7c39fc3a4c395c39ac3a4c3a9c4a9c4aec3aac3afc48cc491c38bc390c480c485c388c38dc4abc4b0c390c395c487c48cc2b8c2bdc4a1c4a6c488c48dc2b8c2bdc2b3c2b8c48ec493c39dc3a2c39ac39fc38bc390c38bc390')
    print(a)