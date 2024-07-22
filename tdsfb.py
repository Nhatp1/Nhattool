import os, sys, requests, re, json, time
from time import sleep
from random import randint as rd
from bs4 import BeautifulSoup as bs
os.system("clear")
tk = input("Nhập Username TDS: ")
mk = input("Nhập Password TDS: ")
cookiefb = input("Nhập Cookie FB: ")
dl = int(input("Nhập Time Delay: "))
os.system("clear")
headersfb= {
'Host': 'mbasic.facebook.com',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Linux; Android 5.1; HUAWEI LUA-U22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
'cookie': cookiefb
}
headers={
'Host': 'traodoisub.com',
'content-length': '40',
'accept': 'application/json, text/javascript, */*; q=0.01',
'x-requested-with': 'XMLHttpRequest',
'user-agent': 'Mozilla/5.0 (Linux; Android 5.1; HUAWEI LUA-U22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'origin': 'https://traodoisub.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': 'https://traodoisub.com/',
'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3'
}
data = {
'username': tk,
'password': mk
}
log = requests.post("https://traodoisub.com/scr/login.php", data=data, headers=headers)
a=log.headers['Set-Cookie']
b = re.findall('_cfduid.*?;', a)
c = re.findall('PHPSESSID.*?;', a)
s = b[0]
ss = c[0].replace(';', '')
ck = s + ss
headerst = {
'Host': 'traodoisub.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Linux; Android 5.1; HUAWEI LUA-U22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'referer': 'https://traodoisub.com/',
'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3',
'cookie': ck
}
headersn = {
'Host': 'traodoisub.com',
'content-length': '18',
'accept': '*/*',
'x-requested-with': 'XMLHttpRequest',
'user-agent': 'Mozilla/5.0 (Linux; Android 5.1; HUAWEI LUA-U22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3',
'cookie': ck
}
headersl = {
'Host': 'traodoisub.com',
'content-length': '19',
'accept': '*/*',
'x-requested-with': 'XMLHttpRequest',
'user-agent': 'Mozilla/5.0 (Linux; Android 5.1; HUAWEI LUA-U22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3',
'cookie': ck
}
headerscx = {
'Host': 'traodoisub.com',
'content-length': '30',
'accept': '*/*',
'x-requested-with': 'XMLHttpRequest',
'user-agent': 'Mozilla/5.0 (Linux; Android 5.1; HUAWEI LUA-U22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3',
'cookie': ck
}
h = requests.get("https://traodoisub.com/", headers=headerst)
print("-"*60)
print("Tool TDS V1".center(60))
print("Admin: NHATTOOL".center(60))
print("Telegram: t.me/Nekozuke1".center(60))
print("-"*60)
access = requests.get("https://traodoisub.com/view/setting/", headers=headerst)
soup = bs(access.text, "html.parser")
t = soup.find_all("input", value=True)
access_token=[]
for t in t:
	access=t["value"]
	access_token.append(access)
access_token = access_token[2]
api_user = "https://traodoisub.com/api/?fields=profile&access_token="+access_token
api_user = requests.get(api_user)
print("[Xin Chào: " + api_user.json()['user'] + "]")
print("[ID Đang Chạy:  " + api_user.json()['idrun'] + "]")
print("[Số dư hiện tại: "+ api_user.json()['xu'] + " xu]")
print("-"*60)
print("Bắt Đầu Vào Tool".center(60))
print("-"*60)
print("Vui lòng chọn !")
print("[1] Follow\n[2] Page\n[3] Like\n[4] Cảm Xúc\n[5] Random All")
chon =  int(input("Vui lòng nhập số tương ứng: "))
if chon == 1:
	while True:
		while True:
			try:
				api_job = "https://traodoisub.com/api/?fields=follow&access_token="+access_token
				api_job = requests.get(api_job)
				id = api_job.json()[0]['id']
			except:
				pass
			link = "https://mbasic.facebook.com/profile.php?id="+str(id)
			fb = requests.get(link, headers=headersfb)
			soup = bs(fb.text, "html.parser")
			seach = soup.find_all("a", href=True)
			for seach in seach:
				link_sub = seach["href"]
				if "/a/subscribe.php?" in link_sub:
					requests.get("https://mbasic.facebook.com"+link_sub, headers=headersfb)
					nt = requests.post("https://traodoisub.com/ex/follow/nhantien.php", data='id='+str(id), headers=headersn)
					h = requests.get("https://traodoisub.com/", headers=headerst)
					soup = bs(h.text, "html.parser")
					t2 = soup.find("strong", id="soduchinh")
					if nt.text == 2 or nt.text == "2":
						print("."*60)
						print("Job: Follow".center(60))
						print("[Link:",link+"]")
						print("[ID:",id+"]")
						print("[TDS] => [Thành Công] => [+600 xu]")
						print("[Số dư] => " + "[" + t2.text + " xu]")
					else:
						print("[TDS] => [Thất Bại]")
					print("."*60)
					for x in range(dl, -1, -1):
						print("Time:", [x], end="            \r")
						sleep(1)
					break
				else:
					pass
