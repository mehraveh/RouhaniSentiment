from InstagramAPI import InstagramAPI
import time
from datetime import datetime
import requests

url = 'https://www.instagram.com/p/BUNuM6vlfp4/?hl=en&taken-by=hrouhani'
req = requests.get('https://api.instagram.com/oembed/?url={}'.format(url))
media_id = req.json()['media_id']

# stop conditions, the script will end when first of them will be true
until_date = '2018-07-07'
count = 3000

API = InstagramAPI("mehrii.m.m", "khkmkmp22")
API.login()
# API.getUsernameInfo('mahnaz_afshar')
has_more_comments = True
max_id = ''
comments = []
cnt = 0
file1 = open('rohaniBeforeCommentsTest.txt', 'a')
while has_more_comments:
    cnt += 1

    _ = API.getMediaComments(media_id, max_id=max_id)
    # comments' page come from older to newer, lets preserve desc order in full list
    ct = 0
    for c in reversed(API.LastJson['comments']):
        comments.append(c)
        text = c['text']
        txt = text.encode('utf-8')
        file1.writelines(txt + '\n')

    has_more_comments = API.LastJson.get('has_more_comments', True)

    # evaluate stop conditions
    if count and len(comments) >= count:
        comments = comments[:count]
        # stop loop
        has_more_comments = False
        print("stopped by count")
    if until_date:

        older_comment = comments[-1]
        dt = datetime.utcfromtimestamp(older_comment.get('created_at_utc', 0))
        # only check all records if the last is older than stop condition


    # next page
    print('has_more_comments2   ', has_more_comments)
    if has_more_comments:
        max_id = API.LastJson.get('next_max_id', '')

file1.close()

