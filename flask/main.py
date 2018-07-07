from flask import Flask, url_for, json, request
from os import path
from subprocess import getoutput


PATH = path.dirname(__file__)
app = Flask(__name__)

# will need a check for system type, touch, rm not in windows ;(((
# TODO: Organise everything, add content, add click-able links, add text/photos, add a file with flag
# TODO: Make tasks - 1. view content of flag file, 2. change content of flag file

def get_photos(path):
    return getoutput("dir " + path)
    # return list of all photos in given directory - this will be vulnerable to code injection / directories browsing

@app.route("/")
def main_page():
    text = "Welcome to PiPhotography (PP)! Albums:"
    return text + get_photos(request.args['path']) if 'path' in request.args else "Put path in"

app.run()
'''
from flask import Flask, url_for, json, request
from pyDes import des
from subprocess import getstatusoutput

# Why import whole pyDes again? Just use from again like before, or don't use from at all
import pyDes

# According to flask documentation app = Flask(__name__.split('.')[0]) is better for debuggin purposes
app = Flask(__name__)

# Should be in a separate file
RANDOM_KEY = "085ZMVsBnTYu060K7gfJpGXeik5VZamC"
# Breaks on windows, use os (path, getcwd etc.) instead (slashes)
# tmp folder will contain other items not related to the program
SECURE_DIRECTORY = '/tmp/'

def secure_store(filename, suffix, data):
    #IVs should be generated by a cryptographically-secure random number generator - another hardcoded issue (?)
    IV = b"\0\0\0\0\0\0\0\0"
    d = des(RANDOM_KEY[0:8], pyDes.ECB, IV, pad=None, padmode=pyDes.PAD_PKCS5)
    f = open(SECURE_DIRECTORY + '/' + filename + '-' + suffix, 'w')
    f.write(d.encrypt(bytes(data)))
    f.close()
    return 'data stored'

# if path is .. or similar it goes before /tmp/, = bad, ex. /employee?cmd=list&ssn="../root"
# also can inject commands ex. /employee?cmd=list&ssn= ; cd ../root/Desktop ; rm ciao
def list_secure_data(path): return commands.getstatusoutput('ls ' + SECURE_DIRECTORY + '/' + path)[1]

@app.route('/')
def api_root(): return 'Welcome to employee data storage api'

@app.route('/employee')
def api_emplyee():
    # Using ssn (social security number) + email with the addition of vulnerable directories is a catastrophy
    s = {"list": lambda: list_secure_data(request.args['ssn']),
         "add": lambda: secure_store(request.args['ssn'], request.args['email'],
         request.args['data'])}
    return s.get(request.args['cmd'], lambda: "no such command")()

if __name__ == '__main__': app.run()'''