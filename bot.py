import tweepy
import urllib.request, re
import time
import calendar
from datetime import date
from datetime import datetime, timedelta
from urllib.request import Request, urlopen

week = []
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
presentday = datetime.now()

for i in range(14):
    week.append(presentday+timedelta(i))

def hasBurger(day:str) -> bool:
    bon = "https://lewisandclark.cafebonappetit.com/cafe/fields-dining-room/"
    bon += day + "/"
    req = Request(
        url=bon, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    webpage = str(urlopen(req).read())
    return webpage.find("beef burger")>0 or webpage.find("beef patty")>0 or webpage.find("Beef Burgers")>0

def nextBurgerDay():
    matrix = [False]*14
    for i in range(14):
        dateCheck = week[i].strftime('%Y-%m-%d')
        if hasBurger(dateCheck):
            matrix[i] = True
    if True in matrix:
        return week[matrix.index(True)]
    else:
        return False

nbd = nextBurgerDay()
if nbd==False:
    update = "No burgers in the foreseeable future :("
else:
    away = (nbd-presentday).days
    if away==0:
        update = "Bon Burgers today!"
    elif away==1:
        update = "Bon Burgers tomorrow!"
    else:
        update = "The next Bon Burger day is " + days[nbd.weekday()] + ", " + calendar.month_name[nbd.month] + " " + str(nbd.day) + ", which is in " + str((nbd-presentday).days)   + " days."
print(update)

client.create_tweet(text=update)
