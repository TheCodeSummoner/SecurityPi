### Purpose

To install and setup the software needed for the *phpmyadmin* challenge.

### Instructions

1. Run following command (agree to everything):

```
sudo apt-get install apache2 mariadb-server-10.1 php -y
```

2. Run following command (agree to everything), choose Apache2, put no password for the database (select *yes* twice):

```
sudo apt-get install phpmyadmin -y
```

3. Run following command:

```
sudo nano /etc/apache2/apache2.conf
```

4. In the config file, add the following line to the end of the file:

```
Include /etc/phpmyadmin/apache.conf
```

5. Run following command:

```
sudo service apache2 restart
```

The service should now be accesible from a web browser via localhost/phpmyadmin (or ip/phpmyadmin where ip is PI's ip).

6. Run following command:

```
sudo chmod  o+w /var/www/html
```

7. Run following command:

```
sudo nano /etc/phpmyadmin/config.inc.php
```

8. In the config file, uncomment all lines with `AllowNoPassword`

9. Run following command:

```
sudo mysql --user=root myqsl
```

10. Within the mysql terminal, run following block of commands:

```
CREATE USER 'admin'@'localhost' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

### Sources

http://www.hackingarticles.in/shell-uploading-web-server-phpmyadmin/

https://askubuntu.com/questions/763336/cannot-enter-phpmyadmin-as-root-mysql-5-7
