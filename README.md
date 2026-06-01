# Autonomous Research Intelligence (ARI)

> An AI-powered multi-agent research platform that autonomously discovers, analyzes, synthesizes, and evaluates information to generate high-quality research reports on any topic.

---

## Overview

**Autonomous Research Intelligence (ARI)** is a multi-agent research system built with **LangChain**, **OpenAI**, and **Streamlit**.

ARI transforms a simple research query into a structured report through a sequence of specialized AI agents that collaborate autonomously.

Whether you're exploring emerging technologies, global politics, education trends, sports analytics, or scientific breakthroughs, ARI performs the entire research workflow for you.

---

## Research Workflow

```text
User Query
     │
     ▼
┌───────────────────┐
│ Discovery Engine  │
│ (Search Agent)    │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Analysis Engine   │
│ (Reader Agent)    │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Synthesis Engine  │
│ (Writer Chain)    │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Review Engine     │
│ (Critic Chain)    │
└─────────┬─────────┘
          │
          ▼
    Final Report
```

---

## Features

### 🔍 Autonomous Research

Searches the web for relevant and reliable information sources.

### 📚 Intelligent Content Extraction

Extracts and analyzes information from selected sources.

### ✍️ Report Generation

Creates comprehensive and structured research reports.

### 🧐 Quality Evaluation

Reviews generated reports and provides constructive feedback.

### 🌐 Interactive Dashboard

Modern Streamlit interface for seamless research workflows.

### 📥 Export Reports

Download complete research outputs for future reference.

---

## Agent Architecture

| Component        | Purpose                                   |
| ---------------- | ----------------------------------------- |
| Discovery Engine | Finds relevant and trustworthy sources    |
| Analysis Engine  | Extracts and analyzes source content      |
| Synthesis Engine | Generates structured research reports     |
| Review Engine    | Evaluates report quality and completeness |

---

## Project Structure

```text
.
├── app.py                 # Streamlit UI
├── pipeline.py            # Research workflow orchestration
├── agents.py              # Agent and chain definitions
├── requirements.txt       # Project dependencies
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/NishthaB1409/autonomous-research-intelligence.git
cd autonomous-research-intelligence
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key

# Optional
TAVILY_API_KEY=your_tavily_api_key
SERPAPI_API_KEY=your_serpapi_api_key
```

---

## Running the Application

### Start Research Pipeline

```bash
python pipeline.py
```

### Launch Streamlit Dashboard

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## Example Research Topics

### Education

* AI-Powered Personalized Learning
* Future of Higher Education
* Global Education Reform

### Politics

* US Presidential Policy Trends
* European Union AI Regulation
* China-US Strategic Competition

### War & Geopolitics

* Ukraine-Russia Conflict Analysis
* Middle East Security Challenges
* Cyber Warfare and National Security

### Sports

* AI in Sports Analytics
* Technology Transforming Professional Sports
* Future of Global Football Competitions

### Technology

* Rise of Autonomous AI Agents
* Quantum Computing Breakthroughs
* Generative AI in Enterprise

### Environment

* Climate Change Adaptation Strategies
* Renewable Energy Transition
* Global Sustainability Initiatives

---

## Technology Stack

* Python
* LangChain
* OpenAI
* Streamlit
* Web Search APIs
* Web Scraping Tools

---

## Future Roadmap

* Citation Generation
* Multi-Source Fact Verification
* PDF Export
* Research Memory
* Multi-Agent Collaboration Enhancements
* Knowledge Graph Integration
* Research Analytics Dashboard

---

## Requirements

* Python 3.10+
* OpenAI API Key
* Internet Connection
* Optional Search Provider API Keys

---

## License

MIT License

