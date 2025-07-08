# Grey Literature Scraper

A lightweight, modular Python tool for retrieving grey literature from Ministry of Health websites and Google Scholar. Developed to support systematic reviews in global health, especially in low- and middle-income countries (LMICs), where key data often reside in grey literature rather than academic databases.

## Background

Grey literature—including Ministry of Health reports, policy briefs, and surveillance data—is an essential source of information in systematic reviews. This is especially true in global health and LMIC settings, where critical data may not be published in academic journals or indexed in databases like PubMed.

Manually identifying grey literature from government websites and Google Scholar can be time-consuming, inconsistent, and difficult to reproduce.

This tool was developed to automate and standardize grey literature searching, as part of a systematic review on maternal colonisation with multidrug-resistant Gram-negative bacteria in LMICs. It is adaptable for other review topics or global health domains where grey literature inclusion is important.

## Features

- **Two modular scrapers**:
  - `scholar_scraper3.py` uses [SerpAPI](https://serpapi.com/) to extract structured results from Google Scholar.
  - `search_moh2.py` uses the Google Custom Search API to query user-defined Ministry of Health websites.
- **Customizable queries** – adapt search terms and filters to fit your systematic review topic.
- **Structured output** – search results are exported to `.csv` files for easy integration into screening workflows.
- **Supports transparency and reproducibility** – automates otherwise manual grey literature searches.
- **LMIC-focused** – originally built to support literature searches across government websites in LMICs, but extensible to other settings.

## Getting Started (for Beginners)

If you're new to Python or programming, this section walks you through the basics.

### 1. What is Python?

Python is a programming language used to run this tool. You’ll need to install it before using the scraper.

### 2. Install Python (if not already installed)

Visit the [official Python website](https://www.python.org/downloads/) and download Python 3.8 or newer for your operating system. Make sure you check the box to **add Python to PATH** during installation.

### 3. Install Git (optional but recommended)

Install Git from [git-scm.com](https://git-scm.com/) to download this tool from GitHub using the command line.

## Installation

Once Python is installed, open your Terminal or Command Prompt, and follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/lafhlafh/grey-literature-scraper.git
cd grey-literature-scraper
```

### 2. (Recommended) Create and activate a virtual environment

This keeps your Python packages isolated and clean.

```bash
python3 -m venv envs/greyenv
source envs/greyenv/bin/activate     # macOS/Linux

# On Windows (Command Prompt)
envs\greyenv\Scripts\activate.bat
```

### 3. Install required packages

```bash
pip install -r requirements.txt
```

## API Setup

Depending on which script you use, you will need one of the following APIs:

### 1. Google Custom Search API (for Ministry of Health website searches)

To run `search_moh2.py`, you will need:
- A **Google API key** (from the Google Cloud Console)
- A **Search Engine ID (cx)** — you can use the default ID provided when enabling the Custom Search API

**Steps:**

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Enable the **Custom Search API** for your project (search for it in the APIs Library)
3. Go to **APIs & Services > Credentials**
4. Click “Create Credentials” and choose **API Key**
5. Your API key will be generated and shown — copy this into the script
6. Go to [Google Programmable Search Engine] (https://programmablesearchengine.google.com/)
7. Click “Add” to name your search engine. 
8. Click Search the entire web 
9. Once saved, go to “Control Panel” and your CSE ID (cx) will be displayed under “Details”

Add your API key and CSE ID to the top of `search_moh2.py`:

```python
API_KEY = "your_api_key"
SEARCH_ENGINE_ID = "your_cse_id"
```

The script dynamically appends `site:{domain}` to restrict searches to Ministry of Health websites.

---

### 2. SerpAPI (for Google Scholar search)

To run `scholar_scraper3.py`, you need a SerpAPI account and API key.

**Steps:**

1. Sign up at [https://serpapi.com/](https://serpapi.com/)
2. Copy your API key from the dashboard
3. Add it to the script or store it in a `.env` file:

```python
api_key = "your_serpapi_key"
```

## How to Run the Scripts

You can run the scripts from Terminal (macOS/Linux) or Command Prompt (Windows):

```bash
python scholar_scraper3.py         # For Google Scholar search
python search_moh2.py              # For Ministry of Health website search
```

## ⚠️ SerpAPI Free Tier Note

- SerpAPI’s free plan only allows **100 searches per month**
- Large searches (e.g. 500 or 1000 results) will consume this quickly

**Tips:**

- Try a small test query first (e.g. `max_results=5`) to ensure everything is working
- If you exceed the quota, SerpAPI will block further requests until the next month unless you upgrade

## Acknowledgements

- Country name and domain filters adapted from:

  > World Health Organization. (2024). *WHO Country Filters for LMIC Countries (March 2024)*. Zenodo. https://doi.org/10.5281/zenodo.10867295

- Code development was supported in part by OpenAI’s ChatGPT.

Developed as part of a PhD project funded by the Wellcome Trust (WT reference code: 324265/Z/25/Z), conducted through Brighton and Sussex Medical School and the MRC/UVRI & LSHTM Uganda Research Unit.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