if chon == 2:
	while True:
		while True:
			try:
				api_job = "https://traodoisub.com/api/?fields=page&access_token="+access_token
				api_job = requests.get(api_job)
				id = api_job.json()[0]['id']
			except:
				pass
			link = "https://mbasic.facebook.com/profile.php?id="+str(id)
			fb = requests.get(link, headers=headersfb)
			soup = bs(fb.text, "html.parser")
			seach = soup.find_all("a", href=True)
			for seach in seach:
				link_sub = seach["href"]
				if "/a/profile.php?" in link_sub:
					requests.get("https://mbasic.facebook.com"+link_sub, headers=headersfb)
					nt = requests.post("https://traodoisub.com/ex/fanpage/nhantien.php", data='id='+str(id), headers=headersn)
					h = requests.get("https://traodoisub.com/", headers=headerst)
					soup = bs(h.text, "html.parser")
					t2 = soup.find("strong", id="soduchinh")
					if nt.text == 2 or nt.text == "2":
						print("."*60)
						print("Job: Page".center(60))
						print("[Link:",link+"]")
						print("[ID:",id+"]")
						print("[TDS] => [Thành Công] => [+600 xu]")
						print("[Số dư] => " + "[" + t2.text + " xu]")
					else:
						print("[TDS] => [Thất Bại]")
					print("."*60)
					for x in range(dl, -1, -1):
						print("Time:", [x], end="            \r")
						sleep(1)
					break
				else:
					pass
if chon == 3:
	while True:
		while True:
			try:
				api_job = "https://traodoisub.com/api/?fields=like&access_token="+access_token
				api_job = requests.get(api_job)
				id = api_job.json()[0]['id']
			except:
				pass
			link = "https://mbasic.facebook.com/"+str(id)
			fb = requests.get(link, headers=headersfb)
			soupp = bs(fb.text, "html.parser")
			seachh = soupp.find_all("meta", content=True)
			for seachh in seachh:
				link_full = seachh['content']
				if link_full.find("https://www.facebook.com/story.php") != -1 or link_full.find("https://www.facebook.com/photo.php") != -1:
					#print(link_full)
					fb=requests.get(link_full, headers=headersfb)
					soup = bs(fb.text, "html.parser")
					seach = soup.find_all("a", href=True)
					for seach in seach:
						link_sub = seach["href"]
						if "/a/like.php?" in link_sub:
							requests.get("https://mbasic.facebook.com"+link_sub, headers=headersfb)
							nt = requests.post("https://traodoisub.com/ex/like/nhantien.php", data='id='+str(id), headers=headersl)
							h = requests.get("https://traodoisub.com/", headers=headerst)
							soup = bs(h.text, "html.parser")
							t2 = soup.find("strong", id="soduchinh")
							if nt.text == 2 or nt.text == "2":
								print("."*60)
								print(str("Job: Like").center(60))
								print("[Link:",link+"]")
								print("[ID:",id+"]")
								print("[TDS] => [Thành Công] => [+200 xu]")
								print("[Số dư] => " + "[" + t2.text + " xu]")
							else:
								print("[TDS] => [Thất Bại]")
							print("."*60)
							for x in range(dl, -1, -1):
								print("Time:", [x], end="            \r")
								sleep(1)
							break
						else:
							pass
				else:
					pass
