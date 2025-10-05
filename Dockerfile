# syntax=docker/dockerfile:1

FROM --platform=linux/amd32 tiangolo/uvicorn-gunicorn-fastapi:python3.9

LABEL maintainer="indrapaul824 - Indrashis Paul"

WORKDIR /app

RUN mkdir -p /app/artifacts

COPY requirements.txt requirements.txt
COPY server_start.sh server_start.sh

RUN chmod +x server_start.sh

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./scripts/api/app.py /app/
COPY ./artifacts /app/artifacts

CMD ["./server_start.sh"]
