FROM python:3.11-slim AS builder

ENV LANG=es_CL.UTF-8 \
    LANGUAGE=es_CL:es \
    LC_ALL=es_CL.UTF-8

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim

ENV LANG=es_CL.UTF-8 \
    LANGUAGE=es_CL:es \
    LC_ALL=es_CL.UTF-8

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY ./app /app

RUN addgroup --system appgroup && adduser --system --group appuser
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
