
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
import importlib
import hashlib
try:
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
except:
    os.system('pip install pystyle')
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

bug_cai_lon_nha = {'pass': 'vLong'}

def is_connected():
    try:
        import socket
        socket.create_connection(('1.1.1.1', 53))
        return True
    except OSError:
        pass
    return False

headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 11; Live 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.28 Mobile Safari/537.36'}
banners = f"""        ██╗░░░██╗██╗░░░░░░█████╗░███╗░░██╗░██████╗░
        ██║░░░██║██║░░░░░██╔══██╗████╗░██║██╔════╝░
        ╚██╗░██╔╝██║░░░░░██║░░██║██╔██╗██║██║░░██╗░
        ░╚████╔╝░██║░░░░░██║░░██║██║╚████║██║░░╚██╗
        ░░╚██╔╝░░███████╗╚█████╔╝██║░╚███║╚██████╔╝
        ░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚══╝░╚═════╝░"""
thongtin = f"""
        Link Box  : https://zalo.me/g/zvqtfl773
        Mua Key Tại : ZALO : 0789041631
        Giá Chỉ 1k / ngày
        MUA CODE - LÀM TOOL GỘP LIÊN HỆ
        Hosting Miễn Phí 6Tháng Chỉ Có Tại : [1;34mhttps://my.h2cloud.vn/
"""

def luu(key):
    try:
        luu = ''
    except:
        pass

def checkkey(key):
    try:
        check_keyphi = requests.get(f'https://dichvukey.site/api/keyvip.php?key={key}').json()
        if check_keyphi['status'] == 'success':
            return check_keyphi
        else:
            return [check_keyphi['msg']]
    except:
        return False

COLOR_RED = '\033[91m'  
COLOR_RESET = '\033[0m'  

def vanlong(so):
    a = '────' * (so - 1) + '─'
    for i in range(len(a)):
        sleep(0.003)
    print(a)


def clear():
    if platform[0:3] == 'lin':
        os.system('clear')
    else:
        os.system('cls')
def vLongzZ():
	print('')

def Api_Facebook():
	print('')
def vLongzZz():
	print('')
def vanlongzZ():
	print('')
def vanlongzZz():
	print('')
def api_fb():
	print('')
def api_cookie():
	print('')
def api_tds():
	print('')

def api_like():
	print('')
def api_camxuc():
	print('')
def banner():
    print('[0m', end='')
    clear()
    a = Colorate.Horizontal(Colors.blue_to_green, banners)
    print(a)
    print(thongtin)
    vanlong(17)

try:
    a = ''
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
        sleep(0.05)
    url = requests.post(f'https://dichvukey.site/key.php', headers = headers, data = bug_cai_lon_nha).json()
    ip = url['ip']
    c = strftime('%d%m%Y')
    d = f'{c}toolvip{ip}'
    p = hashlib.md5(d.encode()).hexdigest()
    ma_key = p[:9]
    link = url['link']
except:
    print('{hong}Key Sai Hoặc Đã Hết Hạn')

banner()

