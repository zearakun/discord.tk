import requests
import random


print("""
██████╗░██╗████████╗░█████╗░██╗░░░░░░█████╗░  ██████╗░░█████╗░██╗██████╗░███████╗██████╗░
██╔══██╗██║╚══██╔══╝██╔══██╗██║░░░░░██╔══██╗  ██╔══██╗██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
██║░░██║██║░░░██║░░░██║░░██║██║░░░░░██║░░██║  ██████╔╝███████║██║██║░░██║█████╗░░██████╔╝
██║░░██║██║░░░██║░░░██║░░██║██║░░░░░██║░░██║  ██╔══██╗██╔══██║██║██║░░██║██╔══╝░░██╔══██╗
██████╔╝██║░░░██║░░░╚█████╔╝███████╗╚█████╔╝  ██║░░██║██║░░██║██║██████╔╝███████╗██║░░██║
╚═════╝░╚═╝░░░╚═╝░░░░╚════╝░╚══════╝░╚════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
[1]抜ける
[2]送信
""")

choice = input("1/2:")



if choice == "1":
  guild = input("guildid:")
  with open('tokens.txt', 'r') as f:
      token = f.read().splitlines()
  for i in token:
    headers={'authorization': i}
    requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild}",headers=headers)

if choice == "2":
  with open('tokens.txt', 'r') as f:
      token = f.read().splitlines()
  with open('channel.txt', 'r') as f:
      channel = f.read().splitlines()
  with open('content.txt', 'r') as f:
      content = f.read()
  for nu in range(100):
            a = random.choice(channel)
            url = 'https://discord.com/api/v9/channels/'+a+'/messages'
            en = ["a","b","c","d","i","e","f","g","h","i","j","k","n","m","l","o","p","q","r","s","","t","u","v","w","s","y","g"]
            enran = f"{random.choice(en)}{random.choice(en)}{random.choice(en)}"
            data = {"content": f"{content} #ditoloはこの活動を支援しています {random.choice(range(0,99999))}{enran}"}
            i = random.choice(token)
            header = {"authorization": i}
            r = requests.post(url, data=data, headers=header)
            if r.status_code == 200:
              print(f"{nu}:行けたよ|{i}|")
            if r.status_code == 400:
              print("失敗...")
