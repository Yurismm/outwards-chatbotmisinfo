import time
import requests
import json


response = requests.get("https://socsem.kmi.open.ac.uk/misinfo/api/swagger.json")
print(response.status_code)

time.sleep(5)

print("Hello! I am Misinfo.Me.Bot and I am here to help you to analyse Twitter profiles for you to know who are those spreading misinformation in your network.")
time.sleep(3)
print("Tell me what Twitter profile you would like to analyse. Can be yours, or someone that you suspect that spreads a lot of misinformation, like Donald Trump, for example ;-) . Please, type the Twitter name after @, like @realDonaldTrump, for example.")
time.sleep(1)
screenname = input("Insert Screenname here:")

wltkm = input("Thank you. I am now gathering information tweeted by @" + screenname + ". In the meantime, would you like to learn more about how Misinfo.Me works?")
### Will continue this at a later time.

### reading json file + screenname

response = requests.get("https://socsem.kmi.open.ac.uk/misinfo/api/credibility/users/?screen_name=" + screenname)
response.raise_for_status()
jsonResponse = response.json()
print("Credibility value(s) (the closer to 1 it is, the more reliable it is, however, if it's in minus numbers that means the profile could be spreading misinfomation.")
value = jsonResponse["credibility"]["value"]
print(value)
tweetcount = jsonResponse["itemReviewed"]["tweets_cnt"]
print("@" + screenname + " has " + str(tweetcount) + " tweets in total.")
sharedurlcount = jsonResponse["itemReviewed"]["shared_urls_cnt"]
print("@" + screenname + " has " + str(sharedurlcount) + " urls shared in tweets in total.")


### Prints the value, we really need to make this number into something more user-friendly.





