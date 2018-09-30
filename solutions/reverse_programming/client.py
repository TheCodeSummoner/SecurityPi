import socket
from solutions.reverse_programming.decrypt import decrypt


class Client:

    def __init__(self, *, ip='localhost', port=50000):

        # Save the ip and port information
        self.ip = ip
        self.port = port

        # Initialise the socket for IPv4 addresses (hence AF_INET) and TCP (hence SOCK_STREAM)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Initialise the list of commands to send
        self.commands = ["!reverse_programming"]

    def run(self):

        # Connect to the server
        self.socket.connect((self.ip, self.port))

        # Remove blocking from the socket
        self.socket.setblocking(0)

        # Set the timeout to ensure non-blocking socket works
        self.socket.settimeout(0.1)

        # Initialise the index iterator
        index = 0

        while True:

            try:
                # Once connected, keep receiving the data, remove the whitespaces
                data = self.socket.recv(2048).strip()

            except socket.timeout:
                # In case there was no data to be received, assign None to the data variable
                data = None

            # If there was any data received
            if data:

                # Convert bytes to string
                data = data.decode("utf-8")

                # Inform what data was received
                print("Received: " + data)

                # Check if encrypted message was received:
                if "Here is the encrypted message: " in data:

                    # Retrieve the data
                    data = data[31:]

                    # Convert string of bytes to bytes
                    data = bytes(data[2:-1], encoding="utf-8")

                    # Decrypt the data
                    data = decrypt(data)

                    # Add the command
                    data = "!reverse_programming " + data

                    # Inform what data will be sent next
                    print("Sending answer: " + data.strip())

                    # Send the answer
                    self.socket.sendall(str.encode(data))

                # Quit if a correct or incorrect message was received
                elif "Correct!" in data or "Incorrect!" in data:
                    break

            # Stop sending messages if the iterator can't be increased more (no more commands to send)
            if index != len(self.commands):

                # Get next command to send
                data = self.commands[index]

                # Inform what data will be sent next
                print("Current command: " + data)

                # Send the data to the server
                self.socket.sendall(str.encode(data))

                # Increment the iterator
                index += 1


if __name__ == "__main__":
    c = Client()  # Set the ip for non-localhost connections
    c.run()
