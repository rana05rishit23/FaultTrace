import argparse
from src.core.sniffer import AsyncSniffer
from src.utils.logger import logger

def main():
    parser = argparse.ArgumentParser(description="FaultTrace: Automated Protocol Verification & Triage Suite")
    parser.add_argument("--mode", choices=["live", "offline"], required=True, help="Capture mode")
    parser.add_argument("--target", required=True, help="Interface name for live, PCAP path for offline")
    parser.add_argument("--workers", type=int, default=4, help="Number of parallel processing workers")
    parser.add_argument("--count", type=int, default=50, help="Number of packets for live capture")
    
    args = parser.parse_args()
    
    logger.info(f"Starting FaultTrace Engine with {args.workers} workers...")
    sniffer_engine = AsyncSniffer(max_workers=args.workers)
    
    if args.mode == 'offline':
        sniffer_engine.start_offline_capture(args.target)
    else:
        sniffer_engine.start_live_capture(args.target, args.count)

if __name__ == "__main__":
    main()
