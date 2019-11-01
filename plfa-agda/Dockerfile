FROM paasim/agda

ENV ruby_ver 2.5.7

COPY emacs /root/.emacs

RUN git clone https://github.com/plfa/plfa.github.io plfa \
  && echo "/data/plfa/plfa.agda-lib" >> ~/.agda/libraries \
  && echo "plfa" >> ~/.agda/defaults \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
    git curl libssl-dev libreadline-dev zlib1g-dev \
    autoconf bison build-essential libyaml-dev \
    libreadline-dev libncurses5-dev libffi-dev libgdbm-dev \
  && export PATH=$PATH:/root/.rbenv/bin:/root/.rbenv/shims:/root/.rbenv/versions/$ruby_ver/bin \
  && curl -sL https://github.com/rbenv/rbenv-installer/raw/master/bin/rbenv-installer | bash - \
  && rm -rf /var/lib/apt/lists/* \
  && rbenv install $ruby_ver \
  && gem install bundler \
  && cd /data/plfa \
  && bundle install

EXPOSE 4000
WORKDIR /data/plfa
ENV PATH="${PATH}:/root/.rbenv/versions/$ruby_ver/bin"

RUN make build

