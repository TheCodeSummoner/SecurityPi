from os import path
from random import choice
from vulnerable_flask.website import start_app

# Declare paths to the files
PATH = path.dirname(__file__)
FLAG_PATH = path.join(PATH, "secrets", "flag.txt")


def main(server, data):

    # Initialise the message to send back to the client
    message = ""

    # Get the number of elements passed in the command
    switch = len(data)

    # If only the command was sent
    if switch == 1:

        # Generate the flag
        flag = generate_flag(12)

        # Inform what flag was generated
        print("Flask: Generated following flag: " + flag)

        # Add the flag to cache, to check the answer later
        server.cache["flask_flag"] = flag

        # Save the flag to the file
        save_flag(flag)

        # Run the server
        start_app()

    # If the help argument was included
    elif switch == 2 and data[1] == "help":

        # Build the help message
        message = "Helpful message describing the usage of command." + "\r\n"

    # If any non-help arguments were included
    else:

        # Retrieve the answer
        answer = data[1]

        # Check if the flag was actually generated before
        if "flask_flag" in server.cache.keys():

            # Inform what answer was received
            print("Flask: Received following answer: " + answer)

            # Check if the answer is correct
            if answer == server.cache.get("flask_flag"):
                # Send the "correct!" message if the answer matches the flag
                message = "Correct! Well done!" + "\r\n"
            else:
                # Send the "incorrect!" message if the answer doesn't match the flag
                message = "Incorrect! Try again!" + "\r\n"

        else:
            # Inform the user that !vulnerable_flask hasn't been executed yet
            message = "No website was ran yet! Type !vulnerable_flask before sending an answer to it." + "\r\n"

    # Send the prepared message to the client
    server.send(message)


def generate_flag(length):
    return "{" + "".join(choice("abcdefghijklmnopqrstuvwxyz_") for _ in range(length)) + "}"


def save_flag(flag):

    with open(FLAG_PATH, "w", encoding="utf-8") as f:

        # Save the flag to the file
        f.write(flag)

        # Release the resources
        f.close()
