# 🧩 Data ETL Pipeline

> **Automated ETL pipeline integrated with Jenkins CI/CD for efficient data ingestion, transformation, and loading.**

---

## 📘 Overview

This project is an **end-to-end ETL (Extract, Transform, Load) pipeline** designed to automate the process of moving data from multiple sources into a clean, analytics-ready format.

It integrates seamlessly with **Jenkins** for continuous integration and deployment, ensuring that data workflows are robust, repeatable, and production-ready.

---

## 🚀 Features

- **🗃️ Extract:** Pull data from multiple sources (APIs, CSV files, databases, etc.)
- **🧹 Transform:** Clean, validate, and enrich raw data using **Python** & **Pandas**
- **📦 Load:** Store processed data into a target database, data warehouse, or file system
- **⏰ Automation:** Schedule runs via **Airflow**, **Cron**, or a custom scheduling script
- **🧾 Logging & Error Handling:** Detailed logging and exception tracking for every pipeline stage
- **⚙️ CI/CD Integration:** Designed for deployment and testing through **Jenkins**

---

## 🏗️ Project Structure

```bash
data-etl-pipeline/
│
├── src/                    # Core ETL scripts
│   ├── extract/            # Extraction logic
│   ├── transform/          # Data cleaning & transformation
│   ├── load/               # Loading to destination
│   └── utils/              # Helper functions and shared modules
│
├── config/                 # Configuration files (YAML/JSON)
├── logs/                   # Pipeline execution logs
├── tests/                  # Unit and integration tests
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation



---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Raajveers/data-etl-pipeline.git
   cd data-etl-pipeline

**2.Create a virtual environment**
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

**3.Install dependencies**
pip install -r requirements.txt


**4.Run the ETL pipeline**
python src/main.py



| Component       | Technology               |
| --------------- | ------------------------ |
| Language        | Python 3.x               |
| Data Processing | Pandas, NumPy            |
| Orchestration   | Airflow / Cron / Jenkins |
| Logging         | Python Logging           |
| Version Control | Git, GitHub              |
| CI/CD           | Jenkins                  |

