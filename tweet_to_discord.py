#!/usr/bin/env python3
import tweepy
import time
import datetime
from discord_hooks import Webhook

ConsumerKey=""
ConsumerSecret=""
AccessToken=""
AccessTokenSecret=""

target_name = ""
reply_flag = 0
retweet_flag = 0
favorite_count_threshold = 0
retweet_count_threshold = 0
collect_interval = 120
stop_tweet = "bot停止"
current_datetime = datetime.datetime(2018, 6, 30, 0, 0, 0)

discord_webhook_url = ""

auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
auth.set_access_token(AccessToken, AccessTokenSecret)
api = tweepy.API(auth)

def collect_tweets(target_name,current_datetime):
    u = api.get_user(screen_name=target_name)
    target_tweets = api.user_timeline(id=u.id)
    new_tweets = []
    for i in target_tweets:
        if i.created_at > current_datetime:
            new_tweets.append(i)
    
    return new_tweets

def delete_rtweets(tweets):
    non_rt_tweets = []
    for i in tweets:
        if "retweeted_status" not in dir(i):
            non_rt_tweets.append(i)
    
    return non_rt_tweets
            
def delete_reply(tweets,target_name):
    non_reply_tweets = []
    for i in tweets:
        if i.in_reply_to_screen_name == None or i.in_reply_to_screen_name == target_name:
            non_reply_tweets.append(i)
    
    return non_reply_tweets

def faved_tweets(tweets,favorite_count_threshold):
    faved_tweets = []
    for i in tweets:
        if i.favorite_count >= favorite_count_threshold:
            faved_tweets.append(i)

    return faved_tweets

def retweeted_tweets(tweets,retweet_count_threshold):
    retweeted_tweets = []
    for i in tweets:
        if i.retweet_count >= retweet_count_threshold:
            retweeted_tweets.append(i)

    return retweeted_tweets

def post_to_discord(discord_webhook_url,tweet_text):
    msg = Webhook(discord_webhook_url,msg=tweet_text)
    msg.post()

if __name__ == '__main__':
    stop_flag = 0
    while stop_flag == 0:
        tweets = collect_tweets(target_name,current_datetime)
        if retweet_flag == 0:
            tweets = delete_rtweets(tweets)
        
        if reply_flag == 0:
            tweets = delete_reply(tweets,target_name)
        
        tweets = faved_tweets(tweets,favorite_count_threshold)
        tweets = retweeted_tweets(tweets,retweet_count_threshold)
        for i in range(len(tweets)):
            j = len(tweets)-i-1
            post_to_discord(discord_webhook_url,tweets[j].text)
            print(tweets[j].text)
            current_datetime = tweets[j].created_at
            time.sleep(1)
            if tweets[j].text == stop_tweet:
                stop_flag = 1    
                break
        
        time.sleep(collect_interval)