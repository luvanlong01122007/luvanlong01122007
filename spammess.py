import requests, os
import socket
os.system("clear")
from time import sleep
ip=socket.gethostbyname(socket.gethostname())
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
time=datetime.now().strftime("%H:%M:%S")
import requests
import socket
from pystyle import *
#import màu
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

LCT_tool = trang + "vL" + trang + "[" + do + trang + "] " + trang + "=> "

toandz = trang + "vL" + trang + "[" + do + trang + "] " + trang + "=> "

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

os.system("cls" if os.name == "nt" else "clear")

banner()
id=input(f'{trang}Nhập id người cần spam: {vang} ')
while True:
    ck=input(f' {trang}Nhập cookie facebook: {vang} ')
    try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={id}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        os.system('cls')
        break
    except:
        print(f'{do}Cookie sai!!')
    


nd=input(f' {trang}hập nội dung:{vang} ')
so_luong=int(input('\033[1;37mNhập số tin nhắn muốn gửi: \033[1;33m '))
delay=int(input('\033[1;37mNhập delay\033[1;37m: \033[1;33m'))
headers = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
    # Requests sorts cookies= alphabetically
    'cookie': ck,
    'origin': 'https://m.facebook.com',
    'referer': 'https://www.facebook.com',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-response-format': 'JSONStream',
}

params = {
    'icm': '1',
}

data = {
    f'ids[{id}]': id,
    'body': nd,
    'waterfall_source': 'message',
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
}
for i in range(1,so_luong+1):
    response = requests.post('https://m.facebook.com/messages/send/', params=params, headers=headers, data=data)
    print(f'{lam}vLong zZ {do}|{vang}{i} Send Success {do}| {vang}{nd}')
    sleep(delay)