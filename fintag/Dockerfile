FROM python:slim

RUN curl -sS https://korp.csc.fi/download/finnish-tagtools/v1.4/finnish-tagtools-1.4.0.zip > fintag.zip \
  && unzip fintag.zip \
  && rm fintag.zip

WORKDIR /finnish-tagtools-1.4.0
ENTRYPOINT ["./finnish-postag"]

