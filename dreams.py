import requests, os, platform, time
from colorama import Fore, Back, Style

os.system("title HOOK SPAMMER - angelo 1777")

print("""
   ▄████████ ███▄▄▄▄      ▄██████▄     ▄████████  ▄█        ▄██████▄  
  ███    ███ ███▀▀▀██▄   ███    ███   ███    ███ ███       ███    ███ 
  ███    ███ ███   ███   ███    █▀    ███    █▀  ███       ███    ███ 
  ███    ███ ███   ███  ▄███         ▄███▄▄▄     ███       ███    ███ 
▀███████████ ███   ███ ▀▀███ ████▄  ▀▀███▀▀▀     ███       ███    ███ 
  ███    ███ ███   ███   ███    ███   ███    █▄  ███       ███    ███ 
  ███    ███ ███   ███   ███    ███   ███    ███ ███▌    ▄ ███    ███ 
  ███    █▀   ▀█   █▀    ████████▀    ██████████ █████▄▄██  ▀██████▀  
                                                 ▀                    
                  Hook Spammer by angelo;#1777
"""
+ "")
print("")

webhook = input("Webhook > ")
text = input("Mensagem > ") 

if platform.system() == "Windows": 
    clearcmd = "cls"
else:
    clearcmd = "clear"

os.system(clearcmd)

data = {
    "content": text 
}
def send(i):
    res = requests.post(webhook, data=data) 
    try:
        print('Cooldown, aguarde ' + str(res.json()["retry_after"]) + 'ms.')
        time.sleep(res.json()["retry_after"]/1000)
        res = 'Aguardado' + str(res.json()["retry_after"]) + 'ms.'
    except:
        i += 1
        res = "Enviado " + text + " com sucesso!"
    print('Quantidade de mensagens enviadas: ' + Fore.BLUE + str(i)) 
    return i
i = 0
while True: 
   i = send(i)
