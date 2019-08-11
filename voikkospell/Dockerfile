FROM debian

RUN apt update \
  && apt install -y voikko-fi libvoikko-dev \
  && rm -rf /var/lib/apt/lists/*

ENV LC_ALL C.UTF-8

CMD ["voikkospell", "-m"]

