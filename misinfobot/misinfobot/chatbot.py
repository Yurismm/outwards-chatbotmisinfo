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

### reading json file + screenname

response = requests.get("https://socsem.kmi.open.ac.uk/misinfo/api/analysis/twitter_accounts?wait=true&screen_name=jamescharles")
response.raise_for_status()
jsonResponse = response.json()

verifcnt = jsonResponse["verified_urls_cnt"]
fkcnt = jsonResponse["fake_urls_cnt"]
unkcnt = jsonResponse["unknown_urls_cnt"]
lastupdated = jsonResponse["updated"]

response = requests.get("https://socsem.kmi.open.ac.uk/misinfo/api/credibility/users/?screen_name=" + screenname)
response.raise_for_status()
jsonResponse = response.json()



print("Credibility value(s): (the closer to 1 it is, the more reliable it is, however, if it's in minus numbers that means the profile could be spreading misinfomation.")
value = jsonResponse["credibility"]["value"]
print(value)
tweetcount = jsonResponse["itemReviewed"]["tweets_cnt"]
print("@" + screenname + " has " + str(tweetcount) + " tweets in total.")
sharedurlcount = jsonResponse["itemReviewed"]["shared_urls_cnt"]
print("@" + screenname + " has " + str(sharedurlcount) + " urls have been shared in their tweets in total.")
print("@" + screenname + " has " + str(fkcnt) + " urls that have been labled as fake links.")
print("@" + screenname + " has " + str(verifcnt) + " urls that have been labled as verified links (This could be 0, because the profile isn't analysed fully yet.")
print("@" + screenname + " has " + str(unkcnt) + " urls that from unknown places, or that are unknown to us.")
print("This result was last updated on: " + str(lastupdated))
time.sleep(2)
if value < 0:
    print("This means that this profile could possibilty be associated with misinfomation")
elif value > 0:
    print("This means that this profile probably isn't associated with misinfomation")
time.sleep(2)

#at stands for anaylse tweet.

at = input("You can also send a link to a tweet to have it analysed for misinfomation. Would you like to do this? (y/n)")
if at == "y":
    tweetid = input("Please insert the ID of the tweet that you would like to gain analyasis from:")
    response = requests.get("https://socsem.kmi.open.ac.uk/misinfo/api/credibility/tweets/" + tweetid + "?wait=true")
    response.raise_for_status()
    jsonResponse = response.json()
    tweetcred = jsonResponse["credibility"]["value"]
    print("The credibility value is: " + str(tweetcred))
    if tweetcred < 0:
        print("This tweet could include sources that are known to have misinfomaiton.")
    elif tweetcred > 0:
        print("This tweet probably doesn't have any misinfomation.")
elif at == "n":
    print("That's alright. Thank you for using MisinfoMeBot.")

