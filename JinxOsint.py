#Script BY JINX-CrazyCode
import webbrowser
import requests
import json
import os
import random
from random import *


#colori
reset = '\033[0m'
bold = '\033[01m'
disable = '\033[02m'
underline = '\033[04m'
reverse = '\033[07m'
strikethrough = '\033[09m'
invisible = '\033[08m'
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lightgrey = '\033[37m'
darkgrey = '\033[90m'
lightred = '\033[91m'
lightgreen = '\033[92m'
yellow = '\033[93m'
lightblue = '\033[94m'
pink = '\033[95m'
lightcyan = '\033[96m'



os.system("clear")
def banner():
        print(f"""
                            {lightblue} ▐▄▄▄▪   ▐ ▄ ▐▄• ▄           {pink}.▄▄ · ▪   ▐ ▄ ▄▄▄▄▄
                            {lightblue}  ·████ •█▌▐█ █▌█▌▪    ▪     {pink}▐█ ▀. ██ •█▌▐█•██  
                            {lightblue}▪▄ ██▐█·▐█▐▐▌ ·██·      {pink}▄█▀▄ ▄▀▀▀█▄▐█·▐█▐▐▌ ▐█.▪
                            {lightblue}▐▌▐█▌▐█▌██▐█▌▪▐█·█▌    {pink}▐█▌.▐▌▐█▄▪▐█▐█▌██▐█▌ ▐█▌·
                            {lightblue} ▀▀▀•▀▀▀▀▀ █▪•▀▀ ▀▀     {pink}▀█▄▀▪ ▀▀▀▀ ▀▀▀▀▀ █▪ ▀▀▀
""" + reset)


def menu2():
        print(f"""
    {lightblue}----------------------------------------------------------------------------------------------------------
    {pink}[19] Linkedin User Info                  {lightblue}[25] Current Weather         {pink}[31] Bin Checker
    {lightblue}[20] Mac Address Lookup                  {pink}[26] SoundCloud User Info    {lightblue}[32] Bin Lookup   
    {pink}[21] Url Shorten                         {lightblue}[27] Phone Number Validator  {pink} [33] Credits 
    {lightblue}[22] Snapchat User Info                  {pink}[28] City Details             
    {pink}[23] Telegram Group Info                 {lightblue}[29] Twitch Channel Info      
    {lightblue}[24] DuckDuckGo Search                   {pink}[30] Pinterest Info User      
    {pink}----------------------------------------------------------------------------------------------------------
    """ + reset)






def menu():
        print(f"""
    {lightblue}----------------------------------------------------------------------------------------------------------
    {pink}[1] Your ip                         {lightblue}[7] Predicts the Nationality        {pink}[13] Instagram User Info
    {lightblue}[2] Track ip                        {pink}[8] TikTok User Info                {lightblue}[14] Spotify Info User   
    {pink}[3] Verify site                     {lightblue}[9] Twitter User Info               {pink}[15] Whois
    {lightblue}[4] Verify Email                    {pink}[10] Fake id                        {lightblue}[16] Covid Statistics
    {pink}[5] Predict a person's age          {lightblue}[11] Social Links Search            {pink}[17] Telegram info
    {lightblue}[6] Populator Person Name           {pink}[12] Email Search                   {lightblue}[18] Secondary Menu
    {pink}----------------------------------------------------------------------------------------------------------
    """ + reset)




banner()
menu()
choice = int(input(f"{lightblue}Jinx{pink}Osint-> " + reset))
if (choice == 1):
    Country = requests.get("https://ipapi.co/country/")
    City = requests.get("https://ipapi.co/city/")
    Region = requests.get("https://ipapi.co/region/")
    Asn = requests.get("https://ipapi.co/asn/")
    Org = requests.get("https://ipapi.co/org/")
    Postal = requests.get("https://ipapi.co/postal/")
    print(pink + "Country: " + reset + darkgrey, Country.content, reset)
    print(lightblue + "City: " + reset  + darkgrey, City.content, reset)
    print(pink + "Region: " + reset + darkgrey, Region.content, reset)
    print(lightblue + "Asn: " + reset + darkgrey, Asn.content, reset)
    print(pink + "org: " + reset + darkgrey, Org.content, reset)
    print(lightblue + "HostName: " + reset + darkgrey, Postal.content, reset)


