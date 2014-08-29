###################################################################################
# Twitter API scraper - designed to be forked and used for more interesting things
###################################################################################

import scraperwiki
import simplejson
import urllib2

# Get results from the Twitter API! Change QUERY to your search term of choice. 
# Examples: 'PCC "Police Commissioner"
QUERY = 'Police Commissioner'
RESULTS_PER_PAGE = '100'
LANGUAGE = 'eng'
NUM_PAGES = 20 

for page in range(1, NUM_PAGES+1):
    base_url = 'http://search.twitter.com/search.json?q=%s&rpp=%s' \
         % (urllib2.quote(QUERY), RESULTS_PER_PAGE)
    try:
        results_json = simplejson.loads(scraperwiki.scrape(base_url))
        for result in results_json['results']:
            data = {}
            data['id'] = result['id']
            data['text'] = result['text']
            data['from_user'] = result['from_user']
            print data['from_user'], data['text']
    except:
        pass