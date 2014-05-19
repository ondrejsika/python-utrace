#!/usr/bin/python

# utrace api
############

# author: Ondrej Sika, http://ondrejsika.com, ondrej@ondrejsika.com
# licence: MIT


from xml.etree import ElementTree as ET
import requests


UTRACE_ORIGIN = 'http://xml.utrace.de'

def utrace(query, origin=UTRACE_ORIGIN):
    url = origin + '/?query=' + query
    response = requests.get(url).text
    xml_root = ET.fromstring(response)
    results = []
    for xml_result in xml_root.findall('result'):
        result = {}
        for attr in xml_result.iter():
            val = attr.text
            if attr.tag in ('latitude', 'longitude', ):
                val = float(val)
            if attr.tag == 'queries':
                val = int(val)
            result[attr.tag] = val
        results.append(result)
    return results

