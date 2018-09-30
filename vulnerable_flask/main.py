# Content from http://www.eveandersson.com/pi/poetry/

from os import path
from random import choice
from vulnerable_flask.website import start_app
from multiprocessing import Process

# Declare paths to the files
PATH = path.dirname(__file__)
FLAG_PATH = path.join(PATH, "secrets", "flag.txt")

# Get the challenge name
NAME = __name__.split(".")[0]


def main(server, data):

    # Initialise the message to send back to the client
    message = ""

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

        # Avoid running server twice
        if NAME + "_flag" not in server.cache.keys():

            # Inform that a website is being created
            print(NAME + ": Creating website...")

            # Run the server
            Process(target=start_app).start()

            # Inform when it was loaded
            print(NAME + ": Website created!")

            # Send the message that a website was created
            message = "Website started!" + "\r\n"

        else:
            # Inform the website is already up
            message = "Website already running!" + "\r\n"

        # Add the flag to cache, to check the answer later
        server.cache[NAME + "_flag"] = flag

    # If the help argument was included
    elif switch == 2 and data[1] == "help":

        # Build the help message
        message = "!" + NAME + " - starts the vulnerable flask challenge" + "\r\n" + \
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
            message = "No website was ran yet! Type !" + NAME + " before sending an answer to it." + "\r\n"

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
