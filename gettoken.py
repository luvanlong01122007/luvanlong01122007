import requests,re

banner()
cookie = input("Nhập cookie acc cần get token: ")
session = requests.Session()
session.cookies.update({'cookie': cookie})
get_data = session.get("https://www.facebook.com/v2.3/dialog/oauth", params={'redirect_uri': 'fbconnect://success','scope': 'email,publish_actions,publish_pages,user_about_me,user_actions.books,user_actions.music,user_actions.news,user_actions.video,user_activities,user_birthday,user_education_history,user_events,user_games_activity,user_groups,user_hometown,user_interests,user_likes,user_location,user_notes,user_photos,user_questions,user_relationship_details,user_relationships,user_religion_politics,user_status,user_subscriptions,user_videos,user_website,user_work_history,friends_about_me,friends_actions.books,friends_actions.music,friends_actions.news,friends_actions.video,friends_activities,friends_birthday,friends_education_history,friends_events,friends_games_activity,friends_groups,friends_hometown,friends_interests,friends_likes,friends_location,friends_notes,friends_photos,friends_questions,friends_relationship_details,friends_relationships,friends_religion_politics,friends_status,friends_subscriptions,friends_videos,friends_website,friends_work_history,ads_management,create_event,create_note,export_stream,friends_online_presence,manage_friendlists,manage_notifications,manage_pages,photo_upload,publish_stream,read_friendlists,read_insights,read_mailbox,read_page_mailboxes,read_requests,read_stream,rsvp_event,share_item,sms,status_update,user_online_presence,video_upload,xmpp_login','response_type': 'token,code','client_id': '356275264482347'}).text
fb_dtsg = re.search('DTSGInitData",,{"token":"(.+?)"', get_data.replace('[]', '')).group(1)
facebook_android = "350685531728" #EAAAAU
messenger_for_android = "256002347743983" #EAAD
facebook_iphone = "6628568379" #EAAAAAY
messenger_for_iphone = "237759909591655" #EAADYP
messenger_for_iphone_dev = "202805033077166" #EAAC4
facebook_lite = "275254692598279" #EAAD6V7
messenger_for_lite = "200424423651082" #EAAC2SPKT
ads_manager_app_android = "438142079694454" #EAAGO
ads_manager_app_ios = "1479723375646806" #EAAVB
page_ios = "165907476854626" #EAACW5F
page_android = "121876164619130" #EAAB
page_windows = "1174099472704185" #EAAQ
business_manager = "436761779744620" #EAAGNO
messenger_kids_ios = "522404077880990" #EAAH
messenger_ios_house = "184182168294603" #EAAC
facebook_ipad = "124024574287414" #EAABwz
print("""
| 01 [FACEBOOK FOR ANDROID]              | 09 [FACEBOOK MESSENGER FOR IPHONE DEV]
| 02 [FACEBOOK MESSENGER FOR ANDROID]    | 10 [PAGES MANAGER FOR IOS]
| 03 [FACEBOOK FOR IPHONE]               | 11 [PAGES MANAGER FOR ANDROID]    
| 04 [FACEBOOK MESSENGER FOR IPHONE]     | 12 [PAGES MANAGER FOR WINDOWS]
| 05 [FACEBOOK FOR LITE]                 | 13 [BUSINESS MANAGER]
| 06 [FACEBOOK MESSENGER FOR LITE]       | 14 [MESSENGER KIDS FOR IOS]
| 07 [ADS MANAGER APP FOR ANDROID]       | 15 [MESSENGER FOR IOS (IN-HOUSE)]
| 08 [ADS MANAGER APP FOR IOS]           | 16 [FACEBOOK FOR IPAD]
""")
type_access_token = input("Nhập dạng token bạn muốn lấy: ")
if type_access_token == '1' or type_access_token == '01':
    app_id = facebook_android
elif type_access_token == '2' or type_access_token == '02':
    app_id = messenger_for_android
elif type_access_token == '3' or type_access_token == '03':
    app_id = facebook_iphone
elif type_access_token == '4' or type_access_token == '04':
    app_id = messenger_for_iphone
elif type_access_token == '5' or type_access_token == '05':
    app_id = facebook_lite
elif type_access_token == '6' or type_access_token == '06':
    app_id = messenger_for_lite
elif type_access_token == '7' or type_access_token == '07':
    app_id = ads_manager_app_android
elif type_access_token == '8' or type_access_token == '08':
    app_id = ads_manager_app_ios
elif type_access_token == '9' or type_access_token == '09':
    app_id = messenger_for_iphone_dev
elif type_access_token == '10':
    app_id = page_ios
elif type_access_token == '11':
    app_id = page_android
elif type_access_token == '12':
    app_id = page_windows
elif type_access_token == '13':
    app_id = business_manager
elif type_access_token == '14':
    app_id = messenger_kids_ios
elif type_access_token == '15':
    app_id = messenger_ios_house
elif type_access_token == '16':
    app_id = facebook_ipad
else:
    session.close()
    exit("Nhập sai số!!!")
