# Sensor Anomaly Detection
Détection d'anomalies sur données de capteurs industriels.

## Stack
- **Data** : TimescaleDB, Polars
- **Pipeline** : Python (ETL)
- **Viz** : Streamlit
- **Infra** : Docker

## Structure
```
├── src/
│   ├── extractors/      # Extraction CSV
│   ├── transformers/    # Nettoyage et transformation
│   └── loaders/         # Chargement TimescaleDB
├── notebooks/           # Exploration et modèles
├── data/raw/            # Données SKAB
├── app.py               # Dashboard Streamlit
└── docker-compose.yml   # TimescaleDB
```

## Installation
```bash
# Cloner le repo
git clone https://github.com/username/sensor-anomaly-detection.git
cd sensor-anomaly-detection

# Environnement virtuel
python -m venv venv
source venv/bin/activate

# Dépendances
pip install -r requirements.txt

# Lancer TimescaleDB
docker-compose up -d
```

## Utilisation
```bash
# Migration des données
python src/migrate_csv.py

# Dashboard
streamlit run app.py
```

## Notebooks

| Notebook | Description |
|----------|-------------|
| `01_anomaly_detection.ipynb` | Comparaison PELT, Z-score, Isolation Forest |

## Dataset
[SKAB - Skoltech Anomaly Benchmark](https://github.com/waico/SKAB)

## À venir
- [x] Modèle de détection d'anomalies 01/02/2026
- [ ] API temps réel + Airflow
- [ ] Déploiement GCP
