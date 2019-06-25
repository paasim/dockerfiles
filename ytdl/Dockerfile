FROM alpine

ENV LC_ALL=C.UTF-8 

WORKDIR /data

RUN apk add --no-cache youtube-dl \
  && addgroup -S app \
  && adduser -D -h $(pwd) -S app -G app

USER app

ENTRYPOINT ["youtube-dl"]

