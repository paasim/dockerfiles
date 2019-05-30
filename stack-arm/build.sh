#/usr/bin/env bash
docker run --rm -it -v $1:/app -v $(pwd):/root/.local/bin paasim/stack-arm 
