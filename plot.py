import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from creds import getLogin
import requests


def read_ip_addrs(filename):
    with open(filename) as fp:
        return fp.read().splitlines()


def ip2geo(addr):
    url = 'http://api.ipstack.com/'
    api_key = getLogin('ipstack')['api_key']
    endpoint = url + addr + '?access_key=' + api_key
    response = requests.get(endpoint)
    data = response.json()
    lat = data['latitude']
    long = data['longitude']
    return {'lat': lat, 'long': long}


# print(read_ip_addrs('mock_data1.txt'))
print(ip2geo('205.153.95.177'))
# print(dir(plt))
