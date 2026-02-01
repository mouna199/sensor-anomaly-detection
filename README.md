# Sensor Anomaly Detection

Anomaly detection pipeline for industrial sensor data.

## Stack

- **Data**: TimescaleDB, Polars
- **Pipeline**: Python (ETL)
- **Viz**: Streamlit
- **Infra**: Docker

## Structure
```
├── src/
│   ├── extractors/      # CSV extraction
│   ├── transformers/    # Data cleaning and transformation
│   └── loaders/         # TimescaleDB loading
├── notebooks/           # Exploration and models
├── data/raw/            # SKAB data
├── app.py               # Streamlit dashboard
└── docker-compose.yml   # TimescaleDB
```

## Installation
```bash
# Clone repo
git clone https://github.com/mouna199/sensor-anomaly-detection.git
cd sensor-anomaly-detection

# Virtual environment
python -m venv venv
source venv/bin/activate

# Dependencies
pip install -r requirements.txt

# Start TimescaleDB
docker-compose up -d
```

## Usage
```bash
# Data migration
python src/migrate_csv.py

# Dashboard
streamlit run app.py
```

## Notebooks

| Notebook | Description |
|----------|-------------|
| `01_anomaly_detection.ipynb` | Comparison of PELT, Z-score, Isolation Forest |

## Dataset

[SKAB - Skoltech Anomaly Benchmark](https://github.com/waico/SKAB)

## Roadmap

- [x] Anomaly detection models (01/02/2026)
- [ ] Real-time API + Airflow
- [ ] GCP deployment
