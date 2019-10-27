FROM paasim/agda

COPY emacs /root/.emacs

RUN git clone https://github.com/plfa/plfa.github.io plfa \
  && echo "/data/plfa/plfa.agda-lib" >> ~/.agda/libraries \
  && echo "plfa" >> ~/.agda/defaults

WORKDIR /data/plfa/src/plfa