elif (choice == 2):
    ip = input(pink + "insert ip address: " + reset)
    country = requests.get("https://ipapi.co/" + ip + "/country/")
    city = requests.get("https://ipapi.co/" + ip + "/city/")
    region = requests.get("https://ipapi.co/" + ip + "/region/")
    org = requests.get("https://ipapi.co/" + ip + "/org/")
    capital = requests.get("https://ipapi.co/" + ip + "/country_capital/")
    asn = requests.get("https://ipapi.co/" + ip + "/asn/")
    latitude = requests.get("https://ipapi.co/" + ip + "/latitude/")
    longitude = requests.get("https://ipapi.co/" + ip + "/longitude/")
    print(lightblue + "Country: " + reset + darkgrey, country.content, reset)
    print(pink + "City: " + reset + darkgrey, city.content, reset)
    print(lightblue + "Region: " + reset + darkgrey, region.content,reset)
    print(pink + "Org: " + reset + darkgrey, org.content,reset)
    print(lightblue + "Capital: " + reset + darkgrey, capital.content,reset)
    print(pink + "Asn: " + reset + darkgrey, asn.content,reset)
    print(lightblue + "latitude, longitude" + reset + darkgrey, latitude.content, longitude.content, reset)


elif (choice == 3):
    url = str(input(lightblue + "insert site: " + reset))
    site = requests.get("https://" + url)
    if (site.status_code == 200):
        print(green + "Online" + reset)
    elif (site.status_code == 404):
        print(red + "Offline" + reset)


elif (choice == 4):
    print( yellow + "WARNING: you can not make more than 1000 requests per month" + reset)
    email = str(input(pink + "insert email: " + reset))
    querystring = {"domain":email}
    headers = {
	"X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	"X-RapidAPI-Host": "mailcheck.p.rapidapi.com"
    }
    mail = requests.get("https://mailcheck.p.rapidapi.com/", headers=headers, params=querystring )
    print(lightblue + "----------------------------------------------------" + reset)
    print(darkgrey,mail.content, reset)
    print(pink + "----------------------------------------------------" + reset)


elif(choice == 5):
    print( yellow + "WARNING: you can not make more than 1000 requests per day" + reset)
    Name = input(lightblue + "insert name: " + reset)
    country = input(pink + "insert country: " + reset)
    names = requests.get("https://api.agify.io?name=" + Name + "&country_id=" + country )
    print(lightblue + "-------------------------------------------" + reset)
    print(darkgrey,names.content, reset)
    print(pink + "-------------------------------------------" + reset)


elif(choice == 6):
   name = input(lightblue + "insert name: " + reset)
   country = input(pink + "insert country: " + reset)
   people = requests.get("https://api.genderize.io?name=" + name + "&country=" + country)
   print(darkgrey,people.content,reset)


elif(choice == 7):
    name = input(lightblue + "insert name: " + reset)
    n = requests.get("https://api.nationalize.io?name=" + name)
    print(darkgrey,n.content,reset)


elif(choice == 8):
    print(yellow + "Warning: Maximum 50 requests per month" + reset)
    user = input(pink + "insert tiktok-user: " + reset)
    querystring = {"username": user}
    headers = {
	"X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	"X-RapidAPI-Host": "tiktok-api6.p.rapidapi.com"
    }
    tiktok = requests.get("https://tiktok-api6.p.rapidapi.com/user/details", headers=headers, params=querystring)
    print(lightblue + "----------------------------------------------------------------" + reset)
    print(darkgrey,tiktok.text,reset)
    print(pink + "----------------------------------------------------------------" + reset)


elif(choice == 9):
    print(yellow + "Warning: Maximum 500 requests per month" + reset)
    user = input(lightblue + "insert Twitter-User: " + reset)
    querystring = {"username": user}
    headers = {
	"X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	"X-RapidAPI-Host": "twitter154.p.rapidapi.com"
    }
    twitter = requests.get("https://twitter154.p.rapidapi.com/user/details", headers=headers , params=querystring)
    
    print(pink + "----------------------------------------------------" + reset)
    print(darkgrey ,twitter.text, reset)
    print(lightblue + "----------------------------------------------------" + reset)


elif(choice== 10):
    print(yellow + "Warning: Maximum 1000 requests per month" + reset)
    headers = {
	"X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	"X-RapidAPI-Host": "fake-users6.p.rapidapi.com"
    }
    fakeid = requests.get("https://fake-users6.p.rapidapi.com/", headers=headers)
    print(pink + "----------------------------------------------------" + reset)
    print(darkgrey, fakeid.text , reset)
    print(lightblue + "----------------------------------------------------" + reset)


