import tweepy
import time
from id_controller import *
from translator import translate

CONSUMER_KEY = 'CONSUMER_KEY'
CONSUMER_SECRET = 'CONSUMER_SECRET'
ACCESS_KEY = 'ACCESS_KEY'
ACCESS_SECRET = 'ACCESS_SECRET'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id()
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id)
        # get parent tweet
        text, to, fro = get_text_from_mention(mention)
        # if there is no text, continue
        if not text or text == "":
            continue
        # translate parent tweet text
        translation = translate(text, to, fro)
        # reply to current tweet with translation
        api.update_status('@' + mention.user.screen_name +
                    ' ' + translation, mention.id)
def get_text_from_mention(mention):
    text_id = mention.in_reply_to_status_id
    t = mention.full_text.split()
    if not text_id:
        return None, None, None
    resp = api.statuses_lookup([text_id])
    return resp[0].text, t[1], t[2]
    
    

while True:
    # reply to latest tweets
    reply_to_tweets()
    # sleep for 2 seconds
    time.sleep(2)
