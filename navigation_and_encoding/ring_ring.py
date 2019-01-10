from random import random
from os import path

# Get the base challenge name
NAME = __name__.split(".")[0]

# Declare paths to the files
PATH = path.normpath(path.dirname(__file__))
FLAG_PATH = path.join(PATH, "outputs", ".ring_ring.txt")


def generate(server, name, word_list_path):

    # Create an answer string
    words = " ".join(x for x in read_words(word_list_path))

    # Inform what words were generated
    print(name + " ring_ring: Generated following words: " + words)

    # Add the key to the cache, to check the answer later
    server.cache[name + "_ring_ring"] = words

    # Generate the cipher text
    cipher_text = generate_cipher_text(words)

    # Output the cipher text to a file
    file_out = open(FLAG_PATH, "w")
    file_out.write(cipher_text)
    file_out.close()
    # print debug message
    print("ring_ring successfully created:" + cipher_text)

    # Inform the user that the challenge was generated successfully
    return "You've been sent a message from an old number. Check the output folder for the message - it might be hiding!" + "\r\n"


def check_answer(server, name, answer):

    # Check if the challenge was ran before
    if name + "_ring_ring" in server.cache.keys():

            # Inform what answer was received
            print(name + " ring_ring: Received following answer: " + answer)

            # Check if the answer is correct
            if answer == server.cache.get(name + "_ring_ring"):
                # Send the "correct!" message if the answer matches the message
                return "Correct! Well done!" + "\r\n"
            else:
                # Send the "incorrect!" message if the answer doesn't match the message
                return "Incorrect! Try again!" + "\r\n"

    else:
        # Inform the user that ring_ring task hasn't been executed yet
        return "No message was generated first! Type !" + name + " ring_ring before sending an answer to it." + "\r\n"


def read_words(file_path):

    with open(file_path, encoding="utf-8") as f:

        # Get the words from the file
        data = f.readlines()

        # Save the length of the file
        length = len(data) - 1

        # Release the resources
        f.close()

        # Initialise a list of words for the challenge
        words = []

        # Populate the list with 5 words randomly chosen from the file
        for i in range(5):
            words.append(data[int(random()*length)].strip())

        # Return the populated list
        return words


def generate_cipher_text(words):
    return convert_letters(words)


def convert_letters(words):
    
    letters_to_numbers = {
        'a': '00000010 00000000',
        'b': '00000010 00000010 00000000',
        'c': '00000010 00000010 00000010 00000000',
        'd': '00000011 00000000',
        'e': '00000011 00000011 00000000',
        'f': '00000011 00000011 00000011 00000000',
        'g': '00000100 00000000',
        'h': '00000100 00000100 00000000',
        'i': '00000100 00000100 00000100 00000000',
        'j': '00000101 00000000',
        'k': '00000101 00000101 00000000',
        'l': '00000101 00000101 00000000',
        'm': '00000110 00000000',
        'n': '00000110 00000110 00000000',
        'o': '00000110 00000110 00000110 00000000',
        'p': '00000111 00000000',
        'q': '00000111 00000111 00000000',
        'r': '00000111 00000111 00000111 00000000',
        's': '00000111 00000111 00000111 00000111 00000000',
        't': '00001000 00000000',
        'u': '00001000 00001000 00000000',
        'v': '00001000 00001000 00001000 00000000',
        'w': '00001001 00000000',
        'x': '00001001 00001001 00000000',
        'y': '00001001 00001001 00001001 00000000',
        'z': '00001001 00001001 00001001 00001001 00000000',
        ' ': ''
    }

    cipher_text = ""
    for c in words:
        cipher_text += " " + (''.join(str((letters_to_numbers[c]))))
    return cipher_text
