import os,sys,json,datetime,requests,re
from time import sleep
from bs4 import BeautifulSoup as bs
from random import randint
os.system("clear")
print("Bản Quyền:NEKO TOOL")

print("___________________________________")
print("[1]=>[Gomlua]")
print("[2]=>[Nuôi Đa Luồng]")
print("[3]=>[AddFriends-Gợi Ý]")
print("[4]=>[Chấp Nhận Lời Mời Kết Bạn]")
print("[5]=>[Tương Tác Cảm Xúc]")
print("[6]=>[Spam Comments]")
print("[7]=[Tương Tác Cảm Xúc Có Cmt và Add Friends]")
print("[8]=[ TRAO ĐỔI SUB ]")
print("[9]=>[Tăng Like Free]")
print("___________________________________")
choose=input("Nhập 1 Số Để Tiếp Tục:")
os.system("clear")
v=0
p=0
red='\u001b[31;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
yellow='\u001b[33;1m'
reset='\u001b[0m'

if choose=="1":
  token=input("Nhập Token:")
  cookie=input("Nhập Cookie:")
  os.system("clear")
  print("Bản Quyền:NEKO TOOL")
  print("ZALO Group:https://zalo.me/g/yvkvew875")
  print("___________________________________")
  head_gl={
  'Host':'gomlua.com',
  'app_token':token,
  'User-Agent':'Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36',
  'Connection':'keep-alive'}
  head_fb={
  "Host":"mbasic.facebook.com",
  "cache-control":"max-age=0",
  "upgrade-insecure-requests":"1",
  "save-data":"on",
  "user-agent":"Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36",
  "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
  "sec-fetch-site":"cross-site",
  "sec-fetch-mode":"navigate",
  "sec-fetch-user":"?1",
  "sec-fetch-dest":"document",
  "accept-language":"vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
  "cookie":"datr=fG6mXx-LH4QuXprjw48ZoSdz;sb=fG6mX0PVfdd08UGNmOyDdCJ-;m_pixel_ratio=2;locale=vi_VN;fr=1GEqAQnEYB2sDWM0X.AWWJ4AJ06b33WGQ9T1TFbhhBx10.Bfpm58.hG.AAA.0.0.Bf1bT7.AWVVWj1WmXg;c_user=100059066334547;xs=20%3A2MYkJqLDhOP0Hg%3A2%3A1607841019%3A-1%3A-1;wd=360x688;x-referer=eyJyIjoiL21rdXIubW8uNTQiLCJoIjoiL21rdXIubW8uNTQiLCJzIjoibSJ9",}
  while True:
    #try:
      web=requests.get("https://gomlua.com/user/info?os=web", headers=head_gl)
      user=web.json()["data"]["username"]
      web1=requests.get("https://gomlua.com/cpi/listCampaignFacebook?os=web&type=like_post",headers=head_gl)
      link=web1.json()["data"]["list"][0]["campaign_url"]
      sửa=link.replace("www","mbasic")
      link_id=web1.json()["data"]["list"][0]["link_id"]
      type=web1.json()["data"]["list"][0]["react_type"]
      check=requests.get("https://gomlua.com/likeToken/checkLikeToken?os=web&link_id="+str(link_id),headers=head_gl)
      mg=check.json()["message"]
      if mg=="Thanh cong":
        print(sửa)
        web2=requests.get(url=sửa,headers=head_fb)
        tìm=re.findall('/reactions/picker/?.*?"',web2.text)
        if tìm==[]:
          print("Không thấy Nút Cảm xúc")
        else:
          bỏ =tìm[0].replace('"',"")
          bỏ_1=bỏ.replace("amp;","")
          web3=requests.get("https://mbasic.facebook.com"+bỏ_1,headers=head_fb)
          soup1=bs(web3.text,"html.parser")
          tìm1=soup1.find_all("a",href=True)
          cx=[]
          for o in tìm1:
            link_cx=o["href"]
            cx.append(link_cx)
          if type=="LIKE":
            m=cx[1]
          if type=="LOVE":
            m=cx[2]
          if type=="CARE":
            m=cx[3]
          if type=="HAHA":
            m=cx[4]
          if type=="WOW":
            m=cx[5]
          if type=="SAD":
            m=cx[6]
          if type=="ANGRY":
            m=cx[7]
          requests.get("https://mbasic.facebook.com"+m,headers=head_fb)
          sleep(5)
          nhận=requests.get(f"https://gomlua.com/likeToken/likeSuccess?os=web&link_id={str(link_id)}&like_count=1",headers=head_gl)
          success=nhận.json()["message"]
          h=datetime.datetime.now()
          p=h.strftime("%H:%M")
          print(p)
          print(sửa)
          print(success)
   # except:
      #print(red+"Lỗi Mạng"+reset,end=" \r")