elif(choice == 11):
    print(yellow + "Warning: Maximum 20 requests per month" + reset)
    user = input(lightblue + "Insert nickname user: " + reset)
    querystring = {"query": user,"social_networks":"facebook,tiktok,instagram,snapchat,twitter,youtube,linkedin,github,pinterest"}
    headers = {
	"X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	"X-RapidAPI-Host": "social-links-search.p.rapidapi.com"
    }
    socials = requests.get("https://social-links-search.p.rapidapi.com/search-social-links", headers=headers, params=querystring)
    print(lightblue + "----------------------------------------------------" + reset)
    print(darkgrey, socials.text,reset)
    print(pink + "----------------------------------------------------" + reset)


elif(choice == 12):
    print(yellow + "Warning: Maximum 5 requests per month" + reset)
    email = input(lightblue + "Insert email: " + reset)
    querystring = {"query": email,"email_domain":"gmail.com","limit":"100"}
    headers = {
	"X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	"X-RapidAPI-Host": "email-search16.p.rapidapi.com"
    }
    gmail = requests.get("https://email-search16.p.rapidapi.com/search-emails", headers=headers, params=querystring)
    print(pink + "----------------------------------------------------------------" + reset)
    print(darkgrey, gmail.text, reset)
    print(lightblue + "----------------------------------------------------------------" + reset)


elif(choice == 13):
    print(yellow + "Warning: Maximum 2000 requests per month" + reset)
    user = input(pink + "Insert User: " + reset)
    querystring = {"username": user}
    headers = {
	"X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	"X-RapidAPI-Host": "instagram-data12.p.rapidapi.com"
    }
    ig = requests.get("https://instagram-data12.p.rapidapi.com/user/details-by-username/", headers=headers, params=querystring)
    print(lightblue + "----------------------------------------------------" + reset)
    print(darkgrey, ig.text, reset)
    print(pink + "----------------------------------------------------" + reset)


elif(choice == 14):
    print(yellow + "Warning: Maximum 500 requests per month" + reset)
    user = input(lightblue + "Insert Spotify User: " + reset)
    querystring = {"q": user,"type":"multi","offset":"0","limit":"10","numberOfTopResults":"5"}
    headers = {
	"X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	"X-RapidAPI-Host": "spotify-data.p.rapidapi.com"
    }
    print(pink + "----------------------------------------------------" + reset)
    spotify = requests.get("https://spotify-data.p.rapidapi.com/search/", headers=headers , params=querystring)
    print(darkgrey,spotify.content, reset)
    print(lightblue + "----------------------------------------------------" + reset)


elif(choice == 15):
    print(yellow + "Warning: Maximum 600 requests per month" + reset)
    domain = input(pink + "Insert Domain: " + reset)
    querystring = {"domain": domain}
    headers = {
	"X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	"X-RapidAPI-Host": "whois-lookup1.p.rapidapi.com"
    }
    Whois = requests.get("https://whois-lookup1.p.rapidapi.com/imnikgoyal/whois-lookup", headers=headers , params=querystring)
    print(lightblue + "----------------------------------------------------" + reset)
    print(darkgrey, Whois.content, reset)
    print(pink + "----------------------------------------------------" + reset)


elif(choice == 16):
    headers = {
	"X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
    }
    covid19 = requests.get("https://covid-193.p.rapidapi.com/statistics", headers=headers)
    print(pink + "----------------------------------------------------" + reset)
    print(darkgrey,covid19.content,reset)
    print(lightblue + "----------------------------------------------------" + reset)


elif(choice == 17):
    print(yellow + "Warning: Maximum 10 requests per month" + reset)
    channel = input(pink + "Insert Channel Telegram: " + reset)
    headers = {
	"X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	"X-RapidAPI-Host": "telegram7.p.rapidapi.com"
    }
    Telegram = requests.get(f"https://telegram7.p.rapidapi.com/channel/{channel}", headers=headers)
    print(lightblue + "----------------------------------------------------" + reset)
    print(darkgrey,Telegram.content, reset)
    print(pink + "----------------------------------------------------" + reset)


