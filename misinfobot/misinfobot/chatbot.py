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



response = requests.get("https://socsem.kmi.open.ac.uk/misinfo/api/credibility/users/?screen_name=" + screenname)
print("Credibility value(s) (the closer to 1 it is, the more reliable it is:")
response.raise_for_status()
jsonResponse = response.json()
print(jsonResponse["credibility"]["value"])

    

