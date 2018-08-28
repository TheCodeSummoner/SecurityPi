## Solution

#### Shell exploit

You can use a web browser to access all the services. The *phpMyAdmin* login site is at *ip/phpmyadmin* (where *ip* is PI's ip) and can be further accessed via the root login with default credentials (login *root* with no password). Despite user restrictions, it is possible to inject a malicious file using a SQL command, because the folder with website files (*/var/www/html*) has read/write permissions set for all users.

#### Correct command

Correct SQL command is present in the *correct_query* file. After executing it, the file content can be viewed at *ip/backdoor.php* (where *ip* is PI's ip).

## Conclusion

Never leave software on default credentials as it always creates a serious security threat. Avoid giving extensive permissions to folders that can be accessed from outside your system, especially to all possible users. Instead, create a user with needed permissions and give him the access to any required software.
