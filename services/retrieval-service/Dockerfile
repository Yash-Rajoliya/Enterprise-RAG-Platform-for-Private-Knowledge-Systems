FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install \
    fastapi \
    uvicorn \
    faiss-cpu \
    rank_bm25 \
    sentence-transformers \
    pytest

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8001"]