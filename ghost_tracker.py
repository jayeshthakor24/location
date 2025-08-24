#!/usr/bin/python
# GHOST TRACKER - TERMUX OPTIMIZED
# CODE BY YOU

import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

# COLOR VARIABLES
Bl = '\033[30m'
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'

# CLEAR TERMINAL
def clear():
    os.system('clear')

# BANNER
def run_banner():
    clear()
    stderr.writelines(f"""{Wh}
         .-.
       .'   `.          {Wh}--------------------------------
       :g g   :         {Wh}| {Gr}GHOST - TRACKER - TERMUX {Wh}|
       : o    `.        {Wh}|       {Gr}CODE BY YOU           {Wh}|
      :         ``.     {Wh}--------------------------------
     :             `.
    :  :         .   `.
    :   :          ` . `.
     `.. :            `. ``;
        `:;             `:'
           :              `.
            `.              `.     .
              `'`'`'`---..,___`;.-'
    """)
    time.sleep(0.5)

# === FUNCTIONS ===

# 1️⃣ Show Live IP & Location
def showIP():
    print(f"\n {Wh}========== {Gr}LIVE IP & LOCATION {Wh}==========")
    print(f"{Wh}[{Gr}+{Wh}] Press Ctrl+C to exit\n")
    try:
        while True:
            # Get public IP
            public_ip = requests.get("https://api.ipify.org").text

            # Get GPS location
            location_json = os.popen("termux-location").read()
            location_data = json.loads(location_json)
            latitude = location_data.get('latitude', 'N/A')
            longitude = location_data.get('longitude', 'N/A')
            accuracy = location_data.get('accuracy', 'N/A')

            # Display info
            print(f"{Wh}[{Gr}+{Wh}] Public IP       : {Gr}{public_ip}")
            print(f"{Wh}[{Gr}+{Wh}] Latitude        : {Gr}{latitude}")
            print(f"{Wh}[{Gr}+{Wh}] Longitude       : {Gr}{longitude}")
            print(f"{Wh}[{Gr}+{Wh}] Accuracy (m)   : {Gr}{accuracy}")
            print(f"{Wh}[{Gr}+{Wh}] Google Maps     : {Gr}https://www.google.com/maps/@{latitude},{longitude},18z")
            print("="*50)

            time.sleep(5)
            clear()
    except KeyboardInterrupt:
        print(f"\n{Wh}[{Re}!{Wh}] {Re}Exiting Live IP & Location{Wh}")
        time.sleep(2)
        return

# 2️⃣ IP Tracker
def IP_Track():
    ip = input(f"{Wh}\n Enter IP target : {Gr}")
    print(f' {Wh}============= {Gr}SHOW INFORMATION IP ADDRESS {Wh}=============')
    try:
        req_api = requests.get(f"http://ipwho.is/{ip}")
        ip_data = req_api.json()

        print(f"{Wh}IP target       : {Gr}{ip}")
        print(f"{Wh}Type IP         : {Gr}{ip_data['type']}")
        print(f"{Wh}Country         : {Gr}{ip_data['country']}")
        print(f"{Wh}City            : {Gr}{ip_data['city']}")
        print(f"{Wh}Region          : {Gr}{ip_data['region']}")
        print(f"{Wh}Latitude        : {Gr}{ip_data['latitude']}")
        print(f"{Wh}Longitude       : {Gr}{ip_data['longitude']}")
        print(f"{Wh}Maps            : {Gr}https://www.google.com/maps/@{ip_data['latitude']},{ip_data['longitude']},8z")
        print(f"{Wh}ISP             : {Gr}{ip_data['connection']['isp']}")
    except:
        print(f"{Re}Failed to get IP info. Check the IP address.")

# 3️⃣ Phone Number Tracker
def phoneGW():
    User_phone = input(f"\n {Wh}Enter phone number target {Gr}Ex [+6281xxxxxx] {Wh}: {Gr}")
    default_region = "ID"
    parsed_number = phonenumbers.parse(User_phone, default_region)

    region_code = phonenumbers.region_code_for_number(parsed_number)
    operator = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "id")
    is_valid = phonenumbers.is_valid_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    timezone1 = ', '.join(timezone.time_zones_for_number(parsed_number))

    print(f"\n {Wh}========== {Gr}PHONE INFO {Wh}==========")
    print(f"Location       : {Gr}{location}")
    print(f"Region Code    : {Gr}{region_code}")
    print(f"Operator       : {Gr}{operator}")
    print(f"Valid Number   : {Gr}{is_valid}")
    print(f"International  : {Gr}{formatted_number}")
    print(f"Timezone       : {Gr}{timezone1}")

# 4️⃣ Username Tracker
def TrackLu():
    username = input(f"\n {Wh}Enter Username : {Gr}")
    results = {}
    social_media = [
        {"url": "https://www.facebook.com/{}", "name": "Facebook"},
        {"url": "https://www.twitter.com/{}", "name": "Twitter"},
        {"url": "https://www.instagram.com/{}", "name": "Instagram"},
        {"url": "https://www.github.com/{}", "name": "GitHub"},
        {"url": "https://www.tiktok.com/@{}", "name": "TikTok"}
    ]
    for site in social_media:
        url = site['url'].format(username)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                results[site['name']] = url
            else:
                results[site['name']] = "Username not found!"
        except:
            results[site['name']] = "Error"

    print(f"\n {Wh}========== {Gr}USERNAME INFO {Wh}==========")
    for site, url in results.items():
        print(f"{Wh}[{Gr}+{Wh}] {site}: {Gr}{url}")

# === MENU SYSTEM ===
options = [
    {'num': 1, 'text': 'IP Tracker', 'func': IP_Track},
    {'num': 2, 'text': 'Show Your IP (Live)', 'func': showIP},
    {'num': 3, 'text': 'Phone Number Tracker', 'func': phoneGW},
    {'num': 4, 'text': 'Username Tracker', 'func': TrackLu},
    {'num': 0, 'text': 'Exit', 'func': exit}
]

def option_text():
    text = ''
    for opt in options:
        text += f"[ {opt['num']} ] {Gr}{opt['text']}\n"
    return text

def call_option(opt):
    for option in options:
        if option['num'] == opt:
            option['func']()

def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n[ {Gr}+ {Wh}] Press Enter to continue')
        main()
    except KeyboardInterrupt:
        print(f"\n{Wh}[{Re}!{Wh}] {Re}Exit")
        time.sleep(2)
        exit()

def main():
    run_banner()
    print(option_text())
    try:
        opt = int(input(f"{Wh}Select Option: {Gr}"))
        execute_option(opt)
    except ValueError:
        print(f"{Re}Please input a number")
        time.sleep(2)
        main()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Wh}[{Re}!{Wh}] {Re}Exit")
        time.sleep(2)
        exit()
