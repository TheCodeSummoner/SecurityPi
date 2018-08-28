From https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/

1. Run 'sudo nano /etc/rc.local'
2. Edit the file - add 'sudo python /home/pi(...)/server.py &' (or python3.6 if python2.7 is default)

Notes:

"If your program runs continuously (runs an infinite loop) or is likely not to exit, you must be sure to
fork the process by adding an ampersand ("&") to the end of the command."