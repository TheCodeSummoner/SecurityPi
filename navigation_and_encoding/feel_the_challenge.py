from random import random
from string import ascii_lowercase

# Get the base challenge name
NAME = __name__.split(".")[0]


def generate(server, name, word_list_path):
    # Create an answer string
    words = " ".join(x for x in read_words(word_list_path))

    # Inform what words were generated
    print(name + " feel_the_challenge: Generated following words: " + words)

    # Add the key to the cache, to check the answer later
    server.cache[name + "_feel_the_challenge"] = words

    # Generate the cipher text
    cipher_text = generate_cipher_text(words)
    # server debug message
    print("feel_the_challenge successfully created:" + cipher_text)

    # Inform the user that the challenge was generated successfully
    return "Successfully generated the challenge. Here is the cipher text! " + "\r\n" + cipher_text + "\r\n"


def check_answer(server, name, answer):
    # Check if the challenge was ran before
    if name + "_feel_the_challenge" in server.cache.keys():

        # Inform what answer was received
        print(name + " feel_the_challenge: Received following answer: " + answer)

        # Check if the answer is correct
        if answer == server.cache.get(name + "_feel_the_challenge"):
            # Send the "correct!" message if the answer matches the message
            return "Correct! Well done!" + "\r\n"
        else:
            # Send the "incorrect!" message if the answer doesn't match the message
            return "Incorrect! Try again!" + "\r\n"

    else:
        # Inform the user that feel_the_challenge task hasn't been executed yet
        return "No message was generated first! Type !" + name + " feel_the_challenge before sending an answer to it." \
               + "\r\n"


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
    cipher_text = encode_letters(words)
    # Return the cipher text
    return cipher_text


def encode_letters(letters):
    # Perform the shift
    alphabet = ascii_lowercase
    braille_alphabet = "⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵"
    table = str.maketrans(alphabet, braille_alphabet)
    return letters.translate(table)
