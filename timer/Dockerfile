FROM haskell as build

RUN git clone https://github.com/paasim/timer.git \
  && cd timer \
  && stack install --install-ghc

FROM scratch

COPY --from=build /root/.local/bin/timer-exe /timer

ENTRYPOINT ["./timer"]

