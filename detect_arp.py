#!/usr/bin/python

import scapy.all as scapy
import time
import os

def get_arp_table():
    # La tabla ARP del sistema
    arp_table = os.popen('arp -a').read()
    return arp_table

def parse_arp_table(arp_table):
    # Parsea la tabla ARP en un diccionario
    arp_dict = {}
    lines = arp_table.split('\n')
    for line in lines:
        if 'at' in line:
            parts = line.split()
            ip = parts[1].strip('()')
            mac = parts[3]
            arp_dict[ip] = mac
    return arp_dict

def detect_arp_spoofing(previous_arp, current_arp):
    for ip, mac in current_arp.items():
        if ip in previous_arp and previous_arp[ip] != mac:
            print(f"[ALERTA] Posible ataque ARP spoofing detectado: {ip} cambió de {previous_arp[ip]} a {mac}")

def main():
    print("Monitoreando la tabla ARP en busca de cambios sospechosos...")
    previous_arp = parse_arp_table(get_arp_table())
    
    try:
        while True:
            time.sleep(5)  # Espera 5 segundos antes de volver a comprobar
            current_arp = parse_arp_table(get_arp_table())
            detect_arp_spoofing(previous_arp, current_arp)
            previous_arp = current_arp
    except KeyboardInterrupt:
        print("\n[!] Proceso detenido.")
        exit(0)

if _name_ == "_main_":
    main()
