"""bot module, runs a loop to check for latest mentions and responds to them."""
import time
import tweepy
from id_controller import retrieve_last_seen_id, store_last_seen_id
from translator import translate

CONSUMER_KEY = 'CONSUMER_KEY'
CONSUMER_SECRET = 'CONSUMER_SECRET'
ACCESS_KEY = 'ACCESS_KEY'
ACCESS_SECRET = 'ACCESS_SECRET'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

def reply_to_tweets():
    """function to retrieve latest mentions and respond to them"""
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
        text, to_lang, from_lang = get_text_from_mention(mention)
        # if there is no text, continue
        if not text or text == "":
            continue
        # translate parent tweet text
        translation = translate(text, to_lang, from_lang)
        # reply to current tweet with translation
        api.update_status('@' + mention.user.screen_name +
                    ' ' + translation, mention.id)
def get_text_from_mention(mention):
    """gets text to translate, from and to languages."""
    text_id = mention.in_reply_to_status_id
    mention_text_parts = mention.full_text.split()
    if not text_id:
        return None, None, None
    resp = api.statuses_lookup([text_id])
    return resp[0].text, mention_text_parts[1], mention_text_parts[2]

while True:
    # reply to latest tweets
    reply_to_tweets()
    # sleep for 2 seconds
    time.sleep(2)