if chon == 4:
	while True:
		while True:
			try:
				api_job = requests.get("https://traodoisub.com/api/?fields=reaction&access_token="+access_token)
				id = api_job.json()[0]['id']
				#print(id)
				type = api_job.json()[0]['type']
			except:
				pass
			link = "https://mbasic.facebook.com/"+str(id)
			fb = requests.get(link, headers=headersfb)
			soupp = bs(fb.text, "html.parser")
			seachh = soupp.find_all("meta", content=True)
			for seachh in seachh:
				link_full = seachh['content']
				if link_full.find("https://www.facebook.com/story.php") != -1 or link_full.find("https://www.facebook.com/photo.php") != -1:
					#print(link_full)
					fb=requests.get(link_full, headers=headersfb)
					soup = bs(fb.text, "html.parser")
					seach = soup.find_all("a", href=True)
					for seach in seach:
						link_sub = seach["href"]
						if "/reactions/picker/?" in link_sub:
							cx = requests.get("https://mbasic.facebook.com"+link_sub, headers=headersfb)
							souppp = bs(cx.text, "html.parser")
							cxxx = souppp.find_all("a", href=True)
							listcx = []
							for cxx in cxxx:
								lcx = cxx["href"]
								listcx.append(lcx)
							if "LOVE" in type:
								link_cx = listcx[2]
							if "CARE" in type:
								link_cx = listcx[3]
							if "HAHA" in type:
								link_cx = listcx[4]
							if "WOW" in type:
								link_cx = listcx[5]
							if "SAD" in type:
								link_cx = listcx[6]
							if "ANGRY" in type:
								link_cx = listcx[7]
							#print(link_cx)
							cxpost = requests.get("https://mbasic.facebook.com"+link_cx, headers=headersfb)
							nt = requests.post("https://traodoisub.com/ex/reaction/nhantien.php", data='id='+str(id)+'&loaicx='+type, headers=headerscx)
							h = requests.get("https://traodoisub.com/", headers=headerst)
							soup = bs(h.text, "html.parser")
							t2 = soup.find("strong", id="soduchinh")
							if nt.text == 2 or nt.text == "2":
								print("."*60)
								print(str("Job: "+type).center(60))
								print("[Link:",link+"]")
								print("[ID:",id+"]")
								print("[TDS] => [Thành Công] => [+400 xu]")
								print("[Số dư] => " + "[" + t2.text + " xu]")
							else:
								print("[TDS] => [Thất Bại]")
							print("."*60)
							for x in range(dl, -1, -1):
								print("Time:", [x], end="            \r")
								sleep(1)
							break
