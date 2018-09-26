from random import random
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

    # Output the cipher text to a file - TODO FILE NAME
    # file_out = open("myfile.txt", "w")
    # file_out.write(cipher_text)
    # Inform the user that the challenge was generated successfully
    # testing
    return "Successfully generated the challenge. The generation was " + cipher_text + "\r\n"
    # add information about where to find the task


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
            words.append(data[int(random()*length)].strip())

        # Return the populated list
        return words
    
    
def generate_cipher_text(words):
    # template text
    file_object = open("flag.txt", "r")
    template = file_object.read()
    file_object.close()
    
    # create the flag sentence
    flag_string = "FLAG:" + words
    
    # format to 42 char total length
    flag_string= '{:<42}'.format(flag_string[:42])

    # alter the flag text
    cipher_text = template.replace("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", flag_string,1)
    # alter the flag text
    
    return cipher_text






