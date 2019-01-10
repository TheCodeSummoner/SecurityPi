from random import random
from os import path

# Get the base challenge name
NAME = __name__.split(".")[0]

# Declare paths to the files
PATH = path.normpath(path.dirname(__file__))
FLAG_PATH = path.join(PATH, "outputs", "fibres.txt")


def generate(server, name, word_list_path):
    # Create an answer string
    words = " ".join(x for x in read_words(word_list_path))

    # Inform what words were generated
    print(name + " fibres: Generated following words: " + words)

    # Add the key to the cache, to check the answer later
    server.cache[name + "_fibres"] = words

    # Generate the cipher text
    cipher_text = generate_cipher_text(words)

    # Output the cipher text to a file
    file_out = open(FLAG_PATH, "w")
    file_out.write(cipher_text)
    file_out.close()
    # Inform the user that the challenge was generated successfully
    return "Successfully generated the challenge. We had to use an optical-deinterleaver however!" + "\r\n"  # add information about where to find the task


def check_answer(server, name, answer):
    # Check if the challenge was ran before
    if name + "_fibres" in server.cache.keys():

        # Inform what answer was received
        print(name + " fibres: Received following answer: " + answer)

        # Check if the answer is correct
        if answer == server.cache.get(name + "_fibres"):
            # Send the "correct!" message if the answer matches the message
            return "Correct! Well done!" + "\r\n"
        else:
            # Send the "incorrect!" message if the answer doesn't match the message
            return "Incorrect! Try again!" + "\r\n"

    else:
        # Inform the user that fibres task hasn't been executed yet
        return "No message was generated first! Type !" + name + " fibres before sending an answer to it." + "\r\n"


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
    return split(convert_to_binary(words))


def convert_to_binary(letters):
    return ''.join(format(ord(x), 'b') for x in letters)


def split(letters):
    return letters[::2] + "\n" + letters[1::2]
