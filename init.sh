#!/bin/bash
GREEN='\033[0;32m'
PURPLE='\033[0;35m'
NC='\033[0m'

echo "${PURPLE}pip install torch torchvision${NC}"
pip install torch torchvision

pip install future
sudo pip install Pillow
sudo python3 -m pip install Pillow
sudo pip install scipy --ignore-installed scipy
#sudo apt-get install python-scipy

sudo pip install h5py
#echo "${PURPLE}pip install librosa${NC}"
#sudo pip install librosa
pip install python_speech_features
