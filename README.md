# Network Scanner

## Overview
This Python-based network scanner allows you to scan your local network to identify connected devices, their IP addresses, MAC addresses, device names, and vendors. It utilizes ARP requests to map the network and provides options to save the results in various formats (JSON, XML, or plain text). Additionally, it includes a packet sniffer, a port scanner, and a ping based scanner to find every device on the network.

## Requirements

- Python 3.x
- The following Python libraries:
  - `tkinter`
  - `requests`
  - `scapy`
  - `dicttoxml`
  - `json`
  - `threading`
  - `datetime`
  - `socket`
  - `subprocess`

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/mitzCanCode/netscan.git
    ```

2. Install the required Python libraries:

    ```sh
    pip install scapy requests dicttoxml
    ```

### Setting up a venv
```bash
python3 -m venv venv
source venv/bin/activate # On windows: venv\Scripts\Activate
```

### Installing Dependencies
```bash
pip install -r requirements.txt
```

### Create .env file
```bash
mv dotenv.template .env
vim .env # or any editor of your choice, do it with notepad idrc.
```
and fill in your macvendors.com API key


## Usage

### How to run CLI
```bash
cd CLI
sudo python3 netscan.py
```

### How to run GUI
```bash
cd GUI
sudo python3 app.py
```
## GUI Usage

### Network Scan

1. Open the application.
2. Navigate to the "Network Scan" tab.
3. Click the "Scan network" button to start scanning.
4. Optionally, you can save the scan results by selecting the "Save Scan Results" checkbox and choosing a file format (JSON, XML, TXT).

### Port Scan

1. Double-click on a device in the network scan results to view detailed information.
2. In the details window, click the "Run Port Scan" button to scan for open ports on the selected device.

### Packet Sniffer

1. Navigate to the "Packet Sniffer" tab.
2. Select a network interface from the dropdown menu.
3. Click "Start Sniffing" to begin capturing packets on the selected interface.
4. Click "Stop Sniffing" to stop packet capture.

### Note
To run the script you must first set an API key at the function api_lookup in the scanner.py file. You can get an API key by creating an account on https://macvendors.com

## Acknowledgements

- The `scapy` library is used for packet manipulation and network scanning.
- The `requests` library is used for making API calls to retrieve device vendor information.


## Capabilities 
This script includes functions to:
- Network Scanning: Scan the local network using ARP requests.
- Vendor Lookup: Lookup device vendor information via an API.
- Save Results: Save scan results in different formats (JSON, XML, TXT).
- Packet Sniffing: Sniff packets on the network.
- Ping Scan: Scan by pinging each device on the network.
- Port Scanning: Scan for open ports on devices in the network.
- OS Detect: Detect the potential OS of a host

## Contribution
Contributions are welcome! Please feel free to submit a Pull Request.

## Contact
For any inquiries or issues, please open an issue on the [GitHub repository](https://github.com/mitzCanCode/netscan).

---

Enjoy scanning your network!

---

**Disclaimer**: This tool is for educational purposes only. Use it responsibly and ensure you have permission to scan the network you are using.


