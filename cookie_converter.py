from colorama import *
from colorama import Fore, Back, init
#init(True, **('autoreset',))
init(autoreset=True)
bl = Fore.BLACK
wh = Fore.WHITE
yl = Fore.YELLOW
red = Fore.RED
res = Style.RESET_ALL
gr = Fore.GREEN
ble = Fore.BLUE
cy = Fore.CYAN
bwh = Back.WHITE
byl = Back.YELLOW
bred = Back.RED
bgr = Back.GREEN

import json

def convert_to_netscape(json_cookie_file, output_file):
    with open(json_cookie_file, 'r') as f:
        cookie_data = json.load(f)

    netscape_cookie = ""
    for cookie_name, cookie_value in cookie_data.items():
        if isinstance(cookie_value, dict):
            cookie_domain = cookie_value.get("domain", "")
            cookie_value_str = json.dumps(cookie_value["value"])
        else:
            cookie_domain = ""
            cookie_value_str = json.dumps(cookie_value)

        netscape_cookie += f"{cookie_domain}\tTRUE\t/\tFALSE\t0\t{cookie_name}\t{cookie_value_str}\n"

    with open(output_file, 'w') as f:
        f.write(netscape_cookie)
    print(f'''{gr}''' + "Successfully converted, please check the text file in this folder\n")
    input("Conversion completed. Press Enter to exit.")



print()
print(f'''{red}''' """\t\t\tCOOKIE CONVERTER\n""")
print(f'''{yl}''' """
This typically convert .json format of the cookie you exported and convert to Netscape format
for easy import to another browser.\n""")
print(f'''{cy}''' """Coded by Holyboii --> contact on Telegram: @holyboii
 \n""")

json_cookie_file = input("Please enter the name of your .json cookie file (e.g., export_cookie.json): ")
output_file = 'netscape_cookies_output.txt'

convert_to_netscape(json_cookie_file, output_file)


