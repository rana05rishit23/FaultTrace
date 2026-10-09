import logging
import sys

def setup_logger(log_file: str = "network_triage.log", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger("FaultTrace")
    logger.setLevel(level)
    
    if logger.hasHandlers():
        logger.handlers.clear()
        
    formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | [%(threadName)s] %(module)s:%(funcName)s | %(message)s')
    
    # File Handler
    fh = logging.FileHandler(log_file)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    
    # Console Handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    return logger

logger = setup_logger()
