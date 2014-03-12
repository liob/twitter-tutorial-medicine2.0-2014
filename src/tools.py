#!/usr/bin/python

def print_tweet(tweet):
    # tweet information description: https://dev.twitter.com/docs/platform-objects/tweets
    try: #sometimes tweets are misformed
        print '\033[1m%s @%s\033[0m' % (tweet['created_at'], tweet['user']['screen_name'])
    except:
        return

    geolocation = get_geolocation(tweet)
    if geolocation:
        lon, lat = geolocation['coordinates']
        print 'Location: %f, %f  (%s)' % (lon, lat, geolocation['type'])
    else:
        print 'Location: None'

    print tweet['text']


def get_geolocation(tweet):
    if tweet['coordinates']:
        # the tweet has geolocation attached. return it
        return dict(type = 'exact', coordinates = tweet['coordinates']['coordinates'])

    if tweet['place']:
        coordinates = tweet['place']['bounding_box']['coordinates'][0]
        for coordinate in tweet['place']['bounding_box']['coordinates'][1:]:
            coordinates = [(coordinates[0] + coordinate[0]) / 2, (coordinates[1] + coordinate[1]) / 2]
        return dict(type = 'approx', coordinates = coordinates)

    # no geolocation found!
    return False
