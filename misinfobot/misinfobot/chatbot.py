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

wltkm = input("Thank you. I am now gathering information tweeted by @" + screenname + ". In the meantime, would you like to learn more about how Misinfo.Me works? (yes/no)")

if wltkm == "yes":
    print("Misinfo.Me extracts the links that part of any tweet created or retweet by the profile under analysis. We then look for these URLs that have been analysed by fact-checkers and check their sources. Based on these assessments, we calculate a score to the Twitter profile that will be presented to you.")
elif wltkm =="no":
    print("Alright. That could be important information later, so if you want to find out more about the score, just ask ‘can I find out more about the score’ once your analysis is complete.")

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
print("@" + screenname + " has " + str(sharedurlcount) + " urls have been shared in their tweets in total.")


### Prints the value, we really need to make this number into something more user-friendly.





