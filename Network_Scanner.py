import scapy.all as scapy
from scapy.layers.l2 import ARP, Ether
import optparse

# 1) arp request
# 2) broadcast
# 3) response

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ipaddress", dest="ip_address", help="Enter IP Address")

    (user_input, arguments) = parse_object.parse_args()

    if not user_input.ip_address:
        print("Enter IP Address")

    return user_input

def scan_network(ip):
    arp_request_packet = ARP(pdst=ip)
    # scapy.ls(ARP())
    broadcast_packet = Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(Ether())
    combined_packet = broadcast_packet/arp_request_packet  # 2 packet in 1, combine two packets
    (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
    answered_list.summary()

user_ip_address = get_user_input()
scan_network(user_ip_address.ip_address)
