FROM arm32v7/debian:bullseye-slim

RUN apt-get update \
  && apt-get install -y haskell-stack ghc zlib1g-dev \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app