while True:
    check_file_key = os.path.exists('vLong_key.txt')
    if check_file_key == False:
        print(f'     {red}{thanh_xau}  Vượt Link Hoặc Mua Key Tại : zalo 0789041631 ')
        print(f'     {thanh_xau}{hong}  Link Lấy Key: {link}')

        vanlong(17)
        key = input(f'     {thanh_xau}{vang}   Nhập Key Đã Mua Hoặc Key Free: {vang}'); print(red, end = '')
        vanlong(17)
        check_keyphi = checkkey(key)
        if key == ma_key:
            print(f'{hong}Key Chính Xác')
            check = ''
            luu(key)
            file_key = open(f"vLong_key.txt", 'a+')
            file_key.write(key)
            file_key.close()
            break
        elif check_keyphi == False:
            print(red + '{hong}Key Sai Hoặc Đã Hết Hạn')
            continue 
        elif check_keyphi != False:
            try:
                name = check_keyphi['name']
                remaining_days = check_keyphi['remaining_days']
                remaining_hours = check_keyphi['remaining_hours']
                remaining_minutes = check_keyphi['remaining_minutes']
                create = check_keyphi['create']
                
                check = True
                keycode = key
                print(f'{hong}Key Chính Xác')
                luu(key)
                file_key = open(f"vLong_key.txt", 'a+')
                file_key.write(key)
                file_key.close()
                break
            except:
                print(f"{red}{check_keyphi[0]}")
                exit(0)
        else:
            print(f"{red} Key Không Chính Xác, Bạn Chắc Chắn Đã Nhập Đúng Key?")
            exit(0)
    else:
        file_key = open(f"vLong_key.txt", 'r')
        key_cu = file_key.read()
        file_key.close()
        check_keyphi = checkkey(key_cu)
        if key_cu == ma_key:
            print(f'{hong}Key Chính Xác ', end = '\r')
            check = ''
            luu(key_cu)
            break
        elif check_keyphi == False:
            print(red + 'Sever Key Phí Đang Lỗi Hãy Dùng Key Free')
            os.remove('vLong_key.txt')
            continue 
        elif check_keyphi != False:
            try:
                name = check_keyphi['name']
                remaining_days = check_keyphi['remaining_days']
                remaining_hours = check_keyphi['remaining_hours']
                remaining_minutes = check_keyphi['remaining_minutes']
                create = check_keyphi['create']

                

                check = True
                keycode = key_cu
                print(f'{hong}Key Chính Xác')
                luu(key_cu)
                break
            except:
                if check_keyphi[0] == 'Key Không Tồn Tại!':
                    print(f'{thanh_xau}{luc}Key {hong}{key_cu} {luc}Đã Được Thay Thế Vui Lòng Lấy Key Mới')
                else:
                    print(red + check_keyphi[0])
                os.remove('vLong_key.txt')
                continue 
        else:
            print(f"{hong} Key Không Chính Xác, Bạn Chắc Chắn Đã Nhập Đúng Key?")
            exit(0)

banner()
if check==True:
    if len(keycode)==3 or len(keycode)==2 or len(keycode)==1:keycode='*'*len(keycode)
    elif len(keycode)==4:keycode=keycode.replace(keycode[0:3],'***')
    elif len(keycode)==5:keycode=keycode.replace(keycode[0:4],'****')
    elif len(keycode)==6:keycode=keycode.replace(keycode[0:5],'*****')
    elif len(keycode)==7:keycode=keycode.replace(keycode[0:5],'*****')
    else:keycode=keycode.replace(keycode[0:len(keycode)-3],'*'*len(keycode[0:len(keycode)-3]))
    print(thanh_xau+luc+'Người Mua: '+vang+name)
    print(thanh_xau+luc+'Key Code: '+vang+keycode)
if check == True:
    if len(keycode) == 0:
        print(f'{thanh_xau}{red}Hãy Mua KeyVip =)) ')
        print(f'{thanh_xau}{luc}Link Lấy Key: {link}')
        exit(0)
    name = check_keyphi['name']
    coun3 = remaining_days
    coun2 = remaining_hours
    coun1 = remaining_minutes
    coun = create

    print(f"{thanh_xau}{luc}Số Ngày Còn Lại: {vang}{coun3} Ngày, {coun2} Giờ, {coun1} Phút{red}")
    print(f"{thanh_xau}{luc}Thời Gian Tạo key : {vang}{coun}")


if check == False:
    pass

print("\033[1;39m   ╔═════════════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL Trao Đổi Sub \033[1;39m  ║ ")
print("\033[1;39m   ╚═════════════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[1.1] \033[38;5;204mTOOL TDS TIKTOK + TIKTOK NOW")
print("\033[38;5;155m      Nhập Số \033[1;36m[1.2] \033[38;5;204mTOOL AUTO TDS FACEBOOK ")
print("\033[38;5;155m      Nhập Số \033[1;36m[1.3] \033[38;5;204mTOOL AUTO TDS PAGE PRO5 ")

