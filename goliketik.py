
try :
    import requests
    import time
    import os 
    from art import *
    from colorama import Fore
    import time
    import json
    import random
    from tabulate import tabulate
except ImportError:
    os.system("pip install requests")
    os.system("pip install tabulate")
    os.system("pip install art")
    os.system("pip install colorama")
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = 'VUI LÒNG CHỜ : {:02d}'.format(secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
def TIKTOKINFO():
    url1_2 = 'https://gateway.golike.net/api/tiktok-account'
    checkurl1_2 = ses.get(url1_2,headers=headers).json()
    user_tiktok1 = []
    account_id1 = []
    STT = []
    STATUS =[]
    print('CÁC TÀI KHỎAN ĐANG HỌAT ĐỘNG')
    i=1
    head = ["STT", "  ACCOUNT","   STATUS"]
    # LIST=Fore.RED+tabulate(mydata, headers=head, tablefmt="grid",)
    for data in checkurl1_2['data'] :
        usernametk = data['nickname']
        # print(str(i)+'.'+usernametk)
        user_tiktok1.append(data['nickname'])
        account_id1.append(data['id'])
        STT.append(i)
        STATUS.append(Fore.GREEN+"DANG HOAT DONG"+Fore.RED)
    # create header
        i=i+1
    table = zip(STT,user_tiktok1,STATUS)
    LIST=Fore.RED+tabulate(table, headers=head, tablefmt="grid",)   
    print(LIST)
    choose = int(input('NHẬP TÀI KHỎAN : '))
    os.system('cls' if os.name== 'nt' else 'clear')
    if choose >=1 or choose <= len(user_tiktok1) :
        user_tiktok1 = user_tiktok1[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_tiktok = user_tiktok1[0] 
        account_id = account_id1[0]
        tprint("NHAT","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY NHATTOOL')
        print('ZALO : 0386358592')
        choose = int(input(Fore.RED+'NHẬP SỐ LƯỢNG JOB : '))
        os.system('cls' if os.name== 'nt' else 'clear')
        tprint("NHAT","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY NHATTOOL')
        print('ZALO : 0386358592')
        DELAY = int(input(Fore.RED+'NHẬP DELAY : '))
        for i in range(choose):
            url2 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id='+str(account_id)+'&data=null'
            checkurl2 = ses.get(url2,headers=headers).json()
            if checkurl2['status'] ==200:
                linkjob = []
                linkjob = str(checkurl2['data']['link'])
                lenjob = len(checkurl2['data']['link'])
                ads_id = checkurl2['data']['id']
                object_id = checkurl2['data']['object_id']
                type = checkurl2['data']['type']
                # os.system("start "+linkjob+"")
                os.system("termux-open-url "+str(linkjob[0:lenjob])+"")
                PARAMS = {
                        'ads_id' : ads_id,
                        'account_id' : account_id,
                        'object_id' : object_id ,
                        'async': 'true',
                        'data': 'null',
                        'type': type,
                        }
                countdown(DELAY)
                url3 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs'
                time.sleep(1)
                checkurl3 = ses.post(url3,params=PARAMS).json()
                if checkurl3['status'] == 400 :

                        time.sleep(2)

                        url3 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs'
                        checkurl3 = ses.post(url3,params=PARAMS).json()
                        if checkurl3['status'] == 200:
                                prices = checkurl3['data']['prices']
                                print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                        else:

                                    time.sleep(2)

                                    url3 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs'
                                    checkurl3 = ses.post(url3,params=PARAMS).json()
                                    if checkurl3['status'] == 200:
                                            prices = checkurl3['data']['prices']
                                            print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                    else:
                                        time.sleep(2)

                                        url3 = 'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs'
                                        checkurl3 = ses.post(url3,params=PARAMS).json()
                                        if checkurl3['status'] == 200:
                                                prices = checkurl3['data']['prices']
                                                print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                        else:
                                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs'
                                            checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                            if checkskipjob['status'] == 200:
                                                message = checkskipjob['message']
                                                print(Fore.RED+str(message))
                                                PARAMSr = {
                                                    'ads_id' : ads_id,
                                                    'account_id' : account_id,
                                                    'object_id' : object_id ,
                                                    'async': 'true',
                                                    'data': 'null',
                                                    'type': type,
                                                    }
                elif checkurl3['status'] == 200:
                    prices = checkurl3['data']['prices']
                    print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                else :
                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs'
                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                    if checkskipjob['status'] == 200:
                        message = checkskipjob['message']
                        print(Fore.RED+str(message))
                        PARAMSr = {
                        'ads_id' : ads_id,
                        'account_id' : account_id,
                        'object_id' : object_id ,
                        'async': 'true',
                        'data': 'null',
                        'type': type,
                        }
            else : 
                countdown(15)
                print(checkurl2['message'])
                skipjob = 'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs'
                checkskipjob = ses.post(skipjob,params=PARAMS).json()
                if checkskipjob['status'] == 200:
                    message = checkskipjob['message']
                    print(Fore.RED+str(message))
                    PARAMSr = {
                    'ads_id' : ads_id,
                    'account_id' : account_id,
                    'object_id' : object_id ,
                    'async': 'true',
                    'data': 'null',
                    'type': type,
                    }        
def TWITTER():
    url1_2 = 'https://gateway.golike.net/api/twitter-account'
    checkurl1_2 = ses.get(url1_2,headers=headers).json()
    user_twitter1 = []
    account_id1 = []
    account = []
    STT = []
    STATUS =[]
    print('CÁC TÀI KHỎAN ĐANG HỌAT ĐỘNG')
    i=1
    head = ["STT", "  ACCOUNT","   STATUS"]
    for data in checkurl1_2['data'] :
        usernametk = data['screen_name']
        user_twitter1.append(data['username'])
        account_id1.append(data['id'])
        STT.append(i)
        account.append(usernametk)
        STATUS.append(Fore.GREEN+"ĐANG HỌAT ĐỘNG"+Fore.RED)
        i=i+1
    table = zip(STT,account,STATUS)
    LIST=Fore.RED+tabulate(table, headers=head, tablefmt="grid",)   
    print(LIST)
    choose = int(input('NHẬP TÀI KHỎAN : '))
    os.system('cls' if os.name== 'nt' else 'clear')
    if choose >=1 or choose <= len(user_twitter1) :
        user_twitter1 = user_twitter1[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_tiktok = user_twitter1[0] 
        account_id = account_id1[0]
        checkfile = os.path.isfile('AUTH'+str(account_id)+'.txt')
        if checkfile == False:
            AUTHURX = input(Fore.GREEN+'[+]''AUTH : ')
            createfile = open('AUTH'+str(account_id)+'.txt','w')
            createfile.write(AUTHURX)
            createfile.close()
            readfile = open('AUTH'+str(account_id)+'.txt','r')
            AUTHURX = readfile.read()
            readfile.close()
        else:
            readfile = open('AUTH'+str(account_id)+'.txt','r')
            AUTHURX = readfile.read()
            readfile.close()
        checkfile2 = os.path.isfile('COOKIE'+str(account_id)+'.txt')
        if checkfile2 == False:
            cookieX = input(Fore.GREEN+'[+]''COOKIE : ')
            createfile = open('COOKIE'+str(account_id)+'.txt','w')
            createfile.write(cookieX)
            createfile.close()
            readfile = open('COOKIE'+str(account_id)+'.txt','r')
            cookieX = readfile.read()
            readfile.close()
        else:
            readfile = open('COOKIE'+str(account_id)+'.txt','r')
            cookieX = readfile.read()
            readfile.close()
        os.system('cls' if os.name== 'nt' else 'clear')
        tprint("NHAT","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY NHATTOOL')
        print('ZALO : 0386358592')
        choose = int(input(Fore.RED+'NHẬP SỐ LƯỢNG JOB : '))
        os.system('cls' if os.name== 'nt' else 'clear')
        tprint("NHAT","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY NHATTOOL')
        print('ZALO : 0386358592')
        DELAY = int(input(Fore.RED+'NHẬP DELAY : '))
        for i in range(choose):
                    job = 'https://gateway.golike.net/api/advertising/publishers/twitter/jobs?account_id='+str(account_id)
                    nos = ses.get(job,headers=headers).json()
                    if nos['status'] ==200:
                        ads_id = nos['data']['id']
                        object_id = nos['data']['object_id']
                        type = nos['data']['type']
                        if type=='like':
                            url = 'https://x.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet'
                            headersX = {
                            'accept': '*/*',
                            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                            'authorization': AUTHURX,
                            'content-type': 'application/json',
                            'cookie': cookieX,
                            'origin': 'https://x.com',
                            'priority': 'u=1, i',
                            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                            'sec-ch-ua-mobile': '?1',
                            'sec-ch-ua-platform': '"Android"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': User_Agent,
                            'x-client-transaction-id': 'urp5610yhQLkM+CVhUdxse7V6km/w/d0jxm8ReTQ0zYMv9OrPxn4mhIlXHxcu5p9VeJWjLh903OGJv8VyMwdt6Mnr31KuQ',
                            'x-client-uuid': '8a14d42e-d7a8-4d47-9e60-cd596f91ad4b',
                            'x-csrf-token': cookieX.split('ct0=')[1].split(';')[0],
                            'x-twitter-active-user': 'yes',
                            'x-twitter-auth-type': 'OAuth2Session',
                            'x-twitter-client-language': 'en',
                                    }
                            json_data = {
                                'variables': {
                                    'tweet_id': object_id,
                                },
                                'queryId': 'lI07N6Otwv1PhnEgXILM7A',
                            }

                            node = requests.post(url,headers=headersX,json=json_data,proxies=proxyy).json()
                            countdown(DELAY)
                            if 'data' or 'has already favorited tweet' in str(node):
                                url = 'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs'
                                json_data = {
                                'ads_id': ads_id,
                                'account_id': account_id,
                                'async': True,
                                }
                                time.sleep(3)
                                response3 = requests.post('https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs',
                                headers=headers,
                                json=json_data,
                                ).json()       
                                if response3['success']==True:
                                    prices =response3['data']['prices']
                                    print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                            elif 'errors' and 'Could not authenticate you' in str(node):
                                print("HẾT HẠN COOKIE")
                                os.remove('COOKIE'+str(account_id)+'.txt')
                                return 0
                        elif type == 'follow':
                            url = 'https://x.com/i/api/1.1/friendships/create.json'
                            headersY = {
                            'accept': '*/*',
                            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                            'authorization': AUTHURX,
                            'content-type': 'application/x-www-form-urlencoded',
                            'cookie': cookieX,
                            'origin': 'https://x.com',
                            'priority': 'u=1, i',
                            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                            'sec-ch-ua-mobile': '?1',
                            'sec-ch-ua-platform': '"Android"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
                            'x-client-transaction-id': 'MPwo7xERotqe3xFS4oEGGDju3YMFR9v2gW2dSTZ/c2S4KYhQfp5ZmZYR/KcwzeyIYp3GBjKulQYFzsWftgEm6c7v0StkMw',
                            'x-csrf-token': cookieX.split('ct0=')[1].split(';')[0],
                            'x-twitter-active-user': 'yes',
                            'x-twitter-auth-type': 'OAuth2Session',
                            'x-twitter-client-language': 'en',
                        }

                            data = {
                            'include_profile_interstitial_type': '1',
                            'include_blocking': '1',
                            'include_blocked_by': '1',
                            'include_followed_by': '1',
                            'include_want_retweets': '1',
                            'include_mute_edge': '1',
                            'include_can_dm': '1',
                            'include_can_media_tag': '1',
                            'include_ext_is_blue_verified': '1',
                            'include_ext_verified_type': '1',
                            'include_ext_profile_image_shape': '1',
                            'skip_status': '1',
                            'user_id': object_id,
                        }

                            response2 = requests.post('https://x.com/i/api/1.1/friendships/create.json', headers=headersY, data=data,proxies=proxyy).json()
                            countdown(DELAY)
                            if 'id' in response2:
                                # DELAY
                                url = 'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs'
                                json_data = {
                                'ads_id': ads_id,
                                'account_id': account_id,
                                'async': True,
                                }
                                time.sleep(3)
                                response = requests.post(
                                'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs',
                                headers=headers,
                                json=json_data,
                                ).json()
                                if response['success']==True:
                                    prices =response['data']['prices']
                                    print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                            elif 'errors' and 'Could not authenticate you' in str(response2):
                                print("HẾT HẠN COOKIE")
                                os.remove('COOKIE'+str(account_id)+'.txt')
                                return 0
                        elif type=='comment':
                            comment = nos['lock']["message"]
                            url = 'https://x.com/i/api/graphql/oB-5XsHNAbjvARJEc8CZFw/CreateTweet'
                            headersZ = {
                            'accept': '*/*',
                            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                            'authorization': AUTHURX,
                            'content-type': 'application/json',
                            'cookie': cookieX,
                            'origin': 'https://x.com',
                            'priority': 'u=1, i',
                            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                            'sec-ch-ua-mobile': '?1',
                            'sec-ch-ua-platform': '"Android"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': User_Agent,
                            'x-client-transaction-id': 'urp5610yhQLkM+CVhUdxse7V6km/w/d0jxm8ReTQ0zYMv9OrPxn4mhIlXHxcu5p9VeJWjLh903OGJv8VyMwdt6Mnr31KuQ',
                            'x-client-uuid': '8a14d42e-d7a8-4d47-9e60-cd596f91ad4b',
                            'x-csrf-token': cookieX.split('ct0=')[1].split(';')[0],
                            'x-twitter-active-user': 'yes',
                            'x-twitter-auth-type': 'OAuth2Session',
                            'x-twitter-client-language': 'en',
                                    }
                            json_data = {
                                'variables': {
                                    'tweet_text': comment,
                                    'reply': {
                                        'in_reply_to_tweet_id': object_id,
                                        'exclude_reply_user_ids': [],
                                    },
                                    'dark_request': False,
                                    'media': {
                                        'media_entities': [],
                                        'possibly_sensitive': False,
                                    },
                                    'semantic_annotation_ids': [],
                                },
                                'features': {
                                    'communities_web_enable_tweet_community_results_fetch': True,
                                    'c9s_tweet_anatomy_moderator_badge_enabled': True,
                                    'tweetypie_unmention_optimization_enabled': True,
                                    'responsive_web_edit_tweet_api_enabled': True,
                                    'graphql_is_translatable_rweb_tweet_is_translatable_enabled': True,
                                    'view_counts_everywhere_api_enabled': True,
                                    'longform_notetweets_consumption_enabled': True,
                                    'responsive_web_twitter_article_tweet_consumption_enabled': True,
                                    'tweet_awards_web_tipping_enabled': False,
                                    'creator_subscriptions_quote_tweet_preview_enabled': False,
                                    'longform_notetweets_rich_text_read_enabled': True,
                                    'longform_notetweets_inline_media_enabled': True,
                                    'articles_preview_enabled': True,
                                    'rweb_video_timestamps_enabled': True,
                                    'rweb_tipjar_consumption_enabled': True,
                                    'responsive_web_graphql_exclude_directive_enabled': True,
                                    'verified_phone_label_enabled': False,
                                    'freedom_of_speech_not_reach_fetch_enabled': True,
                                    'standardized_nudges_misinfo': True,
                                    'tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled': True,
                                    'responsive_web_graphql_skip_user_profile_image_extensions_enabled': False,
                                    'responsive_web_graphql_timeline_navigation_enabled': True,
                                    'responsive_web_enhance_cards_enabled': False,
                                },
                                'queryId': 'oB-5XsHNAbjvARJEc8CZFw',
                            }
                            cf = requests.post(url,headers=headersZ,json=json_data,proxies=proxyy).json()
                            countdown(DELAY)  
                            if 'create_tweet' or 'Authorization: Status is a duplicate.' in str(cf):
                                url = 'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs'
                                json_data = {
                                'ads_id': ads_id,
                                'account_id': account_id,
                                'async': True,
                                'comment_id':nos['lock']['comment_id'],
                                'message':comment,
                                }
                                time.sleep(3)
                                response = requests.post(
                                'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs',
                                headers=headers,
                                json=json_data,
                                ).json()
                                if response['success']==True:
                                    prices =response['data']['prices']
                                    print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                            elif 'errors' and 'Could not authenticate you' in str(cf):
                                print("HET HAN COOKIE")
                                os.remove('COOKIE'+str(account_id)+'.txt')
                    else:
                        print(nos['message'])
                        countdown(15)
def INSTAGRAM():
    url1_2 = 'https://gateway.golike.net/api/instagram-account'
    checkurl1_2 = ses.get(url1_2,headers=headers).json()
    user_INS = []
    account_id1 = []
    account = []
    STT = []
    STATUS =[]
    print('CÁC TÀI KHỎAN ĐANG HỌAT ĐỘNG')
    i=1
    head = ["STT", "  ACCOUNT","   STATUS"]
    for data in checkurl1_2['data'] :
        usernametk = data['instagram_username']
        user_INS.append(data['username'])
        account_id1.append(data['id'])
        STT.append(i)
        STATUS.append(Fore.GREEN+"ĐANG HỌAT ĐỘNG"+Fore.RED)
        account.append(usernametk)
        i=i+1
    table = zip(STT,account,STATUS)
    LIST=Fore.RED+tabulate(table, headers=head, tablefmt="grid",)   
    print(LIST)
    choose = int(input('NHẬP TÀI KHỎAN : '))
    os.system('cls' if os.name== 'nt' else 'clear')
    if choose >=1 or choose <= len(user_INS) :
        user_INS = user_INS[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_tiktok = user_INS[0] 
        account_id = account_id1[0]
        checkfile2 = os.path.isfile('COOKIEINS'+str(account_id)+'.txt')
        if checkfile2 == False:
            cookieX = input(Fore.GREEN+'[+]''COOKIE : ')
            createfile = open('COOKIEINS'+str(account_id)+'.txt','w')
            createfile.write(cookieX)
            createfile.close()
            readfile = open('COOKIEINS'+str(account_id)+'.txt','r')
            cookieINS = readfile.read()
            readfile.close()
        else:
            readfile = open('COOKIEINS'+str(account_id)+'.txt','r')
            cookieINS = readfile.read()
            readfile.close()
        os.system('cls' if os.name== 'nt' else 'clear')
        tprint("NHAT","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY NHATTOOL')
        print('ZALO : 0386358592')
        choose = int(input(Fore.RED+'NHẬP SỐ LƯỢNG JOB : '))
        os.system('cls' if os.name== 'nt' else 'clear')
        tprint("NHAT","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY NHATTOOL')
        print('ZALO : 0386358592')
        headerINS = {
                'accept': '*/*',
                'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                # 'content-length': '0',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': cookieINS,
                'origin': 'https://www.instagram.com',
                'priority': 'u=1, i',
                'referer': 'https://www.instagram.com/p/C9RAZEJNjPC/',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                'x-asbd-id': '129477',
                'x-csrftoken': cookieINS.split('csrftoken=')[1].split(';')[0],
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR1Jw2LrciyrzAQskwSVGREElPZZJZjW74y38oTjDnNHOu9e',
                'x-instagram-ajax': '1014868636',
                'x-requested-with': 'XMLHttpRequest',
            }
        param = {
            'instagram_account_id': account_id,
            'data': 'null',
        }
        DELAY = int(input(Fore.RED+'NHẬP DELAY : '))
        for i in range(choose):
                job = 'https://gateway.golike.net/api/advertising/publishers/instagram/jobs?instagram_account_id='+str(account_id)+'&data=null'
                nos = ses.get(job,headers=headers,params=param).json()
                if nos['status'] ==200:
                    ads_id = nos['data']['id']
                    object_id = nos['data']['object_id']
                    type = nos['data']['type']
                    if type == 'follow':
                        url = 'https://www.instagram.com/api/v1/friendships/create/'+object_id+'/'
                        data = {
                            'container_module': 'profile',
                            'nav_chain': 'PolarisFeedRoot:feedPage:8:topnav-link',
                            'user_id': object_id,
                        }
                        respone = requests.post(url,headers=headerINS,data=data,proxies=proxyy).text
                        countdown(DELAY)
                        if '"status":"ok"' in respone:
                                url = 'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs'
                                json_data = {
                                'instagram_account_id': account_id,
                                'instagram_users_advertising_id': ads_id,
                                'async': True,
                                'data':'null',
                                }
                                time.sleep(3)
                                response = requests.post(
                                'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs',
                                headers=headers,
                                json=json_data,
                                ).json()
                                if response['success']==True:
                                    prices =response['data']['prices']
                                    print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                        else:
                            print('Cookie HẾT HẠN')
                            os.remove('COOKIEINS'+str(account_id)+'.txt')
                            return 0
                    elif type=='like':
                        like_id = nos['data']['description']
                        url = 'https://www.instagram.com/api/v1/web/likes/'+str(like_id)+'/like/'
                        response = requests.post(url,headers=headerINS,proxies=proxyy).text
                        countdown(DELAY)
                        if '"status":"ok"' in response:
                                url = 'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs'
                                json_data = {
                                'instagram_account_id': account_id,
                                'instagram_users_advertising_id': ads_id,
                                'async': True,
                                'data':'null',
                                }
                                time.sleep(3)
                                response = requests.post(
                                'https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs',
                                headers=headers,
                                json=json_data,
                                ).json()
                                if response['success']==True:
                                    prices =response['data']['prices']
                                    print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                        else:
                            print('Cookie HET HAN')
                            os.remove('COOKIEINS'+str(account_id)+'.txt')
                            return 0
                else:
                        print(nos['message'])
                        countdown(15)
def LINKEDIN():
    checkaccount = requests.get('https://gateway.golike.net/api/linkedin-account',headers=headers).json()
    user_linkedin1 = []
    account_id1 = []
    STT = []
    STATUS =[]
    print('CÁC TÀI KHỎAN ĐANG HỌAT ĐỘNG')
    i=1
    head = ["STT", "  ACCOUNT","   STATUS"]
    for data in checkaccount['data'] :
            usernametk = data['name']
            # print(str(i)+'.'+usernametk)
            user_linkedin1.append(data['name'])
            account_id1.append(data['id'])
            STT.append(i)
            STATUS.append(Fore.GREEN+"ĐANG HỌAT ĐỘNG"+Fore.RED)
        # create header
            i=i+1
    table = zip(STT,user_linkedin1,STATUS)
    LIST=Fore.RED+tabulate(table, headers=head, tablefmt="grid",)   
    print(LIST)
    choose = int(input('NHẬP TÀI KHỎAN : '))
    os.system('cls' if os.name== 'nt' else 'clear')
    if choose >=1 or choose <= len(user_linkedin1) :
        user_tiktok1 = user_linkedin1[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_tiktok = user_linkedin1[0] 
        account_id = account_id1[0]
        checkfile = os.path.isfile('COOKIELINKEDIN'+str(account_id)+'.txt')
        if checkfile == False:
            COOKIELINK = input(Fore.GREEN+'[+] COOKIE : ')
            createfile = open('COOKIELINKEDIN'+str(account_id)+'.txt','w')
            createfile.write(COOKIELINK)
            createfile.close()
            readfile = open('COOKIELINKEDIN'+str(account_id)+'.txt','r')
            COOKIELINK = readfile.read()
            readfile.close()
        else:
            readfile = open('COOKIELINKEDIN'+str(account_id)+'.txt','r')
            COOKIELINK = readfile.read()
            readfile.close()
        os.system('cls' if os.name== 'nt' else 'clear')
        tprint("NHAT","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY NHATTOOL')
        print('ZALO : 0386358592')
        choose = int(input(Fore.RED+'NHẬP SỐ LƯỢNG JOB : '))
        os.system('cls' if os.name== 'nt' else 'clear')
        tprint("NHAT","rnd-xlarge")
        print(Fore.RED+'\t\tTOOL BY NHATTOOL')
        print('ZALO : 0386358592')
        DELAY = int(input(Fore.RED+'NHẬP DELAY : '))
        for i in range(choose):
                url2 = 'https://gateway.golike.net/api/advertising/publishers/linkedin/jobs?account_id='+str(account_id)+'&data=null'
                checkurl2 = ses.get(url2,headers=headers).json()
                if checkurl2['status'] ==200:
                    linkjob = []
                    linkjob = str(checkurl2['data']['link'])
                    lenjob = len(checkurl2['data']['link'])
                    ads_id = checkurl2['data']['id']
                    object_id = checkurl2['data']['object_id']
                    type = checkurl2['data']['type']
                    countdown(DELAY)
                    if type == 'follow':
                        haeaders = {
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                            'cache-control': 'max-age=0',
                            'cookie':COOKIELINK ,
                            'priority': 'u=0, i',
                            'referer': 'https://app.golike.net/',
                            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-fetch-dest': 'document',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-site': 'same-origin',
                            'sec-fetch-user': '?1',
                            'upgrade-insecure-requests': '1',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                            }

                        response = requests.get(str(linkjob),  headers=haeaders).text
                        if 'li:fsd_company' not in response and 'identityDashProfilesByMemberIdentity&quot;:{&quot;*elements&quot;:[&quot;urn:li:fsd_profile:' not in response:
                                    json_data2 = {
                                    'account_id': account_id,
                                    'ads_id': ads_id,
                                     }
                                    url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                    check = requests.post(url,headers=headers,json=json_data2).json()
                                    if check['success']==True:
                                            prices =check['data']['prices']
                                            print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                    else:
                                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                            PARAMS = {
                                            'ads_id' : ads_id,
                                            'account_id' : account_id,
                                            'object_id' : object_id ,
                                            }
                                            checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                            if checkskipjob['status'] == 200:
                                                message = checkskipjob['message']
                                                print(Fore.RED+str(message))
                                                PARAMSr = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                                }
                        else:
                            json_data = {
                            'patch': {
                                '$set': {
                                    'following': True,
                                },
                            },
                            }
                            json_data2 = {
                                    'account_id': account_id,
                                    'ads_id': ads_id,
                                }
                            try:
                                crft =  COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                                try:
                                    headersX = {
                                    'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                    'content-type': 'application/json; charset=UTF-8',
                                    'cookie': COOKIELINK,
                                    'csrf-token': COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                                    'origin': 'https://www.linkedin.com',
                                    'priority': 'u=1, i',
                                    'referer': 'https://www.linkedin.com/company/chatplayground-ai/posts/?feedView=all',
                                    'sec-fetch-dest': 'empty',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                    'x-li-lang': 'en_US',
                                    'x-li-page-instance': 'urn:li:page:companies_company_posts_index;7952eddd-435c-428e-9587-a2dd19a42e2f',
                                    'x-li-pem-metadata': 'Voyager - Organization - Member=organization-follow',
                                    'x-li-track': '{"clientVersion":"1.13.19938","mpVersion":"1.13.19938","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                    'x-restli-protocol-version': '2.0.0',
                                    }

                                    ID = response.split('li:fsd_company:')[1].split('&')[0]
                                    follow = requests.post('https://www.linkedin.com/voyager/api/feed/dash/followingStates/urn:li:fsd_followingState:urn:li:fsd_company:'+ID,headers=headersX,json=json_data,proxies=proxyy)
                                    url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                    time.sleep(2)
                                    check = requests.post(url,headers=headers,json=json_data2).json()
                                    if check['success']==True:
                                            prices =check['data']['prices']
                                            print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                    else:
                                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                            PARAMS = {
                                            'ads_id' : ads_id,
                                            'account_id' : account_id,
                                            'object_id' : object_id ,
                                            }
                                            checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                            if checkskipjob['status'] == 200:
                                                message = checkskipjob['message']
                                                print(Fore.RED+str(message))
                                                PARAMSr = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                                }
                                except IndexError:
                                    headersY = {
                                    'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                    'content-type': 'application/json; charset=UTF-8',
                                    'cookie':COOKIELINK,
                                    'csrf-token': COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                                    'origin': 'https://www.linkedin.com',
                                    'priority': 'u=1, i',
                                    'referer': 'https://www.linkedin.com/in/noman-chaudhary-52031148/',
                                    'sec-fetch-dest': 'empty',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                    'x-li-lang': 'en_US',
                                    'x-li-page-instance': 'urn:li:page:d_flagship3_profile_view_base;I6RhpcMURWuRvBmeIhl5BQ==',
                                    'x-li-pem-metadata': 'Voyager - Follows=follow-action,Voyager - Profile Actions=topcard-primary-follow-action-click',
                                    'x-li-track': '{"clientVersion":"1.13.19938","mpVersion":"1.13.19938","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                    'x-restli-protocol-version': '2.0.0',
                                    }
                                    try:
                                        ID = response.split('identityDashProfilesByMemberIdentity&quot;:{&quot;*elements&quot;:[&quot;urn:li:fsd_profile:')[1].split('&')[0]
                                        follow =  requests.post('https://www.linkedin.com/voyager/api/feed/dash/followingStates/urn:li:fsd_followingState:urn:li:fsd_profile:'+ID,headers=headersY,json=json_data,proxies=proxyy) 
                                        time.sleep(2)
                                        url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                        check = requests.post(url,headers=headers,json=json_data2).json()
                                        if check['success']==True:
                                                prices =check['data']['prices']
                                                print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                        else:
                                                skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                                PARAMS = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                                }
                                                checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                                if checkskipjob['status'] == 200:
                                                    message = checkskipjob['message']
                                                    print(Fore.RED+str(message))
                                                    PARAMSr = {
                                                    'ads_id' : ads_id,
                                                    'account_id' : account_id,
                                                    'object_id' : object_id ,
                                                    }
                                    except IndexError:
                                        print('COOKIE DIE')
                                        os.remove('COOKIELINKEDIN'+str(account_id)+'.txt')
                                        return 0
                            except IndexError:
                                try:
                                    headersX = {
                                    'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                    'content-type': 'application/json; charset=UTF-8',
                                    'cookie': COOKIELINK,
                                    'csrf-token': COOKIELINK.split('JSESSIONID=')[1].split(';')[0],
                                    'origin': 'https://www.linkedin.com',
                                    'priority': 'u=1, i',
                                    'referer': 'https://www.linkedin.com/company/chatplayground-ai/posts/?feedView=all',
                                    'sec-fetch-dest': 'empty',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                    'x-li-lang': 'en_US',
                                    'x-li-page-instance': 'urn:li:page:companies_company_posts_index;7952eddd-435c-428e-9587-a2dd19a42e2f',
                                    'x-li-pem-metadata': 'Voyager - Organization - Member=organization-follow',
                                    'x-li-track': '{"clientVersion":"1.13.19938","mpVersion":"1.13.19938","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                    'x-restli-protocol-version': '2.0.0',
                                    }

                                    ID = response.split('li:fsd_company:')[1].split('&')[0]
                                    follow = requests.post('https://www.linkedin.com/voyager/api/feed/dash/followingStates/urn:li:fsd_followingState:urn:li:fsd_company:'+ID,headers=headersX,json=json_data,proxies=proxyy)
                                    time.sleep(2)
                                    url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                    check = requests.post(url,headers=headers,json=json_data2).json()
                                    if check['success']==True:
                                            prices =check['data']['prices']
                                            print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                    else:
                                            skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                            PARAMS = {
                                            'ads_id' : ads_id,
                                            'account_id' : account_id,
                                            'object_id' : object_id ,
                                            }
                                            checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                            if checkskipjob['status'] == 200:
                                                message = checkskipjob['message']
                                                print(Fore.RED+str(message))
                                                PARAMSr = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                                }
                                except IndexError:
                                    headersY = {
                                    'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                    'content-type': 'application/json; charset=UTF-8',
                                    'cookie':COOKIELINK,
                                    'csrf-token': COOKIELINK.split('JSESSIONID=')[1].split(';')[0],
                                    'origin': 'https://www.linkedin.com',
                                    'priority': 'u=1, i',
                                    'referer': 'https://www.linkedin.com/in/noman-chaudhary-52031148/',
                                    'sec-fetch-dest': 'empty',
                                    'sec-fetch-mode': 'cors',
                                    'sec-fetch-site': 'same-origin',
                                    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                    'x-li-lang': 'en_US',
                                    'x-li-page-instance': 'urn:li:page:d_flagship3_profile_view_base;I6RhpcMURWuRvBmeIhl5BQ==',
                                    'x-li-pem-metadata': 'Voyager - Follows=follow-action,Voyager - Profile Actions=topcard-primary-follow-action-click',
                                    'x-li-track': '{"clientVersion":"1.13.19938","mpVersion":"1.13.19938","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                    'x-restli-protocol-version': '2.0.0',
                                    }
                                    try:
                                        ID = response.split('identityDashProfilesByMemberIdentity&quot;:{&quot;*elements&quot;:[&quot;urn:li:fsd_profile:')[1].split('&')[0]
                                        follow =  requests.post('https://www.linkedin.com/voyager/api/feed/dash/followingStates/urn:li:fsd_followingState:urn:li:fsd_profile:'+ID,headers=headersY,json=json_data,proxies=proxyy) 
                                        time.sleep(2)
                                        url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                                        check = requests.post(url,headers=headers,json=json_data2).json()
                                        if check['success']==True:
                                                prices =check['data']['prices']
                                                print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                        else:
                                                skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                                PARAMS = {
                                                'ads_id' : ads_id,
                                                'account_id' : account_id,
                                                'object_id' : object_id ,
                                            
                                                }
                                                checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                                if checkskipjob['status'] == 200:
                                                    message = checkskipjob['message']
                                                    print(Fore.RED+str(message))
                                                    PARAMSr = {
                                                    'ads_id' : ads_id,
                                                    'account_id' : account_id,
                                                    'object_id' : object_id ,
                                                    
                                                    }
                                    except IndexError:
                                        print('COOKIE DIE')
                                        os.remove('COOKIELINKEDIN'+str(account_id)+'.txt')
                                        return 0
                    elif type == 'like':
                        try:
                            crft =  COOKIELINK.split('JSESSIONID')[1].split(';')[0],

                            headersL = {
                                'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                'content-type': 'application/json; charset=UTF-8',
                                'cookie': COOKIELINK,
                                'csrf-token': COOKIELINK.split('JSESSIONID=')[1].split(';')[0],
                                'origin': 'https://www.linkedin.com',
                                'priority': 'u=1, i',
                                'referer': 'https://www.linkedin.com/feed/update/urn:li:activity:7219700822467575808/',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                'x-li-lang': 'en_US',
                                # 'x-li-page-instance': 'urn:li:page:d_flagship3_detail_base;T3jRBiYHTZqgLY+qsIgtkg==',
                                'x-li-track': '{"clientVersion":"1.13.20142","mpVersion":"1.13.20142","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                'x-restli-protocol-version': '2.0.0',
                            }

                            params = {
                                'action': 'execute',
                                'queryId': 'voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b',
                            }

                            json_data = {
                                'variables': {
                                    'entity': {
                                        'reactionType': 'LIKE',
                                    },
                                    'threadUrn': 'urn:li:activity:'+str(object_id),
                                },
                                'queryId': 'voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b',
                                'includeWebMetadata': True,
                            }

                            response = requests.post(
                                'https://www.linkedin.com/voyager/api/graphql',
                                params=params,
                                headers=headersL,
                                json=json_data,
                                proxies=proxyy
                            )
                        except IndexError:
                            headersN = {
                                'accept': 'application/vnd.linkedin.normalized+json+2.1',
                                'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                                'content-type': 'application/json; charset=UTF-8',
                                'cookie': COOKIELINK,
                                'csrf-token': COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                                'origin': 'https://www.linkedin.com',
                                'priority': 'u=1, i',
                                'referer': 'https://www.linkedin.com/feed/update/urn:li:activity:7219700822467575808/',
                                'sec-fetch-dest': 'empty',
                                'sec-fetch-mode': 'cors',
                                'sec-fetch-site': 'same-origin',
                                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
                                'x-li-lang': 'en_US',
                                # 'x-li-page-instance': 'urn:li:page:d_flagship3_detail_base;T3jRBiYHTZqgLY+qsIgtkg==',
                                'x-li-track': '{"clientVersion":"1.13.20142","mpVersion":"1.13.20142","osName":"web","timezoneOffset":7,"timezone":"Asia/Bangkok","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.5625,"displayWidth":2400,"displayHeight":1350}',
                                'x-restli-protocol-version': '2.0.0',
                            }

                            params = {
                                'action': 'execute',
                                'queryId': 'voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b',
                            }

                            json_data = {
                                'variables': {
                                    'entity': {
                                        'reactionType': 'LIKE',
                                    },
                                    'threadUrn': 'urn:li:activity:'+str(object_id),
                                },
                                'queryId': 'voyagerSocialDashReactions.b731222600772fd42464c0fe19bd722b',
                                'includeWebMetadata': True,
                            }

                            response = requests.post(
                                'https://www.linkedin.com/voyager/api/graphql',
                                params=params,
                                headers=headersN,
                                json=json_data,
                                proxies=proxyy
                            )
                        json_data2 = {
                                'account_id': account_id,
                                'ads_id': ads_id,
                            }
                        time.sleep(2)
                        url = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                        check = requests.post(url,headers=headers,json=json_data2).json()
                        if check['success']==True:
                                prices =check['data']['prices']
                                print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                        else:
                                skipjob = 'https://gateway.golike.net/api/advertising/publishers/linkedin/skip-jobs'
                                PARAMS = {
                                'ads_id' : ads_id,
                                'account_id' : account_id,
                                'object_id' : object_id ,
                                }
                                checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                if checkskipjob['status'] == 200:
                                    message = checkskipjob['message']
                                    print(Fore.RED+str(message))
                                    PARAMSr = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }   
                else:        
                    print(checkurl2['message'])
                    countdown(15)
 
def LIST():
    mydata = [
        [Fore.RED+"1", "  Tiktok                ",Fore.GREEN+"  ĐANG HỌAT ĐỘNG"+Fore.RED],
        [Fore.RED+"2", "  Twitter/X             ",Fore.GREEN+"  ĐANG HỌAT ĐỘNG"+Fore.RED], 
        [Fore.RED+"3", "  Instagram             ",Fore.GREEN+"  ĐANG HỌAT ĐỘNG"+Fore.RED], 
        [Fore.RED+"4", "  Linkedin              ",Fore.GREEN+"  ĐANG HỌAT ĐỘNG"+Fore.RED]
    ]
    
    # create header
    head = ["STT", "  TOOL","   STATUS"]
    LIST=Fore.RED+tabulate(mydata, headers=head, tablefmt="grid",)
    print(LIST)
os.system('cls' if os.name== 'nt' else 'clear')
tprint("NHAT","rnd-xlarge")
print(Fore.RED+'\t\tTOOL BY NHATTOOL')
print('ZALO : 0386358592')
checkfile = os.path.isfile('user.txt')
if checkfile == False:
    AUTHUR = input(Fore.GREEN+'[+]''NHẬP Authorization : ')
    createfile = open('user.txt','w')
    createfile.write(AUTHUR)
    createfile.close()
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
else:
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
ses = requests.Session()
User_Agent=random.choice([
"android|Mozilla/5.0 (Linux; U; Android 7.1; GT-I9100 Build/KTU84P) AppleWebKit/603.12 (KHTML, like Gecko) Chrome/50.0.3755.367 Mobile Safari/600.8",
"android|Mozilla/5.0 (Linux; Android 5.0; SM-N910V Build/LRX22C) AppleWebKit/601.33 (KHTML, like Gecko) Chrome/54.0.1548.302 Mobile Safari/537.0",
"android|Mozilla/5.0 (Linux; U; Android 7.1; Pixel C Build/NRD90M) AppleWebKit/600.2 (KHTML, like Gecko) Chrome/53.0.2480.357 Mobile Safari/600.7",
"android|Mozilla/5.0 (Linux; U; Android 7.0; Nexus 7 Build/NME91E) AppleWebKit/537.24 (KHTML, like Gecko) Chrome/55.0.1165.180 Mobile Safari/535.4",
"android|Mozilla/5.0 (Android; Android 4.4.4; IQ4502 Quad Build/KOT49H) AppleWebKit/603.22 (KHTML, like Gecko) Chrome/55.0.3246.371 Mobile Safari/535.0",
"android|Mozilla/5.0 (Linux; U; Android 5.0.1; SAMSUNG SM-G925FQ Build/KOT49H) AppleWebKit/536.8 (KHTML, like Gecko) Chrome/49.0.2349.273 Mobile Safari/533.8",
"android|Mozilla/5.0 (Android; Android 5.1.1; SM-G935S Build/LMY47X) AppleWebKit/601.8 (KHTML, like Gecko) Chrome/51.0.1541.177 Mobile Safari/603.6",
"android|Mozilla/5.0 (Android; Android 7.1; Nexus 6 Build/NME91E) AppleWebKit/533.39 (KHTML, like Gecko) Chrome/52.0.3581.331 Mobile Safari/602.0",
"android|Mozilla/5.0 (Android; Android 7.1; Pixel C Build/NME91E) AppleWebKit/536.42 (KHTML, like Gecko) Chrome/47.0.2862.396 Mobile Safari/534.0",
"android|Mozilla/5.0 (Linux; Android 5.0.1; LG-D725 Build/LRX22G) AppleWebKit/603.18 (KHTML, like Gecko) Chrome/54.0.3919.385 Mobile Safari/601.9",
"android|Mozilla/5.0 (Linux; U; Android 5.0.2; Lenovo A7000-a Build/LRX21M;) AppleWebKit/600.8 (KHTML, like Gecko) Chrome/47.0.1683.316 Mobile Safari/534.4",
"android|Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925M Build/LRX22G) AppleWebKit/533.12 (KHTML, like Gecko) Chrome/48.0.3195.222 Mobile Safari/534.1",
"android|Mozilla/5.0 (Linux; U; Android 5.1.1; MOTOROLA XT1021 Build/LXB22) AppleWebKit/602.21 (KHTML, like Gecko) Chrome/51.0.3324.323 Mobile Safari/536.2",
"android|Mozilla/5.0 (Linux; Android 4.4; LG-D350 Build/KOT49I) AppleWebKit/601.4 (KHTML, like Gecko) Chrome/50.0.1490.201 Mobile Safari/602.6",
"android|Mozilla/5.0 (Linux; Android 7.0; Xperia Build/NDE63X) AppleWebKit/600.18 (KHTML, like Gecko) Chrome/48.0.3885.393 Mobile Safari/602.7",
"android|Mozilla/5.0 (Android; Android 7.1; Nexus 9X Build/NPD90G) AppleWebKit/536.38 (KHTML, like Gecko) Chrome/52.0.2441.242 Mobile Safari/601.0",
"android|Mozilla/5.0 (Linux; U; Android 7.1; GT-I9600 Build/KTU84P) AppleWebKit/602.14 (KHTML, like Gecko) Chrome/53.0.2318.108 Mobile Safari/534.8",
"android|Mozilla/5.0 (Android; Android 5.1.1; MOTO XT1570 MOTO X STYLE Build/LMY47Z) AppleWebKit/534.48 (KHTML, like Gecko) Chrome/55.0.1855.292 Mobile Safari/602.5",
"android|Mozilla/5.0 (Linux; U; Android 5.0.1; HTC Butterfly S 919d Build/LRX22G) AppleWebKit/534.18 (KHTML, like Gecko) Chrome/50.0.1695.312 Mobile Safari/535.3",
"android|Mozilla/5.0 (Android; Android 4.4; MOTOROLA MOTOG Build/KVT49L) AppleWebKit/533.8 (KHTML, like Gecko) Chrome/55.0.3923.147 Mobile Safari/600.9",
"android|Mozilla/5.0 (Linux; U; Android 6.0; HTC One801e dual sim Build/MRA58K) AppleWebKit/536.39 (KHTML, like Gecko) Chrome/47.0.3811.339 Mobile Safari/601.7",
"android|Mozilla/5.0 (Linux; Android 6.0.1; HTC OneS Build/MRA58K) AppleWebKit/600.47 (KHTML, like Gecko) Chrome/51.0.1432.312 Mobile Safari/535.4",
"android|Mozilla/5.0 (Linux; U; Android 4.4.1; LG-H220 Build/KOT49H) AppleWebKit/600.42 (KHTML, like Gecko) Chrome/48.0.2208.322 Mobile Safari/601.2",
"android|Mozilla/5.0 (Linux; U; Android 7.0; Nexus 6 Build/NME91E) AppleWebKit/534.11 (KHTML, like Gecko) Chrome/54.0.3774.223 Mobile Safari/600.6",
"android|Mozilla/5.0 (Linux; U; Android 7.0; GT-I9800 Build/KTU84P) AppleWebKit/601.41 (KHTML, like Gecko) Chrome/50.0.1638.368 Mobile Safari/536.0",
"android|Mozilla/5.0 (Linux; Android 6.0; SM-D925S Build/MDB08I) AppleWebKit/533.20 (KHTML, like Gecko) Chrome/47.0.2004.347 Mobile Safari/537.9",
"android|Mozilla/5.0 (Linux; U; Android 7.1.1; LG-H900 Build/NRD90C) AppleWebKit/536.25 (KHTML, like Gecko) Chrome/48.0.2443.138 Mobile Safari/601.6",
"android|Mozilla/5.0 (Linux; Android 6.0; HTC One_M8 Build/MRA58K) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/47.0.3998.201 Mobile Safari/603.7",
"android|Mozilla/5.0 (Linux; U; Android 5.0; Nokia 1100 wifi Build/GRK39F) AppleWebKit/533.11 (KHTML, like Gecko) Chrome/54.0.1361.195 Mobile Safari/602.4",
"android|Mozilla/5.0 (Linux; U; Android 4.4.4; SGH-I337 Build/KOT49H) AppleWebKit/536.23 (KHTML, like Gecko) Chrome/51.0.1317.102 Mobile Safari/603.0",
"android|Mozilla/5.0 (Linux; Android 5.0; SM-N915G Build/LRX22C) AppleWebKit/533.5 (KHTML, like Gecko) Chrome/50.0.2825.177 Mobile Safari/602.4",
"android|Mozilla/5.0 (Android; Android 5.1; SM-G9350FG Build/LMY47X) AppleWebKit/533.11 (KHTML, like Gecko) Chrome/53.0.2999.116 Mobile Safari/601.3",
"android|Mozilla/5.0 (Android; Android 5.1; SAMSUNG SM-G9350M Build/LMY47X) AppleWebKit/534.37 (KHTML, like Gecko) Chrome/51.0.3632.269 Mobile Safari/533.2",
"android|Mozilla/5.0 (Linux; U; Android 5.1; Nexus 8 Build/LRX22C) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/47.0.3223.257 Mobile Safari/536.7",
"android|Mozilla/5.0 (Linux; U; Android 4.4.1; XT1045 Build/[KXB20.9|KXC21.5]) AppleWebKit/601.38 (KHTML, like Gecko) Chrome/48.0.2780.100 Mobile Safari/535.6",
"android|Mozilla/5.0 (Linux; U; Android 7.1.1; Xperia Build/NDE63X) AppleWebKit/601.40 (KHTML, like Gecko) Chrome/48.0.1946.380 Mobile Safari/537.1",
"android|Mozilla/5.0 (Android; Android 5.1.1; MOTO X PLAY XT1562 Build/LPC23) AppleWebKit/533.10 (KHTML, like Gecko) Chrome/54.0.3715.270 Mobile Safari/537.6",
"android|Mozilla/5.0 (Android; Android 5.1.1; MOTOROLA MOTO E XT1021 Build/LPK23) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/48.0.1929.112 Mobile Safari/603.2",
"android|Mozilla/5.0 (Linux; Android 7.1.1; GT-I9700 Build/KTU84P) AppleWebKit/535.35 (KHTML, like Gecko) Chrome/48.0.3232.317 Mobile Safari/537.8",
"android|Mozilla/5.0 (Linux; Android 5.0.2; LG-D710 Build/LRX22G) AppleWebKit/535.36 (KHTML, like Gecko) Chrome/48.0.1427.177 Mobile Safari/535.9",
"android|Mozilla/5.0 (Android; Android 4.4.4; SAMSUNG SM-T534 Build/KTU84P) AppleWebKit/534.48 (KHTML, like Gecko) Chrome/55.0.1653.292 Mobile Safari/536.3",
"android|Mozilla/5.0 (Android; Android 7.1; SAMSUNG GT-I9700 Build/KTU84P) AppleWebKit/602.46 (KHTML, like Gecko) Chrome/51.0.2298.210 Mobile Safari/603.2",
"android|Mozilla/5.0 (Linux; Android 4.4.4; SM-T534 Build/KOT49H) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/48.0.2865.177 Mobile Safari/601.4",
"android|Mozilla/5.0 (Android; Android 6.0.1; SAMSUNG SM-G925F Build/MMB29K) AppleWebKit/603.6 (KHTML, like Gecko) Chrome/52.0.1707.337 Mobile Safari/600.7",
"android|Mozilla/5.0 (Linux; Android 6.0; HTC One_M9 Build/MRA58K) AppleWebKit/534.48 (KHTML, like Gecko) Chrome/51.0.1871.148 Mobile Safari/603.9",
"android|Mozilla/5.0 (Linux; Android 6.0.1; SM-D920M Build/MDB08I) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/52.0.1990.397 Mobile Safari/536.9",
"android|Mozilla/5.0 (Linux; U; Android 4.4.1; Nexus5 V7.1 Build/KOT49H) AppleWebKit/602.45 (KHTML, like Gecko) Chrome/55.0.2720.129 Mobile Safari/534.2",
"android|Mozilla/5.0 (Android; Android 5.0.1; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/602.15 (KHTML, like Gecko) Chrome/52.0.2125.398 Mobile Safari/603.2",
"android|Mozilla/5.0 (Linux; U; Android 5.0.1; SM-G838K Build/LRX22G) AppleWebKit/601.15 (KHTML, like Gecko) Chrome/51.0.3404.311 Mobile Safari/601.3",
"android|Mozilla/5.0 (Linux; U; Android 5.0; SAMSUNG SM-G490 Build/LRX22C) AppleWebKit/536.29 (KHTML, like Gecko) Chrome/48.0.1322.228 Mobile Safari/533.5",
"android|Mozilla/5.0 (Linux; Android 5.1.1; SM-G9350FQ Build/LMY47X) AppleWebKit/602.46 (KHTML, like Gecko) Chrome/55.0.1253.269 Mobile Safari/534.2",
"android|Mozilla/5.0 (Android; Android 7.1.1; Xperia V Build/NDE63X) AppleWebKit/533.20 (KHTML, like Gecko) Chrome/47.0.1025.370 Mobile Safari/602.9",
"android|Mozilla/5.0 (Linux; U; Android 5.1.1; SAMSUNG SM-G9358 Build/MMB29M) AppleWebKit/535.4 (KHTML, like Gecko) Chrome/47.0.3983.116 Mobile Safari/535.5",
"android|Mozilla/5.0 (Linux; U; Android 5.1.1; Nexus 5 Build/LRX22C) AppleWebKit/600.24 (KHTML, like Gecko) Chrome/53.0.3063.165 Mobile Safari/602.0",
"android|Mozilla/5.0 (Android; Android 6.0.1; SAMSUNG SM-G925F Build/MDB08I) AppleWebKit/536.4 (KHTML, like Gecko) Chrome/50.0.1745.361 Mobile Safari/534.9",
"android|Mozilla/5.0 (Linux; U; Android 5.0.2; SAMSUNG-SM-N910F Build/LRX22C) AppleWebKit/601.39 (KHTML, like Gecko) Chrome/47.0.3525.232 Mobile Safari/536.8",
"android|Mozilla/5.0 (Linux; U; Android 6.0.1; HTC OneS Build/MRA58K) AppleWebKit/600.11 (KHTML, like Gecko) Chrome/48.0.1277.258 Mobile Safari/534.7",
"android|Mozilla/5.0 (Linux; Android 4.4.1; [HM NOTE|NOTE-III|NOTE2 1LTET) AppleWebKit/600.12 (KHTML, like Gecko) Chrome/53.0.2390.359 Mobile Safari/537.9",
"android|Mozilla/5.0 (Linux; U; Android 5.0.2; Lenovo A7000-a Build/LRX21M;) AppleWebKit/603.49 (KHTML, like Gecko) Chrome/49.0.3944.138 Mobile Safari/533.9",
"android|Mozilla/5.0 (Linux; Android 4.4.4; MOTOROLA MSM8960 Build/KVT49L) AppleWebKit/537.41 (KHTML, like Gecko) Chrome/52.0.3875.248 Mobile Safari/533.5",
"android|Mozilla/5.0 (Android; Android 4.4.1; SM-E500F Build/KTU84P) AppleWebKit/535.49 (KHTML, like Gecko) Chrome/51.0.3420.118 Mobile Safari/533.4",
"android|Mozilla/5.0 (Linux; U; Android 4.3.1; Ascend G310 Build/JLS36I) AppleWebKit/536.9 (KHTML, like Gecko) Chrome/51.0.2591.258 Mobile Safari/533.1",
"android|Mozilla/5.0 (Linux; Android 4.4; [HM NOTE|NOTE-III|NOTE2 1LTETD) AppleWebKit/601.29 (KHTML, like Gecko) Chrome/54.0.2437.145 Mobile Safari/600.5",
"android|Mozilla/5.0 (Linux; U; Android 4.3.1; Samsung Galaxy S4 Mega GT-I8900 Build/JDQ39) AppleWebKit/603.41 (KHTML, like Gecko) Chrome/53.0.2227.349 Mobile Safari/535.9",
"android|Mozilla/5.0 (Android; Android 7.0; Xperia V Build/NDE63X) AppleWebKit/535.50 (KHTML, like Gecko) Chrome/48.0.1213.228 Mobile Safari/534.9",
"android|Mozilla/5.0 (Android; Android 5.1; SAMSUNG SM-G920T Build/LRX22G) AppleWebKit/600.9 (KHTML, like Gecko) Chrome/55.0.1773.347 Mobile Safari/600.8",
"android|Mozilla/5.0 (Linux; U; Android 5.0; LG-D325 Build/LRX22G) AppleWebKit/602.12 (KHTML, like Gecko) Chrome/52.0.1615.322 Mobile Safari/603.3",
"android|Mozilla/5.0 (Android; Android 4.4.1; XT1030 Build/[KXB20.9|KXC21.5]) AppleWebKit/602.41 (KHTML, like Gecko) Chrome/54.0.3368.257 Mobile Safari/537.0",
"android|Mozilla/5.0 (Linux; Android 5.0; SM-A800F Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.3412.259 Mobile Safari/535.7",
"android|Mozilla/5.0 (Android; Android 5.0.1; SAMSUNG SM-G440 Build/LRX22C) AppleWebKit/602.10 (KHTML, like Gecko) Chrome/47.0.1899.185 Mobile Safari/601.0",
"android|Mozilla/5.0 (Linux; Android 4.4.1; XT1015 Build/[KXB20.9|KXC21.5]) AppleWebKit/535.50 (KHTML, like Gecko) Chrome/50.0.3256.155 Mobile Safari/533.7",
"android|Mozilla/5.0 (Android; Android 6.0.1; Nexus 5P Build/MMB29K) AppleWebKit/601.28 (KHTML, like Gecko) Chrome/53.0.1250.316 Mobile Safari/602.1",
"android|Mozilla/5.0 (Linux; U; Android 6.0; HTC One0P6B Build/MRA58K) AppleWebKit/603.30 (KHTML, like Gecko) Chrome/55.0.2434.210 Mobile Safari/535.8",
"android|Mozilla/5.0 (Linux; U; Android 4.4; Nexus S Build/GRJ22) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/52.0.2092.313 Mobile Safari/535.1",
"android|Mozilla/5.0 (Android; Android 6.0; Nexus 7 Build/MDB08I) AppleWebKit/601.13 (KHTML, like Gecko) Chrome/55.0.3458.256 Mobile Safari/602.3",
"android|Mozilla/5.0 (Linux; Android 7.0; Xperia Build/NDE63X) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/55.0.2024.290 Mobile Safari/601.7",
"android|Mozilla/5.0 (Linux; Android 6.0; Nexus 7X Build/MMB29K) AppleWebKit/602.9 (KHTML, like Gecko) Chrome/53.0.2233.211 Mobile Safari/536.8",
"android|Mozilla/5.0 (Linux; Android 4.3.1; HTC One max Build/JSS15J) AppleWebKit/600.41 (KHTML, like Gecko) Chrome/47.0.2082.139 Mobile Safari/535.5",
"android|Mozilla/5.0 (Android; Android 4.4.4; [HM NOTE|NOTE-III|NOTE2 1LTETD) AppleWebKit/534.25 (KHTML, like Gecko) Chrome/54.0.1522.241 Mobile Safari/603.8",
"android|Mozilla/5.0 (Android; Android 6.0; HTC One_M8 Build/MRA58K) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/52.0.2870.393 Mobile Safari/533.2",
"android|Mozilla/5.0 (Android; Android 7.1.1; Nexus 5X Build/NME91E) AppleWebKit/600.32 (KHTML, like Gecko) Chrome/53.0.3441.128 Mobile Safari/535.1",
"android|Mozilla/5.0 (Linux; U; Android 4.3.1; GT-I9200 Build/JDQ39) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/54.0.3465.134 Mobile Safari/537.7",
"android|Mozilla/5.0 (Linux; Android 4.3.1; Samsung Galaxy SIV Mega GT-I9200 Build/JDQ39) AppleWebKit/533.25 (KHTML, like Gecko) Chrome/55.0.1686.304 Mobile Safari/534.9",
"android|Mozilla/5.0 (Linux; U; Android 5.0.2; LG-D337 Build/LRX22G) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/52.0.3787.310 Mobile Safari/600.8",
"android|Mozilla/5.0 (Linux; U; Android 5.0; SM-G925I Build/KOT49H) AppleWebKit/603.19 (KHTML, like Gecko) Chrome/54.0.1719.131 Mobile Safari/602.9",
"android|Mozilla/5.0 (Linux; Android 4.4.4; XT1050 Build/[KXB20.9|KXC21.5]) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/51.0.1827.314 Mobile Safari/602.8",
"android|Mozilla/5.0 (Linux; Android 7.1; Pixel C Build/NME91E) AppleWebKit/602.47 (KHTML, like Gecko) Chrome/51.0.1630.100 Mobile Safari/534.2",
"android|Mozilla/5.0 (Linux; U; Android 7.1.1; Nexus 8X Build/NME91E) AppleWebKit/600.23 (KHTML, like Gecko) Chrome/51.0.1659.377 Mobile Safari/602.1",
"android|Mozilla/5.0 (Linux; U; Android 6.0; HTC One801e Build/MRA58K) AppleWebKit/534.5 (KHTML, like Gecko) Chrome/53.0.2981.209 Mobile Safari/601.4",
"android|Mozilla/5.0 (Linux; U; Android 7.0; Nexus 6 Build/NME91E) AppleWebKit/602.15 (KHTML, like Gecko) Chrome/49.0.1127.358 Mobile Safari/536.4",
"android|Mozilla/5.0 (Linux; Android 5.1; MOTOROLA MOTO XT1570 MOTO X STYLE Build/LMY47Z) AppleWebKit/533.27 (KHTML, like Gecko) Chrome/54.0.3887.207 Mobile Safari/537.4",
"android|Mozilla/5.0 (Linux; Android 7.1.1; LG-H910 Build/NRD90C) AppleWebKit/537.28 (KHTML, like Gecko) Chrome/52.0.1337.379 Mobile Safari/533.3",
"android|Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG-SM-N915A Build/LRX22C) AppleWebKit/603.12 (KHTML, like Gecko) Chrome/52.0.1334.307 Mobile Safari/600.1",
"android|Mozilla/5.0 (Linux; Android 4.4.1; SM-N9008 Build/KOT49H) AppleWebKit/600.43 (KHTML, like Gecko) Chrome/55.0.1429.269 Mobile Safari/535.7",
"android|Mozilla/5.0 (Linux; Android 6.0; Nexus 6X Build/MDB08L) AppleWebKit/601.19 (KHTML, like Gecko) Chrome/50.0.2717.179 Mobile Safari/534.2",
"android|Mozilla/5.0 (Android; Android 5.1.1; SAMSUNG SM-G920M Build/LRX22G) AppleWebKit/536.44 (KHTML, like Gecko) Chrome/48.0.3528.122 Mobile Safari/533.8",
"android|Mozilla/5.0 (Android; Android 6.0; HTC One_M8 Pro Build/MRA58K) AppleWebKit/603.50 (KHTML, like Gecko) Chrome/53.0.1373.166 Mobile Safari/537.0",
"android|Mozilla/5.0 (Linux; U; Android 5.1; Nexus 6 Build/LRX22C) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/55.0.2850.150 Mobile Safari/603.5",
"android|Mozilla/5.0 (Linux; U; Android 4.4.4; MOTOROLA MOTOG Build/KVT49L) AppleWebKit/602.10 (KHTML, like Gecko) Chrome/50.0.2856.367 Mobile Safari/603.8",
"android|Mozilla/5.0 (Linux; U; Android 7.1.1; GT-I9100 Build/KTU84P) AppleWebKit/600.13 (KHTML, like Gecko) Chrome/53.0.2579.126 Mobile Safari/602.3",
"android|Mozilla/5.0 (Android; Android 6.0; HTC One_M8 Build/MRA58K) AppleWebKit/533.33 (KHTML, like Gecko) Chrome/47.0.3883.341 Mobile Safari/535.5",
"android|Mozilla/5.0 (Linux; U; Android 6.0; HTC One809d Build/MRA58K) AppleWebKit/533.33 (KHTML, like Gecko) Chrome/53.0.1731.383 Mobile Safari/537.8",
"android|Mozilla/5.0 (Linux; Android 6.0; SAMSUNG SM-D9350V Build/MDB08I) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/54.0.1231.249 Mobile Safari/535.3",
"android|Mozilla/5.0 (Linux; U; Android 5.1; Nexus 7 Build/LRX22C) AppleWebKit/602.6 (KHTML, like Gecko) Chrome/47.0.2414.274 Mobile Safari/534.7",
"android|Mozilla/5.0 (Android; Android 4.4; LG-F200L Build/KOT49I) AppleWebKit/600.17 (KHTML, like Gecko) Chrome/53.0.1408.163 Mobile Safari/537.1",
"android|Mozilla/5.0 (Android; Android 4.4; LG-E989 Build/KOT49I) AppleWebKit/537.5 (KHTML, like Gecko) Chrome/52.0.3070.247 Mobile Safari/533.6",
"android|Mozilla/5.0 (Linux; Android 5.0.1; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/537.7 (KHTML, like Gecko) Chrome/48.0.3336.259 Mobile Safari/602.9",
"android|Mozilla/5.0 (Linux; U; Android 5.1.1; SAMSUNG SM-G925FQ Build/LMY47X) AppleWebKit/600.4 (KHTML, like Gecko) Chrome/49.0.2815.223 Mobile Safari/603.7",
"android|Mozilla/5.0 (Linux; Android 4.4; SM-N9005 Build/KOT49H) AppleWebKit/535.50 (KHTML, like Gecko) Chrome/52.0.1291.199 Mobile Safari/534.1",
"android|Mozilla/5.0 (Linux; U; Android 7.1.1; LG-H920 Build/NRD90M) AppleWebKit/601.8 (KHTML, like Gecko) Chrome/53.0.3173.124 Mobile Safari/601.4",
"android|Mozilla/5.0 (Android; Android 6.0.1; HTC One_M9 Build/MRA58K) AppleWebKit/537.50 (KHTML, like Gecko) Chrome/54.0.2468.260 Mobile Safari/600.0",
"android|Mozilla/5.0 (Linux; Android 7.1; Nexus 6X Build/NME91E) AppleWebKit/600.10 (KHTML, like Gecko) Chrome/55.0.1978.132 Mobile Safari/602.2",
"android|Mozilla/5.0 (Android; Android 5.0; SM-T550 Build/LRX22G) AppleWebKit/535.23 (KHTML, like Gecko) Chrome/55.0.2282.311 Mobile Safari/601.7",
"android|Mozilla/5.0 (Android; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/603.31 (KHTML, like Gecko) Chrome/52.0.3972.282 Mobile Safari/536.8",
"android|Mozilla/5.0 (Linux; U; Android 6.0.1; Nexus 6P Build/MMB29V) AppleWebKit/603.7 (KHTML, like Gecko) Chrome/54.0.3981.308 Mobile Safari/601.5",
"android|Mozilla/5.0 (Android; Android 4.4.1; SAMSUNG SM-N8010 Build/KVT49L) AppleWebKit/535.16 (KHTML, like Gecko) Chrome/47.0.2174.383 Mobile Safari/603.6",
"android|Mozilla/5.0 (Linux; U; Android 5.0.2; Nokia 1100 wifi Build/GRK39F) AppleWebKit/601.45 (KHTML, like Gecko) Chrome/53.0.1677.190 Mobile Safari/602.1",
"android|Mozilla/5.0 (Linux; Android 4.4.1; MOTOROLA RAZR Build/KVT49L) AppleWebKit/533.6 (KHTML, like Gecko) Chrome/47.0.3222.256 Mobile Safari/534.0",
"android|Mozilla/5.0 (Linux; U; Android 5.1; MOTOROLA MOTO X PLAY XT1562 Build/LPK23) AppleWebKit/601.16 (KHTML, like Gecko) Chrome/54.0.3334.251 Mobile Safari/534.8",
"android|Mozilla/5.0 (Android; Android 5.0; Lenovo A7000-a Build/LRX21M;) AppleWebKit/603.21 (KHTML, like Gecko) Chrome/55.0.2110.274 Mobile Safari/602.4",
"android|Mozilla/5.0 (Linux; U; Android 5.0.2; SM-D859T Build/LMY47X) AppleWebKit/603.1 (KHTML, like Gecko) Chrome/54.0.2370.124 Mobile Safari/600.6",
"android|Mozilla/5.0 (Android; Android 4.4.4; SM-J100G Build/KTU84P) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/52.0.2128.221 Mobile Safari/603.6",
"android|Mozilla/5.0 (Linux; Android 4.4.1; LG-V710 Build/KOT49I) AppleWebKit/536.44 (KHTML, like Gecko) Chrome/47.0.2255.142 Mobile Safari/536.3",
"android|Mozilla/5.0 (Android; Android 5.1.1; SM-G935FG Build/LMY47X) AppleWebKit/535.15 (KHTML, like Gecko) Chrome/49.0.1479.172 Mobile Safari/535.1",
"android|Mozilla/5.0 (Android; Android 5.0.2; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/600.11 (KHTML, like Gecko) Chrome/50.0.3814.139 Mobile Safari/603.5",
"android|Mozilla/5.0 (Android; Android 5.1; SM-G925FD Build/LRX22G) AppleWebKit/601.13 (KHTML, like Gecko) Chrome/47.0.2392.367 Mobile Safari/533.1",
"android|Mozilla/5.0 (Linux; Android 4.4; LG-V500 Build/KOT49I) AppleWebKit/537.5 (KHTML, like Gecko) Chrome/50.0.2360.264 Mobile Safari/601.1",
"android|Mozilla/5.0 (Android; Android 6.0.1; HTC One_M8 dual sim Build/MRA58K) AppleWebKit/535.3 (KHTML, like Gecko) Chrome/54.0.3756.104 Mobile Safari/537.8",
"android|Mozilla/5.0 (Android; Android 6.0; SAMSUNG SM-G920V Build/MMB29K) AppleWebKit/537.44 (KHTML, like Gecko) Chrome/52.0.3427.179 Mobile Safari/535.6",
"android|Mozilla/5.0 (Android; Android 5.0.2; Lenovo A7000-a Build/LRX21M;) AppleWebKit/537.24 (KHTML, like Gecko) Chrome/50.0.1129.268 Mobile Safari/603.6",
"android|Mozilla/5.0 (Linux; Android 7.1; SAMSUNG GT-I9100 Build/KTU84P) AppleWebKit/533.35 (KHTML, like Gecko) Chrome/48.0.2803.270 Mobile Safari/537.0",
"android|Mozilla/5.0 (Linux; Android 5.0.2; SM-A700F Build/LMY47X) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/48.0.1877.144 Mobile Safari/533.5",
"android|Mozilla/5.0 (Linux; U; Android 7.1.1; Nexus 5P Build/NPD90G) AppleWebKit/603.50 (KHTML, like Gecko) Chrome/53.0.2745.237 Mobile Safari/533.1",
"android|Mozilla/5.0 (Android; Android 5.0.1; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/602.41 (KHTML, like Gecko) Chrome/48.0.1523.109 Mobile Safari/537.0",
"android|Mozilla/5.0 (Linux; U; Android 5.0.2; SM-G900FQ Build/KTU84F) AppleWebKit/533.38 (KHTML, like Gecko) Chrome/54.0.1080.159 Mobile Safari/535.5",
"android|Mozilla/5.0 (Android; Android 5.0.1; Nokia 1000 LTE Build/GRK39F) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/47.0.3528.369 Mobile Safari/535.7",
"android|Mozilla/5.0 (Linux; Android 4.4.1; XT1048 Build/[KXB20.9|KXC21.5]) AppleWebKit/535.10 (KHTML, like Gecko) Chrome/51.0.2885.225 Mobile Safari/601.5",
"android|Mozilla/5.0 (Linux; Android 4.3.1; SAMSUNG SM-G3645A Build/JLS36C) AppleWebKit/534.46 (KHTML, like Gecko) Chrome/55.0.3990.379 Mobile Safari/536.3",
"android|Mozilla/5.0 (Android; Android 4.4.4; SAMSUNG-SGH-I337M Build/JSS15J) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/47.0.1284.267 Mobile Safari/602.5",
"android|Mozilla/5.0 (Linux; U; Android 5.1.1; SM-G935FD Build/LMY47X) AppleWebKit/536.35 (KHTML, like Gecko) Chrome/48.0.2554.102 Mobile Safari/601.2",
"android|Mozilla/5.0 (Linux; U; Android 5.0.1; LG-D716 Build/LRX22G) AppleWebKit/601.29 (KHTML, like Gecko) Chrome/48.0.2208.232 Mobile Safari/536.2",
"android|Mozilla/5.0 (Linux; Android 5.0.2; SM-G920M Build/LRX21T) AppleWebKit/601.45 (KHTML, like Gecko) Chrome/51.0.3596.122 Mobile Safari/600.9",
"android|Mozilla/5.0 (Linux; U; Android 6.0.1; HTC One_M8 Pro Build/MRA58K) AppleWebKit/600.39 (KHTML, like Gecko) Chrome/52.0.2526.133 Mobile Safari/537.4",
"android|Mozilla/5.0 (Linux; Android 4.3.1; SAMSUNG SM-T265t Build/JLS36C) AppleWebKit/537.33 (KHTML, like Gecko) Chrome/47.0.2810.372 Mobile Safari/536.4",
"android|Mozilla/5.0 (Linux; Android 4.4.1; SAMSUNG SM-J200F Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.3462.236 Mobile Safari/537.6",
"android|Mozilla/5.0 (Android; Android 4.4; Lenovo P772 Build/Lenovo) AppleWebKit/536.49 (KHTML, like Gecko) Chrome/52.0.2987.389 Mobile Safari/535.9",
"android|Mozilla/5.0 (Android; Android 7.0; LG-H920 Build/NRD90C) AppleWebKit/602.49 (KHTML, like Gecko) Chrome/47.0.1614.379 Mobile Safari/533.9",
"android|Mozilla/5.0 (Linux; U; Android 4.3.1; HTC One 801e Build/JLS36C) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/47.0.1150.148 Mobile Safari/533.9",
"android|Mozilla/5.0 (Android; Android 5.0.2; HTC Butterfly S 901 Build/LRX22G) AppleWebKit/601.9 (KHTML, like Gecko) Chrome/49.0.2789.352 Mobile Safari/534.4",
"android|Mozilla/5.0 (Android; Android 4.4.1; SM-G900FG Build/KOT49H) AppleWebKit/535.15 (KHTML, like Gecko) Chrome/54.0.3531.278 Mobile Safari/535.6",
"android|Mozilla/5.0 (Android; Android 7.1.1; Nexus 5P Build/NME91E) AppleWebKit/533.40 (KHTML, like Gecko) Chrome/48.0.2641.230 Mobile Safari/603.8",
"android|Mozilla/5.0 (Android; Android 4.4.1; LG-V700 Build/KOT49I) AppleWebKit/533.23 (KHTML, like Gecko) Chrome/55.0.2303.377 Mobile Safari/537.5",
"android|Mozilla/5.0 (Android; Android 5.0.2; SAMSUNG-SM-N915F Build/LRX22C) AppleWebKit/600.35 (KHTML, like Gecko) Chrome/51.0.1578.331 Mobile Safari/536.5",
"android|Mozilla/5.0 (Linux; Android 7.1; Xperia Build/NDE63X) AppleWebKit/600.2 (KHTML, like Gecko) Chrome/55.0.1022.146 Mobile Safari/600.5",
"android|Mozilla/5.0 (Linux; U; Android 4.3.1; HTC Xplorer A280s Build/GRJ90) AppleWebKit/536.36 (KHTML, like Gecko) Chrome/51.0.3601.368 Mobile Safari/601.0",
"android|Mozilla/5.0 (Linux; U; Android 6.0.1; SM-D928V Build/MMB29V) AppleWebKit/600.47 (KHTML, like Gecko) Chrome/52.0.3830.148 Mobile Safari/603.6",
"android|Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/NPD90G) AppleWebKit/537.16 (KHTML, like Gecko) Chrome/52.0.1028.106 Mobile Safari/534.3",
"android|Mozilla/5.0 (Linux; Android 4.3.1; HP 695 Notebook PC Build/JLS36C) AppleWebKit/534.11 (KHTML, like Gecko) Chrome/51.0.2095.173 Mobile Safari/601.7",
"android|Mozilla/5.0 (Linux; U; Android 5.0.2; SM-A800T Build/LRX22G) AppleWebKit/602.5 (KHTML, like Gecko) Chrome/51.0.2311.188 Mobile Safari/533.0",
"android|Mozilla/5.0 (Android; Android 5.0; Nokia 1000 wifi Build/GRK39F) AppleWebKit/603.14 (KHTML, like Gecko) Chrome/55.0.2543.279 Mobile Safari/535.3",
"android|Mozilla/5.0 (Linux; Android 4.3.1; SAMSUNG SGH-N075T Build/JSS15J) AppleWebKit/536.4 (KHTML, like Gecko) Chrome/55.0.3658.238 Mobile Safari/534.8",
"android|Mozilla/5.0 (Android; Android 5.1.1; SAMSUNG SM-G920H Build/LMY47X) AppleWebKit/533.26 (KHTML, like Gecko) Chrome/51.0.1326.283 Mobile Safari/600.5",
"android|Mozilla/5.0 (Linux; Android 5.0.2; HTC Butterfly S 901 Build/LRX22G) AppleWebKit/602.48 (KHTML, like Gecko) Chrome/49.0.1098.211 Mobile Safari/535.0",
"android|Mozilla/5.0 (Android; Android 7.1.1; LG-H930 Build/NRD90C) AppleWebKit/603.29 (KHTML, like Gecko) Chrome/51.0.1554.312 Mobile Safari/537.2",
"android|Mozilla/5.0 (Linux; U; Android 5.0; Nokia 1100 4G Build/GRK39F) AppleWebKit/535.15 (KHTML, like Gecko) Chrome/48.0.2333.138 Mobile Safari/601.9",
"android|Mozilla/5.0 (Android; Android 6.0; HTC One_M8 dual sim Build/MRA58K) AppleWebKit/602.24 (KHTML, like Gecko) Chrome/51.0.3951.174 Mobile Safari/533.6",
"android|Mozilla/5.0 (Linux; Android 4.3.1; HTC One 801s Build/JLS36C) AppleWebKit/600.34 (KHTML, like Gecko) Chrome/54.0.2066.223 Mobile Safari/533.1",
"android|Mozilla/5.0 (Android; Android 5.1; Nexus 6 Build/LRX22C) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/54.0.2361.195 Mobile Safari/533.3",
"android|Mozilla/5.0 (Android; Android 4.4.4; GT-I9303T Build/KOT49H) AppleWebKit/536.27 (KHTML, like Gecko) Chrome/49.0.1741.382 Mobile Safari/534.6",
"android|Mozilla/5.0 (Linux; Android 7.1.1; Xperia V Build/NDE63X) AppleWebKit/600.24 (KHTML, like Gecko) Chrome/48.0.3928.244 Mobile Safari/537.1",
"android|Mozilla/5.0 (Android; Android 5.1.1; SM-G935FG Build/MMB29M) AppleWebKit/602.27 (KHTML, like Gecko) Chrome/47.0.3208.216 Mobile Safari/533.9",
"android|Mozilla/5.0 (Android; Android 4.3.1; HP Compaq 2110b Build/JLS36C) AppleWebKit/533.31 (KHTML, like Gecko) Chrome/55.0.2801.140 Mobile Safari/533.6",
"android|Mozilla/5.0 (Android; Android 7.1; Pixel C Build/NRD90M) AppleWebKit/537.48 (KHTML, like Gecko) Chrome/48.0.2554.356 Mobile Safari/537.2",
"android|Mozilla/5.0 (Android; Android 7.1.1; LG-H910 Build/NRD90C) AppleWebKit/600.29 (KHTML, like Gecko) Chrome/51.0.2831.187 Mobile Safari/600.4",
"android|Mozilla/5.0 (Android; Android 6.0.1; Nexus 5P Build/MDB08I) AppleWebKit/600.29 (KHTML, like Gecko) Chrome/52.0.2510.347 Mobile Safari/603.5",
"android|Mozilla/5.0 (Linux; Android 5.0.1; HTC 80:number1-2s Build/LRX22G) AppleWebKit/534.8 (KHTML, like Gecko) Chrome/52.0.3570.184 Mobile Safari/536.1",
"android|Mozilla/5.0 (Linux; Android 4.3.1; HUAWEI G6-L11 Build/HuaweiG6-L10) AppleWebKit/600.14 (KHTML, like Gecko) Chrome/47.0.1114.274 Mobile Safari/600.3",
"android|Mozilla/5.0 (Android; Android 7.1.1; Nexus 8P Build/NPD90G) AppleWebKit/534.39 (KHTML, like Gecko) Chrome/52.0.3728.395 Mobile Safari/600.2",
"android|Mozilla/5.0 (Linux; U; Android 5.1; MOTOROLA MOTO XT1580 Build/LPD23) AppleWebKit/536.31 (KHTML, like Gecko) Chrome/48.0.3929.209 Mobile Safari/534.1",
"android|Mozilla/5.0 (Android; Android 5.1.1; Nexus 9 Build/LRX22C) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/49.0.2770.360 Mobile Safari/537.2",
"android|Mozilla/5.0 (Linux; U; Android 6.0; SM-G920F Build/MDB08L) AppleWebKit/603.45 (KHTML, like Gecko) Chrome/54.0.1872.306 Mobile Safari/536.7",
"android|Mozilla/5.0 (Android; Android 7.1.1; Pixel C Build/NME91E) AppleWebKit/602.30 (KHTML, like Gecko) Chrome/47.0.1466.346 Mobile Safari/535.7",
"android|Mozilla/5.0 (Linux; U; Android 5.0.2; LG-D335 Build/LRX22G) AppleWebKit/603.49 (KHTML, like Gecko) Chrome/51.0.3635.337 Mobile Safari/536.5",
"android|Mozilla/5.0 (Linux; U; Android 7.1.1; Nexus 7P Build/NME91E) AppleWebKit/535.16 (KHTML, like Gecko) Chrome/48.0.3288.270 Mobile Safari/600.4",
"android|Mozilla/5.0 (Android; Android 5.0.2; LG-D337 Build/LRX22G) AppleWebKit/537.8 (KHTML, like Gecko) Chrome/49.0.1305.378 Mobile Safari/603.3",
"android|Mozilla/5.0 (Linux; U; Android 5.1.1; SAMSUNG SM-G935M Build/LMY47X) AppleWebKit/533.13 (KHTML, like Gecko) Chrome/48.0.2432.178 Mobile Safari/602.6",
"android|Mozilla/5.0 (Android; Android 5.0.2; SAMSUNG SM-A800I Build/LMY47X) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/47.0.2453.203 Mobile Safari/533.4",
"android|Mozilla/5.0 (Linux; Android 7.0; SAMSUNG GT-I9700 Build/KTU84P) AppleWebKit/601.31 (KHTML, like Gecko) Chrome/55.0.3282.361 Mobile Safari/601.2",
"android|Mozilla/5.0 (Android; Android 5.0; SM-N910F Build/LRX22C) AppleWebKit/601.14 (KHTML, like Gecko) Chrome/48.0.2926.278 Mobile Safari/535.6",
"android|Mozilla/5.0 (Linux; Android 4.3.1; GT-I9400 Build/JDQ39) AppleWebKit/535.46 (KHTML, like Gecko) Chrome/48.0.2444.279 Mobile Safari/536.7",
"android|Mozilla/5.0 (Android; Android 5.0.1; SM-N915V Build/LRX22C) AppleWebKit/601.3 (KHTML, like Gecko) Chrome/47.0.2414.138 Mobile Safari/602.4",
"android|Mozilla/5.0 (Linux; U; Android 7.1.1; SAMSUNG GT-I9600 Build/KTU84P) AppleWebKit/536.48 (KHTML, like Gecko) Chrome/55.0.3810.244 Mobile Safari/600.7",
"android|Mozilla/5.0 (Linux; Android 5.0; HTC Butterfly S 919 Build/LRX22G) AppleWebKit/533.46 (KHTML, like Gecko) Chrome/52.0.1348.138 Mobile Safari/601.6",
"android|Mozilla/5.0 (Linux; Android 5.0.2; HTC Butterfly S 901 Build/LRX22G) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/53.0.1639.337 Mobile Safari/533.0",
"android|Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G920L Build/MMB29K) AppleWebKit/537.33 (KHTML, like Gecko) Chrome/47.0.2380.276 Mobile Safari/533.7",
"android|Mozilla/5.0 (Linux; U; Android 4.4; SAMSUNG GT-I9404N Build/KOT49H) AppleWebKit/535.29 (KHTML, like Gecko) Chrome/48.0.3373.278 Mobile Safari/534.1",
"android|Mozilla/5.0 (Linux; Android 7.1; Nexus 8 Build/NME91E) AppleWebKit/534.45 (KHTML, like Gecko) Chrome/52.0.2765.138 Mobile Safari/600.9",
"android|Mozilla/5.0 (Linux; U; Android 7.1.1; Xperia Build/NDE63X) AppleWebKit/601.31 (KHTML, like Gecko) Chrome/52.0.1234.332 Mobile Safari/602.6",
"android|Mozilla/5.0 (Android; Android 5.1.1; MOTOROLA MOTO XT1570 MOTO X STYLE Build/LPH223) AppleWebKit/536.20 (KHTML, like Gecko) Chrome/48.0.3820.133 Mobile Safari/537.9",
"android|Mozilla/5.0 (Linux; U; Android 4.3.1; SAMSUNG SGH-N085A Build/JSS15J) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/49.0.1325.367 Mobile Safari/603.3",
"android|Mozilla/5.0 (Linux; Android 4.4; GT-I9506V Build/KOT49H) AppleWebKit/534.34 (KHTML, like Gecko) Chrome/53.0.3340.260 Mobile Safari/601.0",
"android|Mozilla/5.0 (Linux; U; Android 4.4; Nexus_S_4G Build/GRJ22) AppleWebKit/534.25 (KHTML, like Gecko) Chrome/49.0.2138.209 Mobile Safari/534.8",
"android|Mozilla/5.0 (Linux; Android 4.4.1; XT1044 Build/[KXB20.9|KXC21.5]) AppleWebKit/601.12 (KHTML, like Gecko) Chrome/54.0.3974.316 Mobile Safari/536.2",
"android|Mozilla/5.0 (Android; Android 5.0; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/535.3 (KHTML, like Gecko) Chrome/55.0.3918.375 Mobile Safari/601.2",
"android|Mozilla/5.0 (Linux; U; Android 5.0.1; SM-G430 Build/LRX22G) AppleWebKit/601.32 (KHTML, like Gecko) Chrome/53.0.3508.229 Mobile Safari/536.9",
"android|Mozilla/5.0 (Android; Android 5.0; HTC [M8|M9|M8 Pro Build/LRX22G) AppleWebKit/537.24 (KHTML, like Gecko) Chrome/54.0.3763.257 Mobile Safari/603.9",
"android|Mozilla/5.0 (Android; Android 4.4; Nexus 10 Build/KOT49H) AppleWebKit/601.1 (KHTML, like Gecko) Chrome/52.0.2811.186 Mobile Safari/603.4",
"android|Mozilla/5.0 (Android; Android 7.1; Xperia V Build/NDE63X) AppleWebKit/601.36 (KHTML, like Gecko) Chrome/55.0.3359.315 Mobile Safari/603.4",
"android|Mozilla/5.0 (Linux; U; Android 5.1; SM-G925FQ Build/LRX22G) AppleWebKit/601.24 (KHTML, like Gecko) Chrome/49.0.1646.236 Mobile Safari/600.6",
"android|Mozilla/5.0 (Linux; Android 4.4.4; GT-I9400I Build/KOT49H) AppleWebKit/601.8 (KHTML, like Gecko) Chrome/50.0.1924.248 Mobile Safari/601.3",
"android|Mozilla/5.0 (Linux; Android 7.1.1; LG-H900 Build/NRD90C) AppleWebKit/601.4 (KHTML, like Gecko) Chrome/47.0.2140.354 Mobile Safari/601.8",
"android|Mozilla/5.0 (Linux; Android 7.1.1; Pixel XL Build/NRD90M) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/52.0.1007.352 Mobile Safari/602.9",
"android|Mozilla/5.0 (Android; Android 4.4.4; LG-F500K Build/KOT49H) AppleWebKit/600.9 (KHTML, like Gecko) Chrome/50.0.2282.333 Mobile Safari/602.7",
"android|Mozilla/5.0 (Linux; Android 5.1.1; MOTO X PLAY XT1562 Build/LPC23) AppleWebKit/600.39 (KHTML, like Gecko) Chrome/47.0.2121.152 Mobile Safari/600.1",
"android|Mozilla/5.0 (Linux; Android 5.0.2; Lenovo A7000-a Build/LRX21M;) AppleWebKit/601.4 (KHTML, like Gecko) Chrome/54.0.1179.257 Mobile Safari/533.3",
"android|Mozilla/5.0 (Linux; U; Android 5.1; Nexus 9 Build/LMY48B) AppleWebKit/537.40 (KHTML, like Gecko) Chrome/54.0.1014.359 Mobile Safari/603.7",
"android|Mozilla/5.0 (Android; Android 5.0.1; LG-D718 Build/LRX22G) AppleWebKit/601.31 (KHTML, like Gecko) Chrome/52.0.3767.366 Mobile Safari/602.5",
"android|Mozilla/5.0 (Android; Android 5.0.2; SAMSUNG SM-G430 Build/LRX22C) AppleWebKit/533.13 (KHTML, like Gecko) Chrome/53.0.3683.262 Mobile Safari/534.9",
"android|Mozilla/5.0 (Linux; Android 7.1; Xperia V Build/NDE63X) AppleWebKit/601.43 (KHTML, like Gecko) Chrome/54.0.2903.103 Mobile Safari/534.0",
"android|Mozilla/5.0 (Linux; Android 4.4.1; SAMSUNG SM-G900H Build/KOT49H) AppleWebKit/603.12 (KHTML, like Gecko) Chrome/53.0.2711.374 Mobile Safari/534.7",
"android|Mozilla/5.0 (Linux; U; Android 7.0; SAMSUNG GT-I9100 Build/KTU84P) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/52.0.3975.390 Mobile Safari/603.1",
"android|Mozilla/5.0 (Linux; Android 4.4.4; SAMSUNG SM-N8010 Build/JZO54K) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/48.0.1993.154 Mobile Safari/600.9",
"android|Mozilla/5.0 (Linux; Android 4.3.1; Nokia 3110 Build/IMM76D) AppleWebKit/603.37 (KHTML, like Gecko) Chrome/55.0.2201.147 Mobile Safari/536.8",
"android|Mozilla/5.0 (Linux; Android 5.1; Nexus 6 Build/LRX22C) AppleWebKit/602.4 (KHTML, like Gecko) Chrome/53.0.2749.332 Mobile Safari/601.1",
"android|Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-A700 Build/LRX22G) AppleWebKit/603.30 (KHTML, like Gecko) Chrome/55.0.3181.364 Mobile Safari/603.6",
"android|Mozilla/5.0 (Android; Android 7.1.1; Pixel C Build/NME91E) AppleWebKit/600.40 (KHTML, like Gecko) Chrome/55.0.2622.240 Mobile Safari/602.3",
"android|Mozilla/5.0 (Linux; U; Android 7.0; Xperia V Build/NDE63X) AppleWebKit/600.15 (KHTML, like Gecko) Chrome/55.0.2495.153 Mobile Safari/534.0",
"android|Mozilla/5.0 (Linux; Android 7.1; LG-H910 Build/NRD90C) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/48.0.1072.270 Mobile Safari/537.7",
"android|Mozilla/5.0 (Android; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/601.1 (KHTML, like Gecko) Chrome/47.0.2715.143 Mobile Safari/534.7",
"android|Mozilla/5.0 (Linux; Android 5.1; MOTO E XT1021 Build/LPD23) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/55.0.3836.222 Mobile Safari/537.9",
"android|Mozilla/5.0 (Linux; Android 4.4.1; SAMSUNG SM-G900T Build/KOT49H) AppleWebKit/601.42 (KHTML, like Gecko) Chrome/54.0.2961.250 Mobile Safari/536.8",
"android|Mozilla/5.0 (Linux; Android 7.0; Xperia V Build/NDE63X) AppleWebKit/600.44 (KHTML, like Gecko) Chrome/53.0.3276.109 Mobile Safari/603.9",
"android|Mozilla/5.0 (Linux; Android 5.0.2; LG-D727 Build/LRX22G) AppleWebKit/602.39 (KHTML, like Gecko) Chrome/55.0.1021.240 Mobile Safari/537.2",
"android|Mozilla/5.0 (Android; Android 5.1; SM-G920S Build/LRX22G) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/52.0.3877.319 Mobile Safari/602.1",
"android|Mozilla/5.0 (Android; Android 5.0.2; HTC M8|M9|M8 Pro Build/LRX22G) AppleWebKit/537.41 (KHTML, like Gecko) Chrome/51.0.3833.224 Mobile Safari/533.3",
"android|Mozilla/5.0 (Linux; U; Android 5.1.1; MOTOROLA XT1021 Build/LXB22) AppleWebKit/533.29 (KHTML, like Gecko) Chrome/50.0.2483.251 Mobile Safari/601.8",
"android|Mozilla/5.0 (Linux; Android 5.1; MOTO X PLAY XT1562 Build/LPC23) AppleWebKit/600.1 (KHTML, like Gecko) Chrome/54.0.1985.202 Mobile Safari/600.7",
"android|Mozilla/5.0 (Linux; U; Android 5.1.1; SM-G920FQ Build/LRX22G) AppleWebKit/533.27 (KHTML, like Gecko) Chrome/55.0.1162.216 Mobile Safari/602.9",
"android|Mozilla/5.0 (Android; Android 5.0.1; SM-A700T Build/LMY47X) AppleWebKit/537.34 (KHTML, like Gecko) Chrome/49.0.2710.223 Mobile Safari/600.6",
"android|Mozilla/5.0 (Linux; U; Android 4.3.1; SM-G310I Build/JLS36C) AppleWebKit/534.42 (KHTML, like Gecko) Chrome/47.0.1023.134 Mobile Safari/601.6",
"android|Mozilla/5.0 (Android; Android 7.0; Xperia V Build/NDE63X) AppleWebKit/602.4 (KHTML, like Gecko) Chrome/54.0.1352.269 Mobile Safari/534.2",
"android|Mozilla/5.0 (Linux; U; Android 5.0.2; SM-G440 Build/LRX22C) AppleWebKit/603.38 (KHTML, like Gecko) Chrome/52.0.1136.254 Mobile Safari/600.8",
"android|Mozilla/5.0 (Linux; U; Android 5.1; MOTO E XT1021 Build/LPH223) AppleWebKit/534.44 (KHTML, like Gecko) Chrome/53.0.1891.215 Mobile Safari/535.8",
"android|Mozilla/5.0 (Linux; U; Android 4.4; LG Optimus G Build/KRT16M) AppleWebKit/535.41 (KHTML, like Gecko) Chrome/54.0.3524.337 Mobile Safari/601.3",
"android|Mozilla/5.0 (Linux; U; Android 6.0; HTC One_M8 Build/MRA58K) AppleWebKit/533.5 (KHTML, like Gecko) Chrome/53.0.2424.297 Mobile Safari/600.1",
"android|Mozilla/5.0 (Linux; Android 5.0.1; Lenovo A7000-a Build/LRX21M;) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/49.0.2645.302 Mobile Safari/534.6",
"android|Mozilla/5.0 (Linux; U; Android 4.4.1; Lenovo P781 Build/JRO03C) AppleWebKit/535.47 (KHTML, like Gecko) Chrome/53.0.3929.197 Mobile Safari/603.5",
"android|Mozilla/5.0 (Linux; Android 7.0; LG-H920 Build/NRD90C) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/54.0.2474.261 Mobile Safari/601.1",
"android|Mozilla/5.0 (Android; Android 5.0; LG-D722 Build/LRX22G) AppleWebKit/600.2 (KHTML, like Gecko) Chrome/55.0.2275.143 Mobile Safari/602.2",
"android|Mozilla/5.0 (Linux; U; Android 6.0.1; SM-G928I Build/MMB29K) AppleWebKit/602.37 (KHTML, like Gecko) Chrome/49.0.2276.245 Mobile Safari/535.1",
])
headers = {'Accept-Language':'vi,en-US;q=0.9,en;q=0.8',
            'Referer':'https://app.golike.net/',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':"Windows",
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-site',
            'T' : 'VFZSamQwOUVSVEpQVkVFd1RrRTlQUT09',
            'User-Agent':User_Agent,
            "Authorization" : file,
            'Content-Type':'application/json;charset=utf-8'            
}

url1 = 'https://gateway.golike.net/api/users/me'
checkurl1 = ses.get(url1,headers=headers).json()
    #user
if checkurl1['status']== 200 :
        print('ĐĂNG NHẬP THÀNH CÔNG')
        time.sleep(3)
        os.system('cls' if os.name== 'nt' else 'clear')
        print(Fore.BLUE+'1.TOOL GOLIKE MOBILE')
        choose = int(input(Fore.WHITE+'\n\n\n\n\nNHAP LUA CHON : '))
        if choose == 1 :
            os.system('cls' if os.name== 'nt' else 'clear')
            tprint("NHAT","rnd-xlarge")
            print(Fore.RED+'\t\tTOOL BY NHATTOOL')
            print('ZALO : 0386358592')
            os.system('cls' if os.name== 'nt' else 'clear')
            tprint("NHAT","rnd-xlarge")
            print(Fore.RED+'\t\tTOOL BY NHATTOOL')
            print('ZALO : 0386358592')
            ses.headers.update(headers)
            username = checkurl1['data']['username']
            coin = checkurl1['data']['coin']
            user_id = checkurl1['data']['id']
            print('________________________________________________________')
            print(Fore.GREEN+'[+] USERNAME : '+Fore.YELLOW+username)
            print(Fore.GREEN+'[+] TIỀN : '+Fore.YELLOW+str(coin))
            print(Fore.RED+'_________________________________________________________')
            LIST()
            choose = int(input(Fore.WHITE+'\n\n\n\n\nNHẬP LỰA CHỌN : '))
            if choose==1:
                 os.system('cls' if os.name== 'nt' else 'clear')
                 TIKTOKINFO()
            elif choose==2:
                os.system('cls' if os.name== 'nt' else 'clear')
                print(Fore.RED+'[*]SỬ DỤNG PROXY (Y/N)')
                choose = str(input(Fore.WHITE+'\n\n\n\n\nNHẬP LỰA CHỌN : '))
                if(choose=='Y' or choose=='y'):
                    os.system('cls' if os.name== 'nt' else 'clear')
                    proxyy = {
                        'http':'http://pfqttemn-rotate:3e4xo8ax3r0i@p.webshare.io:80',
                        'https':'http://pfqttemn-rotate:3e4xo8ax3r0i@p.webshare.io:80',
                    }
                elif(choose=='N' or choose=='n'):
                    os.system('cls' if os.name== 'nt' else 'clear')
                    proxyy= {}
                ip = requests.get('https://api.ipify.org?format=json',proxies=proxyy).json()
                print(Fore.RED+'IP CUA BAN : '+Fore.GREEN+str(ip['ip']))
                TWITTER()
            elif choose == 3:
                os.system('cls' if os.name== 'nt' else 'clear')
                print(Fore.RED+'[*]SU DUNG PROXY (Y/N)')
                choose = str(input(Fore.WHITE+'\n\n\n\n\nNHAP LUA CHON : '))
                if(choose=='Y' or choose=='y'):
                    os.system('cls' if os.name== 'nt' else 'clear')
                    proxyy = {
                        'http':'http://pfqttemn-rotate:3e4xo8ax3r0i@p.webshare.io:80',
                        'https':'http://pfqttemn-rotate:3e4xo8ax3r0i@p.webshare.io:80',
                    }
                elif(choose=='N' or choose=='n'):
                    os.system('cls' if os.name== 'nt' else 'clear')
                    proxyy= {}
                ip = requests.get('https://api.ipify.org?format=json',proxies=proxyy).json()
                print(Fore.RED+'IP CUA BAN : '+Fore.GREEN+str(ip['ip']))
                INSTAGRAM()
            elif choose == 4:
                os.system('cls' if os.name== 'nt' else 'clear')
                print(Fore.RED+'[*]SU DUNG PROXY (Y/N)')
                choose = str(input(Fore.WHITE+'\n\n\n\n\nNHAP LUA CHON : '))
                if(choose=='Y' or choose=='y'):
                    os.system('cls' if os.name== 'nt' else 'clear')
                    proxyy = {
                        'http':'http://pfqttemn-rotate:3e4xo8ax3r0i@p.webshare.io:80',
                        'https':'http://pfqttemn-rotate:3e4xo8ax3r0i@p.webshare.io:80',
                    }
                elif(choose=='N' or choose=='n'):
                    os.system('cls' if os.name== 'nt' else 'clear')
                    proxyy= {}
                ip = requests.get('https://api.ipify.org?format=json',proxies=proxyy).json()
                print(Fore.RED+'IP CUA BAN : '+Fore.GREEN+str(ip['ip']))
                LINKEDIN()
else:
    print(Fore.RED+'DANG NHAP THAT BAI')
    os.remove('user.txt')










    
