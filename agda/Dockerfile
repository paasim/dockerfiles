FROM haskell:8.6

WORKDIR /data

RUN apt-get update \
  && apt-get install -y emacs wget vim \
  && rm -rf /var/lib/apt/lists/* \
  && cabal update \
  && cabal install alex happy \
  && cabal install Agda \
  && wget -O agda-stdlib.tar https://github.com/agda/agda-stdlib/archive/v1.1.tar.gz \
  && tar -xzvf agda-stdlib.tar \
  && rm agda-stdlib.tar \
  && cd agda-stdlib-1.1 \
  && cabal install

COPY emacs /root/.emacs
COPY agda_libraries /root/.agda/libraries
COPY agda_defaults /root/.agda/defaults

ENTRYPOINT bash

