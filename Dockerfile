FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm

EXPOSE 8001

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8001"]