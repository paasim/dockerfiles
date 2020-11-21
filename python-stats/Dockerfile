FROM python:3.8

RUN pip install --upgrade \
    cmdstanpy[all] \
    matplotlib \
    mypy \
    scikit-learn \
    statsmodels \
    tensorflow \
    xgboost \
  && install_cmdstan \
  && apt-get update \
  && apt-get install -y \
    vim \
  && rm -rf /var/lib/apt/lists/*

