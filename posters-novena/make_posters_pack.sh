#!/bin/sh

# Build script that works best on Ubuntu / Debian systems, with Python 3.x and Inkscape

# Run this script from the same directory as translate.py 
if ! [ -f translate.py ]; then
  echo "translate.py must be in the current directory"; exit 1
fi
mkdir -p ~/.local/share/fonts
cp asset/04b_03/*.TTF ~/.local/share/fonts
fc-cache -f -v
# grab inkscape 1.x
sudo add-apt-repository ppa:inkscape.dev/stable
sudo apt update
sudo apt install inkscape
python3 translate.py
