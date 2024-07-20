import requests,os,sys, time
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from bs4 import BeautifulSoup
import json
import requests
import time
from time import strftime
import os
import requests
import urllib.parse
from time import strftime
import os
from datetime import datetime
from time import sleep, strftime
import datetime
#Color
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Gọi hàm để xóa màn hình
clear_screen()

# Lmao
thanh_xau=trang+'~'+do+'['+vang+'⟨⟩'+do+'] '+trang+'➩  '+xanhnhat
thanh_dep=trang+'~'+do+'['+xanh_la+'✓'+do+'] '+trang+'➩  '+xanhnhat
def get_ip_from_url(url):
    # response = requests.get(url)
    # ip_address = socket.gethostbyname(response.text.strip())
    # return ip_address
    return "127.0.0.1"
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url
import os
import requests
from time import strftime
now = datetime.datetime.now()
thu = now.strftime('%A')
ngay_hom_nay = now.strftime('%d')
thang_nay = now.strftime('%m')
nam_ = now.strftime('%Y')
now = datetime.datetime.now()
gio_hien_tai = now.strftime('%H:%M:%S')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def save_key_to_file(key, filename='NhatTool-key.txt'):
    with open(filename, 'w') as file:
        file.write(str(key))


def load_key_from_file(filename='NhatTool-key.txt'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read().strip()
    return None


def fetch_shortened_url(url, token):
    try:
        encoded_url = urllib.parse.quote(url)
        api_url = f'https://yeumoney.com/QL_api.php?token={token}&url={encoded_url}&format=json'
        try:
            response = requests.get(api_url)
        except:
            print('Vui Lòng Kết Nối Mạng !')
            exit("")
        response.raise_for_status()
        result = response.json()
        if result["status"] == "success":
            return result["shortenedUrl"]
        else:
            return result["status"]
    except requests.exceptions.RequestException as e:
        return f"Error fetching shortened URL: {e}"


def main():
    clear_screen()

    ngay = int(strftime('%d'))
    key = "NhatTool" + str(ngay * 2593885817 + 4610273)
    key = "nhattool2802"

    saved_key = load_key_from_file()

    if saved_key == key:
        print('\033[1;32m Key chính xác Đúng Chúc Bạn Ngày Tốt Lành')
    else:

        url = f'https://taoweb1s.net/key-tool?key={key}'
        token_link1s = "432c9b236e4e2a7ca16f55b2029fe3461c78be79bb267c98e4f80f49303dbab3"
        link_key = fetch_shortened_url(url, token_link1s)

        if link_key is None:
            print("Unable to generate shortened URL. Please try again later.")
            return

        nhap_key = input(f'''
   \x1b[38;5;207m╔══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╗
  \033[1;36m ███╗   ██╗██╗  ██╗ █████╗ ████████╗    ████████╗ ██████╗  ██████╗ ██╗     
  \033[1;36m ████╗  ██║██║  ██║██╔══██╗╚══██╔══╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
  \033[1;36m ██╔██╗ ██║███████║███████║   ██║          ██║   ██║   ██║██║   ██║██║     
  \033[1;36m ██║╚██╗██║██╔══██║██╔══██║   ██║          ██║   ██║   ██║██║   ██║██║     
  \033[1;36m ██║ ╚████║██║  ██║██║  ██║   ██║          ██║   ╚██████╔╝╚██████╔╝███████╗
  \033[1;36m ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝          ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
        \x1b[38;5;226mĐÂY LÀ TOOL FREE NÊN KEY SẼ THAY ĐỔI MỖI NGÀY !!
        \x1b[38;5;207mHôm Nay Ngày : \x1b[38;5;46m{thu}/{ngay_hom_nay}/{thang_nay}/{nam_}
        \x1b[38;5;207mGiờ Hiện Tại : \x1b[38;5;46m{gio_hien_tai}
        \x1b[38;5;207mBOT SPAM SMS  : https://t.me/sharebotvip \x1b[38;5;46m
   \x1b[38;5;207m╚══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╝
   \x1b[38;5;46mLink Lấy Key Là : \x1b[38;5;226m{link_key}
   \033[1;32m Nhập Key để Vào Tool : ''')

        if nhap_key == key:
            print('\033[1;32m Key chính xác Đúng Chúc Bạn Ngày Tốt Lành')

            save_key_to_file(nhap_key)
        else:
            print('\033[1;31m Key Sai Vui Lòng Vượt Link Để lấy')
            quit()


if __name__ == "__main__":
    main()
banner = ''' 
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

'''
for i in banner:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.00130)
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
#thanh_xau= print(f"{red}┌─────┬────────────────────────────────────┬─────────┬─────────┐")
#thanh_dep= print(f"{red}│{vang}      {red}│    {vang}      {red}        │ {vang}STATUS {red} │{vang} VERSION {red}│")
#thanh_cuoi=print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")

