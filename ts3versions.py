#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lxml.html
import json
from distutils.version import LooseVersion
from datetime import datetime

baseurl = 'http://dl.4players.de/ts/releases/'
data = {'latest': None, 'versions': []}

releases = lxml.html.parse(baseurl).getroot()
for element,attribute,rlink,pos in releases.iterlinks():
  if element.tag is 'a' \
  and attribute is 'href' \
  and rlink.startswith('3.'):
    files = lxml.html.parse(baseurl + rlink).getroot()
    for element,attribute,flink,pos in files.iterlinks():
      if element.tag is 'a' \
      and attribute is 'href' \
      and flink.find('-server_') > 0:
        data['versions'].append(rlink.strip('/'))
        break

data['versions'].sort(key=LooseVersion)
data['latest'] = data['versions'][-1]
data['checked'] = datetime.utcnow().strftime("%Y%m%d %H:%M:%S +0000 (UTC)")

print json.dumps(data, sort_keys=True, indent=2)
