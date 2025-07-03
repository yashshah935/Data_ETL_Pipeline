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
│   └── retail_etl.py          # Main DAG for orchestrating ETL
├── dbt_project/               # DBT transformation project
│   ├── models/                # DBT models (stg/fact)
│   ├── dbt_project.yml        # DBT config
│   └── profiles.yml           # DBT profiles config
├── etl/                       # Python ETL scripts
│   └── sal;es_load.py         # Loads data from API to PostgreSQL
├── data/                      # Local data volume (optional)
│   └── raw/sales.csv          # Example static data (if needed)
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

### 🐳 2. Build and Start Docker Containers

```bash
docker-compose up --build -d
```


### 🌐 3. Access Airflow UI

Open your browser:

```
http://localhost:8080
```

Login with:

```
username: admin
password: <get it from logs>
```

---

## 📊 Workflow Steps

### 1. **Python or PySpark ETL Script** (`etl/load.py`)

- Fetches  data from `sales.csv` 
- Cleans & transforms data
- Loads into `data_etl.sales_clean` in PostgreSQL

### 2. **DBT Transformations** (`dbt_project/`)

- `stg_sales`: staging layer
- `fact_sales`: deduplicated, aggregated layer

### 3. **Airflow DAG**

- Executes the `sales_load.py` script
- Runs DBT transformations

---

## ⚙️ Common Docker Commands

### 📦 View Running Containers

```bash
docker ps
```

### 🐚 Shell into a Container

```bash
docker exec -it airflow_container bash
```

### 🧪 Run DBT from dbt\_container

```bash
docker exec dbt_container dbt run --project-dir /usr/app
```

### 🔄 Restart the Entire Stack

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
Database: retail_db
```

You can connect using DBeaver, pgAdmin, or `psql`.

---

## 🚀 Fork & Build Something Amazing

This entire **ETL architecture is ready to use**.

- Just fork it and start building amazing pipelines
- Works fully **locally**
- **No cloud dependency**
- **Zero cost**, great for learning & portfolio
- **Extensible & open-source**

---

## ✅ Future Enhancements

- Add Superset/Metabase for BI
- dbt incremental model support
- Live API data streaming
- ML orchestration with Airflow

---

## 🙌 Credits

Built by **Yash Shah**, inspired by Engineer

---

## 📄 License

MIT License. Use freely for learning or showcasing your portfolio.

---

Happy Data Engineering! 🛠️📈

