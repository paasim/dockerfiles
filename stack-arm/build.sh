#/usr/bin/env bash
# for GHC 8.8.4 and
# RESOLVER=lts-16.27

docker run --rm -it \
  -v $1:/app \
  -v $(pwd)/bin:/root/.local/bin \
  -v $(pwd)/.stack:/root/.stack \
  paasim/stack-arm \
  stack install --resolver lts-16.27 --system-ghc

