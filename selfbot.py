from discord_webhook import DiscordWebhook
import os

weburl = input("Enter your webhook url: ")

while True:
    a = input("Testo > ")
    if a != "quit" and a != "break" and a != "exit" and a[:7] != "file > " and a != "cls":
        webhook = DiscordWebhook(url=weburl, content=a)
        webhook.execute()
    elif a[:7] == "file > ":
        try:
            if os.path.getsize(a[7:]) <= 1048576:
                webhook = DiscordWebhook(url=weburl)
                with open(a[7:], "rb") as f:
                    webhook.add_file(file=f.read(), filename=a[7:])
                webhook.execute()
            elif os.path.getsize(a[7:]) > 1048576:
                print("Il file specificato è troppo pesante")
        except:
            print('Il file specificato non esiste')
    elif a == "cls":
        os.system('cls')
    else:
        break
    