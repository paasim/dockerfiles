FROM rocker/r-ver

COPY Makevars /root/.R/Makevars

RUN mkdir -p /home/rstudio/.R \
  && cp /root/.R/Makevars /home/rstudio/.R/Makevars \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
      libxml2-dev \
      libcairo2-dev \
      libsqlite3-dev \
      libmariadbd-dev \
      libmariadb-client-lgpl-dev \
      libpq-dev \
      libssh2-1-dev \
      unixodbc-dev \
      libsasl2-dev \
  && install2.r --error --deps TRUE \
      tidyverse \
      dplyr \
      devtools \
      remotes \
      rstan \
      loo \
      rstanarm \
      shinystan \
  && installGithub.r paasim/stanutils

