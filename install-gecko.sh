#!/bin/bash

if geckodriver -V &>/dev/null; then
  echo "geckodriver is already installed."
  exit 0
fi

if ! [ -w /usr/bin ]; then
  echo "Could not write to /usr/bin. Try to run this script as root or install geckodriver manually." >&2
  exit 1
fi

mkdir /tmp/install-gecko/ &>/dev/null
if ! curl -L https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz -o /tmp/install-gecko/gecko.tar.gz &>/dev/null; then
  echo "Script couldn't download archive. Please install geckodriver manually." >&2
  exit 2
fi

tar -xzf /tmp/install-gecko/gecko.tar.gz
mv geckodriver /usr/bin/geckodriver

echo "geckodriver successfully installed."
exit 0

