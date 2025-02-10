# packet_sniffer.py
import scapy.all as scapy

def packet_callback(packet):
    print(packet.show())

def start_sniffing(interface):
    print(f"Starting packet sniffing on {interface}...")
    scapy.sniff(iface=interface, prn=packet_callback, store=False)

if __name__ == "__main__":
    interface = input("Enter the network interface to sniff on (e.g., eth0, wlan0): ")
    start_sniffing(interface)
