### Purpose

To run the server on boot.

### Instructions

1. Run the following command:

```
sudo nano /etc/rc.local
```

2. Add the following line to the file (before the default script which can print IP):

```
sudo python3.6 /home/pi/Desktop/SecurityPi/server.py & 2> /home/pi/Desktop/server_errors
```

Example file content:

```
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Run the server
sudo python3.6 /home/pi/Desktop/SecurityPi/server.py 2> /home/pi/Desktop/server_errors &

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
printf "My IP address is %s\n" "$_IP"
fi

exit 0
```

This should run the server infinitely as well as redirect all errors to the *server_errors* file on desktop.

### Source

https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/
