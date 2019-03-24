FROM python

RUN DEBIAN_FRONTEND=noninteractive \
  && pip install voikko \
  && curl https://raw.githubusercontent.com/voikko/corevoikko/master/data/subst.aff > /root/subst.aff

WORKDIR /root/
COPY app.py /root/
ENTRYPOINT ["python", "./app.py"]

