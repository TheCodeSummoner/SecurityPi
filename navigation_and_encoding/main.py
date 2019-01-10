from os import path
from navigation_and_encoding import emperor, ring_ring, feel_the_challenge, telegram, fibres

# Get the base challenge name
NAME = __name__.split(".")[0]

# Declare paths to the files
PATH = path.normpath(path.dirname(__file__))
WORD_LIST_PATH = path.join(PATH, "wordlist.txt")

# Declare dictionary with tasks
TASKS = {
    'emperor': emperor,
    'ring_ring': ring_ring,
    'feel_the_challenge': feel_the_challenge,
    'fibres': fibres,
    'telegram': telegram
}


def main(server, data):

    # Get the number of elements passed in the command
    switch = len(data)

    # If only the command was sent or the help argument was included
    if switch == 1 or (switch == 2 and data[1] == "help"):

        # Build the help message
        message = "!" + NAME + " emperor - start the emperor challenge" + "\r\n" + \
                  "!" + NAME + " emperor <answer> - checks the answer of the emperor challenge" + "\r\n" + \
                  "!" + NAME + " ring_ring - start the ring_ring challenge" + "\r\n" + \
                  "!" + NAME + " ring_ring <answer> - checks the answer of the ring_ring challenge" + "\r\n" + \
                  "!" + NAME + " feel_the_challenge - start the feel_the_challenge challenge" + "\r\n" + \
                  "!" + NAME + " feel_the_challenge <answer> - checks the answer of the feel_the_challenge challenge" \
                  + "\r\n" + \
                  "!" + NAME + " fibres - start the fibres challenge" + "\r\n" + \
                  "!" + NAME + " fibres <answer> - checks the answer of the fibres challenge" + "\r\n" + \
                  "!" + NAME + " telegram - start the telegram challenge" + "\r\n" + \
                  "!" + NAME + " telegram <answer> - checks the answer of the telegram challenge" + "\r\n"

    # If any non-help arguments were included
    elif switch == 2:

        # Check if the provided argument is included in implemented tasks, run the task if so
        if data[1] in TASKS:
            message = TASKS[data[1]].generate(server, NAME, WORD_LIST_PATH)

        # Inform the user about wrong input
        else:
            message = "Invalid task argument. Type !" + NAME + " help to learn about available challenges." + "\r\n"

    else:
        # Check if the provided argument is included in implemented tasks, check the answer if so
        if data[1] in TASKS:

            # Build an answer string
            answer = " ".join(arg for arg in data[2:])

            # Get the answer feedback
            message = TASKS[data[1]].check_answer(server, NAME, answer)

        # Inform the user about wrong input
        else:
            message = "Invalid task argument. Type !" + NAME + " help to learn about available challenges." + "\r\n"

    # Send the prepared message to the client
    server.send(message)
