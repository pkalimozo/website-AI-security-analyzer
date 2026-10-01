# 🛡️ AI Security Website Analyzer

An open-source, local-first cybersecurity intelligence tool that scrapes website content and performs automated security threat analysis using **Ollama** and **LLaMA 3.2**.

Designed for security analysts, incident responders, and DevSecOps teams, this tool quickly digests threat advisories, security blogs, vulnerability disclosures, and web application pages to produce structured Markdown summaries.

---

## ✨ Features

- **🏠 100% Local & Private:** Powered by Ollama—no API keys, subscriptions, or external data sharing required.
- **⚡ Fast Vulnerability & Threat Extraction:** Automatically identifies CVEs, zero-days, active breaches, and defensive recommendations.
- **📊 Structured Security Summaries:** Parses unstructured web data into standardized Markdown sections:
  - Executive Summary
  - Threats & Vulnerabilities
  - Incidents & Alerts
  - News & Announcements
  - Actionable Recommendations
- **🛡️ OpenAI-Compatible API Client:** Utilizes standard Python client libraries for lightweight model orchestration.

---

## 📋 Prerequisites

Before running the analyzer, ensure you have the following installed:

1. **Python 3.10+**
2. **Ollama**: [Download & Install Ollama](https://ollama.com/)
3. **LLaMA 3.2 Model**:
   ```bash
   ollama pull llama3.2
   ```

---

## 🚀 Quickstart

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/security-website-analyzer.git
cd security-website-analyzer
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Start Ollama Server
Ensure Ollama is running locally:
```bash
ollama serve
```

### 4. Run the Analyzer
```bash
python main.py
```

---

## 🛠️ Configuration

You can customize the underlying model or local host endpoint inside `main.py`:

```python
OLLAMA_BASE_URL = "http://localhost:11434/v1"
MODEL = "llama3.2"  # Alternatively: mistral, llama3, qwen2.5-coder
```

---

## 📂 Project Structure

```text
.
├── main.py            # Main entry point and Ollama integration
├── scraper.py         # Website scraper and content extractor
├── requirements.txt   # Python dependencies
└── README.md          # Documentation
```

---

## 🔒 Security & Usage Disclaimer

This tool is intended for defensive security research, vulnerability intelligence gathering, and administrative audits. Always ensure you have appropriate permission when scraping or analyzing third-party web assets.

---

## 📄 License

Distributed under the [MIT License](LICENSE).