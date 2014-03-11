#!/usr/bin/python

def print_tweet(tweet):
    # tweet information description: https://dev.twitter.com/docs/platform-objects/tweets
    try: #sometimes tweets are misformed
        print '\033[1m%s @%s\033[0m' % (tweet['created_at'], tweet['user']['screen_name'])
    except:
        return

    if tweet['coordinates']: # there are geo coordinates attached
        lon, lat = tweet['coordinates']['coordinates']
        print 'Location: %f, %f' % (lon, lat)
    else:
        print 'Location: None'
    print tweet['text']
