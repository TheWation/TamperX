#  __     __     ______     ______   __     ______     __   __    
# /\ \  _ \ \   /\  __ \   /\__  _\ /\ \   /\  __ \   /\ "-.\ \   
# \ \ \/ ".\ \  \ \  __ \  \/_/\ \/ \ \ \  \ \ \/\ \  \ \ \-.  \  
#  \ \__/".~\_\  \ \_\ \_\    \ \_\  \ \_\  \ \_____\  \ \_\\"\_\ 
#   \/_/   \/_/   \/_/\/_/     \/_/   \/_/   \/_____/   \/_/ \/_/ 

print("  __     __     ______     ______   __     ______     __   __    ")
print(" /\\ \\  _ \\ \\   /\\  __ \\   /\\__  _\\ /\\ \\   /\\  __ \\   /\\ \"-.\\ \\   ")
print(" \\ \\ \\/ \".\\ \\  \\ \\  __ \\  \\/_/\\ \\/ \\ \\ \\  \\ \\ \\/\\ \\  \\ \\ \\-.  \\  ")
print("  \\ \\__/\".~\\_\\  \\ \\_\\ \\_\\    \\ \\_\\  \\ \\_\\  \\ \\_____\\  \\ \\_\\\"\\_ \\ ")
print("   \\/_/   \\/_/   \\/_/\\/_/     \\/_/   \\/_/   \\/_____/   \\/_/ \\/_/ ")
print("        TamperX V1.0: Verb Tampering Vulnerability Checker")

import requests
import sys
import re

if len(sys.argv) < 2:
    print("[-] URL not provided")
    sys.exit(1)

url = sys.argv[1]
url_pattern = re.compile(r'^https?://(?:[a-z0-9-]+\.)+[a-z]{2,}\/?', re.IGNORECASE)
if not url_pattern.match(url):
    print("[-] Invalid URL format")
    sys.exit(1)

http_methods = ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "TRACE", "PATCH"]

print(f'\n[+] Target Url: {url}\n')

print('Method'.ljust(10), 'Status'.ljust(10), 'Content'.ljust(11))
print("-" * 32)
for method in http_methods:
    response = requests.request(method, url)
    status_text = f'{response.status_code}'.ljust(10)
    content_len_text = f'{len(response.content)}'.ljust(11)
    print(f"{method.ljust(10)} {status_text} {content_len_text}")