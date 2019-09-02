import os
import pandas as pd
import geopandas as gpd
import requests
import random
import matplotlib as mpl
if os.environ.get('DISPLAY', '') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt


def dev_build():
    return os.environ['build'] == 'dev'


def read_ip_addrs(filename):
    with open(filename) as fp:
        return fp.read().splitlines()


def ip2geo(addr, api_key):
    url = 'http://api.ipstack.com/'
    endpoint = url + addr + '?access_key=' + api_key

    response = requests.get(endpoint)
    data = response.json()

    lat = data['latitude']
    long = data['longitude']
    geo = {'lat': lat, 'long': long}
    return geo


def get_points(addrs, api_key):
    lats = []
    longs = []

    for addr in addrs:
        geo = ip2geo(addr, api_key)
        lats.append(geo['lat'])
        longs.append(geo['long'])

    geos = {'lats': lats, 'longs': longs}
    return geos


def gpd_plot(points):
    df = pd.DataFrame(points)
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longs, df.lats))
    print(gdf.head())
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    ax = world.plot()
    gdf.plot(ax=ax, marker='*', color='red', markersize=20)
    plt.savefig('map.png', format='png', dpi=1200)
    plt.savefig('map.svg', format='svg', dpi=1200)
    plt.show()


def main():
    if dev_build():
        ipstack = os.environ['ipstack']
    else:
        from creds import getLogin
        ipstack = getLogin('ipstack')['api_key']

    filename = 'mock_data.txt'
    print('Reading ip addresses from mock data...')
    addrs = read_ip_addrs(filename)
    print('Done reading.')

    print('Shuffling mock data...')
    random.shuffle(addrs)
    choose = 10
    data = addrs[:choose]
    print('Done shuffling.')

    # ip = requests.get('https://api.ipify.org').text
    # geo = ip2geo(ip)
    # print(geo)

    # df = pd.DataFrame({'lat': [geo['lat']], 'long': [geo['long']]})
    # print(data)

    # geos = get_points(data, ipstack)
    geos = {
            'lats': [
                37.56100082397461, None, 36.078330993652344, 42.50128936767578,
                41.84885025024414, 13.756329536437988, 35.69628143310547,
                43.034759521484375, -33.86714172363281, None],
            'longs': [
                126.98265075683594, None, 120.3369369506836, -71.06672668457031,
                -87.67124938964844, 100.50177001953125, 139.73855590820312,
                -78.50792694091797, 151.2071075439453, None]
            }
    print('Plotting points...')
    gpd_plot(geos)
    print('Success.')
    return 0


main()

# print(read_ip_addrs('mock_data1.txt'))

# print(ip2geo('205.153.95.177'))

# 38.85377883911133
# -77.04876708984375
# print(dir(plt))
