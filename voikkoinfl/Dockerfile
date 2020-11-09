FROM python:3.9-slim as builder

WORKDIR /temp_dir
COPY process_infl.py /temp_dir

# "builder-image" for downloading subst.aff and verb.aff
# and constructing inflection class dict
RUN pip install xmltodict \
  && apt-get update \
  && apt-get install -y curl \
  && curl https://raw.githubusercontent.com/voikko/corevoikko/master/data/subst.aff > subst.aff \
  && curl https://raw.githubusercontent.com/voikko/corevoikko/master/data/verb.aff > verb.aff \
  && curl https://raw.githubusercontent.com/voikko/corevoikko/master/voikko-fi/vocabulary/joukahainen.xml > joukahainen.xml \
  && ./process_infl.py \
  && rm joukahainen.xml

FROM python:3.9-slim

RUN pip install voikko

ENV LC_ALL C.UTF-8

WORKDIR /app
COPY app.py /app/
COPY --from=builder /temp_dir/ /app/

ENTRYPOINT ["python", "./app.py"]