url = f'https://www.facebook.com/dialog/oauth/business/cancel/?app_id={app_id}&version=v12.0&logger_id=&user_scopes[0]=user_birthday&user_scopes[1]=user_religion_politics&user_scopes[2]=user_relationships&user_scopes[3]=user_relationship_details&user_scopes[4]=user_hometown&user_scopes[5]=user_location&user_scopes[6]=user_likes&user_scopes[7]=user_education_history&user_scopes[8]=user_work_history&user_scopes[9]=user_website&user_scopes[10]=user_events&user_scopes[11]=user_photos&user_scopes[12]=user_videos&user_scopes[13]=user_friends&user_scopes[14]=user_about_me&user_scopes[15]=user_posts&user_scopes[16]=email&user_scopes[17]=manage_fundraisers&user_scopes[18]=read_custom_friendlists&user_scopes[19]=read_insights&user_scopes[20]=rsvp_event&user_scopes[21]=xmpp_login&user_scopes[22]=offline_access&user_scopes[23]=publish_video&user_scopes[24]=openid&user_scopes[25]=catalog_management&user_scopes[26]=user_messenger_contact&user_scopes[27]=gaming_user_locale&user_scopes[28]=private_computation_access&user_scopes[29]=instagram_business_basic&user_scopes[30]=user_managed_groups&user_scopes[31]=groups_show_list&user_scopes[32]=pages_manage_cta&user_scopes[33]=pages_manage_instant_articles&user_scopes[34]=pages_show_list&user_scopes[35]=pages_messaging&user_scopes[36]=pages_messaging_phone_number&user_scopes[37]=pages_messaging_subscriptions&user_scopes[38]=read_page_mailboxes&user_scopes[39]=ads_management&user_scopes[40]=ads_read&user_scopes[41]=business_management&user_scopes[42]=instagram_basic&user_scopes[43]=instagram_manage_comments&user_scopes[44]=instagram_manage_insights&user_scopes[45]=instagram_content_publish&user_scopes[46]=publish_to_groups&user_scopes[47]=groups_access_member_info&user_scopes[48]=leads_retrieval&user_scopes[49]=whatsapp_business_management&user_scopes[50]=instagram_manage_messages&user_scopes[51]=attribution_read&user_scopes[52]=page_events&user_scopes[53]=business_creative_transfer&user_scopes[54]=pages_read_engagement&user_scopes[55]=pages_manage_metadata&user_scopes[56]=pages_read_user_content&user_scopes[57]=pages_manage_ads&user_scopes[58]=pages_manage_posts&user_scopes[59]=pages_manage_engagement&user_scopes[60]=whatsapp_business_messaging&user_scopes[61]=instagram_shopping_tag_products&user_scopes[62]=read_audience_network_insights&user_scopes[63]=user_about_me&user_scopes[64]=user_actions.books&user_scopes[65]=user_actions.fitness&user_scopes[66]=user_actions.music&user_scopes[67]=user_actions.news&user_scopes[68]=user_actions.video&user_scopes[69]=user_activities&user_scopes[70]=user_education_history&user_scopes[71]=user_events&user_scopes[72]=user_friends&user_scopes[73]=user_games_activity&user_scopes[74]=user_groups&user_scopes[75]=user_hometown&user_scopes[76]=user_interests&user_scopes[77]=user_likes&user_scopes[78]=user_location&user_scopes[79]=user_managed_groups&user_scopes[80]=user_photos&user_scopes[81]=user_posts&user_scopes[82]=user_relationship_details&user_scopes[83]=user_relationships&user_scopes[84]=user_religion_politics&user_scopes[85]=user_status&user_scopes[86]=user_tagged_places&user_scopes[87]=user_videos&user_scopes[88]=user_website&user_scopes[89]=user_work_history&user_scopes[90]=email&user_scopes[91]=manage_notifications&user_scopes[92]=manage_pages&user_scopes[93]=publish_actions&user_scopes[94]=publish_pages&user_scopes[95]=read_friendlists&user_scopes[96]=read_insights&user_scopes[97]=read_page_mailboxes&user_scopes[98]=read_stream&user_scopes[99]=rsvp_event&user_scopes[100]=read_mailbox&user_scopes[101]=business_creative_management&user_scopes[102]=business_creative_insights&user_scopes[103]=business_creative_insights_share&user_scopes[104]=whitelisted_offline_access&redirect_uri=fbconnect%3A%2F%2Fsuccess&response_types[0]=token&response_types[1]=code&display=page&action=finish&return_scopes=false&return_format[0]=access_token&return_format[1]=code&tp=unspecified&sdk=&selected_business_id=&set_token_expires_in_60_days=false'
res = session.post(url, data={'fb_dtsg': str(fb_dtsg)}).text
session.close()
access_token = re.findall(r'access_token=([^"]*)&data_access_expiration_time', res)[0]
print(access_token)
checkgetpage = input('Bạn có muốn get luôn token page không(Y/n): ')
if checkgetpage == 'Y' or checkgetpage == 'y':
    filename = input("Nhập tên file bạn muốn lưu token: ")
    getpage = session.get(f"https://graph.facebook.com/me/accounts?access_token={access_token}").json()
    for save in getpage['data']:
        with open(filename, 'a') as f:
            token = save["access_token"]
            f.write(f"{token}\n")
    print(f"Đã get token vào file {filename} thành công!")