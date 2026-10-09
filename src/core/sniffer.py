from scapy.all import sniff
from concurrent.futures import ThreadPoolExecutor
from src.core.dissector import ProtocolDissector
from src.utils.logger import logger

class AsyncSniffer:
    """Asynchronous network sniffer utilizing ThreadPoolExecutor for high-throughput packet processing."""
    
    def __init__(self, max_workers: int = 4):
        self.executor = ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix="PacketWorker")
        
    def _dispatch_packet(self, packet):
        self.executor.submit(ProtocolDissector.inspect, packet)
        
    def start_offline_capture(self, pcap_file: str):
        logger.info(f"Initializing offline capture verification on {pcap_file}")
        sniff(offline=pcap_file, prn=self._dispatch_packet, store=0)
        self.executor.shutdown(wait=True)
        logger.info("Offline capture session terminated successfully. ThreadPool shut down.")
        
    def start_live_capture(self, interface: str, packet_count: int = 100):
        logger.info(f"Initializing live capture on interface {interface} (Count: {packet_count})")
        sniff(iface=interface, count=packet_count, prn=self._dispatch_packet, store=0)
        self.executor.shutdown(wait=True)
        logger.info("Live capture session terminated successfully. ThreadPool shut down.")
