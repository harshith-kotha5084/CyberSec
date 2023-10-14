In this chapter, we attack web applications. In most modern networks, web applications present the largest attack
surface and therefore are also the most common
avenue for gaining access to the web applications
themselves.

we’ll look at three scenarios for attacking a web app. 

In
the first scenario, you know the web framework that the target uses, and that
framework happens to be open source. A web app framework contains many
files and directories within directories within directories. We’ll create a map
that shows the hierarchy of the web app locally and use that information to
locate the real files and directories on the live target.

In the second scenario, you know only the URL for your target, so we’ll
resort to brute-forcing the same kind of mapping by using a word list to
generate a list of filepaths and directory names that may be present on the
target. We’ll then attempt to connect to the resulting list of possible paths
against a live target.

In the third scenario, you know the base URL of your target and its login
page. We’ll examine the login page and use a word list to brute-force a login.

We gain knowledge on how to use the Web Libraries to interact with Web services. 
In this, we look into the following:
- **_urlib:_** You can request the web application for a GET request or POST request. To test this you can run the urllib_test.py
- **_requests:_** The requests library is useful because it can automatically handle cookies for you. It is a very important tool. run the requests_test.py
- **_lxml & BeautifulSoup:_** These libraries help you parse the contents you get in your response from the web apps. Run the 'lxml_test.py' and 'beautifulsoup_test.py' for testing these libraries.

Note: All the above files include the variable URL which you have to edit based on the web application you are trying to use here. 

**1. Mapping Open Source Web App Installations:** 
In this we try to find out the files and directory structures of an open source web application which we downloaded locally in our kali machine. We do this to store all the structure that can be helpful to hunt for files in real target that uses this framework. 

The file in this directory 'wordpress.zip' is the WordPress Framework that you can download and unzip on your local machine for this task. 

So I have created a site locally on my machine to test this code using the apache2 web server and WordPress framework. This can be accessed using the link 'http://localhost/' 

To run this:
First, keep the web application running(details at the end of this file). Then from a terminal run the command:
> python mapper.py

At last, we try to store all the paths we got by running through the web application are stored inside the file 'myanswers.txt'

**2. Brute-Forcing Directories and File Locations:**
In this case, we do not have all the knowledge we had previously in the section 1. While attacking a custom web application or large e-commerce system, you often won’t be aware of all the files accessible on the web server. So only way to know all the required information is to brute-force.

In a lot of cases, you’ll want to get ahold of configuration
files, leftover development files, debugging scripts, and other security breadcrumbs that can provide sensitive information or expose functionality that
the software developer did not intend.

We’ll build a simple tool that will accept word lists from common brute
forcers, such as the Gobuster project (https://github.com/OJ/gobuster/) and
SVNDigger (https://www.netsparker.com/blog/web-security/svn-digger-better-lists
-for-forced-browsing/), and attempt to discover directories and files that are
reachable on the target web server

The file in this directory 'SVNDigger.zip' has another file inside namely 'all.txt' which has so many common words that can be used for the brute-force task. (you can change the path of this file inside the bruter.py file)

OWASP has a list of vulnerable web applications, both online and offline,
such as virtual machines and disk images, that you can test your tooling
against. In this case, _the URL referenced in the source code(bruter.py)_ points to an
intentionally buggy web application hosted by Acunetix.

To run this and display all the responses:
> python bruter.py

If you want to see only the successes and completely ignore the errors, we redirect all the stderr _/dev/null_
> python bruter.py 2> /dev/null

This displays only the successes

**3. Brute-Forcing HTML Form Authentication:**
Till now, we have seen how to work with files and directory structures of a web application where we know the framework already and also where we know nothing except the URL.

In this section, we know the URL to the login page of the web application. we try bruteforce passwords with a known username. 

We’ll create a simple brute-forcer that will be useful against WordPress,
a popular content management system. Modern WordPress systems include
some basic anti-brute-force techniques but still lack account lockouts or
strong captchas by default.
In order to brute-force WordPress, our tool needs to meet two requirements: it must retrieve the hidden token from the login form before submitting the password attempt, and it must ensure that we accept cookies in our
HTTP session.

1. Retrieve the login page and accept all cookies that are returned.
2. Parse out all of the form elements from the HTML.
3. Set the username and/or password to a guess from our dictionary.
4. Send an HTTP POST to the login processing script, including all
HTML form fields and our stored cookies.
5. Test to see if we have successfully logged in to the web application.

We first setup the web application locally using the WordPress framework and we run the file 'wordpress_killer.py' which takes in the URL of login page and brute forces the HTML form with passwords.

**SETTING UP THE WEB APPLICATION:**
1. Install some packages:
> sudo apt update
> sudo apt install apache2
2. Install an sql server:
> sudo apt install mariadb-server
3. configure the SQL:
> sudo mysql_secure_installation
> sudo mysql -u root -p
4. Create a database:
> CREATE DATABASE wordpressdb;
> GRANT ALL PRIVILEGES ON wordpressdb.* TO 'wordpressuser'@'localhost' IDENTIFIED BY 'your_password';
> FLUSH PRIVILEGES;
> EXIT;
5. Download and install the WordPress:
> cd /tmp
> wget https://wordpress.org/latest.tar.gz
> tar -zxvf latest.tar.gz
6. Move this Wordpress to apache document root directory:
> sudo mv wordpress/* /var/www/html/
7. Configure WordPress:
> sudo mv /var/www/html/wp-config-sample.php /var/www/html/wp-config.php
> sudo nano /var/www/html/wp-config.php
then find these lines and replace with you names:
> define('DB_NAME', 'wordpressdb');
> define('DB_USER', 'wordpressuser');
> define('DB_PASSWORD', 'your_password');
8. Set the required permissions:
> sudo chown -R www-data:www-data /var/www/html/
> sudo chmod -R 755 /var/www/html/
9. Enable Apache modules:
> sudo a2enmod rewrite
> sudo systemctl restart apache2
10. Keep the sql server running:
> sudo systemctl status mysql
> sudo systemctl start mysql

Finally you can open the link 'http://localhost/' on your browser to see the Web Application running. 
