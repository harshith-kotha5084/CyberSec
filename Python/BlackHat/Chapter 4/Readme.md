In this Chapter we experiment with Scapy.

**1. Stealing Email Credentials:**
We’ll build a very simple sniffer to capture Simple
Mail Transport Protocol (SMTP), Post Office Protocol (POP3), and Internet
Message Access Protocol (IMAP) credentials. Later, by coupling the sniffer
with the Address Resolution Protocol (ARP) poisoning man-in-the-middle
(MITM) attack, we can easily steal credentials from other machines on the
network. 

So the file _mail_sniffer.py_ has a small little code to sniff the packets using scapy and a filter ='tcp port 110 or tcp port 25 or tcp port 143' that alows us only to sniff plaintext emails. 

To test this code, I have deployed an SMTP server using Postfix. and using the code _testmail.py_ I have sent some email containing the user and pass in its body to the SMTP server using the _smtp_port 25_. 

This is a very simple code, we have to start the sniffing first and simultaneously send the email indorder to capture it. More details in the ppt attached below. 

**2. **
