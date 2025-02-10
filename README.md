# Packet Sniffer

A simple Python-based packet sniffer that captures and displays network packets in real-time using the `scapy` library.

## Features
- Captures network packets from the specified interface.
- Displays packet details like headers and data.
- Easy to use and extend.

## Prerequisites
- Python 3.x
- `scapy` library (can be installed via pip)

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/packet-sniffer.git
    cd packet-sniffer
    ```

2. Install the required dependencies:
    ```bash
    pip install scapy
    ```

## Usage

1. Run the script by executing the following command:
    ```bash
    python packet_sniffer.py
    ```

2. Enter the network interface you want to sniff on (e.g., `eth0`, `wlan0`).

3. The packet sniffer will start capturing and displaying network packets in real-time.

## Example

```bash
Enter the network interface to sniff on (e.g., eth0, wlan0): wlan0
Starting packet sniffing on wlan0...
