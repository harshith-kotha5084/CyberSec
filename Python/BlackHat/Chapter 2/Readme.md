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
>    sudo python proxy.py <ipaddress> 21 ftp.sun.ac.za 21 True
-    This fires up an FTP server and sets up a proxy that listens to all connections coming to the specified _ipaddress_ via port 21. sudo because port 21 required administrative privileges.
-    In another terminal, we can start an FTP session to test this using:
>    ftp <ipaddress>
-    Here the '_ipaddress_' is the address of the machine where the proxy is running. This proxy acts as the intermediary middleman that reads and logs the hexdump of the communication between the client and the remote server.
-    After starting the session you have to provide username and password for authentication(given in the script).
-    Then we can see the communication happenning. 
