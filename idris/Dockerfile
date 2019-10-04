FROM haskell:8.6.5

RUN cabal update \
  && cabal install idris

WORKDIR /data

ENTRYPOINT ["idris"]

