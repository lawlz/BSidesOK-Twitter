#!/usr/bin/env python3
__version__ = '0.3'
__author__ = 'Jimmy James w/ Help'

# Import the config stuffs
import configparser
# get that config from the OS
import os
# in order to exit this program if exception occurs... maybe
import sys
# Now import the cheater module that does a lot of the heavy lifting to mess with twitter
# even though twitter's api is pretty well documented.
import tweepy
# find friends and parse tweets
import re
# TODO maybe use argparse to get arguments of file location?

def twitter_auth(conf='twitter.cfg'):
	# Thank you @malwareunicorn!!! I got the idea to pull this from file
	# More details here:
	# http://amanda.secured.org/how-to-make-a-simple-twitter-bot/
	config = configparser.ConfigParser()
	#Ge tconfig file from the executing directory.
	try:
		config.readfp(open(conf))
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
	return api

# Everything returned through tweepy is a 'resultset'  Thanks to stack exchange pointed me to this
# https://github.com/tweepy/tweepy/blob/master/tweepy/models.py#L10
# it is a 'list like object that holds results'
# https://stackoverflow.com/questions/42542327/how-to-extract-information-from-tweepy-resultset

def main():
	# Get the config and auth to twitts
	api = twitter_auth()
	# # First try at this...
	# But still this may be a better approach....
	# friends = api.friends()
	# for friend in friends:
	# 	# check the names yo!
	# 	if friendlys.search(friend.name):
	# 		# This does not work because i need to make a list of ids...  crap.
	# 		statuses = api.statuses_lookup(friend.id)
	# 		print(statuses)
	#
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


# First are my friends I am going to retweet other BSiderz?
# regex to the rescue!!
# search it up!
friendlys = re.compile('(^BSides.{1,6}|^bsides.{1,7})')
# Now we need to check the tweet text for CFP things...
retweetCFP = re.compile('(\s[cC][fF][pP]\sis\s(now)?\s?[oO][pP][eE][nN])')


main()
# I think maybe the api.search method is the way to go...
# TODO try and use the api.search to do this and see what happens.
# TODO make an auth def, and a retweet def
# TODO use the api.search method to find othe BSiderz
# TODO maybe ask for what the name of the config file is?
# get_conf = input('Enter the config name, default is twitter.cfg')

# test that regex!
# friendlys = re.search('(^BSides.{1,4}|^bsides.{1,4})','bsidesTest')
# Or use some online gui-ness:
# https://pythex.org/


# If you like json since twitter does its output that way natively here is this:
# https://stackoverflow.com/questions/42542327/how-to-extract-information-from-tweepy-resultset
# result_set = api.favorites('twitter')
# result_set = api.home_timeline()
# status = result_set[0]
# jsonString = status._json.keys() 
# print(jsonString)


# I may want to use streams potentially...
# from tweepy import Stream


# TODO add a way to check the amount of api calls I have done...
# RATELIMIT = api.rate_limit_status() 
# print (RATELIMIT)


