ARG BASE_IMAGE=python:3.12-slim
FROM ${BASE_IMAGE} as build
RUN apt-get update && apt-get install -y libgl1 libwebkit2gtk-4.0-37 \
    && pip install --no-cache-dir -r requirements.txt
ENV PYTHONUNBUFFERED=1
COPY ytm_player /app/ytm_player
ENTRYPOINT ["python", "-m", "ytm_player"]
