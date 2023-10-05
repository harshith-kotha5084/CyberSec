**1. NetCat:**
   Using this we can read and write data across the network, execute commands, pass files back and forth, and open a remote shell.
   The same netcat.py can act as both client and server as it includes functionalities for both listener and sender. We have to pass specific arguments to set up accordingly. The -c argument sets up an interactive shell, the -e argument executes one specific command, the -l argument indicates that a listener should be set up, the -p argument specifies the port on which to communicate, the -t argument specifies the target IP, and the -u argument specifies the name of a file to upload. Both the sender and receiver can use this program, so the arguments define whether it’s invoked to send or listen. The -c, -e, and -u arguments imply the -l argument, because those arguments apply to only the listener side of the communication. The sender side makes the connection to the listener, and so it needs only the -t and -p arguments to define the target listener.
   
   **Steps to run this:**
-    run 'python netcat.py --help' in the terminal to understand the arguments to be given.
-    On Kali Linux machine setup a listener using the command: 'python netcat.py -t 192.168.1.203 -p 5555 -l -c'
> The -l flag here specifies that it is a listener. 
-    On your Local machine setup a client: 'python netcat.py -t 192.168.1.203 -p 5555'
-    Press CTRL-D to stop the script reading from stdin and provide access to the console of the listener.
-    Type any commands you want in your client terminal which gets executed on the Listener. 

**2. TCP Proxy:**
Using this we can understand the various unknown protocols, modify traffic being sent to an application, and create test cases for fuzzers. The hex dump of the communication between a local and a remote machine will be displayed on the console. Using the _Request Handler_ and _Response Handler_ functions, we can modify the packet contents, perform fuzzing tasks, test for authentication issues, and do whatever our heart desires.
   
   **Steps to run this:**
-    First, we have to set our proxy using this command:
>    sudo python proxy.py ipaddress 21 ftp.sun.ac.za 21 True
-    This fires up an FTP server and sets up a proxy that listens to all connections coming to the specified _ipaddress_ via port 21. sudo because port 21 required administrative privileges.
-    In another terminal, we can start an FTP session to test this using:
>    ftp ipaddress
-    Here the '_ipaddress_' is the address of the machine where the proxy is running. This proxy acts as the intermediary middleman that reads and logs the hexdump of the communication between the client and the remote server.
-    After starting the session you have to provide username and password for authentication(given in the script).
-    Then we can see the communication happenning. 

**3. SSH with Paramiko:**
This task contains three files ssh_cmd.py, ssh_rcmd.py, and ssh_server.py. So here we look into how to run SSH using paramiko library. 

_ssh_cmd.py:_ This file, when run acts as a client that makes a connection to ssh server whose details are prompted at the console. Next, it takes in a single command that is sent to the server, executed and its output is then printed back onto the console of the client. 

_ssh_rcmd.py:_ This file, when run acts as a client that again makes a connection to the server like before, but instead of a single command, it runs multiple in a loop. the other difference is that it acts reverse here, instead of sending commands to the server, it receives from it and runs and sends back the output. 

_ssh_server.py:_ This file acts as an SSH server that takes a key ('test_rsa.key') for authentication purposes and also contains a username-password authentication facility. this first connects to the client machine, thereafter accepting an ssh session from the client for ssh communications. 

   **Steps to run this:**
-    First, open the Kali machine and start the server by running:
>    python ssh_server.py
-    Then in the Linux or on any machine run the client file:
>    python ssh_rcmd.py
-    Enter the username and password to log in to the ssh. these are specified inside the server file for authentication purposes.
-    Finally start giving commands from the server's side that run on the client's side and print output on the server's console again.

This directory also includes a file called _paramiko-main.zip_ which includes all the demo files and documentation of the paramiko library which we are going to use in the next section. 

**4. SSH Tunneling:**
In some machines like Windows, we cannot deploy SSH servers for various reasons. Now if we want to expose a service remotely that the system offers, but use SSH with Python, we have to run an SSH client on that Windows system and expose this service to a remote SSH server. This process is called reverse SSH Tunneling. 

   **Steps to run this:**
-    We start with running a web server on any system(here Kali). In this example, we used web.py for that job running it at a particular IP address and port.
-    This web server acts as a service that runs on the internal network of our machine where we cannot deploy an SSH server.
-    Now we start by running a Client on this machine, that exposes this service to a remote SSH server. we run:
>    python rforward.py 192.168.92.1 -p 8081 -r 192.168.92.128:3000 --user='harshith' --password
-    Now, we have to give the password of our ssh server, and this starts the session.
-    If we try to access that web server now, from our remote SSH server, we will be able to open a SSH tunnel and access it. 

The Link to detailed explanation of all these above tasks with outputs attached (google slides): https://docs.google.com/presentation/d/1LTp6GEMtEA-8xxXV11LsQUF29OmX6aBm2zxx_fGsoWE/edit?usp=sharing
