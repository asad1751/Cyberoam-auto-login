import requests
import time

#roll='btech1000618'
roll='' #write your login id here

data = {'mode':'193', 'username' : roll , 'a' : time.time() , 'producttype' : 0}

headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0' ,
             'Referer' : 'https://172.16.1.1:8090/httpclient.html?u=http://detectportal.firefox.com/success.txt' }

url = 'https://172.16.1.1:8090/logout.xml'

session = requests.Session()
session.verify = False
r = session.post(url,data=data,headers=headers)

print(r.text)






