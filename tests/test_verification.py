import os
import pytest
from src.core.dissector import ProtocolDissector
from src.utils.logger import logger

class DummyIP:
    def __init__(self):
        self.proto = 6
        self.src = "192.168.1.1"
        self.dst = "10.0.0.1"

class DummyPacket:
    def __init__(self, layer):
        self._layer = layer
    def haslayer(self, layer_name):
        return self._layer == layer_name
    def summary(self):
        return "Dummy 802.11 Beacon"
    def getlayer(self, layer_name):
        return DummyIP()

def test_dot11_dissection(caplog):
    packet = DummyPacket('Dot11')
    ProtocolDissector.inspect(packet)
    assert "[802.11 Frame] Dummy 802.11 Beacon" in caplog.text

def test_ip_dissection(caplog):
    packet = DummyPacket('IP')
    ProtocolDissector.inspect(packet)
    assert "[IP Traffic] Proto: 6 | 192.168.1.1 -> 10.0.0.1" in caplog.text

def test_log_creation():
    logger.info("Test log entry")
    assert os.path.exists('network_triage.log'), "Triage log was not created!"
