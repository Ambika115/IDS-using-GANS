from scapy.all import sniff

packets_data = []

def capture_packet(packet):
    packet_bytes = bytes(packet)
    packet_size = len(packet_bytes)

    packets_data.append({
        "packet_size_bytes": packet_size,
        "packet_size_bits": packet_size * 8
    })

def start_capture():
    sniff(prn=capture_packet, count=50)

    return packets_data