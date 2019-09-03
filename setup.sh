#!/bin/bash

sudo apt-get update
wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
chmod +x miniconda.sh
./miniconda.sh -b
export PATH=/home/travis/miniconda3/bin:$PATH
conda config --set always_yes yes --set changeps1 no
conda update conda
conda info -a
conda env create -n dev -f environment.yml
source activate dev
