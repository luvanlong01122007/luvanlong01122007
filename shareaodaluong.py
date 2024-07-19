clear()
banner()
import requests
import re
import os
import json
import urllib3
import sys
import random
import concurrent.futures
from time import strftime, sleep
from colorama import Fore, Style
from colored import fg, bg, attr
from pystyle import *

urllib3.disable_warnings()

proxy_nedimemay = [
    'http://164.163.42.27:10000',
    'http://164.163.43.102:10000',
    'http://122.155.165.191:3128',
    'http://190.7.138.78:8080',
    'http://206.62.64.34:8080',
    'https//3.108.115.48:1080',
    'https//158.255.215.50:16993',
    'https//46.17.63.166:9080',
    'https//35.154.71.72:1080',
    'https//47.101.152.131:80',
]

def ngta_đặt_thanh():
    print('───────────────────────────────────────────────────────────')

def tokens(cookie, proxies=None):
    session = requests.Session()
    session.cookies.update({'cookie': cookie})
    
    if proxies:
        session.proxies = {'http': random.choice(proxies)}  # Set proxy if provided
    
    try:
        get_data = session.get("https://www.facebook.com/v2.3/dialog/oauth", params={
            'redirect_uri': 'fbconnect://success',
            'scope': 'email,publish_actions,publish_pages,user_about_me,user_actions.books,user_actions.music,user_actions.news,user_actions.video,user_activities,user_birthday,user_education_history,user_events,user_games_activity,user_groups,user_hometown,user_interests,user_likes,user_location,user_notes,user_photos,user_questions,user_relationship_details,user_relationships,user_religion_politics,user_status,user_subscriptions,user_videos,user_website,user_work_history,friends_about_me,friends_actions.books,friends_actions.music,friends_actions.news,friends_actions.video,friends_activities,friends_birthday,friends_education_history,friends_events,friends_games_activity,friends_groups,friends_hometown,friends_interests,friends_likes,friends_location,friends_notes,friends_photos,friends_questions,friends_relationship_details,friends_relationships,friends_religion_politics,friends_status,friends_subscriptions,friends_videos,friends_website,friends_work_history,ads_management,create_event,create_note,export_stream,friends_online_presence,manage_friendlists,manage_notifications,manage_pages,photo_upload,publish_stream,read_friendlists,read_insights,read_mailbox,read_page_mailboxes,read_requests,read_stream,rsvp_event,share_item,sms,status_update,user_online_presence,video_upload,xmpp_login',
            'response_type': 'token,code',
            'client_id': '356275264482347'
        }).text

        fb_dtsg = re.search('DTSGInitData",,{"token":"(.+?)"', get_data.replace('[]', '')).group(1)

        app_id = "438142079694454"
        url = f'https://www.facebook.com/dialog/oauth/business/cancel/?app_id={app_id}&version=v12.0&logger_id=&user_scopes[0]=user_birthday&user_scopes[1]=user_religion_politics&user_scopes[2]=user_relationships&user_scopes[3]=user_relationship_details&user_scopes[4]=user_hometown&user_scopes[5]=user_location&user_scopes[6]=user_likes&user_scopes[7]=user_education_history&user_scopes[8]=user_work_history&user_scopes[9]=user_website&user_scopes[10]=user_events&user_scopes[11]=user_photos&user_scopes[12]=user_videos&user_scopes[13]=user_friends&user_scopes[14]=user_about_me&user_scopes[15]=user_posts&user_scopes[16]=email&user_scopes[17]=manage_fundraisers&user_scopes[18]=read_custom_friendlists&user_scopes[19]=read_insights&user_scopes[20]=rsvp_event&user_scopes[21]=xmpp_login&user_scopes[22]=offline_access&user_scopes[23]=publish_video&user_scopes[24]=openid&user_scopes[25]=catalog_management&user_scopes[26]=user_messenger_contact&user_scopes[27]=gaming_user_locale&user_scopes[28]=private_computation_access&user_scopes[29]=instagram_business_basic&user_scopes[30]=user_managed_groups&user_scopes[31]=groups_show_list&user_scopes[32]=pages_manage_cta&user_scopes[33]=pages_manage_instant_articles&user_scopes[34]=pages_show_list&user_scopes[35]=pages_messaging&user_scopes[36]=pages_messaging_phone_number&user_scopes[37]=pages_messaging_subscriptions&user_scopes[38]=read_page_mailboxes&user_scopes[39]=ads_management&user_scopes[40]=ads_read&user_scopes[41]=business_management&user_scopes[42]=instagram_basic&user_scopes[43]=instagram_manage_comments&user_scopes[44]=instagram_manage_insights&user_scopes[45]=instagram_content_publish&user_scopes[46]=publish_to_groups&user_scopes[47]=groups_access_member_info&user_scopes[48]=leads_retrieval&user_scopes[49]=whatsapp_business_management&user_scopes[50]=instagram_manage_messages&user_scopes[51]=attribution_read&user_scopes[52]=page_events&user_scopes[53]=business_creative_transfer&user_scopes[54]=pages_read_engagement&user_scopes[55]=pages_manage_metadata&user_scopes[56]=pages_read_user_content&user_scopes[57]=pages_manage_ads&user_scopes[58]=pages_manage_posts&user_scopes[59]=pages_manage_engagement&user_scopes[60]=whatsapp_business_messaging&user_scopes[61]=instagram_shopping_tag_products&user_scopes[62]=read_audience_network_insights&user_scopes[63]=user_about_me&user_scopes[64]=user_actions.books&user_scopes[65]=user_actions.fitness&user_scopes[66]=user_actions.music&user_scopes[67]=user_actions.news&user_scopes[68]=user_actions.video&user_scopes[69]=user_activities&user_scopes[70]=user_education_history&user_scopes[71]=user_events&user_scopes[72]=user_friends&user_scopes[73]=user_games_activity&user_scopes[74]=user_groups&user_scopes[75]=user_hometown&user_scopes[76]=user_interests&user_scopes[77]=user_likes&user_scopes[78]=user_location&user_scopes[79]=user_managed_groups&user_scopes[80]=user_photos&user_scopes[81]=user_posts&user_scopes[82]=user_relationship_details&user_scopes[83]=user_relationships&user_scopes[84]=user_religion_politics&user_scopes[85]=user_status&user_scopes[86]=user_tagged_places&user_scopes[87]=user_videos&user_scopes[88]=user_website&user_scopes[89]=user_work_history&user_scopes[90]=email&user_scopes[91]=manage_notifications&user_scopes[92]=manage_pages&user_scopes[93]=publish_actions&user_scopes[94]=publish_pages&user_scopes[95]=read_friendlists&user_scopes[96]=read_insights&user_scopes[97]=read_page_mailboxes&user_scopes[98]=read_stream&user_scopes[99]=rsvp_event&user_scopes[100]=read_mailbox&user_scopes[101]=business_creative_management&user_scopes[102]=business_creative_insights_share&user_scopes[104]=whitelisted_offline_access&redirect_uri=fbconnect%3A%2F%2Fsuccess&response_types[0]=token&response_types[1]=code&display=page&action=finish&return_scopes=false&return_format[0]=access_token&return_format[1]=code&tp=unspecified&sdk=&selected_business_id=&set_token_expires_in_60_days=false'
        
        res = session.post(url, data={'fb_dtsg': str(fb_dtsg)}).text
        access_token = re.findall(r'access_token=([^"]*)&data_access_expiration_time', res)[0]

        token_dict = {}
        getpage = session.get(f"https://graph.facebook.com/me/accounts?access_token={access_token}").json()
        for save in getpage['data']:
            token = save["access_token"]
            token_dict[save["id"]] = token
        return token_dict
    
    except Exception as e:
        print(f"Error retrieving tokens: {e}")
        return None

