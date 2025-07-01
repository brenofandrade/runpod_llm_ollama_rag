FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && pip install --no-cache-dir r-r requirements.txt

EXPOSE 7860

CMD ["streamlit","run","src/app.py","--server.address=0.0.0.0","--server.port=7860","--server.enableCORS=false","--server.headless=true","--server.enableWebsocketCompression=false"]