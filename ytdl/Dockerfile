FROM alpine

ENV LC_ALL=C.UTF-8 

RUN apk add --no-cache youtube-dl \
  && adduser -D app

USER app

WORKDIR /data

ENTRYPOINT ["youtube-dl"]
