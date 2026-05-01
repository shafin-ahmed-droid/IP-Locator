import requests
from colorama import init, Fore, Style

init(autoreset=True)


ascii_banner = r"""
 _____ _____   _                        _             
|_   _|  __ \ | |                      | |            
  | | | |__) || |     ___   ___   __ _ | |_ ___   _ __
  | | |  ___/ | |    / _ \ / __| / _` || __/ _ \ | '__|
 _| |_| |     | |___| (_) | (__ | (_| || || (_) || |   
 \___/\_|     |______\___/ \___| \__,_| \__\___/ |_|   
"""

print(Fore.CYAN + ascii_banner)


def get_ip(ip):

    try:
        print(Fore.BLUE + "\n[*] Scanning IP . . . . .\n")
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        response.raise_for_status()
        data = response.json()
        return{
            "IP": data.get("ip"),
            "City": data.get("city"),
            "Region": data.get("region"),
            "Country": data.get("country"),
            "Coordinates": data.get("loc"),
            "ISP": data.get("org"),
            "Timezone": data.get("timezone")
        }
    except Exception as e:
        return{
            "Error": f"Failed {str(e)}"
        }
    

def display_result(result):
    print(Fore.CYAN + "=" * 40)

    for key, value in result.items():
        print(Fore.GREEN + f"{key:<15}" + Fore.WHITE + f": {value}")

    print(Fore.CYAN + "=" * 40)


print(Fore.MAGENTA + "=== IP LOCATOR ===")

ip = input(Fore.GREEN + "Enter IP address: ")

result = get_ip(ip)

display_result(result)