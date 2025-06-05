ARG BASE_IMAGE=python:3.12-slim
FROM ${BASE_IMAGE}
WORKDIR /app
RUN apt-get update \
    && apt-get install --no-install-recommends -y libgl1 libwebkit2gtk-4.0-37 \
    && rm -rf /var/lib/apt/lists/*
COPY pyproject.toml requirements.txt ./
RUN pip install --no-cache-dir .
ENV PYTHONUNBUFFERED=1
COPY ytm_player ./ytm_player
ENTRYPOINT ["yt-music-player"]
