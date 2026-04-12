# 📊 Stock Market Data Pipeline using Airflow & GCP

---

## 1️⃣ Problem Statement

The goal of this project is to build a scalable data pipeline that ingests stock market data from the Polygon API, processes it, and stores it in a cloud-based data warehouse for analytics and visualization.

In real-world financial systems, raw API data needs to be:

- reliably ingested
- transformed into structured format
- stored in a data lake and warehouse
- made available for business insights

This project solves that by implementing an end-to-end ETL pipeline using Apache Airflow and Google Cloud Platform.

---

## 2️⃣ Architecture Diagram

```
Polygon API
    ↓
Airflow (Custom Operator)
    ↓
Transform (Pandas)
    ↓
Google Cloud Storage (Data Lake)
    ↓
BigQuery (Data Warehouse)
    ↓
Looker Studio (Dashboard)
```

---

## 3️⃣ Tech Stack

- **Orchestration:** Apache Airflow
- **Programming:** Python
- **API Source:** Polygon API
- **Data Processing:** Pandas
- **Data Lake:** Google Cloud Storage (GCS)
- **Data Warehouse:** BigQuery
- **Visualization:** Looker Studio
- **Containerization:** Docker

---

## 4️⃣ Pipeline Flow

### 🔹 Extract

- Custom Airflow operator fetches stock market data from Polygon API

### 🔹 Transform

- Data is cleaned and structured using Pandas

### 🔹 Load to Data Lake

- Transformed data is uploaded to Google Cloud Storage (GCS)

### 🔹 Load to Data Warehouse

- Data is loaded from GCS into BigQuery

### 🔹 Visualization

- BigQuery data is connected to Looker Studio for dashboards

---

## 5️⃣ How to Run (Step-by-Step)

### 🔹 Prerequisites

- Python 3.9+
- Docker installed
- Google Cloud account
- Polygon API key

---

### 🔹 Step 1: Clone Repository

```bash
git clone https://github.com/akash-patro-coder/Apache-Airflow-ETL
cd Apache-Airflow-ETL
```

---

### 🔹 Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 Step 3: Setup GCP

- Create GCS bucket
- Create BigQuery dataset

Enable APIs:

- BigQuery API
- Cloud Storage API

Authenticate:

```bash
gcloud auth application-default login
```

---

### 🔹 Step 4: Configure Environment

Update values in DAG or use environment variables:

```bash
GCP_BUCKET=your-bucket-name
GCP_PROJECT=your-project-id
BQ_DATASET=your_dataset
BQ_TABLE=market_table
```

---

### 🔹 Step 5: Run Airflow

```bash
docker-compose up
```

- Open Airflow UI: http://localhost:8080
- Trigger DAG: `market_etl`

---

## 6️⃣ Dashboard Screenshot

![Stock Market Dashboard](AAPL%20stock%20dashboard%20overview.png)

## ⚡ Final Summary

End-to-end data pipeline using Airflow and GCP to ingest, transform, and analyze stock market data from Polygon API.

