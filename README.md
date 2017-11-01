# BSidesOK Twitter Bot

This is a concept to automate some of the functions of managing the twitter account for BSidesOK.

The initial goal is to be able to automatically retweet call for papers by other BSides orgs.  Then hopefully even retweet other BSides registration portals, especially the somewhat local ones...

TODO's are riddled and this code is a primitive start.  Please PR as you see fit, and I am sure I will gladly add it to this repo.  

It is sad now, help make it happy...


## Prerequisites

1.  Python 3

⋅⋅⋅[Yes use it and love it, its not that bad](https://docs.python.org/3/)  

2.  Tweepy

⋅⋅⋅[Find out more about Tweepy](http://tweepy.readthedocs.io/en/v3.5.0/)  

3. twitter.cfg file

⋅⋅⋅In order for this to work, create a file with the following structure(with you secrets..) in the working directory of this script:  

⋅⋅⋅[mytwitterbot]  
⋅⋅⋅consumerKey=<consumer key>  
⋅⋅⋅consumerSecret=<consumer secret>  
⋅⋅⋅accessKey=<yep your git'n it>  
⋅⋅⋅accessSecret=<yes that secret too>  
⋅⋅⋅ownerName=<whats your name>  
⋅⋅⋅ownerId=<who own this again>  

⋅⋅⋅Of course fill out the appropriate info in the <>, replaces those <> when you do.  


## More Info

BSidesOK is a local Okie information security conference that strives to be inclusive and share all things infosec.

[Go here for all your BSidesOK info!](https://www.bsidesok.com)
