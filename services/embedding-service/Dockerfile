FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install \
    fastapi \
    uvicorn \
    openai \
    sentence-transformers \
    torch

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8004"]