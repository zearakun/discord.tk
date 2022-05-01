import requests
import random


print("""
██████╗░██╗████████╗░█████╗░██╗░░░░░░█████╗░  ██████╗░░█████╗░██╗██████╗░███████╗██████╗░
██╔══██╗██║╚══██╔══╝██╔══██╗██║░░░░░██╔══██╗  ██╔══██╗██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
██║░░██║██║░░░██║░░░██║░░██║██║░░░░░██║░░██║  ██████╔╝███████║██║██║░░██║█████╗░░██████╔╝
██║░░██║██║░░░██║░░░██║░░██║██║░░░░░██║░░██║  ██╔══██╗██╔══██║██║██║░░██║██╔══╝░░██╔══██╗
██████╔╝██║░░░██║░░░╚█████╔╝███████╗╚█████╔╝  ██║░░██║██║░░██║██║██████╔╝███████╗██║░░██║
╚═════╝░╚═╝░░░╚═╝░░░░╚════╝░╚══════╝░╚════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
[1]抜ける サーバーから抜けます
[2]送信 メッセージ送信できます
[3]チェック 名前,id,token,from,mailが分かります
""")

choice = input("1/2/3:")



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
  with open('proxy.txt', 'r') as f:
      lines = f.readlines()
      randomproxy = random.choice(lines)
      proxy = {
        "http://": randomproxy
      }
  s = int(input("何回送るか"))
  for nu in range(s):
            a = random.choice(channel)
            url = 'https://discord.com/api/v9/channels/'+a+'/messages'
            en = ["a","b","c","d","i","e","f","g","h","i","j","k","n","m","l","o","p","q","r","s","","t","u","v","w","s","y","g"]
            enran = f"{random.choice(en)}{random.choice(en)}{random.choice(en)}"
            data = {"content": f"{content}"}
            i = random.choice(token)
            header = {"authorization": i}
            r = requests.post(url, data=data, headers=header)
            if r.status_code == 200:
              print(f"{nu}:行けた")

if choice == "3":
  with open('tokens.txt', 'r') as f:
      token = f.read().splitlines()
  for token in token:
    header = {
      "authorization": token
    }
    userdata = requests.get("https://discord.com/api/v9/users/@me",headers=header).json()
    print(f"<name>{userdata['username']}#{userdata['discriminator']} <id>{userdata['id']} <mail>{userdata['email']} <token>{token} <from>{userdata['locale']}")
