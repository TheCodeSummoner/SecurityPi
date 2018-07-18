""" Challenge template for the server

This is a template file prepared for everyone who would like to add a challenge to the Raspberry Pi's server.
It will point out the most important bits of creating a challenge and guide through common Python requirements.

Author: Kacper Florianski

=== Purpose ===

This template is a somewhat empty file for people who are confident in their python skills and/or would like to write
their challenges almost from scratch. Please remember that different systems result in different behaviour and
you should always try to write as universal code as possible, and test everything before public release.

=== Testing ===

Rename this module to "main" and run the server to see this template in action.

"""


# Define your main function - remember that it has to take EXACTLY 2 arguments - server and arguments passed in the
# command, as well as it MUST be called "main". This function will be added to the server.
def main(server, data):

    # Initialise the message to send back to the client
    message = ""

    # Get the number of elements passed in the command, ex. !command a b c will result in 4 elements passed.
    switch = len(data)

    # If only the command was sent, ex. !command
    if switch == 1:

        # Do something
        pass

    # If the help argument was included ex. !command help, display the help message
    elif switch == 2 and data[1] == "help":

        # Build the help message, remember to put "\r\n" for a new line
        message = "Helpful message describing the usage of command." + "\r\n"

    # If an argument was included, but it wasn't "help", ex. !command answer
    elif switch == 2:

        # Do something
        pass

    # You can handle more situations, but remember that to put "else" at the end or check for "more than n" arguments
    else:

        # Do something, in this case if 2 or more arguments were passed, ex. !command answer1 answer2
        pass

    # Send the prepared message to the client
    server.send(message)
