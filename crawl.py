# -*- coding:utf-8 -*-

from requests_oauthlib import OAuth1Session
import json

oath_key_dict = {
    "consumer_key": " ",
    "consumer_secret": " ",
    "access_token": " ",
    "access_token_secret": " "
}

def create_oath_session(oath_key_dict):
    oath = OAuth1Session(
    oath_key_dict["consumer_key"],
    oath_key_dict["consumer_secret"],
    oath_key_dict["access_token"],
    oath_key_dict["access_token_secret"]
    )
    return oath

def tweet_search(search_word,oath_key_dict):
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    
    params = {
        "q": search_word,
        "lang": "ja",
        "result_type": "recent",
        "count": "15"
        }
    
    oath = create_oath_session(oath_key_dict)
    responce = oath.get(url, params = params)
    
    if responce.status_code != 200:
        print("Error code: %d" %(responce.status_code))
        return None
    
    tweets = json.loads(responce.text)
    
    return tweets


results = []

def search(tweet):
#   tweet_id = tweet[u'id_str']
    text = tweet[u'text']
    created_at = tweet[u'created_at']
    user_id = tweet[u'user'][u'id_str']
#   user_description = tweet[u'user'][u'description']
#   screen_name = tweet[u'user'][u'screen_name']
#   user_name = tweet[u'user'][u'name']

    return {
        'tweet': text.replace("\n"," "),
        'date': created_at,
        'user_id': user_id
    }

def store_json():
    f = open('tweets.json','w')
    json.dump(results,f,ensure_ascii=False, indent=4, sort_keys=False, separators=(',', ': '))

def main():
    search_word = "#好きなアニメ"
    tweets = tweet_search(search_word,oath_key_dict)
    
    for tweet in tweets["statuses"]:
        result = search(tweet)
        results.append(result)

    store_json()
    print(results)

### Execute                                                                                                                                                       
if __name__ == "__main__":
    main()

