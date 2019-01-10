from random import random
from math import ceil, sqrt
from string import ascii_lowercase
from os import path

# Get the base challenge name
NAME = __name__.split(".")[0]

# Declare paths to the files
PATH = path.normpath(path.dirname(__file__))
FLAG_PATH = path.join(PATH, "outputs", "emperor.txt")


def generate(server, name, word_list_path):
    # Create an answer string
    words = " ".join(x for x in read_words(word_list_path))

    # Inform what words were generated
    print(name + " emperor: Generated following words: " + words)

    # Add the key to the cache, to check the answer later
    server.cache[name + "_emperor"] = words

    # Generate the cipher text
    cipher_text = generate_cipher_text(words)

    # Output the file with the cipher
    file_out = open(FLAG_PATH, "w")
    file_out.write(cipher_text)
    file_out.close()

    # debug message printing
    print("emperor successfully created:" + cipher_text)

    # Inform the user that the challenge was generated successfully
    return "Caesar's been rotating his box again.. Navigate to the output folder to view the task." + "\r\n"


def check_answer(server, name, answer):
    # Check if the challenge was ran before
    if name + "_emperor" in server.cache.keys():

        # Inform what answer was received
        print(name + " emperor: Received following answer: " + answer)

        # Check if the answer is correct
        if answer == server.cache.get(name + "_emperor"):
            # Send the "correct!" message if the answer matches the message
            return "Correct! Well done!" + "\r\n"
        else:
            # Send the "incorrect!" message if the answer doesn't match the message
            return "Incorrect! Try again!" + "\r\n"

    else:
        # Inform the user that emperor task hasn't been executed yet
        return "No message was generated first! Type !" + name + " emperor before sending an answer to it." + "\r\n"


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
            words.append(data[int(random() * length)].strip())

        # Return the populated list
        return words


def generate_cipher_text(words):
    # Perform the caesar shift
    rotated_letters = rotate_letters(words)
    # Perform the box cipher
    cipher_text = box_encode_letters(rotated_letters)
    # Return the cipher text
    return cipher_text


def rotate_letters(letters):
    # Hard coded shift value
    shift = 13
    # Perform the shift
    alphabet = ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return letters.translate(table)


def box_encode_letters(letters):
    # Calculate the number of columns to use
    key = ceil(sqrt(len(letters)))
    order = {
        int(val): num for num, val in enumerate(range(0, int(key)))
    }
    cipher_text = ''

    for index in sorted(order.keys()):
        for part in split_len(letters, key):
            try:
                cipher_text += part[order[index]]
            except IndexError:
                continue
    return cipher_text


def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]
