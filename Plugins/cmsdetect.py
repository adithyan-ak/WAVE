import os
import requests

def CMSdetect(domain, port):
    api_key = os.getenv('WHATCMS_API_KEY')
    if not api_key:
        raise ValueError('API key for WhatCMS not found in environment variable WHATCMS_API_KEY')
    # Additional check to ensure the API key is not empty or whitespace
    if not api_key.strip():
        raise ValueError('API key for WhatCMS is empty or invalid')
    payload = {'key': api_key, 'url': domain}
    cms_url = "https://whatcms.org/APIEndpoint/Detect"
    try:
        response = requests.get(cms_url, params=payload, timeout=10)
        response.raise_for_status()
        cms_data = response.json()
    except (requests.RequestException, ValueError) as e:
        print(f"Error fetching or parsing CMS data: {e}")
        return
    if not isinstance(cms_data, dict):
        print("Unexpected API response format: root element is not a dictionary.")
        return
    cms_info = cms_data.get('result')
    if not isinstance(cms_info, dict):
        print("Unexpected API response format: 'result' key missing or not a dictionary.")
        return
    code = cms_info.get('code')
    if code == 200:
        name = cms_info.get('name', 'N/A')
        version = cms_info.get('version', 'N/A')
        confidence = cms_info.get('confidence', 'N/A')
        print('Detected CMS     : %s' % name)
        print('Detected Version : %s' % version)
        print('Confidence       : %s' % confidence)
    else:
        msg = cms_info.get('msg', 'No message provided')
        name = cms_info.get('name', 'N/A')
        version = cms_info.get('version', 'N/A')
        print(msg)
        print('Detected CMS : %s' % name)
        print('Detected Version : %s' % version)