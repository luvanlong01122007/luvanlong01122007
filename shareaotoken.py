import os
import json
import requests
import urllib3
import sys
import random
import asyncio
from time import strftime, sleep
from colorama import Fore, Style
from colored import fg, bg, attr
from pystyle import *
try:
    import aiohttp
except ImportError:
    os.system("pip install aiohttp")
    os.system("pip install colored")
    import aiohttp
banner()
urllib3.disable_warnings()

def cl():
    os.system("cls" if os.name == "nt" else "clear")

def colorful_print(text, interval=0.005):
    colors = [fg('red'), fg('green'), fg('yellow'), fg('blue'), fg('magenta'), fg('cyan')]
    for char in text:
        print(random.choice(colors) + char, end='', flush=True)
        sleep(interval)
    print(attr('reset'))

async def share_post(session, token, post_id, share_number):
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'connection': 'keep-alive',
        'content-length': '0',
        'host': 'graph.facebook.com'
    }
    try:
        url = f'https://graph.facebook.com/me/feed'
        params = {
            'link': f'https://www.facebook.com/{post_id}',
            'published': '0',
            'access_token': token
        }
        async with session.post(url, headers=headers, params=params) as response:
            res = await response.json()
            if response.status == 200:
                print(f"{strftime('%H:%M:%S')} : {share_number}: thành công: {res}", end='\r')
            else:
                print(f"{strftime('%H:%M:%S')} : {share_number}: thất bại: {res}")
    except Exception as e:
        print(f"{strftime('%H:%M:%S')} : {share_number} thất bại: {e}")

def read_tokens(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

async def main(post_id, tokens, total_shares, chống_block1, chống_block):
    async with aiohttp.ClientSession() as session:
        for start in range(0, total_shares, chống_block1):
            end = min(start + chống_block1, total_shares)
            tasks = []
            for share_number in range(start + 1, end + 1):
                token = random.choice(tokens)
                tasks.append(share_post(session, token, post_id, share_number))
            await asyncio.gather(*tasks)
            
            if start + chống_block1 < total_shares:
                cl()
                print(f"{fg('green')}Chống Block Menu By Ngọc An{attr('reset')}")
                for _ in range(chống_block, 0, -1):
                    print(f"Đang dừng lại để chống block, còn {_} giây...", end='\r')
                    await asyncio.sleep(1)
                print()

if __name__ == "__main__":
    cl()
    colorful_print("Chia sẻ bài viết Facebook by Ngọc An Mod Tool", interval=0.03)
    linkpost = Write.Input("Nhập Link Bài Viết: ", Colors.green_to_blue, interval=0.005)
    
    try:
        get_id_post = requests.post('https://id.traodoisub.com/api.php', data={"link":linkpost}).json()
        if 'success' in get_id_post:
            post_id = get_id_post["id"]
        else:
            print(f"{fg('red')}Sai!!!{attr('reset')}")
            sys.exit(1)
        print(f'{fg("cyan")}id: {post_id}{attr("reset")}')
    except Exception as e:
        print(f"Không thể lấy ID bài viết từ URL: {e}")
        sys.exit(1)
    
    token_file = Write.Input(f"Nhập VD: tokens.txt\nNhập File Chứa: ", Colors.green_to_blue, interval=0.005)
    total_shares = int(Write.Input(f"Nhập Số Lần Chia Sẻ: ", Colors.green_to_blue, interval=0.005))
    chống_block1 = int(Write.Input(f"Bao Nhiêu Share Thì Tool Tạm Nghỉ(chống block-Trên 1000): ", Colors.green_to_blue, interval=0.005))
    chống_block = int(Write.Input(f"Nhập Số Giây Dừng Sau Khi Bật Chống Block(khoảng 10 giây): ", Colors.green_to_blue, interval=0.005))

    tokens = read_tokens(token_file)
    
    try:
        asyncio.run(main(post_id, tokens, total_shares, chống_block1, chống_block))
    except Exception as e:
        print(f"{fg('red')}Lỗi trong quá trình chia sẻ: {e}{attr('reset')}")
