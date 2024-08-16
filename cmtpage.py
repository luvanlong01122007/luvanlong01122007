import requests,sys,os,time,random
den = '[1;90m'
luc = '[1;32m'
trang = '[1;37m'
red = '[1;31m'
vang = '[1;33m'
tim = '[1;35m'
lamd = '[1;34m'
lam = '[1;36m'
purple = '\e[35m'
hong = '[1;95m'
xnhac = '[1;95m'
xduong = '[1;95m'
do = '[1;33m'
thanh_xau = trang + '' + lam + '[' + vang + 'vL' + lam + '] ' + trang + ' ' + luc
thanh_dep = trang + '' + lam + '[' + luc + 'vL' + lam + '] ' + trang + ' ' + luc
import requests
import json
import os
from sys import platform
from datetime import datetime
from time import sleep, strftime
import hashlib
import hmac
import uuid

try:
    from pystyle import Colors, Colorate
except ImportError:
    os.system('pip install pystyle')
    from pystyle import Colors, Colorate

secret_key = 'vLongzZ'

def generate_signature(data, secret_key, nonce):
    message = f'{data}{nonce}'
    return hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()

def is_connected():
    try:
        import socket
        socket.create_connection(('1.1.1.1', 53))
        return True
    except OSError:
        return False

headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36'}

banners = f"""        ██╗░░░██╗██╗░░░░░░█████╗░███╗░░██╗░██████╗░
        ██║░░░██║██║░░░░░██╔══██╗████╗░██║██╔════╝░
        ╚██╗░██╔╝██║░░░░░██║░░██║██╔██╗██║██║░░██╗░
        ░╚████╔╝░██║░░░░░██║░░██║██║╚████║██║░░╚██╗
        ░░╚██╔╝░░███████╗╚█████╔╝██║░╚███║╚██████╔╝
        ░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚══╝░╚═════╝░"""

thongtin = f"""
        Tải Tool + source tool tại : https://dichvukey.site
        Mua Key Tại : ZALO : 0789041631
        Giá Chỉ 1k / ngày
        MUA CODE - LÀM TOOL GỘP LIÊN HỆ
        Bot spam sms free : https://t.me/vlongbotsms
"""

def luu(key):
    try:
        with open("vLong_key.txt", 'w') as file_key:
            file_key.write(key)
    except Exception as e:
        print(f"Lỗi khi lưu key: {e}")

def checkkey(key):
    nonce = str(uuid.uuid4())
    signature = generate_signature(key, secret_key, nonce)
    try:
        response = requests.get(f'https://dichvukey.site/api/keyvip.php?key={key}&signature={signature}&nonce={nonce}')
        response.raise_for_status()
        check_keyphi = response.json()
        return check_keyphi
    except requests.RequestException as e:
        print(f"Lỗi khi check key: {e}")
        return {'status': 'error', 'msg': str(e)}

def vanlong(so):
    a = '────' * (so - 1) + '─'
    for i in range(len(a)):
        sleep(0.003)
    print(a)

def clear():
    if platform.startswith('linux'):
        os.system('clear')
    else:
        os.system('cls')

def banner():
    print('[0m', end='')
    clear()
    a = Colorate.Horizontal(Colors.blue_to_green, banners)
    print(a)
    print(thongtin)
    vanlong(17)

try:
    url = requests.post('https://dichvukey.site/key100.php', headers=headers, data={'pass': 'vLong'}).json()
    user_agent = url['user_agent']
    c = strftime('%d%m%Y')
    d = f'{c}toolvip{user_agent}'
    p = hashlib.md5(d.encode()).hexdigest()
    ma_key = p[:9]
    link = url['link']
except Exception as e:
    print(f'\033[91mKey Sai Hoặc Đã Hết Hạn\033[0m')
    exit(1)

banner()

def prompt_for_key():
    print(f'\033[91mVượt Link Hoặc Mua Key Tại : zalo 0789041631 \033[0m')
    print(f'\033[91mLink Lấy Key: {link}\033[0m')
    print(f'KeyVip Miễn Phí : vLong\033[0m')

    vanlong(17)
    key = input(f'\033[93mNhập Key Đã Mua Hoặc Key Free: \033[0m').strip()
    print('\033[91m', end='')
    vanlong(17)
    return key

