from scapy.all import sniff
from scapy.layers.inet import TCP

def packet_callback(packet):
	if packet.haslayer(TCP) and packet[TCP].payload:
		mypacket = str(packet[TCP].payload.load)
		if 'user' in mypacket.lower() or 'pass' in mypacket.lower():
			print(f"[*] Destination: {packet.dst}")
			print(f"[*] {mypacket}")

def main():
	sniff(filter='tcp port 25', iface='lo', prn=packet_callback, store=0)

if __name__ == '__main__':
	main()