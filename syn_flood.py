import sys
from scapy.all import *

print("Field Values of packet sent")
# Create malformed packet
p=IP(dst=sys.argv[1],id=1111,ttl=99)/TCP(sport=RandShort(),dport=80,seq=12345,ack=1000,window=1000,flags="S")
ls(p)
print("Sending Packets in 0.3 second intervals for timeout of 4 sec")
ans,unans=srloop(p,inter=0.3,retry=2,timeout=4)
print("Summary of answered & unanswered packets")
ans.summary()
print("----------------------------------------")
print("Summary of answered & unanswered packets")
unans.summary()
print("source port flags in response")
for s,r in ans:
    print(r.sprintf("%TCP.sport% \t %TCP.flags%"))