def handle_key(key):
    check_keyphi = checkkey(key)
    if key == ma_key:
        print('\033[91mKey Chính Xác\033[0m')
        luu(key)
        return True
    elif check_keyphi.get('status') == 'error':
        print(f'\033[91mKey Sai Hoặc Đã Hết Hạn\033[0m')
        return False
    else:
        try:
            name = check_keyphi['name']
            remaining_days = check_keyphi['remaining_days']
            remaining_hours = check_keyphi['remaining_hours']
            remaining_minutes = check_keyphi['remaining_minutes']
            create = check_keyphi['create']

            print(f'\033[91mKey Chính Xác\033[0m')
            luu(key)

            # Display remaining time
            print(f'\033[92mSố Ngày Còn Lại: {remaining_days} Ngày, {remaining_hours} Giờ, {remaining_minutes} Phút\033[0m')
            print(f'\033[92mThời Gian Tạo key: {create}\033[0m')

            return True
        except KeyError:
            print(f"\033[91m{check_keyphi.get('msg', 'Key không hợp lệ')}\033[0m")
            return False

while True:
    if not os.path.exists('vLong_key.txt'):
        key = prompt_for_key()
        if len(key) < 1:
            print('\033[91mKey không hợp lệ\033[0m')
            continue
        
        if handle_key(key):
            break
    else:
        with open('vLong_key.txt', 'r') as file_key:
            key_cu = file_key.read().strip()
        
        check_keyphi = checkkey(key_cu)
        if key_cu == ma_key:
            print('\033[91mKey Chính Xác\033[0m', end='\r')
            break
        elif check_keyphi.get('status') == 'error':
            print('\033[91mServer Key Phí Đang Lỗi Hãy Dùng Key Free\033[0m')
            os.remove('vLong_key.txt')
            continue
        else:
            try:
                name = check_keyphi['name']
                remaining_days = check_keyphi['remaining_days']
                remaining_hours = check_keyphi['remaining_hours']
                remaining_minutes = check_keyphi['remaining_minutes']
                create = check_keyphi['create']

                print(f'\033[91mKey Chính Xác\033[0m')


                print(f'\033[92mSố Ngày Còn Lại: {remaining_days} Ngày, {remaining_hours} Giờ, {remaining_minutes} Phút\033[0m')
                print(f'\033[92mThời Gian Tạo key: {create}\033[0m')

                break
            except KeyError:
                if check_keyphi.get('msg') == 'Key Không Tồn Tại!':
                    print(f'\033[91mKey {key_cu} Đã Được Thay Thế Vui Lòng Lấy Key Mới\033[0m')
                else:
                    print(f'\033[91m{check_keyphi.get("msg", "Lỗi không xác định")}\033[0m')
                os.remove('vLong_key.txt')
                continue

banner()
if 'check' in locals() and check:
    keycode = key_cu if len(key_cu) < 4 else '*' * len(key_cu)
    print(f'\033[91mNgười Mua: {name}\033[0m')
    print(f'\033[91mKey Code: {keycode}\033[0m')
    if len(key_cu) == 0:
        print(f'\033[91mHãy Mua KeyVip =)) \033[0m')
        print(f'\033[91mLink Lấy Key: {link}\033[0m')
        exit(0)

if 'check' in locals() and check:
    if len(keycode) == 0:
        print(f'\033[91mHãy Mua KeyVip =)) \033[0m')
        print(f'\033[91mLink Lấy Key: {link}\033[0m')
        exit(0)
    print(f'\033[91mSố Ngày Còn Lại: {remaining_days} Ngày, {remaining_hours} Giờ, {remaining_minutes} Phút\033[0m')
    print(f'\033[91mThời Gian Tạo key: {create}\033[0m')

# Main execution logic to check and handle key input
while True:
    if not os.path.exists('vLong_key.txt'):
        key = prompt_for_key()
        if len(key) < 1:
            print('\033[91mKey không hợp lệ\033[0m')
            continue
        
        if handle_key(key):
            break
    else:
        with open('vLong_key.txt', 'r') as file_key:
            key_cu = file_key.read().strip()
        
        check_keyphi = checkkey(key_cu)
        if key_cu == ma_key:
            print('\033[91mKey Chính Xác\033[0m', end='\r')
            break
        elif check_keyphi.get('status') == 'error':
            print('\033[91mServer Key Phí Đang Lỗi Hãy Dùng Key Free\033[0m')
            os.remove('vLong_key.txt')
            continue
        else:
            try:
                name = check_keyphi['name']
                remaining_days = check_keyphi['remaining_days']
                remaining_hours = check_keyphi['remaining_hours']
                remaining_minutes = check_keyphi['remaining_minutes']
                create = check_keyphi['create']

                print(f'\033[91mKey Chính Xác\033[0m')

                print(f'\033[92mSố Ngày Còn Lại: {remaining_days} Ngày, {remaining_hours} Giờ, {remaining_minutes} Phút\033[0m')
                print(f'\033[92mThời Gian Tạo key: {create}\033[0m')

                break
            except KeyError:
                if check_keyphi.get('msg') == 'Key Không Tồn Tại!':
                    print(f'\033[91mKey {key_cu} Đã Được Thay Thế Vui Lòng Lấy Key Mới\033[0m')
                else:
                    print(f'\033[91m{check_keyphi.get("msg", "Lỗi không xác định")}\033[0m')
                os.remove('vLong_key.txt')
                continue

