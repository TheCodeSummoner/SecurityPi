from flask import Flask, request
from subprocess import getoutput
from os import path
from platform import system

# Declare paths to the files
PATH = path.normpath(path.dirname(__file__))

# Get the challenge name
NAME = __name__.split(".")[0]


def start_app():

    # Initialise a Flask application
    app = Flask('website')

    @app.route("/")
    def main_page():

        # Initialise a string to build for the main page
        message = "Welcome to PiPoetry. Click the links to read the poems: </br>"

        # Add a few links
        message += "<a href=/?path=" + path.join("poems", "clifford_morse") + ">Open Mic at the Sacred Grounds Cafe</a></br>"
        message += "<a href=/?path=" + path.join("poems", "fred_russcol") + ">Circular Reasoning</a></br>"
        message += "<a href=/?path=" + path.join("poems", "tom_wilson") + ">My Favorite Rhyme</a></br></br>"

        # Retrieve the content of the file using the path argument
        message += get_text(request.args['path']).replace("\n", "</br>") if 'path' in request.args else ""

        # Return the message so it can be printed to the screen
        return message

    # Run the website on localhost
    app.run(host="0.0.0.0")


def get_text(file):
    # Initialise the command to execute
    cmd = ""

    # Check what system is being used
    if system() == "Linux":
        # Add the corresponding Linux command
        cmd += "cat "
    else:
        # Add the corresponding Windows command
        cmd += "type "

    # Build the rest of the command
    cmd += path.join(PATH, file)

    # Inform what command was executed
    print(NAME + ": Executing following command: " + cmd)

    # Vulnerable to code injection command listing contents of a file
    return getoutput(cmd)