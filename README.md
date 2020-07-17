# vietanh
A repository of words extracted from a viet anh dictionary (FVDP Vietnamese-English dictionary) along w/ code and sources

# Quickstart

Download `dump-utf8.json` and use it in your program.

# How to reproduce

- Go to http://www.informatik.uni-leipzig.de/~duc/Dict/install.html and download VietAnh.zip, these scripts should work for anything you can download there (actually, this should work for any Dictionary files stored according to the DICT Protocol)
  - I have backed up these files to my Dropbox in case the server goes down. Email me at contactme AT {github_username} DOT com

- Extract it and find the files `vietanh.dict.dz` `vietanh.index`.

- Run `dictdlib.py` in a Python 2.7 environment. This will generate `dump.json`
  - DISCLAIMER: `dictdlib.py` was taken from https://github.com/jgoerzen/dictdlib/blob/master/dictdlib.py so thanks to `jgoerzen` who wrote this 18 years ago.
  - If you are reading a different dictionary, you're going to need to change `vietanh` on line 380 to the name of the dictionary files.

- Now you have a json file of 23,434 vietnamese words and their definitions in English!

- If you want the file to use utf-8 so it's legible, run `convert.py` with Python 3 (I used 3.8 but earlier releases should work)


# Notice

It should be noted that the dumps have the licensing info included with them, look under key `00-database-info`.

```
This is the Vietnamese-English dictionary database of the Free Vietnamese Dictionary Project. It contains more than 23.400 entries with definitions and illustrative examples.\n- This database was compiled by Ho Ngoc Duc and other members of the Free Vietnamese Dictionary Project (http://www.informatik.uni-leipzig.de/~duc/Dict/)\n- Copyright (C) 1997-2003 The Free Vietnamese Dictionary Project\n- This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
```
