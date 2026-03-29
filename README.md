# 🚀 Apache Airflow ETL Pipeline (Market Data Project)

## 📌 Project Overview

This project demonstrates a **production-style ETL pipeline** built using **Apache Airflow**.
It extracts stock market data from an external API, transforms it into a structured format, and loads it into a database.

The project is designed with **modular architecture**, using:

- `dags/` → orchestration
- `include/` → reusable business logic
- `plugins/` → custom Airflow extensions

---

# 🏗️ Architecture Overview

## 🔷 High-Level Flow

```
Polygon API → Extract → Transform → Load → SQLite DB
```

---

## 📊 Architecture Diagram (Text Representation)

```
                ┌──────────────────────┐
                │   Polygon API        │
                └─────────┬────────────┘
                          │
                          ▼
        ┌────────────────────────────────┐
        │  Custom Operator (plugins/)    │
        │  PolygonAPIToXComOperator      │
        └─────────┬──────────────────────┘
                  │ (XCom)
                  ▼
        ┌────────────────────────────────┐
        │  Transform Layer (include/)    │
        │  transform_market_data()       │
        └─────────┬──────────────────────┘
                  │
                  ▼
        ┌────────────────────────────────┐
        │   Load Layer (Airflow Hook)    │
        │   SQLite Database              │
        └────────────────────────────────┘
```

---

# 📂 Project Structure

```
your-project/
├── dags/
│   └── market_etl.py
│
├── include/
│   ├── api/
│   │   └── polygon_api.py
│   ├── utils/
│   │   └── transform.py
│   └── config.py
│
├── plugins/
│   ├── custom_operator.py
│   ├── custom_hook.py
│   └── __init__.py
│
├── tests/
│   └── test_dag.py
│
├── airflow_settings.yaml
├── Dockerfile
├── packages.txt
├── requirements.txt
└── README.md
```

---

# ⚙️ Components Explanation

## 1️⃣ DAG (Orchestration Layer)

📄 `dags/market_etl.py`

- Controls workflow execution
- Defines task dependencies
- Uses Airflow TaskFlow API + Custom Operator

### Flow:

```
extract → transform → load
```

---

## 2️⃣ Plugins (Custom Airflow Extensions)

📂 `plugins/`

### 🔹 Custom Operator

- Handles API extraction logic
- Reusable across multiple DAGs

```python
PolygonAPIToXComOperator
```

👉 Why?

- Keeps DAG clean
- Promotes reuse
- Follows Airflow best practices

---

### 🔹 Custom Hook

- Manages database connection
- Abstracts connection logic

---

## 3️⃣ Include Folder (Business Logic Layer)

📂 `include/`

### 🔹 API Module

- Handles API calls

### 🔹 Transform Module

- Converts JSON → DataFrame

### 🔹 Config Module

- Stores constants like API key

---

## 4️⃣ Load Layer

- Uses `SqliteHook`
- Stores data into SQLite database

---

# 🔄 ETL Process Explanation

## 🟢 1. Extract

- Data fetched from Polygon API
- Implemented using custom operator
- Output stored in XCom

---

## 🟡 2. Transform

- JSON flattened into structured format
- Missing values handled
- Converted to Pandas DataFrame

---

## 🔵 3. Load

- Data inserted into SQLite table
- Append mode used for incremental loads

---

# ⚡ DAG Execution Flow

```
Task 1: extract_market_data
        ↓
Task 2: transform_task
        ↓
Task 3: load_task
```

---

# 🧪 Testing

📂 `tests/`

- DAG validation using `DagBag`
- Ensures DAG loads correctly

---

# 🐳 Docker Setup

## Build & Run

```bash
astro dev start
```

---

## Access UI

```
http://localhost:8080
```

---

# 🔌 Airflow Connection Setup

## Connection Details

| Field   | Value                             |
| ------- | --------------------------------- |
| Conn ID | market_database_conn              |
| Type    | SQLite                            |
| Host    | /usr/local/airflow/market_data.db |

---

# 📦 Requirements

```txt
apache-airflow
pandas
requests
apache-airflow-providers-sqlite
```

---

# 🔐 Environment Variables

Update API key:

```python
API_KEY = "YOUR_API_KEY"
```

---

# 🚀 How to Run

```bash
git clone <repo-url>
cd your-project
astro dev start
```

Then:

- Open Airflow UI
- Enable DAG
- Trigger run

---

# 📈 Key Features

✅ Modular architecture
✅ Custom Airflow plugins
✅ Clean DAG design
✅ Scalable ETL pipeline
✅ Reusable components
✅ Production-ready structure

---

# 🔥 Interview Explanation (1 Minute Pitch)

> “I built a modular ETL pipeline using Apache Airflow where extraction is handled by a custom operator, transformation logic is separated into reusable modules, and data is loaded into SQLite. The DAG only manages orchestration, ensuring scalability and maintainability.”

---

# 🧠 Design Decisions

| Decision         | Reason               |
| ---------------- | -------------------- |
| Use plugins      | Reusability          |
| Use include      | Clean separation     |
| Use SQLite       | Lightweight testing  |
| Use TaskFlow API | Simpler dependencies |

---

# 🚀 Future Enhancements

- Add AWS S3 storage
- Integrate Snowflake / BigQuery
- Add alerting (Slack/Email)
- Implement retries + logging
- Add multiple stock tickers
- CI/CD pipeline

---

# 🧑‍💻 Author

**Akash Patro**

---

# ⭐ Conclusion

This project demonstrates:

- Real-world ETL design
- Airflow best practices
- Production-ready structure

Perfect for:
✔ Data Engineer roles
✔ Backend/Data pipeline interviews

---
