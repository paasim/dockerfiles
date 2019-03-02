FROM jackfirth/racket

RUN raco pkg install --auto pie

WORKDIR /data
CMD ["racket","-l","xrepl","-i"]
