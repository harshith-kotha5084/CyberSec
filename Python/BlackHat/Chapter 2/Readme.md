**1. NetCat:**
   Using this we can read and write data across the network, execute commands, pass files back and forth, and open a remote shell.
   The same netcat.py can act as both client and server as it includes functionalities for both listener and sender. We have to pass specific arguments to set up accordingly. The -c argument sets up an interactive shell, the -e argument executes one specific command, the -l argument indicates that a listener should be set up, the -p argument specifies the port on which to communicate, the -t argument specifies the target IP, and the -u argument specifies the name of a file to upload. Both the sender and receiver can use this program, so the arguments define whether it’s invoked to send or listen. The -c, -e, and -u arguments imply the -l argument, because those arguments apply to only the listener side of the communication. The sender side makes the connection to the listener, and so it needs only the -t and -p arguments to define the target listener.
   
   **Steps to run this:**
-    run 'python netcat.py --help' in the terminal to understand the arguments to be given. 
-  
