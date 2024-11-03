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
print("        TamperX V2.0: Verb Tampering Vulnerability Checker")

import requests
import sys
import re
from pyhttpsnippet import HttpToRequestsConverter

help_text = """
[-] Usage: 
    python tamperx.py -u <url>
    python tamperx.py -f <file_name>.txt
    
[*] Options:
    -p  set proxy - example: socks5://127.0.0.1:9150
    -r  read cookies from raw http request
    -l  save logs in out.txt - default is disable 
    -h  show help text
    -a  set custom user agent
    
"""
if len(sys.argv) < 2:
    print(help_text)
    sys.exit(1)

class SessionMaker:
    def __init__(self):
        self.session = requests.session()

    def setcookies(self, cookies):
        self.session.cookies.update(cookies)

    def setHeaders(self, Headers):
        self.session.headers = Headers

    def setUserAgent(self, agent):
        self.session.headers['User-Agent'] = agent

    def setProxy(self, proxy):
        self.session.proxies = {
            "http": proxy,
            "https": proxy
        }

    def getSession(self):
        return self.session




def doTamper(url,session,save_logs):
    url_pattern = re.compile(r'^https?://(?:[a-z0-9-]+\.)+[a-z]{2,}\/?', re.IGNORECASE)
    if not url_pattern.match(url):
        print("[-] Invalid URL format")
        return

    http_methods = ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "TRACE", "PATCH"]

    print(f'\n[+] Target Url: {url}\n')
    print('Method'.ljust(10), 'Status'.ljust(10), 'Content'.ljust(11))
    print("-" * 32)
    if save_logs:
        file = open("out.txt",'a+')
    for method in http_methods:
        response = session.request(method, url)
        status_text = f'{response.status_code}'.ljust(10)
        content_len_text = f'{len(response.content)}'.ljust(11)
        print(f"{method.ljust(10)} {status_text} {content_len_text}")
        if save_logs:
            file.write(f"{method},{response.status_code},{len(response.content)},{url}\n")

    if save_logs:
        file.close()

if __name__ == "__main__":
    endpoint = None
    file = None
    save_logs = False
    proxy = None
    convert_raw_http = None
    cookies = None
    useragent = None
    session = SessionMaker()

    if '-h' in sys.argv:
        print(help_text)
        sys.exit()

    if '-f' in sys.argv:
        ifile_index = sys.argv.index('-f') + 1
        if ifile_index < len(sys.argv):
            file = sys.argv[ifile_index]

    if '-u' in sys.argv:
        endpoint_index = sys.argv.index('-u') + 1
        if endpoint_index < len(sys.argv):
            endpoint = sys.argv[endpoint_index]

    if '-l' in sys.argv:
        save_logs = True

    if '-p' in sys.argv:
        proxy_index = sys.argv.index('-p') + 1
        if proxy_index < len(sys.argv):
            proxy = sys.argv[proxy_index]
            session.setProxy(proxy)

    if '-r' in sys.argv:
        httpraw_index = sys.argv.index('-r') + 1
        if httpraw_index < len(sys.argv):
            convert_raw_http = sys.argv[httpraw_index]

    if '-a' in sys.argv:
        useragent_index = sys.argv.index('-a') + 1
        if useragent_index < len(sys.argv):
            useragent = sys.argv[useragent_index]

    if not endpoint and not file:
        print("[X] Error: No url or file provided.")
        sys.exit(1)

    if endpoint and file:
        print("[X] Error: Just one of url or file must be provided.")
        sys.exit(1)


    if convert_raw_http:
        __file = open(convert_raw_http,'r').read()
        request = HttpToRequestsConverter(__file)
        session.setcookies(request.cookies)
        session.setHeaders(request.headers)

    if useragent:
        session.setUserAgent(useragent)

    session = session.getSession()
    if endpoint:
        doTamper(endpoint,session,save_logs)
    else:
        for endpoint in open(file,'r').readlines():
            doTamper(endpoint,session, save_logs)






