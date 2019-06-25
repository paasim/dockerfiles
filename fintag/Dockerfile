FROM python:3

RUN curl -sS https://korp.csc.fi/download/finnish-tagtools/v1.3/finnish-tagtools-1.3.2.zip > fintag.zip \
  && unzip fintag.zip \
  && rm fintag.zip

WORKDIR /finnish-tagtools-1.3.2
ENTRYPOINT ["./finnish-postag"]

