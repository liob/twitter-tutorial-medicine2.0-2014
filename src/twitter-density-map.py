#!/usr/bin/python

from twitter import *
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from tools import print_tweet, get_geolocation


search_for = 'flu'

m = Basemap(projection='robin',lon_0=0,resolution='c')
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
m.drawmapboundary(fill_color='aqua')
plt.title("Density Map")
plt.show(block=False)

auth = OAuth(
    '1384877240-NozLxjgB70Ifi2E6QRIuXYIsSUV6LPX5p2Wxi8w',
    'sf7lcW7OnA0lDv42XNrFKohty1j9Mlr4svCMy9WAkwjKV',
    'kv3sQwgtqbkX1imffNyog',
    'yofslYiwVV8SAqQHnxWSwjOG2H8Uo9w2wfqID5Cc')

ts = TwitterStream(auth=auth)

stream = ts.statuses.filter(track=search_for)

for tweet in stream:
    # tweet information description: https://dev.twitter.com/docs/platform-objects/tweets
    geolocation = get_geolocation(tweet)
    if geolocation: # there are geo coordinates attached
        lon, lat = geolocation['coordinates']
        x,y = m(lon, lat)
        m.plot(x, y, 'bo', markersize=8)
        plt.draw()
    print_tweet(tweet)
