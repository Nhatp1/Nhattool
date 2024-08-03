import os,time,re,random,base64
try:
    import requests,prettytable,colorama
except:
    os.system('pip install requests && pip install prettytable && pip install colorama')
import requests
from prettytable import PrettyTable
from colorama import init, Fore
from urllib.parse import urlparse, unquote, quote
from string import ascii_letters, digits
os.system("cls" if os.name == "nt" else "clear")
class ApiZefoy:
    def __init__(self) -> None:
        self.zefoy = "https://zefoy.com/"
        self.headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
        self.session = requests.Session()
        self.captcha = {}
        self.captcha_1 = None
        self.captcha_name = 'captcha_zefoy.png'
        self.services = {}
        self.services_ids = {}
        self.services_status = {}
        self.url = input("Nhập link video: ")
    
    def get_captcha(self):
        rq = self.session.get(self.zefoy, headers=self.headers).text
        try:
            for x in re.findall(r'<input type="hidden" name="(.*)" value="(.*)">', rq):
                self.captcha[x[0]] = x[1]
            self.captcha_1 = rq.split('type="text" name="')[1].split('" oninput="this.value=this.value.toLowerCase()"')[0]
            captcha_url = rq.split('<img src="')[1].split('" onerror="imgOnError()" class="')[0]
            rq = self.session.get(f"{self.zefoy}{captcha_url}",headers=self.headers).content
            open(self.captcha_name, 'wb').write(rq)
            print('</> Đang giải capcha...')
            return False
        except Exception as e:
            print(f"</> Không thể giải captcha: {e}")
            time.sleep(2)
            self.get_captcha()
    
    def solve_captcha(self):
        rq = self.session.post('https://api.ocr.space/parse/image?K87899142388957', headers={'apikey':'K87899142388957'}, files={'task':open(self.captcha_name,'rb')}).json()
        solved_text = rq['ParsedResults'][0]['ParsedText'].replace('\n','').replace('\r','')
        return solved_text
    
    def giai_captcha(self):
        self.get_captcha()
        giai_captcha = self.solve_captcha()
        self.captcha[self.captcha_1] = giai_captcha
        rq = self.session.post(self.zefoy, headers=self.headers, data=self.captcha).text
        if 'Enter Video URL' in rq:
            cookies = self.session.cookies.get('PHPSESSID')
            self.session.cookies.update({'PHPSESSID': cookies})
            print(f"</> Giải capcha thành công: {giai_captcha}")
            self.video_key = rq.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]
    
    def get_status_services(self):
        rq = self.session.get(self.zefoy, headers=self.headers).text
        for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+\n.+', rq):
            self.services[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = x.split('d-sm-inline-block">')[1].split('</small>')[0].strip()
        for x in re.findall(r'<h5 class="card-title mb-3">.+</h5>\n<form action=".+">', rq):
            self.services_ids[x.split('title mb-3">')[1].split('<')[0].strip()] = x.split('<form action="')[1].split('">')[0].strip()
        for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+<button .+', rq):
            if 'disabled class' in x:
                self.services_status[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = False
            else:
                self.services_status[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = True
        return (self.services, self.services_status)

    def get_table(self):
        i = 1
        table = PrettyTable(field_names=["ID", "DỊCH VỤ", "Status"], title="Status Services", header_style="upper",border=True)
        while True:
            if len(self.get_status_services()[0])>1:
                break
            else:
                print('Không có sever nào hoạt động. Thử lại...')
                self.giai_captcha()
                time.sleep(3)
        for service in self.services:
            table.add_row([f"{Fore.CYAN}{i}{Fore.RESET}", service, f"{Fore.GREEN if 'ago updated' in self.services[service] else Fore.RED}{self.services[service]}{Fore.RESET}"])
            i+=1
        table.title =  f"{Fore.YELLOW}Số Dịch Vụ Hoạt Động: {len([x for x in self.services_status if self.services_status[x]])}{Fore.RESET}"
        os.system("cls" if os.name == "nt" else "clear")
        print(table)
        while True:
            self.service = int(input("Nhập số: "))-1
            if self.service > len(self.services_status)-1 or self.service < 0:
                print("Bạn nhập sai số!")
            else:
                ten_chedo = list(self.services.keys())
                self.service = ten_chedo[self.service]
                if self.services_status[self.service]:
                    break
                else:
                    print("Chế độ không hoạt động!")
    
    def use_service(self):
        if self.find_video()[0] is False:
            return False
        self.token = "".join(random.choices(ascii_letters+digits, k=16))
        request = self.session.post(f'{self.zefoy}{self.services_ids[self.service]}', headers={'content-type':f'multipart/form-data; boundary=----WebKitFormBoundary{self.token}', 'user-agent':self.headers['user-agent'], 'origin':'https://zefoy.com'}, data=f'------WebKitFormBoundary{self.token}\r\nContent-Disposition: form-data; name="{self.video_info[0]}"\r\n\r\n{self.video_info[1]}\r\n------WebKitFormBoundary{self.token}--\r\n')
        try:
            res = base64.b64decode(unquote(request.text.encode()[::-1])).decode()
        except:
            time.sleep(3)
            return ""
        if 'Session expired. Please re-login' in res:
            print('</> Phiên hết hạn. Đang đăng nhập lại...')
            self.giai_captcha()
            return ""
        elif 'Too many requests. Please slow' in res:
            time.sleep(3)
        elif 'service is currently not working' in res:
            return ('</> Dịch vụ hiện không hoạt động, hãy thử lại sau. | Bạn có thể thay đổi nó trong cấu hình.')
        else:
            print(res.split("sans-serif;text-align:center;color:green;'>")[1].split("</")[0])
    
    def find_video(self):
        if self.service is None:
            return False, "You didn't choose the service"
        while True:
            if self.service not in self.services_ids:
                self.get_status_services()
                time.sleep(1)
            request = self.session.post(f'{self.zefoy}{self.services_ids[self.service]}', headers={'content-type':'multipart/form-data; boundary=----WebKitFormBoundary0nU8PjANC8BhQgjZ', 'user-agent':self.headers['user-agent'], 'origin':'https://zefoy.com'}, data=f'------WebKitFormBoundary0nU8PjANC8BhQgjZ\r\nContent-Disposition: form-data; name="{self.video_key}"\r\n\r\n{self.url}\r\n------WebKitFormBoundary0nU8PjANC8BhQgjZ--\r\n')
            try:
                self.video_info = base64.b64decode(unquote(request.text.encode()[::-1])).decode()
            except:
                time.sleep(3)
                continue
            if 'Session expired. Please re-login' in self.video_info:
                print('</> Phiên hết hạn. Đang đăng nhập lại...')
                self.giai_captcha()
                return
            elif 'service is currently not working' in self.video_info:
                return True,'</> Dịch vụ hiện không hoạt động, hãy thử lại sau. | Bạn có thể thay đổi nó trong cấu hình.'
            elif """onsubmit="showHideElements""" in self.video_info:
                self.video_info = [self.video_info.split('" name="')[1].split('"')[0],self.video_info.split('value="')[1].split('"')[0]]
                return True, request.text
            elif 'Checking Timer...' in self.video_info:
                try: 
                    t=int(re.findall(r'ltm=(\d*);', self.video_info)[0])
                    lamtilo = int(re.findall(r'ltm=(\d*);', self.video_info)[0])
                except: 
                    return (False,)
                if lamtilo==0:self.find_video()
                elif lamtilo >= 1000: print('</> Your IP was banned')
                _=time.time()
                while time.time()-2<_+lamtilo:
                    t-=1
                    print(f"</> Vui lòng chờ: {t} giây...", end="\r")
                    time.sleep(1)
                continue
            elif 'Too many requests. Please slow' in self.video_info:
                time.sleep(3)
            else:
                print(self.video_info)

Z = ApiZefoy()
Z.giai_captcha()
Z.get_table()
while True:
    try: 
        if 'Service is currently not working, try again later' in str(Z.use_service()):
            print('\033[1;31m</>Dịch vụ hiện không hoạt động, hãy thử lại sau. | Bạn có thể thay đổi nó trong cấu hình.')
            time.sleep(5)
    except Exception as e:
        print(f'LỖI NGHIÊM TÚC | thử lại sau 10 giây.|| {e}');time.sleep(10)