FROM python:3.8

RUN pip install --upgrade \
    cmdstanpy[all] \
    matplotlib \
    pylint \
    scikit-learn \
    tensorflow \
    xgboost \
  && install_cmdstan \
  && apt-get update \
  && apt-get install -y \
    vim \
  && rm -rf /var/lib/apt/lists/*

