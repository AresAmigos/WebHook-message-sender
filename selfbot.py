from discord_webhook import DiscordWebhook
import os
from sys import platform as c

weburl = input("Enter your webhook url: ")

while True:
    a = input("Message > ")
    if a != "clear" and a != "quit" and a != "break" and a != "exit" and a[:7] != "file > " and a != "cls":
        webhook = DiscordWebhook(url=weburl, content=a)
        webhook.execute()
    elif a[:7] == "file > ":
        try:
            if os.path.getsize(a[7:]) <= 25 * 1024 * 1024:
                webhook = DiscordWebhook(url=weburl)
                with open(a[7:], "rb") as f:
                    webhook.add_file(file=f.read(), filename=a[7:])
                webhook.execute()
            elif os.path.getsize(a[7:]) > 25 * 1024 * 1024:
                print("The file is too big")
        except:
            print("The file doesn't exist")
    elif a == "cls" or a == "clear":
        if c == "win32":
            os.system('cls')
        elif c == "linux":
            os.system('clear')
        else:
            print("What the fuck operation system do you have? Unix? LOL")
    else:
        break