banner()
if 'check' in locals() and check:
    keycode = key_cu if len(key_cu) < 4 else '*' * len(key_cu)
    print(f'\033[91mNgười Mua: {name}\033[0m')
    print(f'\033[91mKey Code: {keycode}\033[0m')
    if len(key_cu) == 0:
        print(f'\033[91mHãy Mua KeyVip =)) \033[0m')
        print(f'\033[91mLink Lấy Key: {link}\033[0m')
        exit(0)

if 'check' in locals() and check:
    if len(keycode) == 0:
        print(f'\033[91mHãy Mua KeyVip =)) \033[0m')
        print(f'\033[91mLink Lấy Key: {link}\033[0m')
        exit(0)
    print(f'\033[91mSố Ngày Còn Lại: {remaining_days} Ngày, {remaining_hours} Giờ, {remaining_minutes} Phút\033[0m')
    print(f'\033[91mThời Gian Tạo key: {create}\033[0m')
# SETUP TOOL
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
put = f"{vang}[{do}vL{vang}] => {xnhac}"
out = f"{vang}[{do}vL{vang}] => {xnhac}"
list_cmt = []
tokenl = []
list_acc = []
success = []

def tool_cmt(session, listcmt, tokenl, post, sl, time, acc, jsondatapage):
    while True:
        for acccmt in acc:
            tokenrun = tokenl[acccmt]
            name = jsondatapage['data'][acccmt]['name']
            id = jsondatapage['data'][acccmt]['id']
            print(f"{out}TÊN : {vang}{name} {luc}: ID : {xduong}{id}")
            for i in range(int(sl)):
                message = random.choice(listcmt)
                data = {
                    'access_token': tokenrun,
                    'message': message
                }
                rq = session.post(f"https://graph.facebook.com/{post}/comments", data=data).json()
                if 'id' in rq:
                    print(f"{trang}[{do}{len(success)+1}{trang}]{luc} MESSAGE : {message} : STATUS : SUCCESS")
                    success.append(rq['id'])
                    sleep(time)
                else:
                    print(f"{trang}[{do}{i+1}{trang}]{vang} MESSAGE : {message} : STATUS : FAILED")
                    break

banner()
session = requests.Session()
id_post = input(f"{put}Nhập ID Bài Viết: {vang}")
cookie = input(f"{put}Nhập Cookie Acc: {vang}")
session.cookies.update({'cookie': cookie})
token = "EAAG"+session.get('https://business.facebook.com/business_locations/').text.split("EAAG")[1].split('"')[0]
getpage = session.get(f"https://graph.facebook.com/me/accounts?access_token={token}").json()
for getp in getpage['data']:
    print(f"{trang}[{do}{len(tokenl)+1}{trang}] {luc}Tên : {vang}{getp['name']}{luc} : ID : {xduong}{getp['id']}")
    tokenl.append(getp['access_token'])
banner()
soacc = input(f"{put}Nhập Acc Cần Chạy Comment (1+2+3...) Hoặc (all): {vang}")
if soacc == 'all':
    for i in range(len(tokenl)):
        list_acc.append(i)
else:
    acc = soacc.split('+')
    for accrun in acc:
        list_acc.append(int(accrun)-1)
while True:
    socmt = int(len(list_cmt))+1
    cmt = input(f"{out}Nhập Comments {socmt}: {vang}")
    if cmt == '':
        break
    list_cmt.append(cmt)
slcmt = input(f"{put}Sau Bao Nhiêu Comments Thì Đổi Acc: {vang}")
delaytime = int(input(f"{put}Delay Comments: {vang}"))
banner()
tool_cmt(session,list_cmt,tokenl,id_post,slcmt,delaytime,list_acc,getpage)
