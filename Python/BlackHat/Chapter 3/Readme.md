This chapter is about sniffing the packets using raw sockets to understand the underlying low-level networking bits work. 

**1. Simple Sniffer:**
First we start with building a very simple UDP Host Discovery Tool, that just takes in a single packet, prints and quits. 
But this only uses Raw Sockets. 

Supported in both _Windows_ and _Linux_. 
  **Things To Highlight here:**
-   This completely works on Raw Sockets. we first create a Raw Socket based on Windows or Linux.
-   In Linux, the socket_protocol to be specified particularly as ICMP, TCP or UDP.
-   Whereas in Windows(can be determined using _os.name == 'nt'_), all IP packets can be sniffed.
-   We then bind to the host that we like to sniff on.
>   sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
-   This should be specified to include IP Header in the capture while working with RAW sockets. (IP not included by default)
-   On Promiscous mode: to get admin privileges in Windows:
>   sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
-   Again switch it off when work done:
>   sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

The additional step of sending an IOCTL to the network card driver to enable promiscuous mode. If you’re running Windows in a virtual machine, you will likely get a notification that the guest operating system is enabling promiscuous mode

To test, just run the code normally
> sudo python3 sniffer.py

**2. Sniff and Decode IP Layer:**
In the previous code, we just sniffed a single packet and when printed: there was a binary that appeared!
Now here we actually get an IP Header by Binary manipulation. Details on how we do it is mentioned in the slides attached. 
This code actually keeps running and takes every packet through that host, and extracts its IP Header into a readable form. Prints the details required to understand the packets.

We can directly run the code, if Linux, you can check this by just pinging google.com through the host you specified. 
> sudo python3 sniffer_ip_header_decode.py

For Windows: Run the code and observe all types of packets: ICMP, UDP, and TCP start appearing. Whereas in Linux, we can only see ICMP packets as we have to specifically search for other packets, else it only reads the ICMP packets. But now we are building a scanner.

**3. Decode ICMP:**
Decode the ICMP responses that our scanner will elicit from
sending UDP datagrams to closed ports. ICMP messages can vary greatly in
their contents, but each message contains three elements that stay consistent: the type, code, and checksum fields. The type and code fields tell the
receiving host what type of ICMP message is arriving, which then dictates
how to decode it properly.
For the purpose of our scanner, we are looking for a type value of 3 and
a code value of 3. This corresponds to the Destination Unreachable class of
ICMP messages and the code value of 3 indicates that the Port Unreachable
error has been caused.

This is an additional step further to the previous code that actually extracts the ICMP details as well which will help us write our scanner for hosts in the next section.

> sudo python3 sniffer_with_icmp
To test this, simply start pinging through another terminal.

**4. Scanner:**
Now this get's interesting as we actually use the '_ipaddress_' module to work with subnets and other details of IPv4 network. We start by sending UDP datagrams all over the subnet and wait for the ICMP packets that come back which say error and unreachable indicating there is an active host on the other side. 

> sudo python3 scanner.py
we will be able to get all the active hosts that are present on the network local to our system(the address we mentioned in the code). 

For a detailed explanation: https://docs.google.com/presentation/d/18s7v-rdSYV9tud04ALG4U6gPTv4z_sU2c9xrEqCLPQQ/edit?usp=sharing
