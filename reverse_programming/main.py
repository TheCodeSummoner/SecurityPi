# Content from http://1001truisms.webs.com/truisms.htm

from os import path
from reverse_programming.encrypt import encrypt
from random import randint, choice

# Declare paths to the files
PATH = path.normpath(path.dirname(__file__))
OUTPUT_PATH = path.join(PATH, "output.txt")
SENTENCES_PATH = path.join(PATH, "sentences.txt")

# Get the challenge name
NAME = __name__.split(".")[0]


def main(server, data):

    # Get the number of elements passed in the command
    switch = len(data)

    # If only the command was sent, encrypt a message and send it to the user
    if switch == 1:

        # Randomly get a sentence to encrypt and save it to the output file
        get_secret(randint(0, 997))

        # Load the output into a variable
        with open(OUTPUT_PATH, encoding="utf-8") as f:
            output = f.readline()
            f.close()

        # Inform what message was loaded
        print(NAME + ": Encrypting following sentence: " + output)

        # Add the sentence to cache, to check the answer later
        server.cache[NAME + "_message"] = output

        # Encrypt the sentence and save it to the output file
        save_output(str(encrypt(output)))

        # Load the output into a variable
        with open(OUTPUT_PATH, encoding="utf-8") as f:
            output = f.readline()
            f.close()

        # Send the output to the client
        message = "Here is the encrypted message: " + output + "\r\n"

    # If the help argument was included, display the help message
    elif switch == 2 and data[1] == "help":

        # Build the help message
        message = "!" + NAME + " - starts the programming challenge described under id 01 on the website" + "\r\n" + \
                  "!" + NAME + " <answer> - checks the answer of the programming challenge" + "\r\n" \
                  "!" + NAME + " no_key - starts the previous challenge, but with an unknown key of length 5" + "\r\n" \
                  "!" + NAME + " no_key <answer> - checks the answer of the no_key challenge" + "\r\n"

    # If a no_key argument was included, generate a key, encrypt a message and start the challenge
    elif switch == 2 and data[1] == "no_key":

        # Generate they key of certain length
        key = generate_key(5)

        # Add the key to cache, to check the answer later
        server.cache[NAME + "_key"] = key

        # Inform what key was generated
        print(NAME + ": Generated following key: " + key)

        # Randomly get a sentence to encrypt and save it to the output file
        get_secret(randint(0, 997))

        # Load the output into a variable
        with open(OUTPUT_PATH, encoding="utf-8") as f:
            output = f.readline()
            f.close()

        # Inform what message was loaded
        print(NAME + ": Encrypting following sentence: " + output)

        # Encrypt the sentence and save it to the output file
        save_output(str(encrypt(output, key=key)))

        # Load the output into a variable
        with open(OUTPUT_PATH, encoding="utf-8") as f:
            output = f.readline()
            f.close()

        # Send the output to the client
        message = "Here is the encrypted message encrypted with a random key: " + output + "\r\n"

    # If a non-help, non-no_key arguments were included, check if the answer is correct
    else:

        # If an answer to the no_key challenge was provided
        if data[1] == "no_key":

            # Check if the key was actually generated before
            if NAME + "_key" in server.cache.keys():

                # Inform what answer was received
                print(NAME + ": Received following answer: " + data[2])

                # Check if the answer is correct
                if data[2] == server.cache.get(NAME + "_key"):
                    # Send the "correct!" message if the answer matches the message
                    message = "Correct! Well done!" + "\r\n"
                else:
                    # Send the "incorrect!" message if the answer doesn't match the message
                    message = "Incorrect, removing the key! Try again!" + "\r\n"

                    # Remove the key to not allow straight brute force
                    server.cache.pop(NAME + "_key")

            else:
                # Inform the user that no_key hasn't been executed yet
                message = "No key was generated yet! Type !" + NAME + " no_key before sending an answer to it." + "\r\n"

        # If an answer to standard challenge was provided
        else:
            # Check if the message to encrypt was actually generated before
            if NAME + "_message" in server.cache.keys():

                # Initialise an answer string
                answer = ""

                # Build the answer string
                for arg in data[1:]:
                    answer += arg
                    answer += " "

                # Remove the whitespace character on the end
                answer = answer[:-1]

                # Inform what answer was received
                print(NAME + ": Received following answer: " + answer)

                # Check if the answer is correct
                if answer == server.cache.get(NAME + "_message"):
                    # Send the "correct!" message if the answer matches the message
                    message = "Correct! Well done!" + "\r\n"
                else:
                    # Send the "incorrect!" message if the answer doesn't match the message
                    message = "Incorrect! Try again!" + "\r\n"

            else:
                # Inform the user that the challenge hasn't been executed yet
                message = "No message was generated yet! Type !" + NAME + " before sending an answer to it." + "\r\n"

    # Send the prepared message to the client
    server.send(message)


def generate_key(length):
    return "".join(choice("abcdefghijklmnopqrstuvwxyz") for _ in range(length))


def get_secret(index):

    with open(SENTENCES_PATH, encoding="utf-8") as f:

        # Get the sentence from the file
        sentence = f.readlines()[index][:-1]

        # Release the resources
        f.close()

        # Save the sentence to the file
        save_output(sentence)


def save_output(data):

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:

        # Save the sentence to the output file
        f.write(data)

        # Release the resources
        f.close()
