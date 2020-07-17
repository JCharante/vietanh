# Python 3.8
import json
from typing import Dict
import codecs

with open("dump.json", "r") as fp:
    data = json.load(fp) # type: Dict

# Thanks to Trần Quang Hiệp for this helpful line
# source: https://stackoverflow.com/a/40585572
with codecs.open('dump-utf8.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