if chon == 5:
	while True:
		while True:
			k = rd(1, 4)
			#print(k, '\n')
			if k == 1:
				try:
					api_job = "https://traodoisub.com/api/?fields=follow&access_token="+access_token
					api_job = requests.get(api_job)
					id = api_job.json()[0]['id']
				except:
					pass
				link = "https://mbasic.facebook.com/profile.php?id="+str(id)
				fb = requests.get(link, headers=headersfb)
				soup = bs(fb.text, "html.parser")
				seach = soup.find_all("a", href=True)
				for seach in seach:
					link_sub = seach["href"]
					if "/a/subscribe.php?" in link_sub:
						requests.get("https://mbasic.facebook.com"+link_sub, headers=headersfb)
						nt = requests.post("https://traodoisub.com/ex/follow/nhantien.php", data='id='+str(id), headers=headersn)
						h = requests.get("https://traodoisub.com/", headers=headerst)
						soup = bs(h.text, "html.parser")
						t2 = soup.find("strong", id="soduchinh")
						if nt.text == 2 or nt.text == "2":
							print("."*60)
							print("Job: Follow".center(60))
							print("[Link:",link+"]")
							print("[ID:",id+"]")
							print("[TDS] => [Thành Công] => [+600 xu]")
							print("[Số dư] => " + "[" + t2.text + " xu]")
						else:
							print("."*60)
							print("Job: Follow".center(60))
							print("[Link:",link+"]")
							print("[ID:",id+"]")
							print("[TDS] => [Thất Bại]")
						print("."*60)
						for x in range(dl, -1, -1):
							print("Time:", [x], end="            \r")
							sleep(1)
						break
					else:
						pass
			if k == 2:
				try:
					api_job = "https://traodoisub.com/api/?fields=page&access_token="+access_token
					api_job = requests.get(api_job)
					id = api_job.json()[0]['id']
				except:
					pass
				link = "https://mbasic.facebook.com/profile.php?id="+str(id)
				fb = requests.get(link, headers=headersfb)
				soup = bs(fb.text, "html.parser")
				seach = soup.find_all("a", href=True)
				for seach in seach:
					link_sub = seach["href"]
					if "/a/profile.php?" in link_sub:
						requests.get("https://mbasic.facebook.com"+link_sub, headers=headersfb)
						nt = requests.post("https://traodoisub.com/ex/fanpage/nhantien.php", data='id='+str(id), headers=headersn)
						h = requests.get("https://traodoisub.com/", headers=headerst)
						soup = bs(h.text, "html.parser")
						t2 = soup.find("strong", id="soduchinh")
						if nt.text == 2 or nt.text == "2":
							print("."*60)
							print("Job: Page".center(60))
							print("[Link:",link+"]")
							print("[ID:",id+"]")
							print("[TDS] => [Thành Công] => [+600 xu]")
							print("[Số dư] => " + "[" + t2.text + " xu]")
						else:
							print("."*60)
							print("Job: Page".center(60))
							print("[Link:",link+"]")
							print("[ID:",id+"]")
							print("[TDS] => [Thất Bại]")
						print("."*60)
						for x in range(dl, -1, -1):
							print("Time:", [x], end="            \r")
							sleep(1)
						break
				else:
					pass
			if k == 3:
				try:
					api_job = "https://traodoisub.com/api/?fields=like&access_token="+access_token
					api_job = requests.get(api_job)
					id = api_job.json()[0]['id']
				except:
					pass
				link = "https://mbasic.facebook.com/"+str(id)
				fb = requests.get(link, headers=headersfb)
				soupp = bs(fb.text, "html.parser")
				seachh = soupp.find_all("meta", content=True)
				for seachh in seachh:
					link_full = seachh['content']
					if link_full.find("https://www.facebook.com/story.php") != -1 or link_full.find("https://www.facebook.com/photo.php") != -1:
						#print(link_full)
						fb=requests.get(link_full, headers=headersfb)
						soup = bs(fb.text, "html.parser")
						seach = soup.find_all("a", href=True)
						for seach in seach:
							link_sub = seach["href"]
							if "/a/like.php?" in link_sub:
								requests.get("https://mbasic.facebook.com"+link_sub, headers=headersfb)
								nt = requests.post("https://traodoisub.com/ex/like/nhantien.php", data='id='+str(id), headers=headersl)
								h = requests.get("https://traodoisub.com/", headers=headerst)
								soup = bs(h.text, "html.parser")
								t2 = soup.find("strong", id="soduchinh")
								if nt.text == 2 or nt.text == "2":
									print("."*60)
									print(str("Job: Like").center(60))
									print("[Link:",link+"]")
									print("[ID:",id+"]")
									print("[TDS] => [Thành Công] => [+200 xu]")
									print("[Số dư] => " + "[" + t2.text + " xu]")
								else:
									print("."*60)
									print(str("Job: Like").center(60))
									print("[Link:",link+"]")
									print("[ID:",id+"]")
									print("[TDS] => [Thất Bại]")
								print("."*60)
								for x in range(dl, -1, -1):
									print("Time:", [x], end="            \r")
									sleep(1)
								break
							else:
								pass
					else:
						pass
			if k == 4:
				try:
					api_job = requests.get("https://traodoisub.com/api/?fields=reaction&access_token="+access_token)
					id = api_job.json()[0]['id']
					#print(id)
					type = api_job.json()[0]['type']
				except:
					pass
				link = "https://mbasic.facebook.com/"+str(id)
				fb = requests.get(link, headers=headersfb)
				soupp = bs(fb.text, "html.parser")
				seachh = soupp.find_all("meta", content=True)
				for seachh in seachh:
					link_full = seachh['content']
					if link_full.find("https://www.facebook.com/story.php") != -1 or link_full.find("https://www.facebook.com/photo.php") != -1:
						#print(link_full)
						fb=requests.get(link_full, headers=headersfb)
						soup = bs(fb.text, "html.parser")
						seach = soup.find_all("a", href=True)
						for seach in seach:
							link_sub = seach["href"]
							if "/reactions/picker/?" in link_sub:
								cx = requests.get("https://mbasic.facebook.com"+link_sub, headers=headersfb)
								souppp = bs(cx.text, "html.parser")
								cxxx = souppp.find_all("a", href=True)
								listcx = []
								for cxx in cxxx:
									lcx = cxx["href"]
									listcx.append(lcx)
								if "LOVE" in type:
									link_cx = listcx[2]
								if "CARE" in type:
									link_cx = listcx[3]
								if "HAHA" in type:
									link_cx = listcx[4]
								if "WOW" in type:
									link_cx = listcx[5]
								if "SAD" in type:
									link_cx = listcx[6]
								if "ANGRY" in type:
									link_cx = listcx[7]
								#print(link_cx)
								cxpost = requests.get("https://mbasic.facebook.com"+link_cx, headers=headersfb)
								nt = requests.post("https://traodoisub.com/ex/reaction/nhantien.php", data='id='+str(id)+'&loaicx='+type, headers=headerscx)
								h = requests.get("https://traodoisub.com/", headers=headerst)
								soup = bs(h.text, "html.parser")
								t2 = soup.find("strong", id="soduchinh")
								if nt.text == 2 or nt.text == "2":
									print("."*60)
									print(str("Job: "+type).center(60))
									print("[Link:",link+"]")
									print("[ID:",id+"]")
									print("[TDS] => [Thành Công] => [+400 xu]")
									print("[Số dư] => " + "[" + t2.text + " xu]")
								else:
									print("."*60)
									print(str("Job: "+type).center(60))
									print("[Link:",link+"]")
									print("[ID:",id+"]")
									print("[TDS] => [Thất Bại]")
								print("."*60)
								for x in range(dl, -1, -1):
									print("Time:", [x], end="            \r")
									sleep(1)
								break
							else:
								pass
					else:
						pass
