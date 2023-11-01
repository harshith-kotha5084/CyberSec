**1. Encrypt and Decrypt:**
we encrypt all the information we want to exfiltrate using the pycryptodomex package. we use both symmetric encryption(uses one key for encrypting and decrypting which is a simple process and efficient but less secure) and asymmetric encryption which uses both private and public keys for encryption, though a complicated, very secure method. 

First, we run the _cryptor.py_ file  with _generate()_ in the main while other commented. this generates the keys we need for encryption and decryption of the session key that is used to encrypt the information we need. The keys are then saved in separate files as observed in this directory: _key.pri and key.pub_

Then we run the file commenting out _generate()_ and call the functions we need for our tasks.

**2. Email Exfiltration:**
run the file _email_exfil.py_ by changing the required columns inside the code by specifying you login details or the email you want to send this info to. for Windows use the outlook function for this job. 

you will be able to exfiltrate the contents of whatever you want by extending this code. 

**3. File Transfer Exfiltration:**

we have to set up an FTP server in our virtual machine or wherever possible and supply the IP address of that server in this _transmit_exfil.py_ file. and run the file. 

For Windows-specific function _transmit_: we have to open socket connections and transmit the file using the win32 library. 

**4. webserver:** 

Go to the website https://pastebin.com/ and create an account. note the login details along with the api_dev_key. 

specify those inside the file _paste_exfil.py_ and run it. Also, edit the main section where you have to specify the contents you want to exfiltrate. now run the file as usual. 

you can log into in the Pastebin website and find the pasted file which you can decrypt later. 
For Windows: you make use of the Internet Explorer COM object to navigate, change the HTML code and paste whatever you want. 

link to slides: https://docs.google.com/presentation/d/1GMfplMfh1MtG91CiFoDOhsszuxgW_bYcuor-H8bvqRs/edit?usp=sharing

The last file _exfil.py_ puts everything together so you can use any methods based on your need and convenience.
