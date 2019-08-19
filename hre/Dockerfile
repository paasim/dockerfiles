FROM arm32v7/debian:9-slim

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    netbase \
    ca-certificates \
    libgmp10 \
  && rm -rf /var/lib/apt/lists/*

