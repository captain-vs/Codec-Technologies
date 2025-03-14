from scapy.all import *
from scapy.layers.http import HTTPRequest  # import HTTP packet
import threading

# Global flag to indicate if any packets were captured
packets_captured = False


def monitor_packet(packet):
    global packets_captured
    # Check if the packet has HTTP layer
    if packet.haslayer(HTTPRequest):
        packets_captured = True
        http_layer = packet[HTTPRequest]
        http_host = http_layer.Host.decode() if http_layer.Host else "Unknown"
        http_path = http_layer.Path.decode() if http_layer.Path else ""
        http_method = http_layer.Method.decode() if http_layer.Method else "Unknown"

        print(f"HTTP Request: {http_method} {http_host}{http_path}")

        if packet.haslayer(Raw):
            print(f"Payload: {packet[Raw].load}")


def stop_sniffing():
    if not packets_captured:
        print("No HTTP traffic detected.")
    # Stop sniffing after a timeout
    raise SystemExit


def start_monitoring():
    # Start a timer to stop sniffing after 30 seconds
    timer = threading.Timer(30, stop_sniffing)
    timer.start()

    # Sniff HTTP packets
    sniff(filter="tcp port 80", prn=monitor_packet, store=0)


if __name__ == "__main__":
    print("Starting HTTP Traffic Monitor...")
    start_monitoring()
