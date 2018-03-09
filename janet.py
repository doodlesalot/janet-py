#!/usr/bin/env python
import requests
from secrets import zendesk_user, zendesk_token
from util import jprint
import urllib.parse
import sys
from collections import Counter

#Your ZD info
USER = zendesk_user + '/token'
PWD = zendesk_token
VIEWS = viewid
ZENDESK_SUBDOMAIN = zendesk_subdomain
#Just Slack Thingz
SLACK_WEBHOOK_URL = slack_webhook

view_url_encoded = urllib.parse.quote(VIEWS)
url = 'https://%s.zendesk.com/api/v2/views/%s/tickets.json?sort_by=updated_requester,asc' % (ZENDESK_SUBDOMAIN, view_url_encoded)

response = requests.get(url, auth=(USER, PWD))
data = response.json()

tickets = data['tickets']

tixcount = len(tickets)

if tixcount > 100:
    slack_data = "Welcome to the Emergency Operation Tier :boat: There are currently %s tickets"
elif tixcount > 80:
    slack_data = "80+ tix in the boundless void. Hop on in!"
elif tixcount > 50:
    slack_data = "There are 50+ tix awaiting you! %s to be exact.\n" % (tixcount)
elif tixcount > 30:
    slack_data = "In the zoooone! By zone, I mean we're looking at relatively low numbers now! %s tickets up for the taking.\n" % (tixcount)
else:
    slack_data = "There are less than 30 tix, carry on\n"

# Send the message to Slack.
slack_payload = {"channel": "support", "username": "janet", "text": slack_data, "icon_emoji": ":janet:"}
post_req = requests.post(SLACK_WEBHOOK_URL, json=slack_payload)

if post_req.status_code == 200:
    print ("Posted.")
else:
    print ("Failed: {0}, {1}".format(post_req.status_code,post_req.text))