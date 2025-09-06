# Cyber Bot

A FastAPI and Next.js-based web application that scrapes, analyzes, and provides insights on cybersecurity threats (CVEs) using a vector database (ChromaDB) and an LLM (via OpenRouter API). The app features a chat interface for querying CVE data, fetching raw CVE info, analyzing threats, and notifying users of critical issues.

## Features
- **Chat Interface**: Query CVE details (e.g., "What is the risk associated with CVE-2024-20130?") with LLM-generated responses.
- **CVE Fetching**: Scrape recent CVE data from sources (via `fetcher.py`).
- **Analysis**: Process CVE data for risk assessment and actions (via `analyzer.py`).
- **Notifications**: Generate alerts based on analysis (via `notifier.py`).
- **Vector Storage**: Store and query CVE data efficiently using ChromaDB (via `vector.py`).
- **Modern UI**: Clean, responsive UI.

## Tech Stack
- **Backend**: FastAPI (Python)
- **Database**: ChromaDB (vector store for CVE data)
- **LLM**: OpenRouter API
- **Frontend**: Next.js


## Setup
### Prerequisites
- Python 3.12+
- Poetry (for dependency management)
- Node.js (for Next.js frontend)
- OpenRouter API key (set in `.env`)

