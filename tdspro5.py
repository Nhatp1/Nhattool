#==Màu==#
do = "\033[1;91m"
xanhbien = "\033[1;36m"
vang = "\033[0;33m"
hong = "\033[1;35m"
xanhduong = "\033[1;20m"
xanhla = "\033[1;32m"
xanh="\033[1;32m"
cam="\033[1;33m"
blue="\033[1;20m"
lam="\033[1;20m"
tim="\033[1;20m"
syan="\033[1;36m"
xnhac= "\033[1;96m"
den="\033[1;90m"
luc="\033[1;92m"
xduong="\033[1;94m"
trang="\033[1;97m"
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;20m"
lam = "\033[1;36m"
tim = "\033[35m"
hong = "\033[1;95m"
# Đánh dấu bản quyền
edit = red + "[" + vang + "⟨⟩" + red + "] " + trang + "➩ "
edit1 = red + "[" + luc + "✓" + red + "] " + trang + "➩ "
#####[THƯ VIỆN]#######
import os, sys
try:
	import requests, json, re, random
except:
	os.system("pip install requests")
	import requests, json, re, random
from random import randint
from time import sleep
from pystyle import Colors, Colorate
from pystyle import *
from datetime import datetime
import uuid
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from pystyle import Write,Colors
from bs4 import BeautifulSoup
import socket
from datetime import datetime
System.Clear()
System.Title("nhattool")
System.Size(140, 40)                           
banner = r"""
  \x1b[38;5;207m╔══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╗
  \033[1;36m ███╗   ██╗██╗  ██╗ █████╗ ████████╗    ████████╗ ██████╗  ██████╗ ██╗     
  \033[1;36m ████╗  ██║██║  ██║██╔══██╗╚══██╔══╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
  \033[1;36m ██╔██╗ ██║███████║███████║   ██║          ██║   ██║   ██║██║   ██║██║     
  \033[1;36m ██║╚██╗██║██╔══██║██╔══██║   ██║          ██║   ██║   ██║██║   ██║██║     
  \033[1;36m ██║ ╚████║██║  ██║██║  ██║   ██║          ██║   ╚██████╔╝╚██████╔╝███████╗
  \033[1;36m ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝          ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
        \x1b[38;5;226m CHÚC MỌI NGƯỜI MỘT NGÀY VUI VẼ!!
        \x1b[38;5;207mBOX ZALO : \x1b[38;5;46mhttps://zalo.me/g/ozebne540
        \x1b[38;5;207m ADMIN : \x1b[38;5;46m NHẬT TOOL
        \x1b[38;5;207m MUA KEY VIP LIÊN HỆ ZALO: 0386358592 (500đ/1day) \x1b[38;5;46m
        \x1b[38;5;207m BOT SPAM SMS: https://t.me/sharebotvip \x1b[38;5;207m
   \x1b[38;5;207m╚══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╝

"""
######[DEF AUTO]########
def echo(text):
	for i in range(len(text)):
		sys.stdout.write(text[i])
		sys.stdout.flush()
		sleep(0.0001)
	print()
def frive(frive):
   echo(trang + "───"*frive)
def clear():
	if os.name=='nt':os.system('cls')
	else:os.system('clear')
def idelay(delaymin, delaymax):
	delay = randint(delaymin, delaymax)
	for demtg in range(int(delay), -1, -1):
		print(trang+"["+xanh+"HDT-TOOL"+trang+"] ["+xanh+"L         "+trang+"] ["+xanh+str(demtg)+trang+"]",end="\r")
		sleep(0.1)
		print(trang+"["+cam+"NHẬT-TOOL"+trang+"] ["+cam+"L"+xanh+"O        "+trang+"] ["+cam+str(demtg)+trang+"]",end="\r")
		sleep(0.1)
		print(trang+"["+blue+"NHẬT-TOOL"+trang+"] ["+blue+"L"+xanh+"O"+cam+"A       "+trang+"] ["+blue+str(demtg)+trang+"]",end="\r")
		sleep(0.1)
		print(trang+"["+lam+"NHẬT-TOOL"+trang+"] ["+lam+"L"+xanh+"O"+cam+"A"+blue+"D      "+trang+"] ["+lam+str(demtg)+trang+"]",end="\r")
		sleep(0.1)
		print(trang+"["+tim+"NHẬT-TOOL"+trang+"] ["+tim+"L"+xanh+"O"+cam+"A"+blue+"D"+lam+"I     "+trang+"] ["+tim+str(demtg)+trang+"]",end="\r")
		sleep(0.1)
		print(trang+"["+xnhac+"NHẬT-TOOL"+trang+"] ["+xnhac+"L"+xanh+"O"+cam+"A"+blue+"D"+lam+"I"+tim+"N    "+trang+"] ["+xnhac+str(demtg)+trang+"]",end="\r")
		sleep(0.1)
		print(trang+"["+den+"NHẬT-TOOL"+trang+"] ["+den+"L"+xanh+"O"+cam+"A"+blue+"D"+lam+"I"+tim+"N"+xnhac+"G   "+trang+"] ["+den+str(demtg)+trang+"]",end="\r")
		sleep(0.1)
		print(trang+"["+do+"NHẬT-TOOL"+trang+"] ["+do+"L"+xanh+"O"+cam+"A"+blue+"D"+lam+"I"+tim+"N"+xnhac+"G.  "+trang+"] ["+do+str(demtg)+trang+"]",end="\r")
		sleep(0.2)
		print(trang+"["+vang+"NHẬT-TOOL"+trang+"] ["+vang+"L"+xanh+"O"+cam+"A"+blue+"D"+lam+"I"+tim+"N"+xnhac+"G.. "+trang+"] ["+vang+str(demtg)+trang+"]",end="\r")
		sleep(0.3)
		print(trang+"["+vang+"NHẬT-TOOL"+trang+"] ["+vang+"L"+xanh+"O"+cam+"A"+blue+"D"+lam+"I"+tim+"N"+xnhac+"G..."+trang+"] ["+vang+str(demtg)+trang+"]",end="\r")
	print(trang+" ĐANG LÀM JOB TDS",end="\r")
