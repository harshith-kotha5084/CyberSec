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

This is a very simple code, we have to start the sniffing first and simultaneously send the email in order to capture it. More details in the ppt attached below. 

Or we can also test by logging into a server and sending credentials by plaintext wire. 

**2. ARP Cache Poisoning:**
ARP poisoning is one of the oldest yet most effective tricks in a hacker’s
toolkit. Quite simply, we will convince a target machine that we have become
its gateway, and we will also convince the gateway that in order to reach
the target machine, all traffic has to go through us. Every computer on a
network maintains an ARP cache that stores the most recent media access
control (MAC) addresses matching the IP addresses on the local network.
We’ll poison this cache with entries that we control to achieve this attack.

So in this, we have connected out Kali Linux(attack machine) to the same physical network as the victim machine(Ubuntu in this case). 
- First, we try to get the MAC details of the Gateway and other systems on the network using:
>  arp -a
- Then we tell the local host machine that we can forward packets along to both the gateway and the target IP address.
>  echo 1 > /proc/sys/net/ipv4/ip_forward
- The file _arper.py_ in this directory is used to launch the **ARP Poisoning Attack** on the victim Ubuntu machine by running:
>  python arper.py 192.168.0.118 192.168.0.1 eth0
- Here '_192.168.0.118_' is the IP address of the victim machine. '_192.168.0.1_' is the IP address of the gateway. '_eth0_' is the interface.

What happens here?
- First, the attack machine sends poisoned ARP packets to both the victim machine and the gateway.
- They belive it and change their Cache entries, with IPs remaining one another's but MAC changing to attack the machine's MAC.
- SO all the packets, though destined for each other between the Victim machine and Gateway, everything goes through the attack machine.
- We collect all the packet traces and store them in pcap files for further inspection.(in arper.pcap files here)

