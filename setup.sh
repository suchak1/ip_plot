#!/bin/bash

sudo apt-get update
wget https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh -O anaconda.sh
chmod +x anaconda.sh
./anaconda.sh -b
sudo chown -R travis "$HOME/anaconda3"
export PATH="$HOME/anaconda3/bin:$PATH"
hash -r
conda config --set always_yes yes --set changeps1 no
conda update conda
conda info -a
conda env create -n dev -f environment.yml
source activate dev
