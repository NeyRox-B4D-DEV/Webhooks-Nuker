import requests, time, utils
from colorama import Fore, Back, Style
from discord import Webhook, RequestsWebhookAdapter

utils.checker_intro()
webhook = input(Fore.MAGENTA + Style.DIM + " [NEYROX] URL: ")
print(Style.RESET_ALL)

check = requests.get(webhook)
if check.status_code == 404:
    print(Fore.RED + Style.BRIGHT + "\n [DB0X] Webhook non correct!" + Style.RESET_ALL)
    time.sleep(5)
elif check.status_code == 200:
    print(Fore.GREEN + Style.BRIGHT + "\n [DB0X] Webhook correct!" + Style.RESET_ALL)
    time.sleep(1)
    utils.killer_intro()
    print(Fore.YELLOW + Style.BRIGHT + "\n [DB0X] Supression du webhhook...!" + Style.RESET_ALL)
    requests.delete(webhook)
    checker = requests.get(webhook)
    if checker.status_code == 404:
        print(Fore.GREEN + Style.BRIGHT + "\n [DB0X] Webhook detruit avec succes!" + Style.RESET_ALL)
    elif checker.status_code == 200:
        print(Fore.RED + Style.BRIGHT + "\n [DB0X] Une erreur c'est prodruite au moment de la destruction du webhook!" + Style.RESET_ALL)
    time.sleep(5)