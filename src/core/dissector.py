from scapy.all import Packet
from src.utils.logger import logger

class ProtocolDissector:
    """Handles deep packet inspection and protocol decoding."""
    
    @staticmethod
    def inspect(packet: Packet) -> None:
        try:
            if packet.haslayer('Dot11'):
                ProtocolDissector._handle_dot11(packet)
            elif packet.haslayer('IP'):
                ProtocolDissector._handle_ip(packet)
        except Exception as e:
            logger.error(f"Failed to dissect packet: {str(e)}", exc_info=True)

    @staticmethod
    def _handle_dot11(packet: Packet) -> None:
        logger.info(f"[802.11 Frame] {packet.summary()}")

    @staticmethod
    def _handle_ip(packet: Packet) -> None:
        ip_layer = packet.getlayer('IP')
        logger.info(f"[IP Traffic] Proto: {ip_layer.proto} | {ip_layer.src} -> {ip_layer.dst}")
