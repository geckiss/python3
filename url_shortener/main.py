#!/usr/bin/python3
# Pretasks:
# cd proj_dir && pipenv install requests
import sys
import requests
import random

domain = "https://shortener.geckiss.sk/"

def getShortUrl():
    short_url=""
    for i in range(0, 10):
        num = 0
        if random.randint(0, 1):
            num = random.randint(65, 90)
        else:
            num = random.randint(97, 122)
        short_url += chr(num)
        
    return(domain + short_url)

long_url=str(sys.argv[-1])
#print("The url is: " + url)
if long_url:
    print(getShortUrl())
else:
    print("You need to specify URL to shorten")