elif(choice == 18):
    os.system("clear")
    os.system("cls")
    os.system("title JinxOsint menu 2")
    banner()
    menu2()
    choice = int(input(f"{lightblue}Jinx{pink}Osint-> " + reset))
    if(choice ==19):
        print(yellow + "Warning: Maximum 10 requests per month" + reset)
        url = input(pink + "Insert Url Linkedin User: " + reset)
        querystring = {"url": url}
        headers = {
	    "X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	    "X-RapidAPI-Host": "linkedin-profile-data.p.rapidapi.com"
        }
        Linkedin = requests.get("https://linkedin-profile-data.p.rapidapi.com/linkedin-data", headers=headers, params=querystring)
        print(lightblue + "----------------------------------------------------" + reset)
        print(darkgrey,Linkedin.content,reset)
        print(pink + "----------------------------------------------------" + reset)


    elif(choice == 20):
        print(yellow + "Warning: Maximum 1000 requests per day" + reset)
        Mac = input(lightblue + "Insert Mac Address: " + reset)
        querystring = {"query":Mac}
        headers = {
	    "X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	    "X-RapidAPI-Host": "mac-address-lookup1.p.rapidapi.com"
        }
        lookup = requests.get("https://mac-address-lookup1.p.rapidapi.com/static_rapid/mac_lookup/", headers=headers, params=querystring)
        print(pink + "----------------------------------------------------" + reset)
        print(darkgrey, lookup.content, reset)
        print(lightblue + "----------------------------------------------------" + reset)


    elif(choice == 21):
        print(yellow + "Warning: Maximum 150 requests per month" + reset)
        url = input(pink + "Insert Url: " + reset)
        querystring = {"url": f"https://{url}"}

        headers = {
	    "X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	    "X-RapidAPI-Host": "url-shortener-german-quality-and-speed.p.rapidapi.com"
        }
        Shorten = requests.get("https://url-shortener-german-quality-and-speed.p.rapidapi.com/",headers=headers, params=querystring)
        print(lightblue + "----------------------------------------------------" + reset)
        print(darkgrey, Shorten.text, reset)
        print(pink + "----------------------------------------------------" + reset)


    elif(choice == 22):
        print(yellow + "Warning: Maximum 10 requests per month" + reset)
        user = input(lightblue + "insert User Snapchat: " + reset)
        querystring = {"username": user}
        headers = {
	    "X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	    "X-RapidAPI-Host": "snapchat-profile-scraper-api.p.rapidapi.com"
        }
        Snapchat = requests.get("https://snapchat-profile-scraper-api.p.rapidapi.com/profile", headers=headers, params=querystring)
        print(pink + "----------------------------------------------------" + reset)
        print(darkgrey, Snapchat.text, reset)
        print(lightblue + "----------------------------------------------------" + reset)


    elif(choice == 23):
        print(yellow + "Warning: Maximum 10 requests per month" + reset)
        group = input(lightblue + "insert Telegram Group: " + reset)
        headers = {
	    "X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	    "X-RapidAPI-Host": "telegram7.p.rapidapi.com"
        }
        Telegram = requests.get(f"https://telegram7.p.rapidapi.com/group/{group}", headers=headers)
        print(pink + "----------------------------------------------------" + reset)
        print(darkgrey,Telegram.text,reset)
        print(lightblue + "----------------------------------------------------" + reset)


    elif(choice == 24):
        print(yellow + "Warning: Maximum 500 requests per month" + reset)
        Search = input(pink + "Insert site to search: " + reset)
        querystring = {"q":Search}
        headers = {
	    "X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	    "X-RapidAPI-Host": "duckduckgo8.p.rapidapi.com"
        }
        DuckDuckGo = requests.get("https://duckduckgo8.p.rapidapi.com/", headers=headers, params=querystring)
        print(lightblue + "----------------------------------------------------" + reset)
        print(darkgrey ,DuckDuckGo.text, reset)
        print(pink + "----------------------------------------------------" + reset)


    elif(choice == 25):
        print(yellow + "Warning: Maximum 25 requests per day" + reset)
        lat = input(lightblue + "Insert Latitude: " + reset) 
        lon = input(pink + "Insert Longitude: " + reset)
        querystring = {"lon": lon,"lat": lat}
        headers = {
	    "X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	    "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
        }
        weather = requests.get("https://weatherbit-v1-mashape.p.rapidapi.com/current", headers=headers, params=querystring)
        print(lightblue + "----------------------------------------------------" + reset)
        print(darkgrey ,weather.text, reset)
        print(pink + "----------------------------------------------------" + reset)


    elif(choice == 26):
        print(yellow + "Warning: Maximum 10 requests per day" + reset)
        user = input(lightblue + "insert Url SoundCloud profile: " + reset)
        querystring = {"profile_url": user}

        headers = {
	    "X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	    "X-RapidAPI-Host": "soundcloud4.p.rapidapi.com"
        }
        soundcloud = requests.get("https://soundcloud4.p.rapidapi.com/user/info", headers=headers,params=querystring)
        print(lightblue + "----------------------------------------------------" + reset)
        print(darkgrey,soundcloud.text,reset)
        print(pink + "----------------------------------------------------" + reset)


    elif(choice == 27):
        number = input(pink + "Insert Phone number with prefix: " + reset)
        Country = input(lightblue + "Insert country: " + reset)
        querystring = {"number": number,"country": Country}
        headers = {
	    "X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	    "X-RapidAPI-Host": "phonenumbervalidatefree.p.rapidapi.com"
        }
        phone = requests.get(f"https://phonenumbervalidatefree.p.rapidapi.com/ts_PhoneNumberValidateTest.jsp", headers=headers, params=querystring)
        print(lightblue + "----------------------------------------------------" + reset)
        print(darkgrey, phone.text,reset)
        print(pink + "----------------------------------------------------" + reset)
    


    elif(choice == 28):
        print(yellow + "Warning: Maximum 1000 requests per day" + reset)
        city = input(lightblue + "Insert City id: " + reset)
        headers = {
	    "X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	    "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
        }
        lookup = requests.get(f"https://wft-geo-db.p.rapidapi.com/v1/geo/cities/{city}", headers=headers)
        print(pink + "----------------------------------------------------" + reset)
        print(darkgrey,lookup.text,reset)
        print(lightblue + "----------------------------------------------------" + reset)
    

    elif(choice == 29):
        print(yellow + "Warning: Maximum 400 requests per day" + reset)
        user = input(pink + "Insert username or id channel: " + reset)
        headers = {
	    "X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	    "X-RapidAPI-Host": "gwyo-twitch.p.rapidapi.com"
        }
        twitch = requests.get(f"https://gwyo-twitch.p.rapidapi.com/user/{user}", headers=headers)
        print(lightblue + "----------------------------------------------------" + reset)
        print(darkgrey,twitch.content,reset)
        print(pink + "----------------------------------------------------" + reset)


    elif(choice == 30):
        print(yellow + "Warning: Maximum 25 requests per month" + reset)
        user = input(lightblue + "Insert Username: " + reset)
        querystring = {"username": user}
        headers = {
	    "X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	    "X-RapidAPI-Host": "pinterest-scraper.p.rapidapi.com"
        }
        pinterest = requests.get("https://pinterest-scraper.p.rapidapi.com/profile/", headers=headers, params=querystring)
        print(pink + "----------------------------------------------------" + reset)
        print(darkgrey,pinterest.content,reset)
        print(lightblue + "----------------------------------------------------" + reset)
    
    elif(choice == 31):
        print(yellow + "Warning: Maximum 1000 requests per month" + reset)
        bin = input(lightblue + "Insert Bin: " + reset)
        querystring = {"bin": bin}
        payload = {"bin": bin}
        headers = {
	    "content-type": "application/json",
	    "X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	    "X-RapidAPI-Host": "bin-ip-checker.p.rapidapi.com"
        }
        Bank = requests.post("https://bin-ip-checker.p.rapidapi.com/", json=payload, headers=headers, params=querystring)
        print(pink + "----------------------------------------------------" + reset)
        print(darkgrey,Bank.text,reset)
        print(lightblue + "----------------------------------------------------" + reset)


    elif(choice == 32):
        print(yellow + "Warning: Maximum 10 requests per day" + reset)
        bin = input(pink + "Insert Bin: " + reset)
        ip = input(pink + "Insert ip Address: " + reset)
        payload = f"bin-number={bin}&customer-ip={ip}"
        headers = {
	    "content-type": "application/x-www-form-urlencoded",
	    "X-RapidAPI-Key": "83a4cb274bmshaf52c25e3788f30p1444c2jsn6aa2a6e38942",
	    "X-RapidAPI-Host": "neutrinoapi-bin-lookup.p.rapidapi.com"
        }
        Bank = requests.post("https://neutrinoapi-bin-lookup.p.rapidapi.com/bin-lookup", data=payload, headers=headers)
        print(lightblue + "----------------------------------------------------" + reset)
        print(darkgrey,Bank.text,reset)
        print(pink + "----------------------------------------------------" + reset)     
    elif (choice == 33):
        webbrowser.open_new("https://github.com/Jinx-CrazyCode")