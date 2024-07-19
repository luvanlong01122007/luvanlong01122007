import os, json, sys, requests 
from sys import platform
from time import sleep
from datetime import datetime
from random import randint
from pystyle import Colors, Colorate
import uuid, re
from bs4 import BeautifulSoup
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
time=datetime.now().strftime("%H:%M:%S")
import socket
from pystyle import *
#màu
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
#Đánh Dấu Bản Quyền
HĐ_tool = trang + " " + trang + "[" + do + "vL" + trang + "] " + trang + "=> "
hdang = trang + " " + trang + "[" + do + "÷_+" + trang + "] " + trang + "=> "
thanh = trang + "-------------------------------------------------------------------------"
#today nand clear
os.system('cls')
data_machine = []
today = date.today()
os.system('clear')
#daystime
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")

def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
a = " \033[1;97m[\033[1;31mvL\033[1;97m] => "
__check__ = requests.get('https://raw.githubusercontent.com/vlong07/vlong07/main/sever.txt').text
if "off" in __check__:
  exit("Buồn Của vLong")

banner()
id=input(f' {trang}Nhập ID Box Cần Spam:{vang} ')
while True:
    ck=input(f' {trang}Nhập Cookie Facebook:{vang} ')
    try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={id}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        os.system('clear')
        break
    except:
        print('Cookie sai!!')
    


banner()
nd = input(f" {trang}Nhập Nội Dung: {vang} ")
soluong = int(input(f"\033[1;37mSố Lượng: \033[1;33m "))
delay = int(input(f"\033[1;37mDelay: \033[1;33m "))

params = {
	"icm": '1',
}

headers = {
	"Host":"mbasic.facebook.com",
	"content-length":"247",
	"content-type":"application/x-www-form-urlencoded",
	"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	"sec-fetch-site":"same-origin",
	"sec-fetch-mode":"navigate",
	"sec-fetch-user":"?1",
	"sec-fetch-dest":"document",
	"accept-encoding":"gzip, deflate, br",
	"accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
	"cookie":ck,
}
data = f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body={nd}&send=Send&tids=cid.g.{id}&wwwupp=C3&platform_xmd=&referrer=&ctype=&cver=legacy&csid=366a74a7-2d30-45dd-94c2-ad47d662dcfb"

def nghingoi(delay):
	for x in range(delay,0,-1):
		print(f"\r\033[1;31m[\033[1;33mvLong zZ\033[1;31m] \033[1;91m ~>       \033[1;92m LO      \033[1;91m | {x} | \r ", end='')
		sleep(0.14)
		print(f"\r\033[1;31m[\033[1;33mvLong zZ\033[1;31m] \033[1;91m   ~>     \033[1;92m LOA     \033[0;31m | {x} | \r ", end='')
		sleep(0.14)
		print(f"\r\033[1;31m[\033[1;33mvLong zZ\033[1;31m] \033[1;91m     ~>   \033[1;92m LOAD    \033[0;31m | {x} | \r", end='')
		sleep(0.14)
		print(f"\r\033[1;31m[\033[1;33mvLong zZ\033[1;31m] \033[1;91m       ~> \033[1;92m LOADI   \033[0;31m | {x} | \r", end='')
		sleep(0.14)
		print(f"\r\033[1;31m[\033[1;33mvLong zZ\033[1;31m] \033[1;91m        ~>\033[1;92m LOADIN  \033[0;31m | {x} | \r", end='')
		sleep(0.14)
		print(f"\r\033[1;31m[\033[1;33mvLong zZ\033[1;31m] \033[1;91m        ~>\033[1;92m LOADING \033[0;31m | {x} | \r", end='')
		sleep(0.14)
		print(f"\r\033[1;31m[\033[1;33mvLong zZ\033[1;31m] \033[1;91m        ~>\033[1;92m LOADING.\033[0;31m | {x} | \r", end='')
		sleep(0.14)
	print("\r\r\033[1;95m   vLong zZ                       \r", end='')
	sleep(0.1)

for i in range(soluong):
	rq = requests.post("https://mbasic.facebook.com/messages/send/",params=params,headers=headers,data=data)
	i=i+1
	print(f" \033[1;31m[\033[1;33m{i}\033[1;31m] \033[1;31m| {trang}ID BOX: {vang}{id} \033[1;31m| {trang}NỘI DUNG: {vang}{nd} \033[1;31m| {vang}TRẠNG THÁI:{luc} SUCCESS")
	nghingoi(delay)