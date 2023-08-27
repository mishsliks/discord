import requests
from pymongo import MongoClient
import time
import threading
from config import Your_data_base

password = 'QRFfsca9UaLUH9H2'
cluster_url = 'mongodb+srv://uchisasuke468:' + \
    password + '@cluster0.byr4qsl.mongodb.net/'

client = MongoClient(cluster_url)

db = client['BNSL']

cli = Your_data_base

data = db[cli]

url = "https://discord.com/api/v9/channels/1144174264128389181/messages"

def main():
    while True:
        dat = data.find_one({'cli':cli})
        if dat:
            for aut in dat['auths']:
                try:
                    auth = {'authorization':aut}
                    msg = {'content':'!work'}
                    requests.post(url,headers=auth,data=msg)
                    time.sleep(10)
                except Exception:
                    continue
        time.sleep(7200)

def main2():
    while True:
        dat = data.find_one({'cli':cli})
        if dat:
            for aut in dat['auths']:
                try:
                    auth = {'authorization':aut}
                    msg = {'content':'!daily'}
                    requests.post(url,headers=auth,data=msg)
                    time.sleep(10)
                except Exception:
                    continue
        time.sleep(86400)

time_thread = threading.Thread(target=main2)
time_thread.start()

main()
