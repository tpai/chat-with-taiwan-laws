FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY faiss_index faiss_index
COPY main.py .

CMD ["streamlit", "run", "main.py"]