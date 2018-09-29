from random import random
import os.path
import os
import tarfile

# Get the base challenge name
NAME = __name__.split(".")[0]


def generate(server, name, path):
    # Create an answer string
    words = " ".join(x for x in read_words(path))

    # Inform what words were generated
    print(name + " telegram: Generated following words: " + words)

    # Add the key to the cache, to check the answer later
    server.cache[name + "_telegram"] = words

    # Generate the cipher text
    cipher_text = generate_cipher_text(words)

    # Output the cipher text to a file
    complete_name = os.path.join("navigation_and_encoding/outputs", "telegram.tar.gz")
    temp_name = os.path.join("navigation_and_encoding/outputs", "telegram.txt")

    # create the file
    temp_file_out = open(temp_name, "w")
    temp_file_out.write(cipher_text)
    temp_file_out.close()

    with tarfile.open(complete_name, "w:gz") as tar:
        tar.add(temp_name, arcname=os.path.basename("navigation_and_encoding"))
        tar.close()
    os.remove(temp_name)
    # server debug message
    print("telegram output successfully created:" + cipher_text)
    # Inform the user that the challenge was generated successfully
    return "Successfully generated the challenge. Check the output folder for the file - " \
           "we compressed it to save space!" + "\r\n"


def check_answer(server, name, answer):
    # Check if the challenge was ran before
    if name + "_telegram" in server.cache.keys():

        # Inform what answer was received
        print(name + " telegram: Received following answer: " + answer)

        # Check if the answer is correct
        if answer == server.cache.get(name + "_telegram"):
            # Send the "correct!" message if the answer matches the message
            return "Correct! Well done!" + "\r\n"
        else:
            # Send the "incorrect!" message if the answer doesn't match the message
            return "Incorrect! Try again!" + "\r\n"

    else:
        # Inform the user that telegram task hasn't been executed yet
        return "No message was generated first! Type !" + name + " telegram before sending an answer to it." + "\r\n"


def read_words(path):
    with open(path, encoding="utf-8") as f:
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
    # template text
    file_object = open("navigation_and_encoding/flag.txt", "r")
    template = file_object.read()
    file_object.close()

    # create the flag sentence
    flag_string = "FLAG:" + words

    # format to 42 char total length
    flag_string = '{:<42}'.format(flag_string[:42])

    # alter the flag text
    ascii_art = template.replace("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", flag_string, 1)
    # convert to binary
    binary = ' '.join('{0:08b}'.format(ord(x), 'b') for x in ascii_art)
    # convert to morse
    binary_to_morse = {
        '0': '----- ',
        '1': '.---- ',
        ' ': '/ '
    }
    cipher_text = ""
    for c in binary:
        cipher_text += " " + (''.join(str((binary_to_morse[c]))))
    return cipher_text
