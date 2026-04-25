FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Run BOTH subscriber + API + dashboard
CMD ["sh", "-c", "python mqtt_subscriber.py & uvicorn api:app --host 0.0.0.0 --port 8000 & streamlit run dashboard.py --server.port=8501 --server.address=0.0.0.0"]