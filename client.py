import tweepy
import winsound
    


class Client:
    def __init__(self, bearer, userid):
        self.userid = userid
        self.bearer = bearer
        self.client = tweepy.Client(bearer_token=bearer)
        self.last = self.client.get_users_tweets(id=self.userid, tweet_fields=['text'], max_results=5).data[0]

    
    def checker(self):
        tweet = self.client.get_users_tweets(id=self.userid, tweet_fields=['text'], max_results=5).data[0]

        if self.last != tweet:
            print(tweet)
            self.last = tweet
            winsound.Beep(800, 10000)


