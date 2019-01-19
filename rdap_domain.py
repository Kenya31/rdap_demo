# -*- coding: utf-8 -*-

import json
import requests

if __name__ == "__main__":
    TARGET = 'google.com'
    URL = 'http://rdap.org/domain/' + TARGET
    RES = requests.get(URL)
    RES_JSON = json.loads(RES.text)
    with open('result_domain.json', 'w', encoding='utf-8-sig') as f:
        f.write(json.dumps(RES_JSON, ensure_ascii=False,
                           indent=4, separators=(',', ': ')))
