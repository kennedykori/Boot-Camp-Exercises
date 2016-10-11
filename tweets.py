"""
	Name	  : Andela
	Password  : Andelabootcamp
	Username  : @Andela_BootCamp	

	Consumer Key (API Key) 			4BbR3sBrAC8tK4R3XlgORC0cV
	Consumer Secret (API Secret)	UBLCOqpPs1b8j1XVnja6sxeBfaJI2cF2NJyak0f7Rap5mQwHci 
	
	Access Token 					785463654405799937-7vRn2gZ26QfpSvM5KpKOC2hHH5z9N3t
	Access Token Secret 			xjBlMyfHdvKGKqPBCxsoDaTfbfEu8aUz0qUOfY1D51kj2 
"""

import sys
import time
#from tweety import *
from twitter import *

if __name__ == "__main__":
	Consumer_Key 	= 	"4BbR3sBrAC8tK4R3XlgORC0cV"
	Consumer_Secret = 	"UBLCOqpPs1b8j1XVnja6sxeBfaJI2cF2NJyak0f7Rap5mQwHci" 
	Access_Token 	= 	"785463654405799937-7vRn2gZ26QfpSvM5KpKOC2hHH5z9N3t"
	Access_Secret 	= 	"xjBlMyfHdvKGKqPBCxsoDaTfbfEu8aUz0qUOfY1D51kj2" 


	t = Twitter(auth = OAuth(Access_Token,Access_Secret,Consumer_Key,Consumer_Secret))

	tweet = ""

	for size in range(1,len(sys.argv)):
	 	tweet +=str(sys.argv[size])+" "

	try:
		t.statuses.update(status = tweet)
	except Exception as e:
		print "Error :: ",str(e)

	print "Tweet Posted at :: ",time.ctime()

	"""
		To run the program use:

		name_of_file.py tweet
		Example :

		tweets.py This is Andela and i am happy to be here

		or

		tweet.py "This is Andela and i am happy to be here"	
	"""
