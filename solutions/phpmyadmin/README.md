## Solution

#### Logging in

You can use a web browser to access all the services. The *phpMyAdmin* login site is at *ip/phpmyadmin* (where *ip* is PI's ip) and can be further accessed after logging in as an admin (login *admin* with no password).

#### Shell exploit

Despite user restrictions, it is possible to inject a malicious file using a SQL command, because the folder with website files (*/var/www/html*) has read/write permissions set for all users. The file itself should contain a PHP script that calls shell and prints the output.

#### Correct command

Correct SQL command is present in the *correct_command* file. After executing it, the file content can be viewed at *ip/backdoor.php* (where *ip* is PI's ip).

## Conclusion

Never leave software on default credentials as it always creates a serious security threat. Avoid giving extensive permissions to folders that can be accessed from outside your system, especially to all possible users. Instead, create a user with needed permissions and give him the access to any required software.
