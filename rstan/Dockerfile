FROM rocker/verse:4.0.3

COPY Makevars /root/.R/Makevars

RUN mkdir -p /home/rstudio/.R \
  && cp /root/.R/Makevars /home/rstudio/.R/Makevars \
  && install2.r --error loo shinystan \
  && installGithub.r stan-dev/cmdstanr \
  && R -e 'fs::dir_create("/home/rstudio/.cmdstanr"); cmdstanr::install_cmdstan("/home/rstudio/.cmdstanr")'

