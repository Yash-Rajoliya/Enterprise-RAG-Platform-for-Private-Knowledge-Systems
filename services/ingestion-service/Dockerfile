FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install \
    fastapi \
    uvicorn \
    pypdf \
    python-docx \
    beautifulsoup4 \
    boto3 \
    httpx

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8002"]