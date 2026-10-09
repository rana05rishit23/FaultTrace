# FaultTrace - Advanced Wi-Fi Protocol Analyzer & SDET Automation Framework

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Scapy](https://img.shields.io/badge/Scapy-2.5.0-green.svg)
![Pytest](https://img.shields.io/badge/Pytest-8.2.0-yellow.svg)

FaultTrace is an automated, high-performance network protocol analyzer and testing framework engineered in Python. Designed for Quality Engineering and SDET workflows, it leverages `Scapy` to capture and dissect **802.11 (Wi-Fi) protocols** and standard TCP/UDP traffic. The project is paired with a robust `pytest` suite for automated **log parsing**, execution tracing, and root-cause failure triage.

## 🚀 Key Features

- **Deep Protocol Analysis:** Captures and deeply inspects 802.11 wireless frames, tracking SSIDs, MAC addresses, and network anomalies. Includes fallback for standard IP/TCP/UDP traffic.
- **Automated SQA Testing:** Utilizes `pytest` to run automated assertions on generated network logs, ensuring zero packet dissection failures and maintaining high test coverage.
- **System Logging & Failure Triage:** Implements structured, 3-tier logging mechanisms to extract precise execution traces. This accelerates root-cause identification and failure triage during complex network debugging.
- **Lightweight & Scalable Architecture:** Streams captured packets directly to logs without memory bloat (`store=0`), simulating enterprise-grade network monitoring tools suitable for continuous integration (CI) pipelines.

## 🛠️ Tech Stack & SQA Tools

- **Core Language:** Python 3.8+
- **Testing & Test Automation:** `pytest`, Unit/Integration Testing methodologies
- **Networking Tools:** `Scapy`, Wireless Packet Sniffing, 802.11 Protocols, TCP/UDP Stack
- **Data Analysis:** Automated Log Parsing, Failure Triage

## 📂 Repository Structure

```text
FaultTrace/
├── .github/workflows/ # GitHub Actions CI workflows
├── src/
│   ├── core/
│   │   ├── dissector.py # Handles deep packet inspection
│   │   └── sniffer.py   # Asynchronous ThreadPool-driven sniffer
│   └── utils/
│       └── logger.py    # Structured logging configuration
├── tests/               # PyTest regression suite
├── faulttrace.py          # CLI Entry Point
├── requirements.txt     # Dependencies
├── .gitignore           # Git ignore rules
└── README.md            # Documentation
```

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/FaultTrace.git
   cd FaultTrace
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the analyzer (Offline verification mode):**
   ```bash
   python faulttrace.py --mode offline --target dot11-sample_traffic.pcap --workers 4
   ```

4. **Run the automated test suite:**
   ```bash
   pytest tests/ -v
   ```
