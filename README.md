# vietanh
repository of words extracted from a viet anh dictionary along w/ code and sources

# Quickstart

Download `dump.json` and use it in your program.

# How to reproduce

- Go to http://www.informatik.uni-leipzig.de/~duc/Dict/install.html and download VietAnh.zip, these scripts should work for anything you can download there (actually, this should work for any Dictionary files stored according to the DICT Protocol)
  - I have backed up these files to my Dropbox in case the server goes down. Email me at contactme AT {github_username} DOT com

- Extract it and find the files `vietanh.dict.dz` `vietanh.index`.

- Run `dictdlib.py` in a Python 2.7 environment. This will generate `dump.json`
  - DISCLAIMER: `dictdlib.py` was taken from https://github.com/jgoerzen/dictdlib/blob/master/dictdlib.py so thanks to `jgoerzen` who wrote this 18 years ago.

Now you have a json file of 23,434 vietnamese words and their definitions in English.

