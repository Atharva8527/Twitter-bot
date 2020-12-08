import tweepy
import time
import os
from random_anime import suggest

#You will find these keys in your twiiter developer account
consumer_key = 'SmMEd6DeeL9tV8W1o3AS1KKSf'
consumer_secret = '2Yj9lPGss0DFaeUzQblKvqtweh47Bwkz3uyRsj6LIMsLV5afj5'
access_token = '1328682492157521922-ITTAz4dDJYlnmzLEIeBOnJQxcavB5X'
access_token_secret = 'Mi7bEtq8rFrOqjhdvwMKocS8BdChPguwtAjL9PboXReJz'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#creating a file to store the last seen id's
FILE_NAME = 'last_seen_id.txt'


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return
#function to reply to tweets
def reply_to_tweets():

    #verifying the last seen id
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                        last_seen_id,
                        )
    for mention in reversed(mentions):
            print(str(mention.id) + ' - ' + mention.text, flush=True)
            last_seen_id = mention.id
            store_last_seen_id(last_seen_id, FILE_NAME)
            #verifying if the keyword is present in the tweet
            if '#animesuggests' in mention.text.lower():
                x = suggest()
                time.sleep(5)

                print('found #animesuggests', flush=True)
                print('responding back...', flush=True)
                api.update_status('@'+ mention.user.screen_name + ' Here is your anime suggestion ' + str(x) , mention.id)




while True:
    reply_to_tweets()
    time.sleep(10)
