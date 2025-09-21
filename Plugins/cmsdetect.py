import os
import requests

def CMSdetect(domain, port):
    api_key = os.getenv('WHATCMS_API_KEY')
    if not api_key:
        raise ValueError('API key for WhatCMS not found in environment variable WHATCMS_API_KEY')
    payload = {'key': api_key, 'url': domain}
    cms_url = "https://whatcms.org/APIEndpoint/Detect"
    response = requests.get(cms_url, params=payload)
    cms_data = response.json()
    cms_info = cms_data['result']
    if cms_info['code'] == 200:
        print('Detected CMS     : %s' % cms_info['name'])
        print('Detected Version : %s' % cms_info['version'])
        print('Confidence       : %s' % cms_info['confidence'])
    else:
        print(cms_info['msg'])
        print('Detected CMS : %s' % cms_info['name'])
        print('Detected Version : %s' % cms_info['version'])