# Import the stuffs
import configparser
import os
import sys
# Now import the cheater module that does a lot of the heavy lifting to mess with twitter
# even though twitter's api is pretty well documented.
import tweepy
"""
Thank you @malwareunicorn!!! I got the idea to pull this from file
More details here:
http://amanda.secured.org/how-to-make-a-simple-twitter-bot/
"""
config = configparser.ConfigParser()
#Get config file from the executing directory.
try:
	config.readfp(open('twitter.cfg'))
except FileNotFoundError:
	print("Is the auth file located in this directory and named twitter.cfg?")
	sys.exit(1)
CONSUMERKEY=config.get('mytwitterbot','consumerKey')
CONSUMERSECRET=config.get('mytwitterbot', 'consumerSecret')
ACCESSKEY=config.get('mytwitterbot', 'accessKey')
ACCESSSECRET=config.get('mytwitterbot', 'accessSecret')
OWERNAME=config.get('mytwitterbot', 'ownerName')
OWNERID=config.get('mytwitterbot', 'ownerId')
# Authenticate to the tweet mobile
auth = tweepy.OAuthHandler(CONSUMERKEY, CONSUMERSECRET)
auth.set_access_token(ACCESSKEY, ACCESSSECRET)
try:
	api = tweepy.API(auth)
except tweepy.error.TweepError:
	print("Error in authentication")
	sys.exit(1)


# Everything returned through tweepy is a 'resultset'  Thanks to stack exchange pointed me to this
# https://github.com/tweepy/tweepy/blob/master/tweepy/models.py#L10
# it is a 'list like object that holds results'
# https://stackoverflow.com/questions/42542327/how-to-extract-information-from-tweepy-resultset


# First are my friends I am going to retweet other BSiderz?
# regex to the rescue!!
import re
# search it up!
friendlys = re.compile('(^BSides.{1,6}|^bsides.{1,7})')
# Now we need to check the tweet text for CFP things...
retweetCFP = re.compile('(\s[cC][fF][pP]\sis\s(now)?\s?[oO][pP][eE][nN])')


# # First try at this...
# But still this would be a better approach....
# friends = api.friends()
# for friend in friends:
# 	# check the names yo!
# 	if friendlys.search(friend.name):
# 		# This does not work because i need to make a list of ids...  crap.
# 		statuses = api.statuses_lookup(friend.id)
# 		print(statuses)

# Now I am going to just try the timeline approach...
tweets = api.home_timeline(count=100)
for tweet in tweets:
	# find out if they are bsiderz
	if friendlys.search(tweet.user.screen_name):
		print("searching ", tweet.user.screen_name, " timeline!")
		# now check if it is retweetable
		if retweetCFP.search(tweet.text):
			print("Found a tweet to twitter!:  ", tweet.text)
			try:
				api.retweet(tweet.id)
				print("retweeted ", tweet.user.screen_name, "tweet!")
			except tweepy.error.TweepError:
				print("You have already tweeted this one!  Moving on.")


print("Twitter Bot is done processing...")



# I think maybe the api.search method is the way to go...
# TODO try and use the api.search to do this and see what happens.
# TODO make an auth def, and a retweet def
# TODO use the api.search method to find othe BSiderz


# test that regex!
# friendlys = re.search('(^BSides.{1,4}|^bsides.{1,4})','bsidesTest')
# Or use some online gui-ness:
# https://pythex.org/


# If you like json since twitter does its output that way natively here is this:
# https://stackoverflow.com/questions/42542327/how-to-extract-information-from-tweepy-resultset
# result_set = api.favorites('twitter')
# result_set = api.home_timeline()
# status = result_set[0]
# REALSTR = status._json.keys() 
# print(REALSTR)


# I may want to use streams...
# from tweepy import Stream


# TODO add a way to check the amount of api calls I have done...
# RATELIMIT = api.rate_limit_status() 
# print (RATELIMIT)


