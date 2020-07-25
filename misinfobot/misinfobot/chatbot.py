import time
import requests

response = requests.get("https://socsem.kmi.open.ac.uk/misinfo/api/swagger.json")
print(response.status_code)

time.sleep(5)

print("Hello! I am Misinfo.Me.Bot and I am here to help you to analyse Twitter profiles for you to know who are those spreading misinformation in your network.")
time.sleep(3)
print("Tell me what Twitter profile you would like to analyse. Can be yours, or someone that you suspect that spreads a lot of misinformation, like Donald Trump, for example ;-) . Please, type the Twitter name after @, like @realDonaldTrump, for example.")
time.sleep(1)
id = input("Insert ID here")


##This is the id of the tweet, for now we will use the tweet, instead of the profile to test the requests.

print("The id is:" + id) 