# 🥊 UFC Data Engineering Pipeline

## 📌 Overview
This project is an end-to-end data engineering pipeline that extracts, transforms, and analyzes UFC fighter data using public API sources. The goal is to build a structured dataset of fighter statistics and generate meaningful performance metrics for analysis and visualization.

This project was built to demonstrate practical data engineering skills including API ingestion, ETL pipeline design, data cleaning, and analytical modeling.

---

## ⚙️ Architecture

UFC API  
→ Python ETL Pipeline  
→ Pandas Data Processing  
→ Structured Dataset (CSV / SQLite)  
→ Analytics / Dashboard Layer

---

## 🚀 Features

- Extracts fighter data from UFC API (RapidAPI)
- Cleans and standardizes raw fighter statistics
- Computes performance metrics:
  - Win rate
  - Strike accuracy (if available)
  - Fight history aggregation
- Loads structured data into CSV or SQLite
- Supports downstream analytics and visualization
- Modular ETL pipeline design for scalability

---

## 🛠️ Tech Stack

- Python
- Pandas
- Requests (API integration)
- SQLite (optional storage layer)
- python-dotenv (environment variables)
- Matplotlib / Streamlit (optional visualization)

---

## 📁 Project Structure
```text
ufc-data-engineering-pipeline/
├── src/
│   ├── extract/
│   ├── transform/
│   └── load/
├── main.py
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── sql/
├── config/
├── requirements.txt
└── README.md
```


---

## 🔐 Environment Variables

This project uses environment variables to securely store API credentials.

Create a `.env` file in the root directory:

Do NOT commit your `.env` file to GitHub.

---

## ▶️ How to Run

```bash
git clone https://github.com/jeffreyjblee/ufc-data-engineering-pipeline.git
cd ufc-data-engineering-pipeline

pip install -r requirements.txt

python src/main.py

```

**👤 Author**

Jeffrey Lee

