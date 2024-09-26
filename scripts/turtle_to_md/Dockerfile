FROM python:3.10.15-bookworm

WORKDIR /app
COPY . .
RUN python3 -m pip install --no-cache-dir --progress-bar off -U pip && \
    python3 -m pip install --no-cache-dir --progress-bar off -e .[tests]

ENTRYPOINT ["turtle_to_md"]
