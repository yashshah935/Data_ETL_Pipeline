# 🍎 Retail Sales Analytics ETL Project (Dockerized)

This project demonstrates a **complete local ETL pipeline** using only **open-source tools**. It loads retail sales data, transforms it with DBT, and orchestrates the workflow using Apache Airflow. The entire stack runs locally via **Docker**. Now supports **PySpark** for large-scale data processing.
---

## 🧱 Tech Stack

- **Apache Airflow** – ETL orchestration
- **PostgreSQL** – Data warehouse
- **Python (Pandas + SQLAlchemy)** – Data ingestion
- **DBT (Data Build Tool)** – SQL-based data transformation
- **PySpark** – Big data processing support
- **Docker** – Local containerized setup

---

## 🚀 Project Structure

```
retail-etl/
├── dags/                      # Airflow DAGs
│   └── ETL.py                 # Main DAG for orchestrating ETL
├── dbt_project/               # DBT transformation project
│   ├── models/                # DBT models (stg/fact)
│   ├── dbt_project.yml        # DBT config
│   └── profiles.yml           # DBT profiles config
├── etl/                       # Python ETL scripts
│   ├── sales_load.py          # Loads sales data to PostgreSQL
│   └── ingest_taxi_data.py    # Loads NYC taxi data using PySpark or Pandas
├── data/                      # Local data volume (optional)
│   ├── sales.csv
│   └── taxi_data.parquet          
├── docker-compose.yml         # Docker setup for all services
├── Dockerfile                 # Custom Airflow image with PySpark
└── README.md                  # Documentation

```

---

## 🛠️ How to Set Up & Run

### 🧩 1. Clone the Repository

```bash
git clone https://github.com/your-username/retail-etl.git
cd retail-etl
```

## 📥 2. Download Required Datasets

Ensure the following files are present in the `./data/raw/` directory:

1. `sales.csv`  
2. `taxi_data.parquet`

### Option A: Download Manually

- **sales.csv**: [UCI Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail) (convert to CSV format)
- **taxi_data.parquet**: Use any NYC Yellow Taxi Trip parquet file  
  Example: [NYC TLC Trip Data (Parquet)](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

Place both files in:

```
retail-etl/data/raw/
```

### Option B: Download via script (optional)

Add this in a script if you want to automate download using `wget` or `requests`.

---

## 🐳 3. Build and Start Docker Containers

```bash
docker-compose up --build -d
```

---

## 🌐 4. Access Airflow UI

Visit:

```
http://localhost:8080
```

Login with:

```
Username: admin
Password: <check container logs>
```

---
## 📊 Workflow Steps

### 1. **ETL Scripts** (`etl/`)

- `sales_load.py`: Cleans and loads retail sales data into `data_etl.sales_clean`
- `ingest_taxi_data.py`: Ingests NYC Taxi data to `data_etl.raw_taxi_data` using Pandas or PySpark

### 2. **DBT Transformations**

- `stg_sales`, `fact_sales`
- `stg_taxi_data`, `fact_trips`

### 3. **Airflow DAG**

- Orchestrates both ETL scripts and triggers DBT models

---

## ⚙️ Docker Commands

```bash
docker ps                             # Running containers
docker exec -it airflow_container bash  # Shell into airflow
docker exec dbt_container dbt run --project-dir /usr/app  # Trigger dbt models
docker-compose down && docker-compose up --build -d       # Rebuild and restart
```
## 🔄 Restart the Entire Stack

```bash
docker-compose down
docker-compose up --build -d
```


---

## 🗃️ PostgreSQL Connection Info

```
Host: localhost
Port: 5432
Username: airflow
Password: airflow
Database: analytics
```

Use pgAdmin, DBeaver, or `psql` for querying.

---

## 🚀 Fork & Build Something Amazing

This entire **ETL architecture is ready to use**:

- 🧩 Fork and plug in your data  
- 💻 Works 100% locally  
- ☁️ Zero cloud dependency  
- 🧪 No hidden cost  
- 🔁 Easily extendable & open-source  

---


## ✅ Future Enhancements

- BI dashboard (Superset / Metabase)
- dbt incremental models
- Real-time API ingestion
- ML model orchestration via Airflow

---

## 🙌 Credits

Built by **Yash Shah**, inspired by Engineer

---

## 📄 License

MIT License. Use freely for learning or showcasing your portfolio.

---

Happy Data Engineering! 🛠️📈

