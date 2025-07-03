# Dockerfile for Airflow with PySpark
FROM apache/airflow:latest-python3.12

USER 0

# Install OpenJDK 17 and set JAVA_HOME manually
RUN apt-get update && apt-get install -y openjdk-17-jdk-headless curl  && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

USER airflow
# Install Python dependencies
RUN pip install --no-cache-dir \
    pandas \
    requests \
    sqlalchemy \
    psycopg2-binary \
    pyspark

