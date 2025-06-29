# 🛒 Retail Sales Analytics ETL Project (Dockerized)

This project demonstrates a **complete local ETL pipeline** using only **open-source tools**. It loads retail sales data, transforms it with DBT, and orchestrates the workflow using Apache Airflow. The entire stack runs locally via **Docker**.

---

## 🧱 Tech Stack

- **Apache Airflow** – ETL orchestration
- **PostgreSQL** – Data warehouse
- **Python (Pandas + SQLAlchemy)** – Data ingestion
- **DBT (Data Build Tool)** – SQL-based data transformation
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
└─── docker-compose.yml        # Docker setup for all services

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

### 1. **Python ETL Script** (`etl/load.py`)

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

## ✅ Future Enhancements

- Add Superset/Metabase for BI
- Implement dbt incremental models
- Use real-time API for incremental loads
- Add data tests and docs (`dbt test`, `dbt docs`)

---

## 🙌 Credits

Built by Yash Shah

---

## 📄 License

MIT License. Use freely for learning or showcasing your portfolio.

---

Happy Data Engineering! 🛠️📈