def cl():
    os.system("cls" if os.name == "nt" else "clear")

def colorful_print(text, interval=0.005):
    colors = [fg('red'), fg('green'), fg('yellow'), fg('blue'), fg('magenta'), fg('cyan')]
    for char in text:
        print(random.choice(colors) + char, end='', flush=True)
        sleep(interval)
    print(attr('reset'))

def share_post(token, post_id, share_number, proxies=None):
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
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
        
        if proxies:
            response = requests.post(url, headers=headers, params=params, proxies={'http,https': random.choice(proxies)})
        else:
            response = requests.post(url, headers=headers, params=params)
        
        res = response.json()
        if response.status_code == 200:
            print(f"{strftime('%H:%M:%S')} : {share_number}: thành công: {res}", end='\r')
        else:
            print(f"{strftime('%H:%M:%S')} : {share_number}: thất bại: {res}")
    except Exception as e:
        print(f"{strftime('%H:%M:%S')} : {share_number} thất bại: {e}")

def main(post_id, token_dict, total_shares, chống_block1, chống_block, da_luong, proxies=None):
    token_list = list(token_dict.values())
    with concurrent.futures.ThreadPoolExecutor(max_workers=da_luong) as executor:
        for start in range(0, total_shares, chống_block1):
            end = min(start + chống_block1, total_shares)
            futures = []
            for share_number in range(start + 1, end + 1):
                token = random.choice(token_list)
                futures.append(executor.submit(share_post, token, post_id, share_number, proxies))
            concurrent.futures.wait(futures)
            
            if start + chống_block1 < total_shares:
                cl()
                print(f"{fg('green')}Chống Block Menu By Ngọc An{attr('reset')}")
                for _ in range(chống_block, 0, -1):
                    print(f"Đang dừng lại để chống block, còn {_} giây...", end='\r')
                    sleep(1)
                print()

