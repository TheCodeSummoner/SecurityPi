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

The service should now be accesible from a webbrowser via localhost/phpmyadmin (or ip/phpmyadmin where ip is PI's ip).

**TO BE CHECKED**

Should be enough to make the challenge work

sudo chmod  o+w /var/www/html should work
sudo nano /etc/phpmyadmin/confg.inc.something all lines with AllowNoPassword to TRUE

### Source

http://www.hackingarticles.in/shell-uploading-web-server-phpmyadmin/
