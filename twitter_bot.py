#!/usr/bin/python
# coding: utf-8


from twython import Twython
import time, random, re


# default settings
# First Configuration Your Default Tokens for access Twitter Api
APP_KEY = "< Your Twitter App key >"
APP_SECRET = "< Your Twitter App secret >"
OAUTH_TOKEN = "< Your Access Token  >"
OAUTH_TOKEN_SECRET = "< Your Access Token Secret >"

# Then Create a twitter objects make sure it works.
# You can post tweet by this object
twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)




# Default Search list for Get https://api.twitter.com/1.1/search/tweets.json?q=<SEARCH_LIST>
SEARCH_LIST = ['python','django framework' ,'ruby on rails','javascript','reactjs','nodejs','amazing','funny','programming','big data','data mining','software','hardware','computer','science','biology','physics'][:6]


# This function Search Twitter
def search(word):
    """
        return Search results type status list
    """
    obj = twitter.search(q=word)
    status_list= []
    for x in obj['statuses']:
        status_list.append(x['text'])
    return status_list


def check_words(text):
    """
        This method check status and match Japan and Chinese words
        If find Cannot share tweet ignore this words
    """
    status = True
    for n in re.findall(ur'[\u4e00-\u9fff]+',text):
        status = False
    return status





while True:
    # The main Code start here
    # First define status list for searching random word
    # text_list return list of status contain 10 tweets
    # after find from text_list one random status
    # chech status words ignore Japan and Chinese lang
    # then tweet it 
    # and stop 5 minutes and work again
    text_list = search(SEARCH_LIST[random.randint(0,len(SEARCH_LIST)-1)])
    text = text_list[random.randint(0,len(text_list)-1)][:140]
    if check_words(text):
        try:
            twitter.update_status(status=text)
        except:
            pass
    time.sleep(5*60)