if __name__ == "__main__":
    cl()
    ngta_đặt_thanh()
    linkpost = Write.Input("Nhập Link Bài Viết: ", Colors.green_to_blue, interval=0.005)
    
    try:
        get_id_post = requests.post('https://id.traodoisub.com/api.php', data={"link":linkpost}).json()
        if 'success' in get_id_post:
            post_id = get_id_post["id"]
        else:
            print(f"{fg('red')}Sai!!!{attr('reset')}")
            sys.exit(1)
        ngta_đặt_thanh()
        print(f'{fg("cyan")}id: {post_id}{attr("reset")}')
    except Exception as e:
        ngta_đặt_thanh()
        print(f"Không thể lấy ID bài viết từ URL: {e}")
        sys.exit(1)
    
    ngta_đặt_thanh()
    da_luong = int(Write.Input(f"Nhập Số Luồng: ", Colors.green_to_blue, interval=0.005))
    ngta_đặt_thanh()
    cookie = Write.Input(f"Nhập Cookie : ", Colors.green_to_blue, interval=0.005)
    ngta_đặt_thanh()
    
    proxies = proxy_nedimemay  
    
    token_dict = tokens(cookie, proxies)
    ngta_đặt_thanh()
    total_shares = int(Write.Input(f"Nhập Số Lần Chia Sẻ: ", Colors.green_to_blue, interval=0.005))
    ngta_đặt_thanh()
    chống_block1 = int(Write.Input(f"Bao Nhiêu Share Thì Tool Tạm Nghỉ(chống block-Trên 1000): ", Colors.green_to_blue, interval=0.005))
    ngta_đặt_thanh()
    chống_block = '10'
    ngta_đặt_thanh()
    
    try:
        main(post_id, token_dict, total_shares, chống_block1, chống_block, da_luong, proxies)
    except Exception as e:
        ngta_đặt_thanh()
        print(f"{fg('red')}Lỗi trong quá trình chia sẻ: {e}{attr('reset')}")
