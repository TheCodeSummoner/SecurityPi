""" Server for RaspberryPi (Python 3.6)

This is a server written during the internship with dr. Charles Morisset, Newcastle University.
Its purpose is to teach security in live but safe environment, with the help of Raspberry Pi.

Author: Kacper Florianski

=== Usage ===

Run $ python server.py where python refers to version 3.6. From that moment you can connect to the server
by specifying Pi's ethernet IP and port (defaults to 50000).

Once ran the server should never stop listening to incoming connections, however it will only accept 1 at a time.

Raspberry Pi should run the server on startup, if you have access to pi's console you can check if it's running
by typing $ ps aux | grep python and looking for process with server.py in name.

=== Adding your own challenge ===

You can make your own challenge with the help of methods and variables existing in the server. There are some rules:

 - you have to create a separate folder for your challenge, with a unique name
 - you have to provide a python's module called 'main' (ex. module main in folder reverse)
 - you have to develop a single python function that can be called from the server (the function can call other scripts)
 - the function mentioned has to have the same name as the module (ex. function main in module main in folder reverse)
 - the function mentioned has to take EXACTLY 2 arguments - server and command data (ex. main(server, data))
 - your function should implement the usage of help argument

If the following requirements are met, the server will automatically add a command and use provided files.

In your challenge you can access:

 - cache variable, it's a python dictionary where you can store information required for your challenge
 - send(data) method, which sends a message (string) to the connected client

While it is not possible to restrict the access to other variables or methods, I do not encourage to use them.

Please refer to the template files for additional guidance regarding making your own challenge, including good practice.
Templates can be found in the templates folder.

=== Example ===

Let's say a client connects to the pi and enters following commands in given order:

Input: Hello
Output: Invalid command. Type !help to display available commands.

Input: !help
Output: Here are the available commands:
 - !help
 - !reverse_programming
To learn more about each command, type <command> help.
To add arguments to a command, type <command> <argument1> <argument2> (...)

Input: !reverse_programming help
Output: !reverse_programming - starts the programming challenge
!reverse_programming <answer> - checks the answer of the programming challenge
!reverse_programming no_key - starts the previous challenge, but with an unknown key of length 5
!reverse_programming no_key <answer> - checks the answer of the no_key challenge

Note that "!reverse_programming help" command had to be coded within the reverse function, and used the data argument to
achieve desired functionality (precisely, in that case data = ["!reverse_programming", "help"])
"""

from os import listdir, path
from importlib import import_module
import socket


# TODO: Add docs of each element
class Server:

    def __init__(self, *, host_ip='0.0.0.0', port=50000):

        # Save the host and port information
        self.host_ip = host_ip
        self.port = port

        # Initialise the socket for IPv4 addresses (hence AF_INET) and TCP (hence SOCK_STREAM)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Bind the socket to the given address
            self.socket.bind((self.host_ip, self.port))
        except socket.error as e:
            print("Failed to bind socket to the given ip and port - " + str(e))

        # Tell the server to listen to only one connection
        self.socket.listen(1)

        # Initialise client information
        self.client_socket = None
        self.client_address = None
        self.client_ip = None

        # Initialise possible commands, add hardcoded help method
        self.commands = {
            "!help": self.help,
        }

        # Create an empty dictionary to let the challenge creators store important information
        self.cache = {}

        # Build the commands for all properly prepared file structures
        self.build()

    def build(self):

        # Get the path to current (root) directory
        root = path.normpath(path.dirname(__file__))

        # Retrieve immediate child directories of root directory
        directories = [child for child in listdir(root) if path.isdir(path.join(root, child))]

        # Iterate over each sub-folder
        for directory in directories:

            try:
                # Check if a following command already exists (name clash)
                if "!" + directory in self.commands:
                    raise NameError

                # Attempt to add a function from a module that both have the same name as directory
                self.commands["!" + directory] = getattr(import_module(directory + ".main"), "main")

            # In case a module couldn't be found
            except ModuleNotFoundError:
                print("Could not find \"main\" module within the " + directory + " folder.")

            # In case the directory name was resulting in an error, for example it had a dot ('.') character
            except TypeError:
                print("Invalid name for the " + directory + " directory.")

            # In case a function couldn't be found
            except AttributeError:
                print("Could not find \"main\" function within the " + directory + " folder.")

            # In case the given name already exists
            except NameError:
                print("Function !" + directory + " was already added to the server.")

    def run(self):

        # Never stop the server once it was started
        while True:

            # Inform that the server is ready to receive a connection
            print("Waiting for a connection to {} on port {}...".format(self.host_ip, self.port))

            # Wait for a connection (accept function blocks the program until a client connects to the server)
            self.client_socket, self.client_address = self.socket.accept()

            # Inform that someone has connected
            print("Client with address {} connected".format(self.client_address))

            # Store the ip separate to other address details for convenience
            self.client_ip = self.client_address[0]

            # Inform the user that he is connected
            self.send("Connected! Type !help to display available commands." + "\r\n")

            while True:

                try:
                    # Once connected, keep receiving the data, break in case of errors
                    data = self.client_socket.recv(2048)
                except ConnectionResetError:
                    break
                except ConnectionAbortedError:
                    break

                # If 0-byte was received, close the connection
                if not data:
                    break

                try:
                    # Convert bytes to string, remove white spaces
                    data = data.decode("utf-8").strip()
                except UnicodeDecodeError:
                    # Ignore if an invalid character was sent (ex. Putty's telnet sends hex characters at start)
                    data = None

                # If data was valid
                if data:

                    # Inform what data was received
                    print("Received: " + data)

                    # Split the data string if so to retrieve the command and the arguments
                    data = data.split(" ")

                    # Check if an existing command was requested
                    if data[0] in self.commands:

                        # Execute a valid command
                        self.commands.get(data[0])(self, data)

                        # Inform that a command was executed
                        print("Command " + data[0] + " executed")

                    else:
                        # Inform the user that an invalid command was sent
                        self.send("Invalid command. Type !help to display available commands." + "\r\n")

            # Clean up
            self.client_socket.close()
            self.cache = {}

            # Inform that the connection is closed
            print("Connection from {} address closed successfully".format(self.client_ip))

    def send(self, data):
        self.client_socket.sendall(str.encode(data))

    @staticmethod
    def help(server, data):

        # Construct the help message's header
        message = "Here are the available commands:\r\n"

        # Construct the content
        for command in server.commands.keys():
            message = message + " - " + command + "\r\n"

        # Add further help info
        message = message + "To learn more about each command, type <command> help. " + "\r\n"
        message = message + "To add arguments to a command, type <command> <argument1> <argument2> (...)" + "\r\n"

        # Send the prepared message to the client
        server.send(message)


if __name__ == "__main__":
    s = Server()
    s.run()