print("\033[1;39m   ╔═════════════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL Tương Tác Chéo\033[1;39m ║ ")
print("\033[1;39m   ╚═════════════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[2.1] \033[38;5;204mTOOL TTC PAGE PRO5")
print("\033[1;39m   ╔══════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL GOLIKE\033[1;39m  ║ ")
print("\033[1;39m   ╚══════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[3.1] \033[38;5;204mTOOL GOLIKE TIKTOK \033[1;33m[MỚI]")

print("\033[1;39m   ╔═══════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL KIẾM XU\033[1;39m  ║ ")
print("\033[1;39m   ╚═══════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[555] \033[38;5;204mTOOL HAMSTER ")



print("\033[1;39m   ╔═════════════════════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL LIÊN QUAN VỀ FACEBOOK\033[1;39m  ║ ")
print("\033[1;39m   ╚═════════════════════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.1] \033[38;5;204mTOOL CMT DẠO FB")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.2] \033[38;5;204mTOOL REG PAGE \033[1;33m[Chống Block]")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.3] \033[38;5;204mTOOL BUFF FOLLOW BẰNG PAGE PRO5")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.4] \033[38;5;204mTOOL CHUYỂN QUYỀN PAGE PRO5")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.5] \033[38;5;204mTOOL SPAM COMMENT FB")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.6] \033[38;5;204mTOOL SPAM BOX MESSENGER")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.7] \033[38;5;204mTOOL SPAM MESSENGER")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.9] \033[38;5;204mTOOL REG MAIL ẢO TẠO NICK FB")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.11] \033[38;5;204mTOOL GET COOKIE BẰNG TK MK \033[1;33m[VIP]")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.12] \033[38;5;204mTOOL NUÔI NICK FB \033[1;33m[VIP]")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.13] \033[38;5;204mTOOL GET TOKEN 16 LOẠI")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.14] \033[38;5;204mTOOL SPAM CMT PRO5")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.15] \033[38;5;204mTOOL LẤY ID BÀI VIẾT - ID NICK FB")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.16] \033[38;5;204mTOOL MẮNG NHAU Ở MESS VÀ BOX \033[1;33m[CÓ NGÔN SẴN]")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.17] \033[38;5;204mTOOL CHECK THÔNG TIN NICK FB")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.18] \033[38;5;204mTOOL GET COOKIE PAGE")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.19] \033[38;5;204mTOOL SHARE ẢO MAX SPEED \033[1;33m[COOKIE]")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.21] \033[38;5;204mTOOL SHARE ẢO ĐA LUỒNG + PROXY \033[1;33m[Key Vip Mới Được Sài]")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.22] \033[38;5;204mTOOL SHARE ẢO MAX SPEED \033[1;33m[TOKEN]")
print("\033[38;5;155m      Nhập Số \033[1;36m[5.23] \033[38;5;204mTOOL TỐ CÁO NICK FB \033[1;33m[VIP]")

print("\033[1;39m   ╔════════════════════════════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL SPAM SMS VÀ BUFF VIEW TIKTOK\033[1;39m  ║ ")
print("\033[1;39m   ╚════════════════════════════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[6.1] \033[38;5;204mTOOL SPAM SMS")
print("\033[38;5;155m      Nhập Số \033[1;36m[6.2] \033[38;5;204mTOOL BUFF VIEW TIKTOK PROXY")
print("\033[38;5;155m      Nhập Số \033[1;36m[6.3] \033[38;5;204mTOOL BUFF VIEW TIKTOK ZEFOY \033[1;33m[Key Vip + PC Mới Được Sài]")
print("\033[1;39m   ╔═════════════════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL VỀ MAIL VÀ PROXY \033[1;39m  ║ ")
print("\033[1;39m   ╚═════════════════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[7.1] \033[38;5;204mTOOL LỌC - CHECK MAIL [HMK]")
print("\033[38;5;155m      Nhập Số \033[1;36m[7.2] \033[38;5;204mTOOL TÌM PROXY")
print("\033[38;5;155m      Nhập Số \033[1;36m[7.3] \033[38;5;204mTOOL LỌC PROXY")

print("\033[1;39m   ╔═══════════════════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL CÙI BẮP DỄ BỊ CRACK\033[1;39m  ║ ")
print("\033[1;39m   ╚═══════════════════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[8.1] \033[38;5;204mTOOL CỦA HDTTOOL \033[1;33m[BẢN NEW] ")


print("\033[1;39m   ╔══════════════╗")
print("\033[1;39m   ║ \033[1;34mTOOL DECODE\033[1;39m  ║ ")
print("\033[1;39m   ╚══════════════╝")
print("\033[38;5;155m      Nhập Số \033[1;36m[9.1] \033[38;5;204mTOOL DEC Kramer-Specter Deobf")
print("\033[38;5;155m      Nhập Số \033[1;36m[9.2] \033[38;5;204mTOOL DEC Marshal/PYC")
print("\033[38;5;155m      Nhập Số \033[1;36m[9.3] \033[38;5;204mTOOL DEC Marshal dump")



chon = float(input('\033[1;31m     Nhập Số \033[1;32m: \033[1;33m'))

import requests,os,sys, time
def check_internet_connection():
    try:
        response = requests.get("https://google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False
if not check_internet_connection():
    print("\n\033[1;39mBạn bug 1 lần nữa sẽ bị dính botnet ngay nhé")
    sys.exit(1) 
if chon == 1.1 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/tdstiktok.py').text)

if chon == 1.2 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/tdsfb.py').text)
if chon == 1.3 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/tdspage.py').text)
if chon == 2.1 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/ttcpage.py').text)
if chon == 3.1 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/goliketiktok.py').text)
if chon == 5.1 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/cmtdaofb.py').text)
if chon == 5.2 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/regpage.py').text)
if chon == 5.3 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/buffpage.py').text)
if chon == 5.4 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/chuyenquyenqtv.py').text)
if chon == 5.5 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/cmtfb.py').text)
if chon == 5.6 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/spambox.py').text)
if chon == 5.7 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/spammess.py').text)

if chon == 5.9 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/mailfb.py').text)
if chon == 5.11 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/getcookie.py').text)
if chon == 5.12 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/nuoifb.py').text)
if chon == 5.13 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/gettoken.py').text)
if chon == 5.14 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/cmtpage.py').text)
if chon == 5.15 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/id.py').text)
if chon == 5.16 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/chuinhau.py').text)
if chon == 5.17 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/checkthongtinfb.py').text)
if chon == 5.18 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/cookiepro5.py').text)
if chon == 5.19 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/shareao.py').text)
if chon == 5.21 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/shareaodaluong.py').text)
if chon == 5.22 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/shareaotoken.py').text)
if chon == 5.23 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/tocao.py').text)
if chon == 6.1 :
	exec(requests.get('https://raw.githubusercontent.com/vlong07/vlong07/main/spamsms2.txt').text)
if chon == 6.2 :
	exec(requests.get('https://raw.githubusercontent.com/vlong07/vlong07/main/viewprx.txt').text)
if chon == 6.3 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/zefoy.py').text)
if chon == 7.1 :
	exec(requests.get('https://raw.githubusercontent.com/vlong07/vlong07/main/mail.txt').text)
if chon == 7.2 :
	exec(requests.get('https://raw.githubusercontent.com/vlong07/vlong07/main/timproxy.txt').text)
if chon == 7.3 :
	exec(requests.get('https://raw.githubusercontent.com/vlong07/vlong07/main/locproxy.txt').text)
if chon == 8.1 :
	exec(requests.get('https://raw.githubusercontent.com/luvanlong01122007/luvanlong01122007/main/hdt.py').text)

	
#tool kiếm xu
if chon == 9.1 :
	exec(requests.get('https://raw.githubusercontent.com/KhanhNguyen9872/kramer-specter_deobf/main/kramer-specter-deobf.py').text)
if chon == 9.2 :
	exec(requests.get('https://raw.githubusercontent.com/vlong07/vlong07/main/pyc.txt').text)
if chon == 9.3 :
	exec(requests.get('https://raw.githubusercontent.com/KhanhNguyen9872/dump_marshal_py/main/dump_marshal.py').text)
if chon == 555 :
	exec(requests.get('https://raw.githubusercontent.com/vlong07/vlong07/main/ham.txt').text)
else :
	exit()
