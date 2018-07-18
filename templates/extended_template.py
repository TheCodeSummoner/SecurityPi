""" Challenge template for the server

This is a template file prepared for everyone who would like to add a challenge to the Raspberry Pi's server.
It will point out the most important bits of creating a challenge and guide through common Python requirements.

Author: Kacper Florianski

=== Purpose ===

This template is an extended version of the simple template. It provides examples on loading external files, calling
system commands and using server cache.

=== Imports ===

In order to import modules from current directory simply call "import directory_name.module_you_want_to_import".

If you want to load other files you will need to give the program full path to them, as relative paths are dependant on
current workspace, which changes depending from where are the server files executed. It will also help to keep
the server multi-platform - you can test it on ex. Windows first, and then test it on the pi afterwards. The path import
will make it possible to work on both, and the system import will help calling external scripts using system's prompt.

=== Program flow ===

This program will sent back to the client whatever was saved in "ouput.txt" file. It will first check if the file exists
using server's cache (just for the example sake, there are other methods to check if a file exists), then save whatever
is stored in it to a string variable, and send the variable's content to the client. The file itself will be populated
by redirecting system's echo command's output, and the command will be executed with arguments passed by the client.

=== Testing ===

Rename this module to "main" and run the server to see this template in action.

"""

from os import path, system

# Retrieve the absolute path to current directory, this will allow the usage of any files placed in this folder
PATH = path.normpath(path.dirname(__file__))

# Get the challenge name, this will make name changes very easy, as only the folder name has to be changed
NAME = __name__.split(".")[0]


# Define your main function - remember that it has to take EXACTLY 2 arguments - server and arguments passed in the
# command, as well as it MUST be called "main". This function will be added to the server.
def main(server, data):

    # Get the number of elements passed in the command, ex. !command a b c will result in 4 elements passed.
    switch = len(data)

    # If only the command was sent, ex. !command
    if switch == 1:

        # Check using server's cache if the file exists (here simple check - check if specified cache entry exists)
        if NAME + "_template_test" in server.cache:

            # Load and the contents of "output.txt" if yes
            message = load_message() + "\r\n"

        else:
            # Otherwise inform the client that he has to call the command with arguments first
            message = "No content. Use command's help to learn about its usage." + "\r\n"

    # If the help argument was included ex. !command help, display the help message
    elif switch == 2 and data[1] == "help":

        # Build the help message, remember to put "\r\n" for a new line
        message = "Helpful message describing the usage of command." + "\r\n"

    # You can handle more situations, but remember that to put "else" at the end or check for "more than n" arguments
    else:

        # Build an echo command with given arguments and save the output to the "output.txt" file in current folder
        command = "echo " + "".join(arg + " " for arg in data[1:])[:-1] + " > " + path.join(PATH, "output.txt")

        # Execute the command
        system(command)

        # Inform te client that the scripts was executed
        message = "Script executed, message saved, cache populated." + "\r\n"

        # Populate the cache
        server.cache[NAME + "_template_test"] = True

    # Send the prepared message to the client
    server.send(message)


def load_message():
    """

    You can trigger the error message to be sent by first calling the command with arguments and later deleting the
    "output.txt" file.

    """

    # You can put code in try-catch blocks if you want to handle errors
    try:

        # Load the output into a variable
        with open(path.join(PATH, "output.txt")) as f:
            output = f.readline()[:-1]
            f.close()

    # You should always specify concrete exceptions to handle, catching all existing exceptions is not the best idea
    except FileNotFoundError:

        # Inform the client that there was a server-side (or rather challenge-side) error by returning this sentence
        return "Something went wrong and the message wasn't saved, sorry!"

    return "Saved message: " + output
