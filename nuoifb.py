import requests
from bs4 import BeautifulSoup
import random
from time import sleep
import os, json, sys, requests 

class NuoiFacebook:
    @staticmethod
    def AddFriend(cookie):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'vi',
            'cookie': cookie,
            'dpr': '1',
            'priority': 'u=0, i',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.172", "Google Chrome";v="124.0.6367.172", "Not-A.Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'viewport-width': '767',
        }
        
        access = requests.get('https://mbasic.facebook.com/friends/center/suggestions/', headers=headers).text
        find = BeautifulSoup(access, 'html.parser').find_all('a', href=lambda href: href and '/a/friends/add/?encrypted_id=' in href)
        
        if len(find) == 0:
            print('Không tìm thấy bạn bè gợi ý để thêm.')
        else:
            add = find[0]['href'].replace("amp;", '').replace('"', '')
            id = add.split('subject_id=')[1].split('&')[0]
            ten = requests.get('https://mbasic.facebook.com/profile.php?id='+id, headers=headers).text.split('<title>')[1].split('<')[0]
            requests.get('https://mbasic.facebook.com'+add, headers=headers)
            print(f'[1;33mĐã thêm bạn bè: {ten} | {id}')
        
        sleep(5)  # Delay between actions

    @staticmethod
    def JoinGroup(cookie):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'vi',
            'cookie': cookie,
            'dpr': '1',
            'priority': 'u=0, i',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.172", "Google Chrome";v="124.0.6367.172", "Not-A.Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'viewport-width': '767',
        }
        
        access = requests.get('https://mbasic.facebook.com/groups/?category=membership/', headers=headers).text
        find = BeautifulSoup(access, 'html.parser').find_all('a', href=lambda href: href and '/a/group/join/?button_id=' in href)
        
        if len(find) == 0:
            print('Không tìm thấy nhóm gợi ý để tham gia.')
        else:
            join = find[0]['href'].replace("amp;", '').replace('"', '')
            id = join.split('group_id=')[1].split('&')[0]
            ten = requests.get('https://mbasic.facebook.com/groups/'+id, headers=headers).text.split('<title>')[1].split('<')[0]
            requests.get('https://mbasic.facebook.com'+join, headers=headers)
            print(f'[1;33mĐã tham gia nhóm: {ten} | {id}')
        
        sleep(5)  # Delay between actions

    @staticmethod
    def likepost(cookie):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'vi',
            'cookie': cookie,
            'dpr': '1',
            'priority': 'u=0, i',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.172", "Google Chrome";v="124.0.6367.172", "Not-A.Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'viewport-width': '767',
        }
        
        access = requests.get('https://mbasic.facebook.com/', headers=headers).text
        find_post = BeautifulSoup(access, 'html.parser').find_all('a', string='Toàn bộ tin')
        
        if len(find_post) == 0:
            print('Không tìm thấy bài viết để tương tác.')
        else:
            link = find_post[0]
            nxt = link.find_previous_sibling('a')
            if nxt:
                id = nxt['href'].split('sid=')[1].split('&')[0]
                access = requests.get('https://mbasic.facebook.com/reactions/picker/?ft_id='+id, headers=headers).text
                find = BeautifulSoup(access, 'html.parser').find_all('a', href=lambda href: href and '/ufi/reaction/?ft_ent_identifier=' in href)
                chon = random.choice(['LIKE', 'LOVE', 'TT', 'HAHA', 'WOW', 'SAD', 'ANGRY'])
                
                if chon == 'LIKE':
                    requests.get('https://mbasic.facebook.com/'+str(find[0]).split('<a href="')[1].split('"')[0].replace("amp;", '').replace('"', ''), headers=headers)
                    print(f'[1;33mĐã thả Like cho bài viết: {id}')
                
                sleep(5)  # Delay between actions

    @staticmethod
    def RunAll(cookie):
        while True:
            NuoiFacebook.likepost(cookie)
            NuoiFacebook.AddFriend(cookie)
            NuoiFacebook.JoinGroup(cookie)

banner()
# Example usage:
cookie = input("[1;32mNhập Cookie : ")
NuoiFacebook.RunAll(cookie)