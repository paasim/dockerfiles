FROM python:slim

WORKDIR /app

RUN pip install voikko \
  && apt-get update \
  && apt-get install -y curl \
  && curl https://raw.githubusercontent.com/voikko/corevoikko/master/data/subst.aff > subst.aff \
  && apt-get purge -y --auto-remove curl \
  && rm -rf fintag.zip /var/lib/apt/lists/*

ENV LC_ALL C.UTF-8

COPY app.py /app/
ENTRYPOINT ["python", "./app.py"]