if choose=="2":
  #Tạo Đa Luồng
  acc=int(input("Nhập Số Acc Muốn Chạy:"))
  data=[]
  for i in range(acc):
    print(green+"[Facebook]:",red,"[",i,"]")
    ck=input(green+"Nhập Cookie:")
    data.append(ck)
  h=int(input(blue+"Nhập Delay:"))
  os.system("clear")
  print("Bản Quyền:NEKO TOOL")
  print("ZALO Group:https://zalo.me/g/yvkvew875")
  print("___________________________________")
  while True:
    try:
      for p in range(acc):
        cookie=data[p]
        head_fb={
        "Host":"mbasic.facebook.com",
        "cache-control":"max-age=0",
        "upgrade-insecure-requests":"1",
        "save-data":"on",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site":"cross-site",
        "sec-fetch-mode":"navigate",
        "sec-fetch-user":"?1",
        "sec-fetch-dest":"document",
        "accept-language":"vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "cookie":cookie,}
        web=requests.get("https://mbasic.facebook.com/",headers=head_fb)
        tìm=re.findall('/story.php?.*?"',web.text)
        if tìm==[]:
          tìm=re.findall('/photo.php?.*?"',web.text)
        else:
          fb=re.findall('id="mbasic_logout_button".*?</a>',web.text)
          b0=fb[0].replace('id="mbasic_logout_button">Đăng xuất (',"")
          bo1=b0.replace(")</a>","")
          print("[Facebook]:","[",bo1,"]")
          tách=tìm[0].replace('"',"")
          tách_1=tách.replace("amp;","")
          web1=requests.get("https://mbasic.facebook.com"+tách_1,headers=head_fb)
          soup1=bs(web1.text,"html.parser")
          a= soup1.title
          for hiện in a.children:
            print("",end=" \r")
          tìm1=soup1.find_all("a",href=True)
          for tìm1 in tìm1:
            link1=tìm1["href"]
            if  "/a/like.php?" in link1:
              requests.get("https://mbasic.facebook.com"+link1,headers=head_fb)
              print(green+"Đã Like Bài Viết:",hiện)
              for l in range(h,-1,-1):
                sleep(1)
                print(yellow+"Đợi",l,end=" \r")
        
    except:
      print("",end=" \r")
if choose=="3":
  acc=int(input("Nhập Số Acc Muốn Chạy:"))
  data=[]
  for i in range(acc):
    print("[Facebook]:","[",i,"]")
    ck=input("Nhập Cookie:")
    data.append(ck)
  delay=int(input("Nhập Delay:"))
  os.system("clear")
  print("Bản Quyền:NEKO TOOL")
  print("ZALO Group:https://zalo.me/g/yvkvew875")
  print("___________________________________")
  while True:
    try:
      for i in range(acc):
        cookie=data[i]
        head_fb={
        "Host":"mbasic.facebook.com",
        "cache-control":"max-age=0",
        "upgrade-insecure-requests":"1",
        "save-data":"on",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site":"cross-site",
        "sec-fetch-mode":"navigate",
        "sec-fetch-user":"?1",
        "sec-fetch-dest":"document",
        "accept-language":"vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "cookie":cookie,}
        web=requests.get("https://mbasic.facebook.com/friends/center/suggestions/?mff_nav=1",headers=head_fb)
        fb=re.findall('id="mbasic_logout_button".*?</a>',web.text)
        b0=fb[0].replace('id="mbasic_logout_button">Đăng xuất (',"")
        bo1=b0.replace(")</a>","")
        print("[Facebook]:","[",bo1,"]")
        tìm =re.findall('/friends/hovercard/mbasic/?.*?"',web.text)
        bỏ=tìm[0].replace('"',"")
        bỏ_1=bỏ.replace("amp;","")
        web1=requests.get("https://mbasic.facebook.com"+bỏ_1,headers=head_fb)
        tìm1=re.findall("<head><title>.*?</title>",web1.text)
        bo=tìm1[0].replace("<head><title>","")
        bo1=bo.replace("</title>","")
        tìm2=re.findall('/a/mobile/friends/add_friend.php?.*?"',web1.text)
        b=tìm2[0].replace('"',"")
        b1=b.replace("amp;","")
        requests.get("https://mbasic.facebook.com"+b1,headers=head_fb)
        print("Đã Thêm Bạn Bè:",bo1)
        for time in range(delay,-1,-1):
          sleep(1)
          print("Đợi",time,end=" \r")
    except:
      print("",end=" \r")
if choose=="4":
  acc=int(input("Nhập Số Acc Muốn Chạy:"))
  data=[]
  for i in range(acc):
    print("[Facebook]:","[",i,"]")
    ck=input("Nhập Cookie:")
    data.append(ck)
  delay=int(input("Nhập Delay:"))
  os.system("clear")
  print("Bản Quyền:NEKO TOOL")
  print("ZALO Group:https://zalo.me/g/yvkvew875")
  print("___________________________________")
  while True:
    try:
      for i in range(acc):
        cookie=data[i]
        head_fb={
        "Host":"mbasic.facebook.com",
        "cache-control":"max-age=0",
        "upgrade-insecure-requests":"1",
        "save-data":"on",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site":"cross-site",
        "sec-fetch-mode":"navigate",
        "sec-fetch-user":"?1",
        "sec-fetch-dest":"document",
        "accept-language":"vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "cookie":cookie,}
        web=requests.get("https://mbasic.facebook.com/friends/center/requests/all/",headers=head_fb)
        fb=re.findall('id="mbasic_logout_button".*?</a>',web.text)
        b0=fb[0].replace('id="mbasic_logout_button">Đăng xuất (',"")
        bo1=b0.replace(")</a>","")
        print("[Facebook]:","[",bo1,"]",)
        tìm =re.findall('/friends/hovercard/mbasic/?.*?"',web.text)
        bỏ=tìm[0].replace('"',"")
        bỏ_1=bỏ.replace("amp;","")
        web1=requests.get("https://mbasic.facebook.com"+bỏ_1,headers=head_fb)
        tìm1=re.findall("<head><title>.*?</title>",web1.text)
        bo=tìm1[0].replace("<head><title>","")
        bo1=bo.replace("</title>","")
      #print(bo1)
        tìm2a=re.findall('/a/notifications.php?.*?"',web1.text)
        bỏi=tìm2a[0].replace('"',"")
        bỏ_1_i=bỏi.replace("amp;","")
        requests.get("https://mbasic.facebook.com"+bỏ_1_i,headers=head_fb)
        print("Đã Xác Nhận Bạn Bè:",bo1)
        for time in range(delay,-1,-1):
          sleep(1)
          print("Đợi",time,end=" \r")
    except:
      print("",end=" \r")
if choose=="5":
  acc=int(input("Nhập Số Acc Muốn Chạy:"))
  data=[]
  for i in range(acc):
    print("[Facebook]:","[",i,"]")
    ck=input("Nhập Cookie:")
    data.append(ck)
  delay=int(input("Nhập Delay:"))
  os.system("clear")
  print("Bản Quyền:NEKO TOOL")
  print("ZALO Group:https://zalo.me/g/yvkvew875")
  print("___________________________________")
  while True:
    try:
      for i in range(acc):
        cookie=data[i]
        head_fb={
        "Host":"mbasic.facebook.com",
        "cache-control":"max-age=0",
        "upgrade-insecure-requests":"1",
        "save-data":"on",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site":"cross-site",
        "sec-fetch-mode":"navigate",
        "sec-fetch-user":"?1",
        "sec-fetch-dest":"document",
        "accept-language":"vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "cookie":cookie,}
        web=requests.get("https://mbasic.facebook.com/",headers=head_fb)
        tìm=re.findall('/story.php?.*?"',web.text)
        if tìm==[]:
          tìm=re.findall('/photo.php?.*?"',web.text)
        else:
          fb=re.findall('id="mbasic_logout_button".*?</a>',web.text)
          b0=fb[0].replace('id="mbasic_logout_button">Đăng xuất (',"")
          bo1=b0.replace(")</a>","")
          print("[Facebook]:","[",bo1,"]",)
          tách=tìm[0].replace('"',"")
          tách_1=tách.replace("amp;","")
          web1=requests.get("https://mbasic.facebook.com"+tách_1,headers=head_fb)
          tìm1=re.findall("<head><title>.*?</title>",web1.text)
          bo=tìm1[0].replace("<head><title>","")
          bo1=bo.replace("</title>","")
          tìm=re.findall('/reactions/picker/?.*?"',web1.text)
          bỏ_i=tìm[0].replace('"',"")
          bỏ_1_i=bỏ_i.replace("amp;","")
          web2=requests.get("https://mbasic.facebook.com"+bỏ_1_i,headers=head_fb)
          cx=re.findall('/ufi/reaction/?.*?"',web2.text)
          i=randint(0,6)
          cx_1=cx[i].replace('"',"")
          cx_2=cx_1.replace("amp;","")
          requests.get("https://mbasic.facebook.com"+cx_2,headers=head_fb)
          if i==0:
            print("Đã Like Bài Viết:",bo1)
          if i==1:
            print("Đã Love Bài Viết:",bo1)
          if i==2:
            print("Đã Thương Thương Bài Viết:",bo1)
          if i==3:
            print("Đã HaHa Bài Viết:",bo1)
          if i==4:
            print("Đã Wow Bài Viết:",bo1)
          if i==5:
            print("Đã Buồn Bài Viết:",bo1)
          if i==6:
            print("Đã Phẫn Nộ Bài Viết:",bo1)
          for time in range(delay,-1,-1):
            sleep(1)
            print("Đợi",time,end=" \r")
    except:
      print("Lỗi",end=" \r")
      
      
      
     
if choose=="7":
  cookie=input(green+"Nhập Cookie:")
  user=input(green+"Nhập User-Agent:")
  chọn1=input(green+"Thêm Bạn Bè(y/n):")
  chọn=input(green+"Comment(y/n):")
  if chọn=="y":
    cmt=input(red+"Nhập Nội Dung:")
  delay=int(input(yellow+"Nhập Delay:"))
  os.system("clear")

  print(green+"Bản Quyền:NEKO TOOL")
  print("ZALO Group:https://zalo.me/g/yvkvew875")
  print("___________________________________")
  job=0
  while True:
    try:
        job=job+1
        head_fb={
        "Host":"mbasic.facebook.com",
        "cache-control":"max-age=0",
        "upgrade-insecure-requests":"1",
        "save-data":"on",
        "user-agent":user,
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site":"cross-site",
        "sec-fetch-mode":"navigate",
        "sec-fetch-user":"?1",
        "sec-fetch-dest":"document",
        "accept-language":"vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "cookie":cookie,}
        web=requests.get("https://mbasic.facebook.com/",headers=head_fb)
        tìm=re.findall('/story.php?.*?"',web.text)
        if tìm==[]:
          tìm=re.findall('/photo.php?.*?"',web.text)
          pass
        else:
          fb=re.findall('id="mbasic_logout_button".*?</a>',web.text)
          b0=fb[0].replace('id="mbasic_logout_button">Đăng xuất (',"")
          bi=b0.replace(")</a>","")
          tách=tìm[0].replace('"',"")
          tách_1=tách.replace("amp;","")
          web1=requests.get("https://mbasic.facebook.com"+tách_1,headers=head_fb)
          tìm1=re.findall("<head><title>.*?</title>",web1.text)
          bo=tìm1[0].replace("<head><title>","")
          bo1=bo.replace("</title>","")
          tìm=re.findall('/reactions/picker/?.*?"',web1.text)
          bỏ_i=tìm[0].replace('"',"")
          bỏ_1_i=bỏ_i.replace("amp;","")
          web2=requests.get("https://mbasic.facebook.com"+bỏ_1_i,headers=head_fb)
          cx=re.findall('/ufi/reaction/?.*?"',web2.text)
          i=randint(0,6)
          cx_1=cx[i].replace('"',"")
          cx_2=cx_1.replace("amp;","")
          requests.get("https://mbasic.facebook.com"+cx_2,headers=head_fb)
          
          print(green+"[Facebook]:","[",bi,"]",)
          if i==0:
            print("[",job,"]","Đã Like Bài Viết:",bo1)
          if i==1:
            print("[",job,"]","Đã Love Bài Viết:",bo1)
          if i==2:
            print("[",job,"]","Đã Thương Thương Bài Viết:",bo1)
          if i==3:
            print("[",job,"]","Đã HaHa Bài Viết:",bo1)
          if i==4:
            print("[",job,"]","Đã Wow Bài Viết:",bo1)
          if i==5:
            print("[",job,"]","Đã Buồn Bài Viết:",bo1)
          if i==6:
            print("[",job,"]","Đã Phẫn Nộ Bài Viết:",bo1)
          #comment
          pass
          if chọn=="y":
            web_cmt=requests.get("https://mbasic.facebook.com"+tách_1,headers=head_fb)
            c=re.findall('fs=.*?"',web_cmt.text)
            c=c[0].replace('"',"")
            c=c.replace("amp;","")
            #lâý fb_dtsg
            b=re.findall('name="fb_dtsg" value=".*?"',web_cmt.text)
            fb=b[0].replace('name="fb_dtsg" value="',"")
            fb=fb.replace('"',"")
           #lâý jazoest
            ii=re.findall('name="jazoest" value=".*?"',web_cmt.text)
            ja=ii[0].replace('name="jazoest" value="',"")
            ja=ja.replace('"',"")
           
            data={'fb_dtsg':fb, 'jazoest':ja,'comment_text':cmt}
            requests.post("https://mbasic.facebook.com/a/comment.php?"+c,headers=head_fb,data=data)
            print(blue+"Đã Cmt Với Nội Dung:",cmt)
          if chọn1=="y":
            web_add=requests.get("https://mbasic.facebook.com/friends/center/suggestions/?mff_nav=1",headers=head_fb)
            tìm =re.findall('/friends/hovercard/mbasic/?.*?"',web_add.text)
            bỏ=tìm[0].replace('"',"")
            bỏ_1=bỏ.replace("amp;","")
            web1=requests.get("https://mbasic.facebook.com"+bỏ_1,headers=head_fb)
            tìm1=re.findall("<head><title>.*?</title>",web1.text)
            bo=tìm1[0].replace("<head><title>","")
            bo1=bo.replace("</title>","")
            tìm2=re.findall('/a/mobile/friends/add_friend.php?.*?"',web1.text)
            b=tìm2[0].replace('"',"")
            b1=b.replace("amp;","")
            requests.get("https://mbasic.facebook.com"+b1,headers=head_fb)
            print(yellow+"Đã Thêm Bạn Bè:",bo1)
            pass
          for time in range(delay,-1,-1):
            sleep(1)
            print("Đợi",time,end=" \r")
    except:
      print("Lỗi",end=" \r")
if choose=="8":
  page="y"
  like="y"
  follow="n"
  head_tds={
        'Host':'traodoisub.com',
        'accept':'*/*',
        'x-requested-with':'XMLHttpRequest',
        'user-agent':'Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36',
        'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie':'__cfduid=d0ab5c02b234e98035ddda33fedf53f751605863119;PHPSESSID=4u07nb93c99vr83qfo98n3c7c8',}
  head_fb={
        "Host":"mbasic.facebook.com",
        "cache-control":"max-age=0",
        "upgrade-insecure-requests":"1",
        "save-data":"on",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site":"cross-site",
        "sec-fetch-mode":"navigate",
        "sec-fetch-user":"?1",
        "sec-fetch-dest":"document",
        "accept-language":"vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "cookie":"datr=kwmdXzVJOzaQFMUNpzwCWI_S;sb=kwmdX-uAllEpVqv2oYgaB1qX;m_pixel_ratio=2;c_user=100041768436459;xs=11%3AzyUNmjRXHQSj9w%3A2%3A1607581229%3A16758%3A6312;fr=1NRyZqGnUlf8veZ4A.AWXcTXFcCRPas2qhHUUH9BM9ZeQ.BfnQmT.IF.F_D.0.0.Bf1rSn.AWX5ylJcIAQ;wd=360x688;x-referer=eyJyIjoiL2ZyaWVuZHMvY2VudGVyL3N1Z2dlc3Rpb25zLz9tZmZfbmF2PTEiLCJoIjoiL2ZyaWVuZHMvY2VudGVyL3N1Z2dlc3Rpb25zLz9tZmZfbmF2PTEiLCJzIjoibSJ9"}
  data_tds="key=dcfcd07e645d245babe887e5e2daa016"
  while True:
    if like=="y":
      try:
        web=requests.post("https://traodoisub.com/ex/like/load.php",headers=head_tds,data=data_tds)
        id=re.findall('<button title="http://fb.com/.*?"',web.text)
        id=id[0].replace('"',"")
        id=id.replace('<button title=http://fb.com/',"")
        web1=requests.get("https://mbasic.facebook.com/"+id,headers=head_fb)
        link=web1.url
        web2=requests.get(link,headers=head_fb)
        like=re.findall('/a/like.php?.*?"',web2.text)
        like=like[0].replace('"',"")
        like=like.replace("amp;","")
        requests.get("https://mbasic.facebook.com"+like,headers=head_fb)
        print("Like:",id)
        nhan=requests.post("https://traodoisub.com/ex/like/nhantien.php",headers=head_tds,data="id="+id)
        if nhan.text=="2":
          print("+200 Xu")
      except:
        pass
    if page=="y":
      try:
        webpage=requests.post("https://traodoisub.com/ex/fanpage/load.php",headers=head_tds,data=data_tds)
        idpage=re.findall('<button title="https://www.facebook.com/.*?"',webpage.text)
        idpage=idpage[0].replace('"',"")
        idpage=idpage.replace('<button title=https://www.facebook.com/',"")
        webpage1=requests.get("https://mbasic.facebook.com/profile.php?id="+idpage,headers=head_fb)
        lp=re.findall('/a/profile.php?.*?"',webpage1.text)
        lp=lp[0].replace('"',"")
        lp=lp.replace("amp;","")
        requests.get("https://mbasic.facebook.com"+lp,headers=head_fb)
        print("Page:",idpage)
        nhận=requests.post("https://traodoisub.com/ex/fanpage/nhantien.php",headers=head_tds,data="id="+idpage)
        if nhận.text=="2":
          print("+600 Xu")
      except:
        pass
    if follow=="y":
      try:
        webfl=requests.post("https://traodoisub.com/ex/follow/load.php",headers=head_tds,data=data_tds)
        idfl=re.findall('<button title="https://www.facebook.com/.*?"',webfl.text)
        idfl=idfl[0].replace('"',"")
        idpfl=idfl.replace('<button title=https://www.facebook.com/',"")
        webfl1=requests.get("https://mbasic.facebook.com/profile.php?id="+idfl,headers=head_fb)
        fl=re.findall('/a/subscribe.php?.*?"',webfl1.text)
        fl=fl[0].replace('"',"")
        fl=fl.replace("amp;","")
        requests.get("https://mbasic.facebook.com"+fl,headers=head_fb)
        print("Follow:",idfl)
        nhận=requests.post("https://traodoisub.com/ex/fanpage/nhantien.php",headers=head_tds,data="id="+idfl)
        if nhận.text=="2":
          print("+600 Xu")
      except:
        pass
if choose=="9":
  while True:
    try:
      head_fb={
        "Host":"mbasic.facebook.com",
        "cache-control":"max-age=0",
        "upgrade-insecure-requests":"1",
        "save-data":"on",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; RMX1929) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site":"cross-site",
        "sec-fetch-mode":"navigate",
        "sec-fetch-user":"?1",
        "sec-fetch-dest":"document",
        "accept-language":"vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "cookie":"datr=iky3XyEyNYM9g2W_Aeu_RLdD;sb=iky3X9EFcHnRA3DABvHjqcPx;dpr=2;c_user=100050011458036;xs=46%3AqpwjY1NNxuifUQ%3A2%3A1607957062%3A16758%3A6312;m_pixel_ratio=2;wd=360x800;fr=1QEbJChVvSiNOGSwm.AWUR0BWCINjEccBOINunsDJM4Aw.Bft0yL.ME.F_a.0.0.Bf3DyC.AWWNeZmrU78",}
      head_tlf={
        'Host':'tanglikefree.com',
        'Connection':'keep-alive',
        'Accept':'application/json, text/plain, */*',
        'X-Requested-With':'XMLHttpRequest',
        'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvdGFuZ2xpa2VmcmVlLmNvbVwvYXBpXC9hdXRoXC9sb2dpbiIsImlhdCI6MTYwNzM0MzE1NiwibmJmIjoxNjA3MzQzMTU2LCJqdGkiOiJaYzdOOXF2VVV1RHhVSzhqIiwic3ViIjoxMDgzODEsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEifQ.z72mMFVb-yx7m4JOMp9A9SGTQ90_vfoUmnpuyBt_DBw',
        'User-Agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36',
         'Referer': 'https://tanglikefree.com/makemoney', }
      app=requests.get("https://tanglikefree.com/api/auth/Post/getpost",headers=head_tlf)
      id=app.json()[0]["idpost"]
      web=requests.get("https://mbasic.facebook.com/"+id,headers=head_fb)
      link=web.url
      print(link)
      web1=requests.get(url=link,headers=head_fb)
      a=bs(web1.text,"html.parser")
      b=a.find_all("a",href=True)
      for b in b:
        lie=b["href"]
        if "/a/like.php?" in lie:
          requests.get("https://mbasic.facebook.com"+lie,headers=head_fb)
      re=requests.get("https://tanglikefree.com/api/auth/creat_request",headers=head_tlf)
      rq=re.json()["request_id"]
      nhận=requests.post("https://tanglikefree.com/api/auth/Post/submitpost",headers=head_tlf,data={"idpost":id,"request_id":rq})
      print(nhận.json()["messages"])
    except:
      print("Lỗi",end=" \r")