#!/usr/bin/python

from twitter import *
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


map = Basemap(projection='merc', lat_0 = 50, lon_0 = -100,
              resolution = 'l', area_thresh = 1000.)
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color = 'coral')
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
plt.show()

auth = OAuth(
    '1384877240-NozLxjgB70Ifi2E6QRIuXYIsSUV6LPX5p2Wxi8w',
    'sf7lcW7OnA0lDv42XNrFKohty1j9Mlr4svCMy9WAkwjKV',
    'kv3sQwgtqbkX1imffNyog',
    'yofslYiwVV8SAqQHnxWSwjOG2H8Uo9w2wfqID5Cc')

ts = TwitterStream(auth=auth)

openstream = ts.statuses.filter(track='flu')

for item in openstream:
    print "id:%s %s :: %s" % (item['id'], str(item['coordinates']), item['text'])

