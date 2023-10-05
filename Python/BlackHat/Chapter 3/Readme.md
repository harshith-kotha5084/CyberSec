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

For detailed explanation: https://docs.google.com/presentation/d/18s7v-rdSYV9tud04ALG4U6gPTv4z_sU2c9xrEqCLPQQ/edit?usp=sharing
