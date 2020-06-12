FROM rocker/geospatial

COPY Makevars /root/.R/Makevars

RUN mkdir -p /home/rstudio/.R \
  && cp /root/.R/Makevars /home/rstudio/.R/Makevars \
  && install2.r --error rstan loo rstanarm shinystan
