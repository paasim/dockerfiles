FROM arm32v7/debian

RUN apt-get update \
  # llvm needed for compiling
  && apt-get install -y curl llvm \
  && curl -sSL https://get.haskellstack.org/ | sh \
  && rm -rf /var/lib/apt/lists/*

