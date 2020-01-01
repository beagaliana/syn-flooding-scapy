from scapy.all import *
from scapy.layers.http import HTTPRequest

def sniff_packet(packet):
    if(packet.haslayer(TCP)):
        print(packet.show())


def main():
     print("Sniffing TCP Packets...")
     sniff(filter="ip", iface="wlp1s0", prn=sniff_packet)
        

if __name__=='__main__':
    main()
