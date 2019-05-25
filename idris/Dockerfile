FROM haskell

RUN git clone https://github.com/idris-lang/Idris-dev.git idris && cd idris \
  && cabal update \
  && make \
  && cabal install idris

WORKDIR /data

ENTRYPOINT ["idris"]
