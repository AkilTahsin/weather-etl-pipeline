# Weather Data ETL Pipeline using OpenWeather API

An end-to-end ETL pipeline that extracts weather data from the OpenWeather API, stores raw data locally, transforms it using Pandas, and loads it into PostgreSQL running inside Docker.

## Tech Stack

- Python  
- PostgreSQL  
- Docker  
- SQLAlchemy  
- Pandas  
- python-dotenv  
- Streamlit (optional dashboard)

## Project Structure

```
root/
├── app/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── config.py
│   ├── pipeline.py
│
├── logs/
│
├── data/
│    ├── raw/
│    ├── processed/
│
├── requirements.txt
├── docker-compose.yml
├── .env
├── .gitignore
└── README.md
```

## 1. Create and Configure Environment Variables

Create a `.env` file in the project root:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password

WEATHER_API_KEY=your_openweather_api_key
```

⚠ Add `.env` to `.gitignore` to avoid committing secrets.

## 2. Launch PostgreSQL with Docker

Start the database container:
```
docker compose up -d
```

Verify container is running:
```
docker compose ps
```

Optional: check logs to confirm readiness:
```
docker compose logs -f
```


Wait until you see:
<blockquote>database system is ready to accept connections</blockquote>

## 3. Create Python Virtual Environment

```
python -m venv venv
```

## 4. Activate Virtual Environment

### Git Bash (Windows)
```
source venv/Scripts/activate
```


### Linux / macOS
```
source venv/bin/activate
```

You should see `(venv)` at the start of your terminal line.

## 5. Install Dependencies
```
pip install requests pandas sqlalchemy psycopg2-binary python-dotenv matplotlib streamlit
```

Save dependencies:
```
pip freeze > requirements.txt
```

## 6. Run the ETL Pipeline

```
python app/pipeline.py
```

### Expected Flow

1. Extract weather data from OpenWeather API  
2. Save raw JSON to `data/raw/`  
3. Transform into structured DataFrame  
4. Save processed data to `data/processed/`  
5. Load into PostgreSQL  

## 7. Stop or Reset the Database

Stop containers:

```
docker compose down
```

Stop and delete database volume (full reset):
```
docker compose down -v
```

## Features

- Modular architecture (extract / transform / load separation)
- Environment variable configuration
- Dockerized database
- Logging support
- Error handling
- Reproducible environment via `requirements.txt`

## Future Improvements

- Add Airflow orchestration  
- Deploy raw storage to AWS S3  
- Add automated tests  
- Add CI/CD pipeline  
- Expand dashboard with Streamlit  

