FROM python:slim

RUN apt-get update \
  && apt-get install -y curl unzip \
  && curl -sS https://korp.csc.fi/download/finnish-tagtools/v1.4/finnish-tagtools-1.4.0.zip > fintag.zip \
  && unzip fintag.zip \
  && apt-get purge -y --auto-remove unzip curl \
  && rm -rf fintag.zip /var/lib/apt/lists/*

WORKDIR /finnish-tagtools-1.4.0
ENTRYPOINT ["./finnish-postag"]

