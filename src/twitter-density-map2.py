#!/usr/bin/python

from twitter import *
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from tools import print_tweet

search_for = 'flu'

m = Basemap(projection='robin',lon_0=0,resolution='c')
m.drawcoastlines()
m.fillcontinents(color='coral',lake_color='aqua')
m.drawmapboundary(fill_color='aqua')
plt.title("Density Map")

auth = OAuth(
    '1384877240-NozLxjgB70Ifi2E6QRIuXYIsSUV6LPX5p2Wxi8w',
    'sf7lcW7OnA0lDv42XNrFKohty1j9Mlr4svCMy9WAkwjKV',
    'kv3sQwgtqbkX1imffNyog',
    'yofslYiwVV8SAqQHnxWSwjOG2H8Uo9w2wfqID5Cc')

t = Twitter(auth=auth)

nr_geos = 0

tweets = t.search.tweets(q=search_for, count=100, locations='-180,-90,180,90')['statuses']

for tweet in tweets:
    # tweet information description: https://dev.twitter.com/docs/platform-objects/tweets
    print_tweet(tweet)
    lon, lat = tweet['coordinates']['coordinates']
    x,y = m(lon, lat)
    m.plot(x, y, 'bo', markersize=8)

print "number of tweets: %i" % len(tweets)
plt.show()