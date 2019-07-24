FROM nvcr.io/nvidia/l4t-base:r32.2

# h5py with apt as I was not able to get pip find the correct headers (libhdf5-dev)
RUN sudo apt-get update \
  && sudo apt-get install -y \
   zlib1g-dev \
   zip \
   libjpeg8-dev \
   python3-pip \
   python3-h5py \
  && sudo pip3 install -U pip \
  && sudo pip3 install -U \
   numpy \
   grpcio \
   absl-py \
   py-cpuinfo \
   psutil \
   portpicker \
   six \
   mock \
   requests \
   gast \
   astor \
   termcolor \
   protobuf \
   keras-applications \
   keras-preprocessing \
   wrapt \
   google-pasta \
  && sudo pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v42 tensorflow-gpu \
  && rm -rf /var/lib/apt/lists/* 