def LoadJob(delay):
	for demtg in range(int(delay), -1, -1):
		print(trang+"Load Job Tiếp Theo Sau: "+str(demtg), end="\r")
		sleep(0.8)
def jsoncookie(cookies):
    result = {}
    try:
        for i in cookies.split(';'):
            result.update({i.split('=')[0]: i.split('=')[1]})
        return result
    except(Exception,):
        for i in cookies.split('; '):
            result.update({i.split('=')[0]: i.split('=')[1]})
        return result

def GETID(cookie):
	head = {'authority': 'www.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','viewport-width': '1366',}
	url = requests.get("https://www.facebook.com/me", headers=head, cookies=cookie).url
	get = requests.get(url, headers=head, cookies=cookie).text
	fb = get.split('["DTSGInitialData",[],{"token":"')[1].split('"')[0]
	jazoest = get.split('jazoest=')[1].split('"')[0]
	lsd = get.split('["LSD",[],{"token":"')[1].split('"')[0]
	data = {
	'fb_dtsg' :fb,
	'jazoest' :jazoest,
	'variables' : '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
	'doc_id' : '5300338636681652'
	}
	get = requests.post("https://www.facebook.com/api/graphql/", headers=head, cookies=cookie, data=data).json()
	return get['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
class Facebook:
	def __init__ (self, cookie) -> None:
		self.cookie = jsoncookie(cookie)
		self.head = {'authority': 'www.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','viewport-width': '1366',}
		self.user_id = cookie.split("i_user=")[1].split(";")[0]
		url = requests.get("https://www.facebook.com/me", headers=self.head, cookies=self.cookie).url
		get = requests.get(url, headers=self.head, cookies=self.cookie).text
		self.fb = get.split('["DTSGInitialData",[],{"token":"')[1].split('"')[0]
		self.jazoest = get.split('jazoest=')[1].split('"')[0]
		self.lsd = get.split('["LSD",[],{"token":"')[1].split('"')[0]
	def infocookie(self):
		get = requests.get("https://www.facebook.com/me", headers=self.head, cookies=self.cookie).text
		try:
			name = get.split('<title>')[1].split('</title>')[0]
			return {"success":200,"name":name, "id":self.user_id}
		except:
			return {"error":200}
	def CamXuc(self, id, type):
		url = requests.get("https://www.facebook.com/"+id, headers=self.head, cookies=self.cookie).url
		get = requests.get(url, headers=self.head, cookies=self.cookie).text
		feedback = "ZmV"+get.split('"feedback_id":"ZmV')[1].split('"')[0]
		trackingdata = get.split('trackingdata":{"id":"')[1].split('"')[0]
		if type == "LIKE":id = "1635855486666999"
		if type == "LOVE":id = "1678524932434102"
		if type == "CARE":id = "613557422527858"
		if type == "HAHA":id = "115940658764963"
		if type == "WOW":id = "478547315650144"
		if type == "SAD":id = "908563459236466"
		if type == "ANGRY":id = "444813342392137"
		data = {"av" : self.user_id,"__user" : self.user_id,"__a" : "1","__dyn" : "7AzHJ16U9ob8ng5K8G6EjBWo2nDwAxu13wFwhUngS3q32360CEboG4E762S1DwUx60GE3Qwb-q7oc81xoswMwto88422y11xmfz83WwgEcEhwGxu782lwv89kbxS2218wc61axe3S7Udo5qfK0zEkxe2GewGwkUtxGm2SUbElxm3y11xfxmu3W3y261eBx_y88E3VBwJCwLyES0Io88cA0z8c84qifxe3u364UrwFg662S269wkoqw","__csr" : "g9Q9OOhthsIBFPQYFzQyOtvFsy4TFsyRozTsGGHN9k8W8ObECQD4QParJ4Iz8yp6A_AKlAKUKjuh5BBBVfUx3Z7AFABGl5LvKmK9yCF8xeaVAex14gGAXQ8DyKV8hyE9F8XCAyQECqcg94EgzUdGKmELCCCxycxuUfEKbwwwjEhG2JojgcobE8VEdoc8pxa9zoWfwgoC9wUw9i1awdW0G84K49UaUhwtoiwdu1sw8KUdE11o0cVU0Iq03vm00Id80qKG3-0tW0hq02Kd0ee07qi2E0hmwoU0j_w0CCw1We0Hpo1ao0x69w1jO3u0W817UgwfC2a","__req" : "l","__hs" : "19438.HYP:comet_pkg.2.1..2.1","dpr" : "2","__ccg" : "GOOD","__rev" : "1007150578","__s" : "ajoats:subbv5:fs4kwq","__hsi" : "7213197347307427052","__comet_req" : "15","fb_dtsg" : self.fb,"jazoest" : "25611","lsd" : self.lsd,"__aaid" : "710580363942837","__spin_r" : "1007150578","__spin_b" : "trunk","__spin_t" : "1679453381","fb_api_caller_class" : "RelayModern","fb_api_req_friendly_name" : "CometUFIFeedbackReactMutation",'variables' : '{"input":{"attribution_id_v2":"CometGroupPermalinkRoot.react,comet.group.permalink,via_cold_start,1679453388936,459905,2361831622,","feedback_id":"'+feedback+'","feedback_reaction_id":"'+id+'","feedback_source":"OBJECT","is_tracking_encrypted":true,"tracking":["'+trackingdata+'"],"session_id":"12845410-1d81-40bd-95d0-ccd042ba90eb","actor_id":"'+self.user_id+'","client_mutation_id":"3"},"useDefaultActor":false,"scale":2}','server_timestamps' : 'true',"doc_id" : "5703418209680126"}
		get = requests.post("https://www.facebook.com/api/graphql/", headers=self.head, cookies=self.cookie, data=data)
		return get
	def likepage(self, id):
		url = requests.get("https://www.facebook.com/"+id, headers=self.head, cookies=self.cookie).url
		head = {"Host":"id.atpsoftware.vn","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://id.atpsoftware.vn","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","referer":"https://id.atpsoftware.vn/"}
		get = requests.get("https://id.atpsoftware.vn/", headers=head)
		ck = get.cookies.get_dict()
		get = requests.post("https://id.atpsoftware.vn/", headers=head, cookies=ck, data="linkCheckUid="+url).text
		getid = get.split('padding: 10px 100px 0px 100px;text-transform: uppercase;font-size: 16px;font-weight: 700;outline: none;position: relative;transition: all .3s ease-out;z-index: 0;text-align: center;overflow: hidden;">')[1].split('<')[0]
		if "1000" in getid:
			idpro = getid
			get = requests.get(url, headers=self.head, cookies=self.cookie).text
			id = get.split('delegate_page":{"id":"')[1].split('"')[0]
			data = {"av" : self.user_id,"__user" : self.user_id,"__a" : "1","__dyn" : "7AzHxqU5a5Q1ryUbFuC0BVU98nwgUao5-ewSwMwNw9G2S7o762S1DwUx60p-0LVEtwMw65xO0FE886C11xmfz83WwgEcEhwGxu782lwv89kbxS2218wc61uwZx-3m1mzXw8W58jwGzEaE766FobrwKxm5o7G4-5pUfEe872m7-8wywfCm2Sq2-azo2NwwwOg2cwMwhF8-4UdUcojxK2B0oobo8oC1hxG","__csr" : "g94hqPtB5JRh9lQAAAAQZimKRluh99CF4_WmZDmLqrB8Z29oKVGKQmbKrBBWBgCqmrx24WVUux6Ex0Ex2aBz9UC4U4O3C15xCdwsUhxa2WbwhUeE4Kby-0lfwam0q-00oQGA0haySJiKHg8UhwgogwEw","__req" : "o","__hs" : "19422.HYP:comet_pkg.2.0.0.2.1","dpr" : "2","__ccg" : "GOOD","__rev" : "1007055511","__s" : "adfco7:2ievkh:x4z7bk","__hsi" : "7207283130392575182","__comet_req" : "15","fb_dtsg" : self.fb,"jazoest" : self.jazoest,"lsd" : self.lsd,"__aaid" : "710580363942837","__spin_r" : "1007055511","__spin_b" : "trunk","__spin_t" : "1678076370","fb_api_caller_class" : "RelayModern","fb_api_req_friendly_name" : "CometProfilePlusLikeMutation",'variables' : '{"input":{"page_id":"'+id+'","source":null,"actor_id":"'+self.user_id+'","client_mutation_id":"1"},"scale":2}',"server_timestamps" : "true","doc_id" : "4867271226642619"}
			get = requests.post("https://www.facebook.com/api/graphql/", headers=self.head, data=data, cookies=self.cookie)
		else:
			data = {'av':self.user_id,'__user':self.user_id,'__a':'1','__dyn':'7AzHxqU5a5Q1ryaxG4VuC0BVU98nwgU765QdwSwAyU8EW0CEboG4E762S1DwUx60gu0BU2_CxS320om78bbwto88422y11xmfz83WwgEcHzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK0zEkxe2GewGwkUtxGm2SUbElxm3y11xfxmu3W2i4U72m7-8wywfCm2Sq2-azo2NwwwOg2cwMwhF8-4UdUcojxK2B0oobo8o','__csr':'g8JNc9n2tWr5W4til-I_On8J9rshlR8nZFiELH_Hnij4JfOJLOGiLoxLBlGRuZaGF4CZddQ4L_JfCiDKWVryuiqqFAcy8x6CBtqJkF8ZVExauAbgOtLAG5FUGFptxqfxi4Hzaz8CQ2SaxC9xCi48Wqqq11g8EaoS9g9U4m224oG68sGucx68wyg6G22mfxa4Xxq7EKbwi82LwNxu48c814EC2K3O5U-2WEhCxO1EwioeUiwiE6e3HwTw18C02k-0exw0deO0jV05Swe20bTw5_w1zF03I202po6e07Co0K6Zlw0jjo0E-0qW08ug8UhBw21e0fLw5Ww9K0Z86u','__req':'o','__hs':'19363.HYP:comet_pkg.2.1.0.2.1','dpr':'2','__ccg':'GOOD','__rev':'1006793331','__s':'v80lqo:poayhk:qxdcmk','__hsi':'7185553908092803679','__comet_req':'15','fb_dtsg':self.fb,'jazoest':self.jazoest,'lsd':'V64c7kKr5hAtzX2IIDgKp8','__aaid':'775223720487728','__spin_r':'1006793331','__spin_b':'trunk','__spin_t':'1673017141','fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometPageLikeCommitMutation','variables':'{"input":{"attribution_id_v2":"CometSinglePageHomeRoot.react,comet.page,via_cold_start,1673017144344,576155,250100865708545,","is_tracking_encrypted":true,"page_id":"'+id+'","source":"unknown","tracking":[],"actor_id":"'+self.user_id+'","client_mutation_id":"1"},"isAdminView":false}','server_timestamps':'true','doc_id':'5491200487600992',}
			get = requests.post('https://www.facebook.com/api/graphql/',headers=self.head, cookies=self.cookie, data=data)
		return get
	def group(self, id):
		data = {'av':self.user_id,'__user':self.user_id,'__a':'1','__dyn':'7AzHJ16U9ob8ng5K8G6EjBWo2nDwAxu13wsongS3q2ibwyzE2qwJyEiwsobo6u3y4o2Gwfi0LVEtwMw65xO321Rwwwg8a8465o-cwfG12wOKdwGxu782lwv89kbxS2218wc61axe3S1lwlE-U2exi4UaEW2G1jxS6FobrwKxm5oe8464-5pUfEe88o4Wm7-8xmcwfCm2CVEbUGdG1Fwh888cA0z8c84qifxe3u364UrwFg662S26','__csr':'gadNAIYllhsKOE8IpidFPhcIx34Omy9-O9OO8hZ_8-kAymHGAybJqGlvmWl7nWBWJ7GqaXHz7GFe9oy_KBl7h6h4KVah94QeKVHACDyryqKdF5GuXXBCgNpbJ5jjGm8yQEWrCixl6xWuiih5yo-8wAy84mq4poN0Vzbxe16whAufgO5U8UKi4Eyu4EjwGK78527o8411wgocU5u1MwSwFyU8Uf8igaElw8e9xK2GewNgy5o5m1nDwLwrokm16www8G03cy0arw0Zyw0aaC0mG0eJzl8ow2Jw6tw44w4uzo045W1UgSeg0z-07X81-E0cNo0By1Wwi8fE0lYw2h81a8gw9u','__req':'k','__hs':'19363.HYP:comet_pkg.2.1.0.2.1','dpr':'2','__ccg':'EXCELLENT','__rev':'1006794317','__s':'gtlvj8:fxbzro:f2kk19','__hsi':'7185658639628512803','__comet_req':'15','fb_dtsg':self.fb,'jazoest':self.jazoest,'lsd':'gKT7R4dxIBjI4wUDUP5ivT','__aaid':'1576489885859472','__spin_r':'1006794317','__spin_b':'trunk','__spin_t':'1673041526','fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'GroupCometJoinForumMutation','variables':'{"feedType":"DISCUSSION","groupID":"'+id+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1673041528761,114928,2361831622,","group_id":"'+id+'","group_share_tracking_params":{"app_id":"2220391788200892","exp_id":"null","is_from_share":false},"actor_id":"'+self.user_id+'","client_mutation_id":"1"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":2,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true,"__relay_internal__pv__GlobalPanelEnabledrelayprovider":false}','server_timestamps':'true','doc_id':'5853134681430324','fb_api_analytics_tags':'["qpl_active_flow_ids=431626709"]',}
		join = requests.post('https://www.facebook.com/api/graphql/',headers=self.head, cookies=self.cookie, data=data)
		return join
	def follow(self, id):
		data = {"av" : self.user_id,"__user" : self.user_id,"__a" : "1","__dyn" : "7AzHJ16UW5Eb8ng5K8G6EjBWobVo66u2i5U4e2C17xt3odEnz8K361twYwJyEiwsobo6u3y4o2Gwfi0LVEtwMw65xO2OU7m2210wEwgolzUO0-E4a3a4oaEnxO0Bo7O2l2Utwwwi831wiEjwZx-3m1mzXw8W58jwGzE8FU5e7oqBwJK2W5olwUwgojUlDw-wUwxwjFovUy2a0SEuBwJCwLyES0Io88cA0z8c84qifxe3u364UrwFg662S269wkoqw","__csr" : "grl2YAW3lsBl4neziQkJhtlXNlFTsWEPsAGlkGjq8gygPqAmKoIBaQBLSWHQlpHpiHQG9QFeYyhWyFVq-iKKi8x2fKiFFFKWzpkiGDihVayCcQngjmmuFbzpUOWgpzEvy8WuueVkVUjKUC4WxmbyebzVE9oyt0xwDK4GxKUF6xOu4UWUu-EaosK7E4S3eEfE8Q58kxaHw_y8WUK9Bwfi8wCwiUhwTxqawam2G5Uc8yewFxW2t0s89Umgowue7awRwg8c80dp80Ka06980mow0b6aE0C648iO04vw10-0b9Bwa20TU0bn4A0zA0gO02oe2a2ibQ0kW03nq02cm0tGu0hm0_A08cg0Q210w2383IwSw","__req" : "l","__hs" : "19438.HYP:comet_pkg.2.1..2.1","dpr" : "2","__ccg" : "GOOD","__rev" : "1007155328","__s" : "x9k4g6:qvnrn2:gabyl2","__hsi" : "7213309158787601147","__comet_req" : "15","fb_dtsg" : self.fb,"jazoest" : "25533","lsd" : self.jazoest,"__aaid" : "2192309537797609","__spin_r" : "1007155328","__spin_b" : "trunk","__spin_t" : "1679479414","fb_api_caller_class" : "RelayModern","fb_api_req_friendly_name" : "CometUserFollowMutation",'variables' : '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1679479423097,686412,190055527696468,","is_tracking_encrypted":false,"subscribe_location":"PROFILE","subscribee_id":"'+id+'","tracking":null,"actor_id":"'+self.user_id+'","client_mutation_id":"1"},"scale":2}',"server_timestamps" : "true","doc_id" : "5967051660053260"}
		fl = requests.post('https://www.facebook.com/api/graphql/',headers=self.head, cookies=self.cookie, data=data)
		return fl
	def cmt(self, id, nd):
		data={'fb_dtsg': self.fb, 'jazoest': self.jazoest,'comment_text': nd, 'photo': '(binary)', 'post': 'Bình luận'}
		url='https://upload.facebook.com/_mupload_/ufi/mbasic/advanced/?ids&photosrc=advanced_composer_comment&lpwfwef&ft_ent_identifier='+str(id)
		r=requests.post(url, headers=self.head, cookies=self.cookie, data=data)
		return r
	def share(self, id_post):
		data = {'fb_dtsg': self.fb,'jazoest': self.jazoest,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'useCometFeedToFeedReshare_FeedToFeedMutation','variables': '{"input":{"attachments":{"link":{"share_scrape_data":"{\\"share_type\\":22,\\"share_params\\":['+id_post+']}"}},"audiences":{"undirected":{"privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}}},"is_tracking_encrypted":true,"navigation_data":{"attribution_id_v2":"CometSinglePostRoot.react,comet.post.single,via_cold_start,1667131156143,908005,,"},"source":"www","tracking":["AZXOdDS2v_ZDJSDytbos1u5RXGugxb3OhZDbZyYCHeZ2BrvYu3bItkld1wPFdskAq-5K88-e9701dA_oMoXT0zuUhJnMZXXU6BO_MxONTSqjlEw7bJ-4xD31Gu2ZbEGkwVVHqgAXzioO3EdQK8VTlpDFlm3pCa66yMRxMhj_nyJD7teGP1rNsPo0y1ORuIt9TjhYgJZbimPC3FHaEjTsPPexCorotwXgF3W6IejdjsEIKGUud10LKHuJ3RQk2I7u6NNj6itxPCmOoLACwncbr4yDn1Z-D5TKZF_yxqYCDPv6Yh2zVJHHGOYP6noPYYFcLbHfgIeXq50FqOrd2kLwkeavk5wVA3a9Ig9PXPXfmB_JfA"],"actor_id":"'+self.user_id+'","client_mutation_id":"26"},"renderLocation":"homepage_stream","scale":1,"privacySelectorRenderLocation":"COMET_STREAM","useDefaultActor":false,"displayCommentsContextEnableComment":null,"feedLocation":"NEWSFEED","displayCommentsContextIsAdPreview":null,"displayCommentsContextIsAggregatedShare":null,"displayCommentsContextIsStorySet":null,"displayCommentsFeedbackContext":null,"feedbackSource":1,"focusCommentID":null,"UFI2CommentsProvider_commentsKey":"CometModernHomeFeedQuery"}','server_timestamps': 'true','doc_id': '5624054241022832',}
		response = requests.post('https://www.facebook.com/api/graphql/', headers=self.head, cookies=self.cookie, data=data)
		return response
class TDS:
	def __init__ (self, token) -> None:
		self.token = token
		self.head = {
		"Host":"traodoisub.com",
		"user-agent":"Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
		"accept":"*/*",
		"x-requested-with":"mark.via.gp",
		"sec-fetch-site":"same-origin",
		"sec-fetch-mode":"cors",
		"sec-fetch-dest":"empty",
		"referer":"https://traodoisub.com/ex/like/",
		"accept-encoding":"gzip, deflate",
		"accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
		}
	def login(self):
		get = requests.get("https://traodoisub.com/api/?fields=profile&access_token="+self.token, headers=self.head).json()
		if "success" in get:
			self.xu = get["data"]["xu"]
			self.user = get["data"]["user"]
			return {"xu":self.xu, "user":self.user}
		else:
			return {"error":{"code":190}}
	def Cauhinh(self, id):
		get = requests.get("https://traodoisub.com/api/?fields=run&id="+id+"&access_token="+self.token, headers=self.head).json()
		if "success" in get:
			return {"success":200}
		else:
			return {"error":200}
	def GetJob(self, type):
		get = requests.get("https://traodoisub.com/api/?fields="+type+"&access_token="+self.token, headers=self.head).json()
		try:
			if get["error"] == "Thao tác quá nhanh vui lòng chậm lại":
				print(do+"TẠM THỜI HẾT NHIỆM VỤ "+type+"                         ".upper(), end="             \r")
			else:
				print(do+"TẠM THỜI HẾT NHIỆM VỤ "+type+"                         ".upper(), end="             \r")
		except:
			return get
	def NhanJob(self, id, type):
		get = requests.get("https://traodoisub.com/api/coin/?type="+type+"&id="+id+"&access_token="+self.token, headers=self.head).json()
		if "success" in get:
			return {"success":200, "xu":get["data"]["xu"], "msg":get["data"]["msg"].replace("+", "").replace(" Xu", "")}
		else:
			return {"error":200}
def NhapTds():
	while True:
		if os.path.exists('TokenTds.txt'):
			with open('TokenTds.txt', 'r') as f:
				list = json.loads(f.read())
			frive(20)
			print(edit+'NHẬP '+trang+'['+vang+'1'+trang+']'+luc+' SỬ DỤNG TOKEN TDS '+vang+list["user"].upper())
			print(edit+'NHẬP '+trang+'['+vang+'2'+trang+']'+luc+' NHẬP TOKEN TDS MỚi')
			chon = input(edit+'VUI LÒNG NHẬP LỰA CHỌN: '+trang)
			if chon == '1':
				frive(20)
				return list
			elif chon == '2':
				os.remove('TokenTds.txt'); frive(20)
			else:
				print(do+'LỰA CHỌN KHÔNG XÁC ĐỊNH.'); frive(20); continue
		if not os.path.exists('TokenTds.txt'):
			while True:
				frive(20)
				tk = input(edit+"NHẬP TOKEN TDS: "+trang)
				login = TDS(tk).login()
				if "error" in login:
					print(do+"TOKEN TDS KO CHÍNH XÁC")
					continue
				else:
					user = login["user"]
					with open('TokenTds.txt', 'w') as f:
						json.dump({"user":user, "token":tk}, f)
					break
			try:
				with open('TokenTds.txt', 'r') as f:
					list = json.loads(f.read())
				return list
				break
			except:
				os.remove('TokenTds.txt'); frive(20)
def success(dem, id, type, msg, xu):
	uid = id.split('_')[1] if '_' in id else id
	time=datetime.now().strftime("%H:%M:%S")
	echo(f"{luc}[{vang}{dem}{luc}]{trang} | {xnhac}{time}{trang} | {luc}{type}{trang} | {xnhac}ID: {id}{trang} | +{luc}{msg}{trang} | {luc}{str(format(int(xu), ','))} Xu")
def error(id, type, dem):
	time=datetime.now().strftime("%H:%M:%S")
	uid = id.split('_')[1] if '_' in id else id
	print(f'{do}[{vang}{dem}{do}] | {time} | {type} | {uid} | ERROR',end = '\r');sleep(1); print('                                                        ', end = '\r')
def NhapCookieFb():
	list = []
	z = 0
	frive(20)
	print(f"{trang}[{red}LƯU Ý{trang}] {luc}XÓA DẤU CÁCH Ở CUỐI COOKIE ĐỂ TRÁNH BỊ LỖI\n")
	cookie = input(f'{edit}NHẬP COOKIE FACEBOOK {trang}: ')
	getid = GETID(jsoncookie(cookie))
	for i in getid:
		z += 1
		id = i["profile"]["id"]
		name = i["profile"]["name"]
		o = input(f'{edit} [{z}] FACEBOOK: {vang}{name}(Y/N): ')
		if o.upper() == "Y":list.append(cookie+"; i_user="+id+";")
	frive(20)
	return list
def chongblock(delaybl):
	for i in range(delaybl, -1, -1):
		print(f'Đang hoạt động chống block sẽ chạy lại sau {i} giây  ',end = '\r');sleep(1); print('                                                        ', end = '\r')
	
def LuuCookie():
	while True:
		if os.path.exists('Cookie-Page-Fb-tds.txt'):
			print(edit+'NHẬP '+trang+'['+vang+'1'+trang+']'+luc+' SỬ DỤNG COOKIE PAGE FACEBOOK ĐÃ LƯU')
			print(edit+'NHẬP '+trang+'['+vang+'2'+trang+']'+luc+' NHẬP COOKIE FACEBOOK MỚI')
			chon = input(edit+'VUI LÒNG NHẬP LỰA CHỌN: '+trang)
			if chon == '1':
				with open('Cookie-Page-Fb-tds.txt', 'r') as f:
					list = json.loads(f.read())
					break
			elif chon == '2':
				os.remove('Cookie-Page-Fb-tds.txt'); frive(20)
			else:
				print(do+'LỰA CHỌN KHÔNG XÁC ĐỊNh.'); frive(20); continue
		if not os.path.exists('Cookie-Page-Fb-tds.txt'):
			list = NhapCookieFb()
			with open('Cookie-Page-Fb-tds.txt', 'w') as f:
				json.dump(list, f)
			break
	return list
def main():
	clear()
	echo(banner)
	get = NhapTds()
	xu = requests.get("https://traodoisub.com/api/?fields=profile&access_token="+get["token"]).json()["data"]["xu"]
	listck = LuuCookie()
	clear()
	print(banner)
	frive(20)
	print(edit+vang+"USER: "+get["user"].upper())
	print(edit+xnhac+"COIN: "+str(format(int(xu), ','))+" XU")
	frive(20)
	print(edit+"NHẬP "+vang+"["+trang+"1"+vang+"]"+luc+" CHẠY JOB LIKE")
	print(edit+"NHẬP "+vang+"["+trang+"2"+vang+"]"+luc+" CHẠY JOB LIKE 2")
	print(edit+"NHẬP "+vang+"["+trang+"3"+vang+"]"+luc+" CHẠY JOB CẢM XÚC")
	print(edit+"NHẬP "+vang+"["+trang+"4"+vang+"]"+luc+" CHẠY JOB SHARE")
	print(edit+"NHẬP "+vang+"["+trang+"5"+vang+"]"+luc+" CHẠY JOB CMT")
	print(edit+"NHẬP "+vang+"["+trang+"6"+vang+"]"+luc+" CHẠY JOB JOIN GROUP")
	print(edit+"NHẬP "+vang+"["+trang+"7"+vang+"]"+luc+" CHẠY JOB LIKE PAGE")
	print(edit+trang+"BẠN CÓ THỂ CHỌN (1+2+3)")
	frive(20)
	nhap = input(edit+"NHẬP LỰA CHỌN: ")
	listnv = []
	if "+" in nhap:
		nhap = nhap.replace("+", "")
	elif "-" in nhap:
		nhap = nhap.replace("-", "")
	elif "," in nhap:
		nhap = nhap.replace(",", "")
	elif "_" in nhap:
		nhap = nhap.replace("_", "")
	elif "." in nhap:
		nhap = nhap.replace(".", "")
	listnv.append(nhap)
	delaymin = int(input(edit+'NHẬP DELAY MIN: '+trang))
	delaymax = int(input(edit+'NHẬP DELAY MAX: '+trang))
	print(edit+'SAU ____ '+luc+'NHIỆM VỤ THÌ KÍCH HOẠT CHỐNG BLOCK.',end='\r')
	nvblock = int(input(edit+'SAU '+trang))
	print(f'{edit}SAU {nvblock} NHIỆM VỤ NGHỈ NGƠI ____ {luc}GIÂY       ',end='\r')
	delaybl = int(input(f'{edit}SAU {nvblock} NHIỆM VỤ NGHỈ NGƠI '+trang))
	if str(len(listck)) == "1":jjjj="0"
	else:
		doinick = int(input(edit+'SAU BAO NHIÊU NHIỆM VỤ THÌ ĐỔI NICK: '+trang))
	dem = 0
	demck = 0
	while True:
		if len(listck) == 0:
			frive(20)
			print(do+'ĐÃ XOÁ TẤT CẢ COOKIE, VUI LÒNG NHẬP LẠI')
			listck = NhapCookieFb()
			with open('Cookie-Page-Fb-tds.txt', 'w') as f:
				json.dump(listck, f)
		with open('Cookie-Page-Fb-tds.txt', 'w') as f:
			json.dump(listck, f)
		for cookie in listck:
			demck += 1
			try:
				nhiemvu = listnv[0]
				idck = cookie.split("i_user=")[1].split(";")[0]
				face = Facebook(cookie)
				aaa = face.infocookie()
				if "success" in aaa:
					Tds = TDS(get["token"])
					cauhinh = Tds.Cauhinh(idck)
					if "success" in cauhinh:
						frive(20)
						print(luc+'             PAGE ID: '+vang+idck+trang+' <|> '+luc+'NAME PAGE: '+vang+aaa['name']+'              ')
						frive(20)
					else:
						print(do+"PAGE: "+vang+idck+do+" CHƯA ADD VÔ TDS")
						listck.remove(cookie)
						continue
				else:
					print(do+"COOKIE FB: "+vang+idck+do+" BỊ LOGOUT RỒI")
					listck.remove(cookie)
					continue
				spam = 0
				error_like_a = 0
				error_like_b = 0
				error_cx = 0
				error_share = 0
				error_cmt = 0
				error_group = 0
				while True:
					if spam == 1:break
					if nhiemvu == "":
						print(do+"PAGE "+vang+aaa["name"]+do+" ĐÃ BỊ BLOCK TẤT CẢ TƯƠNG TÁC")
						listck.remove(cookie)
						spam = 1
						break
					if "1" in nhiemvu:
						try:
							listnvlike = Tds.GetJob("like")
							print(xnhac+" ĐÃ TÌM THẤY "+vang+str(len(listnvlike))+xnhac+" NHIỆM VỤ LIKE", end="                     \r"); sleep(1)
							for D in listnvlike:
								id = D["id"]
								if "_" in id:idlike = id.split("_")[1]
								else:idlike = id
								try:
									like = face.CamXuc(idlike, "LIKE")
									nhan = Tds.NhanJob(id, "LIKE")
									if "success" in nhan:
										dem += 1
										error_like_a = 0
										success(dem, id, "LIKE", nhan["msg"], nhan["xu"])
										if str(len(listck)) == "1":jjjj="0"
										else:
											if dem % doinick == 0:
												spam = 1
												break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											idelay(delaymin, delaymax)
									else:
										error_like_a += 1
										error(id, "LIKE", error_like_a)
										if error_like_a % 2 == 0: break
								except:
									error_like_a += 1
									error(id, "LIKE", error_like_a)
									if error_like_a % 2 == 0: break
							if error_like_a == 10:
								aaa = face.infocookie()
								if "error" in aaa:
									check = requests.get("https://graph.facebook.com/"+idck+"/picture?redirect=false").json()
									try:
										if str(check["data"]["height"]) == "50":
											print(do+"FACEBOOK "+vang+demck+do+" BỊ CP RỒI")
										else:
											print(do+"COOKIE "+vang+idck+do+" BỊ LOGOUT RỒI")
									except:
										print(do+"COOKIE "+vang+idck+do+" BỊ LOGOUT RỒI")
									listck.remove(cookie)
								else:
									print(do+"PAGE "+vang+aaa["name"]+do+" ĐÃ BỊ CHẶN LIKE")
									nhiemvu = nhiemvu.replace("1", "")
						except:print(end="\r")
					if "2" in nhiemvu:
						try:
							listnvlike = Tds.GetJob("likegiare")
							print(xnhac+" ĐÃ TÌM THẤY "+vang+str(len(listnvlike))+xnhac+" NHIỆM VỤ LIKE 2", end="                     \r"); sleep(1)
							for D in listnvlike:
								id = D["id"]
								if "_" in id:idlike = id.split("_")[1]
								else:idlike = id
								try:
									like = face.CamXuc(idlike, "LIKE")
									nhan = Tds.NhanJob(id, "LIKEGIARE")
									if "success" in nhan:
										dem += 1
										error_like_b = 0
										success(dem, id, "LIKE 2", nhan["msg"], nhan["xu"])
										if str(len(listck)) == "1":jjjj="0"
										else:
											if dem % doinick == 0:
												spam = 1
												break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											idelay(delaymin, delaymax)
									else:
										error_like_b += 1
										error(id, "LIKE 2", error_like_b)
										if error_like_b % 2 == 0: break
								except:
									error_like_b += 1
									error(id, "LIKE 2", error_like_b)
									if error_like_b % 2 == 0: break
							if error_like_b == 10:
								aaa = face.infocookie()
								if "error" in aaa:
									check = requests.get("https://graph.facebook.com/"+idck+"/picture?redirect=false").json()
									try:
										if str(check["data"]["height"]) == "50":
											print(do+"FACEBOOK "+vang+demck+do+" BỊ CP RỒI")
										else:
											print(do+"COOKIE "+vang+idck+do+" BỊ LOGOUT RỒI")
									except:
										print(do+"COOKIE "+vang+idck+do+" BỊ LOGOUT RỒI")
									listck.remove(cookie)
								else:
									print(do+"PAGE "+vang+aaa["name"]+do+" ĐÃ BỊ CHẶN LIKE")
									nhiemvu = nhiemvu.replace("2", "")
						except:print(end="\r")
					if "3" in nhiemvu:
						try:
							listnvcx = Tds.GetJob("reaction")
							print(xnhac+" ĐÃ TÌM THẤY "+vang+str(len(listnvcx))+xnhac+" NHIỆM VỤ REACTION", end="                     \r"); sleep(1)
							for D in listnvcx:
								id = D["id"]
								type = D["type"]
								if "_" in id:idlike = id.split("_")[1]
								else:idlike = id
								try:
									like = face.CamXuc(idlike, type)
									nhan = Tds.NhanJob(id, type)
									if "success" in nhan:
										dem += 1
										error_cx = 0
										success(dem, id, type, nhan["msg"], nhan["xu"])
										if str(len(listck)) == "1":jjjj="0"
										else:
											if dem % doinick == 0:
												spam = 1
												break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											idelay(delaymin, delaymax)
									else:
										error_cx += 1
										error(id, type, error_cx)
										if error_cx % 2 == 0: break
								except:
									error_cx += 1
									error(id, type, error_cx)
									if error_cx % 2 == 0: break
							if error_cx == 10:
								aaa = face.infocookie()
								if "error" in aaa:
									check = requests.get("https://graph.facebook.com/"+idck+"/picture?redirect=false").json()
									try:
										if str(check["data"]["height"]) == "50":
											print(do+"FACEBOOK "+vang+demck+do+" BỊ CP RỒI")
										else:
											print(do+"COOKIE "+vang+idck+do+" BỊ LOGOUT RỒI")
									except:
										print(do+"COOKIE "+vang+idck+do+" BỊ LOGOUT RỒI")
									listck.remove(cookie)
								else:
									print(do+"PAGE "+vang+aaa["name"]+do+" ĐÃ BỊ CHẶN TƯƠNG TÁC CẢM XÚC")
									nhiemvu = nhiemvu.replace("3", "")
						except:print(end="\r")
					if "4" in nhiemvu:
						try:
							listnvshare = Tds.GetJob("share")
							print(xnhac+" ĐÃ TÌM THẤY "+vang+str(len(listnvshare))+xnhac+" NHIỆM VỤ SHARE", end="                     \r"); sleep(1)
							for D in listnvshare:
								id = D["id"]
								if "_" in id:idshare = id.split("_")[1]
								else:idshare = id
								try:
									share = face.share(idshare)
									nhan = Tds.NhanJob(id, "SHARE")
									if "success" in nhan:
										dem += 1
										error_share = 0
										success(dem, id, "SHARE", nhan["msg"], nhan["xu"])
										if str(len(listck)) == "1":jjjj="0"
										else:
											if dem % doinick == 0:
												spam = 1
												break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											idelay(delaymin, delaymax)
									else:
										error_share += 1
										error(id, "SHARE", error_share)
										if error_share % 2 == 0: break
								except:
									error_share += 1
									error(id, "SHARE", error_share)
									if error_share % 2 == 0: break
							if error_share == 10:
								aaa = face.infocookie()
								if "error" in aaa:
									check = requests.get("https://graph.facebook.com/"+idck+"/picture?redirect=false").json()
									try:
										if str(check["data"]["height"]) == "50":
											print(do+"FACEBOOK "+vang+demck+do+" BỊ CP RỒI")
										else:
											print(do+"COOKIE "+vang+idck+do+" BỊ LOGOUT RỒI")
									except:
										print(do+"COOKIE "+vang+idck+do+" BỊ LOGOUT RỒI")
									listck.remove(cookie)
								else:
									print(do+"PAGE "+vang+aaa["name"]+do+" ĐÃ BỊ CHẶN SHARE BÀI")
									nhiemvu = nhiemvu.replace("4", "")
						except:print(end="\r")
					if "5" in nhiemvu:
						try:
							listnvcmt = Tds.GetJob("comment")
							print(xnhac+" ĐÃ TÌM THẤY "+vang+str(len(listnvcmt))+xnhac+" NHIỆM VỤ CMT", end="                     \r"); sleep(1)
							for D in listnvcmt:
								id = D["id"]
								msg = D["msg"]
								if "_" in id:idcmt = id.split("_")[1]
								else:idcmt = id
								try:
									cmt = face.cmt(idcmt, msg)
									nhan = Tds.NhanJob(id, "COMMENT")
									if "success" in nhan:
										dem += 1
										error_cmt = 0
										success(dem, id, "CMT", nhan["msg"], nhan["xu"])
										if str(len(listck)) == "1":jjjj="0"
										else:
											if dem % doinick == 0:
												spam = 1
												break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											idelay(delaymin, delaymax)
									else:
										error_cmt += 1
										error(id, "CMT", error_cmt)
										if error_cmt % 2 == 0: break
								except:
									error_cmt += 1
									error(id, "CMT", error_cmt)
									if error_cmt % 2 == 0: break
							if error_cmt == 10:
								aaa = face.infocookie()
								if "error" in aaa:
									check = requests.get("https://graph.facebook.com/"+idck+"/picture?redirect=false").json()
									try:
										if str(check["data"]["height"]) == "50":
											print(do+"FACEBOOK "+vang+demck+do+" BỊ CP RỒI")
										else:
											print(do+"COOKIE "+vang+idck+do+" BỊ LOGOUT RỒI")
									except:
										print(do+"COOKIE "+vang+idck+do+" BỊ LOGOUT RỒI")
									listck.remove(cookie)
								else:
									print(do+"PAGE "+vang+aaa["name"]+do+" ĐÃ BỊ CHẶN CMT")
									nhiemvu = nhiemvu.replace("5", "")
						except:print(end="\r")
					if "6" in nhiemvu:
						try:
							listnvgr = Tds.GetJob("group")
							print(xnhac+" ĐÃ TÌM THẤY "+vang+str(len(listnvgr))+xnhac+" NHIỆM VỤ GROUP", end="                     \r"); sleep(1)
							for D in listnvgr:
								id = D["id"]
								if "_" in id:idgr = id.split("_")[1]
								else:idgr = id
								try:
									gr = face.group(idgr)
									nhan = Tds.NhanJob(id, "GROUP")
									if "success" in nhan:
										dem += 1
										error_group = 0
										success(dem, id, "GROUP", nhan["msg"], nhan["xu"])
										if str(len(listck)) == "1":jjjj="0"
										else:
											if dem % doinick == 0:
												spam = 1
												break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											idelay(delaymin, delaymax)
									else:
										error_group += 1
										error(id, "GROUP", error_group)
										if error_group % 2 == 0: break
								except:
									error_group += 1
									error(id, "GROUP", error_group)
									if error_group % 2 == 0: break
							if error_group == 10:
								aaa = face.infocookie()
								if "error" in aaa:
									check = requests.get("https://graph.facebook.com/"+idck+"/picture?redirect=false").json()
									try:
										if str(check["data"]["height"]) == "50":
											print(do+"FACEBOOK "+vang+demck+do+" BỊ CP RỒI")
										else:
											print(do+"COOKIE "+vang+idck+do+" BỊ LOGOUT RỒI")
									except:
										print(do+"COOKIE "+vang+idck+do+" BỊ LOGOUT RỒI")
									listck.remove(cookie)
								else:
									print(do+"PAGE "+vang+aaa["name"]+do+" ĐÃ BỊ CHẶN JOIN GROUP")
									nhiemvu = nhiemvu.replace("6", "")
						except:print(end="\r")
					if "7" in nhiemvu:
						try:
							listnvpage = Tds.GetJob("page")
							print(xnhac+" ĐÃ TÌM THẤY "+vang+str(len(listnvpage))+xnhac+" NHIỆM VỤ LIKE PAGE", end="                     \r"); sleep(1)
							for D in listnvpage:
								id = D["id"]
								if "_" in id:idpage = id.split("_")[1]
								else:idpage = id
								try:
									page = face.likepage(idpage)
									nhan = Tds.NhanJob(id, "PAGE")
									if "success" in nhan:
										dem += 1
										error_group = 0
										success(dem, id, "PAGE", nhan["msg"], nhan["xu"])
										if str(len(listck)) == "1":jjjj="0"
										else:
											if dem % doinick == 0:
												spam = 1
												break
										if dem % nvblock == 0:
											chongblock(delaybl)
										else:
											idelay(delaymin, delaymax)
									else:
										error_page += 1
										error(id, "PAGE", error_page)
										if error_page % 2 == 0: break
								except:
									error_page += 1
									error(id, "PAGE", error_page)
									if error_page % 2 == 0: break
							if error_page == 10:
								aaa = face.infocookie()
								if "error" in aaa:
									check = requests.get("https://graph.facebook.com/"+idck+"/picture?redirect=false").json()
									try:
										if str(check["data"]["height"]) == "50":
											print(do+"FACEBOOK "+vang+demck+do+" BỊ CP RỒI")
										else:
											print(do+"COOKIE "+vang+idck+do+" BỊ LOGOUT RỒI")
									except:
										print(do+"COOKIE "+vang+idck+do+" BỊ LOGOUT RỒI")
									listck.remove(cookie)
								else:
									print(do+"PAGE "+vang+aaa["name"]+do+" ĐÃ BỊ CHẶN LIKE PAGE")
									nhiemvu = nhiemvu.replace("7", "")
						except:print(end="\r")
					LoadJob("10")
			except:
				print(do+"COOKIE THỨ "+vang+str(demck)+do+" DIE RỒI")
				listck.remove(cookie)
				os.remove('Cookie-Page-Fb-tds.txt')
main()
