# ⚠️ ARPGuard — Python ARP Spoofing & Network Analysis Tool

ARPGuard is an educational cybersecurity project that demonstrates how ARP spoofing (ARP poisoning) works inside a local network using Python.

The project simulates a Man-in-the-Middle (MITM) attack in a controlled lab environment to help students understand ARP protocol vulnerabilities and network security concepts.

⚠ This tool is for educational and ethical testing purposes only.

---

## 📁 Project Structure

```
ARPGuard/
│
├── arp-spoof.py        # Main ARP spoofing script
└── README.md
```

---

## 🚀 Features

### ✅ ARP Spoofing (ARP Poisoning)
- Sends forged ARP replies
- Redirects traffic between victim and gateway
- Simulates MITM attack scenario

### ✅ Network Monitoring
- Uses Scapy for packet manipulation
- Sends continuous spoofed ARP packets
- Restores ARP tables after stopping attack

### ✅ Safe Exit Handling
- Automatically restores original ARP tables on Ctrl+C
- Prevents permanent network disruption

---

## 🧩 Technologies Used

- Python 3.x
- Scapy
- Socket Programming
- OS networking tools

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/arpguard.git
cd arpguard
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

⚠ Must be run with root/administrator privileges.

```bash
sudo python arp-spoof.py
```

You may need to specify:
- Victim IP
- Gateway IP
- Network interface

Example:

```bash
sudo python arp-spoof.py --target 192.168.1.10 --gateway 192.168.1.1
```

---

## 🔄 How It Works

1. The script sends fake ARP responses to the victim.
2. It tells the victim that the attacker’s MAC address belongs to the gateway.
3. It tells the gateway that the attacker’s MAC belongs to the victim.
4. Traffic flows through the attacker (MITM).
5. On exit, ARP tables are restored.

---

## 📚 What This Project Demonstrates

- ARP protocol behavior
- ARP cache poisoning
- Man-in-the-Middle attacks
- Network traffic interception
- Importance of secure protocols (HTTPS, TLS)
- Why ARP is insecure by design

---

## ⚠️ Legal Disclaimer

This tool is created for educational use in controlled lab environments only.

Do NOT use this tool on networks without explicit authorization.

The author is not responsible for any misuse.

---

## 🎓 Educational Purpose

This project helps students understand:

- Network layer vulnerabilities
- How MITM attacks work
- Why encrypted communication is critical
- How attackers exploit ARP weaknesses

---

## 📈 Possible Improvements

- Add packet sniffing module
- Add GUI interface
- Add detection mode (ARP spoofing detection)
- Add logging system
- Add multi-target support

---

## 👨‍💻 Author

Developed as part of cybersecurity studies.

Field: Network & Cyber Security

---

## 📄 License

MIT License

Educational use only.
