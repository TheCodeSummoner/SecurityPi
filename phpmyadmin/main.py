from os import path, sep
from random import choice

# Get the challenge name
NAME = __name__.split(".")[0]

# Declare path to the file
FLAG_PATH = path.join(sep, "var", "www", "html", "flag.txt")


def main(server, data):

    # Get the number of elements passed in the command
    switch = len(data)

    # If only the command was sent
    if switch == 1:

        # Generate the flag
        flag = generate_flag(32)

        # Inform what flag was generated
        print(NAME + ": Generated following flag: " + flag)

        # Save the flag to the file
        save_flag(flag)

        # Add the flag to cache, to check the answer later
        server.cache[NAME + "_flag"] = flag

        # Send the message that the challenge was setup successfully
        message = "Challenge started!" + "\r\n"

    # If the help argument was included
    elif switch == 2 and data[1] == "help":

        # Build the help message
        message = "!" + NAME + " - starts the phpMyAdmin shell exploit challenge" + "\r\n" + \
                  "!" + NAME + " <answer> - checks the answer of the challenge" + "\r\n"

    # If any non-help arguments were included
    else:

        # Retrieve the answer
        answer = data[1]

        # Check if the flag was actually generated before
        if NAME + "_flag" in server.cache.keys():

            # Inform what answer was received
            print(NAME + ": Received following answer: " + answer)

            # Check if the answer is correct
            if answer == server.cache.get(NAME + "_flag"):
                # Send the "correct!" message if the answer matches the flag
                message = "Correct! Well done!" + "\r\n"
            else:
                # Send the "incorrect!" message if the answer doesn't match the flag
                message = "Incorrect! Try again!" + "\r\n"

        else:
            # Inform the user that the challenge hasn't been executed yet
            message = "No flag generated yet! Type !" + NAME + " before sending an answer to it." + "\r\n"

    # Send the prepared message to the client
    server.send(message)


def generate_flag(length):
    return "".join(choice("abcdefghijklmnopqrstuvwxyz_") for _ in range(length))


def save_flag(flag):

    with open(FLAG_PATH, "w", encoding="utf-8") as f:

        # Save the flag to the file
        f.write(flag)

        # Release the resources
        f.close()
