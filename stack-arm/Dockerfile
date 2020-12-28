FROM arm32v7/debian:bullseye-slim

RUN apt-get update \
  && apt-get install -y haskell-stack ghc \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# for GHC 8.8.4
ENV RESOLVER=lts-16.27

ENTRYPOINT stack install --resolver $RESOLVER --system-ghc