print(f"{hong}┌─────┬────────────────────────────────────┬─────────┬─────────┐")
print(f"{hong}│{vang} STT {red}│    {xanhnhat}         MENU TOOL      {red}        │ {vang}STATUS {red} │{vang} VERSION {red}│")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│{vang}  1 {red} │{lam} TDS TIKTOK    {red}                     │{luc} ONLINE {red} │ {lam} [2.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 2 {red} │{lam} TDS FACEBOOK PRO5     {red}             │{luc} ONLINE {red} │ {lam} [2.1] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 3 {red} │{lam} TDS FACEBOOK      {red}                 │{luc} ONLINE {red} │{lam} [1.3] {red}  │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 3.1 {red} │{lam} TDS FACEBOOK (VIP FIVEX)    {red}                 │{luc} ONLINE {red} │{lam} [5.0] {red}  │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 4 {red} │{lam} TDS INSTAGRAM          {red}            │{luc} ONLINE {red} │ {lam} [1.9] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 5 {red} │{hong}  KIẾM TIỀN (GOLIKE) {red}            │{luc} ONLINE {red} │ {lam} [2.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 6 {red} │{tim} BUFF VIEW TIKTOK  {red}            │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 7 {red} │{vang} TTC VIP INSTAGRAM   {red}            │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 7.1 {red} │{vang} TTC TIKTOK   {red}            │{red} OFFLINE {red} │ {lam} [1.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 7.2 {red} │{vang} TTC FACEBOOK    {red}            │{red} OFFLINE {red} │ {lam} [1.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 7.3 {red} │{vang} TTC PRO5    {red}            │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 8 {red} │{trang} VIEW STR FACEBOOK  PRO5   {red}            │{luc} ONLINE {red} │ {lam} [3.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 8.1 {red} │{trang} SHARE ẢO PRO5   {red}            │{luc} ONLINE {red} │ {lam} [3.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 8.2 {red} │{trang} KẾT BẠN FACEBOOK    {red}            │{luc} ONLINE {red} │ {lam} [3.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 8.3 {red} │{trang} NUÔI FACEBOOK   {red}            │{luc} ONLINE {red} │ {lam} [3.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 8.4 {red} │{trang} REG PRO5  {red}            │{red} OFFLINE {red} │ {lam} [1.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 8.5 {red} │{trang} COMMENT FACEBOOK    {red}            │{luc} ONLINE {red} │ {lam} [3.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 9 {red} │{hong} TẤN CÔNG WEBSITE   {red}            │{red} OFFLINE {red} │ {lam} [3.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 10 {red} │{lamd} AUTO TAP HAMTER   {red}            │{luc} ONLINE {red} │ {lam} [3.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 11 {red} │{lamd} REPORT FACEBOOK    {red}            │{luc} ONLINE {red} │ {lam} [2.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 12 {red} │{hong} KÉO MEM TELEGRAM    {red}            │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 13 {red} │{trang} GET TOKEN 16 LOẠI    {red}            │{luc} ONLINE {red} │ {lam} [1.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
print(f"{hong}│ {vang} 14 {red} │{trang} GET PROXY     {red}            │{luc} ONLINE {red} │ {lam} [1.0] {red} │")

print(f"{hong} │                       TOOL GỘP CÁC YOUTUBER                   │      ")

print(f"{hong}┌─────┬────────────────────────────────────┬─────────┬─────────┐")
print(f"{hong}│ {vang} 1000 {red} │{lamd} TOOL HDT-TOOL   {red}            │{luc} ONLINE {red} │ {lam} [2.0] {red} │")
print(f"{hong}├─────┼────────────────────────────────────┼─────────┼─────────┤")
import requests

chon = str(input('\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩ \033[1;34mNhập Số \033[1;37m: \033[1;33m'))

if chon == '1':
    exec(requests.get('https://raw.githubusercontent.com/Nhattool/Nhattool/main/tdstiktok.py').text)
elif chon == '2':
    exec(requests.get('https://raw.githubusercontent.com/Nhattool/Nhattool/main/tdspro5.py?token=GHSAT0AAAAAACVCRFF3KVL6OPQTG4V4UXT6ZU3OJOQ').text)
elif chon == '3':
    exec(requests.get('https://raw.githubusercontent.com/Nhattool/Nhattool/main/tdsfb.py?token=GHSAT0AAAAAACVCRFF2D62RDYGY36BSHCP2ZU3OMSQ').text)
elif chon == '4':
    exec(requests.get('https://raw.githubusercontent.com/Nhattool/Nhattool/main/tdsig.py?token=GHSAT0AAAAAACVCRFF3GIX35ZDMTXMQGNLAZU3OZQA').text)
elif chon == '5':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/golike.py').text)
elif chon == '8':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/viewfb.py').text)
elif chon == '8.1':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/shareao.py').text)
elif chon == '8.2':
	exec(requests.get(' https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/addbb.py').text)
elif chon == '8.3':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/nuoifb.py').text)
elif chon == '6':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/tim.py').text)
elif chon == '8.5':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/cmt.py').text)
elif chon == '1000':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/dec_hdttool.py').text)
elif chon == '9':
	exec(requests.get('').text)
elif chon == '8.4':
	exec(requests.get('').text)
elif chon == '10':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/hamter.py').text)
elif chon == '7.3':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/ttcpro5.py').text)
elif chon == '7':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/ttcig.py').text)
elif chon == '12':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/memtele.py').text)
elif chon =='11':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/rpfb.py').text)
elif chon == '3.1':
	exec(requests.get('https://raw.githubusercontent.com/Nhattool/Nhattool/main/tdsfivex.py?token=GHSAT0AAAAAACVCRFF3NTDHFDUIJZYB2AMSZU3OPOQ').text)
elif chon == '13':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/gettoken.py').text)
elif chon == '14':
	exec(requests.get('https://raw.githubusercontent.com/Nhatp1/Nhatp1/main/prx.py').text)
else:
    print("Sai Lựa Chọn")
    exit()
    
