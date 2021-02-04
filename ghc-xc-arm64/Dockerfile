FROM debian:buster AS builder

RUN grep -v "^#" /etc/apt/sources.list | sed "s/deb /deb-src /g" > apt.tmp \
  && cat apt.tmp >> /etc/apt/sources.list \
  && apt-get update \
  && apt-get build-dep -y ghc \
  && apt-get install -y \
    alex happy \
    git \
    gcc-aarch64-linux-gnu \
  && git clone https://gitlab.haskell.org/ghc/ghc.git && cd ghc \
  && git checkout tags/ghc-8.8.4-release \
  && git submodule update --init --recursive \
  && sed 's/#.* = quick-cross/BuildFlavour = quick-cross/' mk/build.mk.sample > mk/build.mk \
  && perl boot \
  && ./configure --target=aarch64-linux-gnu --prefix=/ghc-cross/ --enable-unregisterised \
  && make -j2 \
  && make install


FROM debian:buster-slim

COPY --from=builder /ghc-cross /ghc-cross

RUN apt update \
  && apt install -y libatomic1 gcc-aarch64-linux-gnu \
  && rm -rf /var/lib/apt/lists/*

