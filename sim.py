import requests
import time
import threading
import random
import os
import csv

def sim_google():
    query = ['fortnite', 'youtube', 'stocks', 'divorce', 'archwiki', 'wpi']
    requests.get("https://www.google.com/search?q={}".format(random.choice(query)))

def others():
    site=['github.com', 'reddit.com', 'apple.com', 'netflix.com', 'microsoft.com', 'raspberrypi.com']
    requests.get("https://{}.".format(random.choice(site)))

hostfile = open("/etc/trafficsim/top-1m.csv",'r')
hostf = csv.reader(hostfile)
hosts = []
name_servers = ["1.1.1.1","8.8.8.8","8.8.4.4","9.9.9.9","208.67.222.222","8.26.56.26"]
for i in hostf:
    hosts.append(i[1])
while True:
    time.sleep(random.randrange(1,15))
    if random.random() < 0.5:
        sim_google()
    else:
        others()
    if random.randrange(0,59):
        os.system("apt update")
    os.system("dig {} @{}".format(random.choice(hosts),random.choice(name_servers)))
    
