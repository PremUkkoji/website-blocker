import time
from datetime import datetime as dt

website_list = ["www.facebook.com","facebook.com"]
redirect = "127.0.0.1"
filepath = "/etc/hosts"

start = 8
end = 16

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,start) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
        #print("working time...")
        with open(filepath,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        #print("Fun time...")
        with open(filepath,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website for website in website_list):
                    file.write(content)
            file.truncate()
    time.sleep(5)
