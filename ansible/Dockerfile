FROM debian

COPY ansible.list /ansible.list

RUN apt-get update \
  && apt-get install -y gnupg2 \
  && mv /ansible.list /etc/apt/sources.list.d/ \
  && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367 \
  && apt-get purge -y --auto-remove gnupg2 \
  && apt-get update \
  && apt-get install -y ansible \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /data

ENTRYPOINT ["ansible"]


