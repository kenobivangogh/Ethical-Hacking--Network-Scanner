import scapy.all as scapy
from scapy.layers.l2 import ARP, Ether

# 1) arp request
# 2) broadcast
# 3) response

arp_request_packet = ARP(pdst="10.0.2.1/24")
# scapy.ls(ARP())
broadcast_packet = Ether(dst="ff:ff:ff:ff:ff:ff")
# scapy.ls(Ether())
combined_packet = broadcast_packet/arp_request_packet  # 2 packet in 1, combine two packets
# result = scapy.srp(combined_packet, timeout=1)
# print(result)

(answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
# print(list(answered_list))
answered_list.summary()
