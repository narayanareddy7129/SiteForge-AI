# SiteForge AI

**LLM-powered frontend website generator**

SiteForge AI turns a plain-English description of a website into a working frontend — HTML for structure, CSS for styling, and JavaScript for interactivity. Describe what you want, and the app generates the files for you.

The project is a hands-on exploration of how LLMs can be wired into a real development workflow to automate frontend scaffolding, rather than just generating text.

---

## Overview

Normally, building a frontend means writing HTML, CSS, and JS by hand. SiteForge AI automates that first pass.

Give it a prompt like:

> "Create a modern portfolio website for a Python developer with a navigation bar, hero section, skills section, projects section, and contact form."

and it generates:

```
HTML → page structure
CSS  → styling and responsive layout
JS   → interactivity
```

You end up with a complete, working frontend you can use as-is or build on.

---

## Features

- **LLM-powered code generation** — uses a large language model to turn plain-language requirements into frontend code
- **Natural language input** — no need to hand-write markup to get started
- **HTML, CSS, and JS generation** — structure, styling, and behavior, all generated together
- **Multi-file output** — produces separate `index.html`, `style.css`, and `script.js`
- **Rapid prototyping** — go from an idea to a working page in minutes
- **Streamlit interface** — simple UI for entering prompts and generating sites

---

## Architecture

![Alt Text](https://github.com/narayanareddy7129/SiteForge-AI/blob/bd7d1a5832caa4ef71360d5e440f3b048a733068/siteforgeai_workflow.png) 
---

## Tech stack

**Generative AI**
- Large language models
- Prompt engineering

**Backend / application**
- Python
- LangChain
- Google Gemini
- Streamlit

**Frontend**
- HTML5
- CSS3
- JavaScript

**Tooling**
- Git / GitHub
- Python virtual environment
- VS Code

---

## Project structure

```
SiteForge-AI/
│
├── web/
│   └── files/
│       ├── main.py
│       ├── requirements.txt
│       └── ...
│
├── .gitignore
├── README.md
└── ...
```

---

## How it works

1. **User input** — you describe the website you want in plain language.
2. **Prompt processing** — the app builds a structured prompt and sends it to the LLM via LangChain, asking for HTML, CSS, and JS.
3. **Code generation** — the LLM generates the frontend code based on your description.
4. **Code extraction** — the response is parsed to pull out the HTML, CSS, and JS sections.
5. **File output** — the code is written to `index.html`, `style.css`, and `script.js`, which together form the finished site.

### Example

**Input:**
```
Create a modern portfolio website for a Machine Learning Engineer.

Include:
- Navigation bar
- Hero section
- About section
- Skills
- Projects
- Contact section
- Responsive design
```

**Output:** `index.html`, `style.css`, `script.js` — a complete frontend built to spec.

---

## API key setup

The app talks to Gemini using an API key.

**Local development** — create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Make sure `.env` is listed in `.gitignore` so it never gets committed:

```gitignore
.env
```

**Streamlit deployment** — use Streamlit's Secrets manager instead of committing the `.env` file.

---

## Installation

**1. Clone the repo**
```bash
git clone https://github.com/narayanareddy7129/SiteForge-AI.git
cd SiteForge-AI
```

**2. Create a virtual environment**
```bash
python -m venv web
```
Activate it on Windows:
```bash
web\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set your API key**

Create a `.env` file with:
```env
GEMINI_API_KEY=your_api_key_here
```

**5. Run it**
```bash
streamlit run main.py
```

The app opens in your browser.

---

## Requirements

```
streamlit
langchain
langchain-google-genai
python-dotenv
```

---

## Security

API keys and other credentials are kept out of the repo entirely:

- `.env` for local development
- Streamlit Secrets for deployment
- `.gitignore` keeps `.env` from ever being committed

---

## Use cases

- Rapid website prototyping
- Landing pages and portfolios
- UI experimentation
- Frontend development assistance
- Learning HTML, CSS, and JavaScript
- Turning a product idea into a quick prototype

---

## Roadmap / ideas

- Live preview of the generated site
- Conversational, iterative editing of a generated site
- Better automatic responsive design
- AI-generated images as part of the output
- Component-level generation
- Downloadable ZIP of the generated site
- HTML/CSS/JS validation
- AI-assisted debugging of generated frontends
- Multiple design themes
- Multi-page site generation
- One-click deployment

---

## What I learned building this

- Working with LLMs as part of an application, not just a chat interface
- Prompt engineering for structured, multi-part output
- LangChain fundamentals
- Parsing and organizing LLM output into usable files
- API integration and environment variable management
- Building and shipping a Streamlit app
- Git/GitHub workflow for a real project

---

## Author

**Muvva Lakshmi Narayana Reddy**

Aspiring AI/ML engineer, interested in machine learning, generative AI, and LLM-powered applications.

If you find this useful, a star on the repo is appreciated.
