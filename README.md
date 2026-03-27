# Agents with Tools

A collection of AI agents built with **Google ADK** and **Gemini 2.5 Flash**.

## Agents


| # | Agent | Description |
|---|-------|-------------|
| 01 | Geography Assistant | Answers questions about countries, capitals, regions, and geography facts |
| 02 | Math Assistant | Solves mathematical problems and performs calculations |
| 03 | Research Assistant | Searches and summarizes information on a given topic |
## Setup

```bash
git clone https://github.com/Hayou-Azizkd/Agents_with_tools.git
cd Agents_with_tools
python3 -m venv .venv
source .venv/bin/activate
pip install google-adk
```

Add your API key to the relevant agent's `.env` file:
```bash
echo "GOOGLE_API_KEY=your_api_key_here" > <agent_folder>/.env
```

Then run:
```bash
adk web
```

Open http://127.0.0.1:8000 in your browser.

## Tech Stack

- Python 3.12
- Google ADK
- Gemini 2.5 Flash
- Linux (Ubuntu via WSL)
