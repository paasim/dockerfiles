FROM debian as build

RUN apt-get update \
  && apt-get install -y curl \
  && curl -sSL https://get.haskellstack.org/ | sh \
  && git clone https://github.com/paasim/timer.git \
  && cd timer \
  && stack install --resolver lts-13.11

FROM scratch

COPY --from=build /root/.local/bin/timer-exe /timer

ENTRYPOINT ["./timer"]

