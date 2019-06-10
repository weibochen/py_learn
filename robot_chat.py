#!/usr/bin/env python
# coding=utf-8

import urllib
import json
from urllib import request
from urllib import parse

def get_html(url, data):
    page = request.urlopen(url, data)
    html = page.read()
    html = html.decode("utf-8")
    return html

if __name__ == "__main__":
    key = "feed526ff94e4923b2e6c67e57caca38"
    url = "http://www.tuling123.com/openapi/api"
    while True:
        req_info = input('我: ')
        query = {'key': key, 'info': req_info}
        data = parse.urlencode(query).encode('utf-8')
        response = get_html(url, data)
        data = json.loads(response)
        print(data)
        print('机器人: ' + data['text'])

