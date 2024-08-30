#!/usr/bin/python3

#Copyright = ['TuNguyen2712']

if __name__ != '__main__':__import__('sys').exit()

LIBRARIES = ["subprocess", "platform", "pystyle", "os", "sys", "requests", "time", "random", "datetime", "json"]
for LIB in LIBRARIES:
    try:
        __import__(LIB)
    except ImportError:
        print(f"Đang tiến hành cài đặt thư viện: [{LIB}]")
        try:
            result = __import__('subprocess').run([sys.executable, "-m", "pip", "install", LIB], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Cài đặt thành công: [{LIB}]")
            else:
                print(f"Cài đặt thất bại: [{LIB}]. Vui lòng thử lại sau.")
                print(result.stderr)
                __import__('sys').exit(1)
        except Exception as e:
            print(f"Đã xảy ra lỗi khi cài đặt {LIB}: {e}")
            __import__('sys').exit(1)

import os, sys, requests, platform, time, random, datetime, json 
from pystyle import *
 
try:
    import selenium
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
except ImportError:
    if platform.system() == 'Windows': 
        os.system('pip install selenium')
    else:
        input('Thư Viện Chính Khá Là Nặng Mọi Người Cân Nhắc Dung Lượng Khi Cài Vài Cái Khá Lâu Nhé! Enter Để Tiếp Tục')            
        os.system('pip install selenium==4.9.1')
        os.system('yes | pkg install x11-repo -y')
        os.system('yes | pkg install tur-repo -y')
        os.system('yes | pkg install chromium -y')
except Exception as e:
    print("Lỗi Khi Tải Thư Viện: {}".format(str(e)))

def Check_Internet():
    try:
        response = requests.get("https://www.google.com.vn", timeout=3)
        return True
    except (requests.ConnectionError, requests.exceptions.ReadTimeout):
        return False
    except requests.exceptions.RequestException as e:
        print(f"Lỗi kết nối không xác định: {e}")
        return False
try:
    if not Check_Internet():
        print("Vui lòng bật Wifi hoặc kiểm tra lại kết nối của bạn.")
        sys.exit(1)
    else:
        print("Đang vào Tool...")
except Exception as e:
    print(f"Lỗi: {e}")
    sys.exit(1)
    
date_time = str(time.strftime("Time: %H:%M:%S | Date: %d/%m/%Y - (UTC)")) 
pyver = ".".join(sys.version.split(" ")[0].split(".")[:-1])

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Banner():
    banner = """
╔═══════════════════════════════════════════════════════════════════════╗
║ TOOL >>> [ TRAODOISUB TIKTOK AUTO ]                                   ║
║ DATE TIME >>> [ {} ]           ║
║ VERSION PYTHON >>> [ {} ]                                           ║   
║ VERSION TOOL >>> [ 1.0 ]                                              ║   
╚═══════════════════════════════════════════════════════════════════════╝
\n""".format(date_time, pyver)
    print(banner)

def custom_delay(delay):
    for remaining in range(delay, 0, -1):
        mins, secs = divmod(remaining, 60)
        time_str = f"[T-TOOL][DELAY][{mins:02}:{secs:02}]"
        for phase in ['....X', '...XX', '..XXX', '.XXXX', 'XXXXX']:
            print(f'{time_str}[{phase}]', end='\r')
            time.sleep(0.1)
    print('              Trao đổi sub Tool                ', end="\r")
    
def save_file(path, content):
    with open(path, 'w') as file:
        file.write(content)

def open_file(path):
    with open(path, 'r') as file:
        return file.read()

def send_request(url):
    try:
        response = requests.get(url)
        if response.ok:
            return response.json()
    except requests.RequestException:
        return None

class Config_Tiktok:
    def __init__(self, cookie):
        self.cookie = cookie
        self.chromeoptions = webdriver.ChromeOptions()
        self.chromeoptions.add_argument("--window-size=580,800")
        self.chromeoptions.add_argument('--lang=en')
        self.chromeoptions.add_argument('--disable-gpu')
        self.chromeoptions.add_argument('--log-level=3')
        self.chromeoptions.add_argument("--mute-audio")
        self.chromeoptions.add_argument('--disable-blink-features=AutomationControlled')
        self.chromeoptions.add_argument("--no-sandbox")
        self.chromeoptions.add_argument("--disable-dev-shm-usage")
        if platform.system() != 'Windows':
            self.chromeoptions.add_argument("--headless=new")
        self.chromeoptions.add_experimental_option("excludeSwitches", ["enable-automation", 'enable-logging'])
        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        self.chromeoptions.add_experimental_option("prefs", prefs)        
        win = random.choice([x for x in range(7, 12) if x != 9])
        self.chromeoptions.add_argument(f'--user-agent=Mozilla/5.0 (Windows NT {win}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(85, 102)}.0.4844.82 Safari/537.36')        
        self.chromeoptions.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=self.chromeoptions)
        self.driver.get("https://www.tiktok.com")
    def outchrome(self):
        try:
            self.driver.close()
        except Exception as e:
            print(f"Error closing browser: {e}")
    def info(self):
        try:
            return self.driver.page_source.split('uniqueId":"')[1].split('"')[0]
        except IndexError:
            return "Unable to extract uniqueId."
    def login(self):
        try:
            cookiett = ''
            for x in ['msToken', 'multi_sids', 'odin_tt', 'passport_csrf_token_default', 'sid_guard', 'ssid_ucp_v1', 'uid_tt', 'tt_chain_token', 'sid_ucp_v1', 'tt-target-idc-sign', 'sessionid_ss', 'sid_tt', 'uid_tt_ss', 'sessionid', 'store-country-code', 'cmpl_token', 'passport_csrf_token', 'tt-target-idc', 'ttwid', 'store-idc', 'tt_csrf_token', 'store-country-code-src']:
                cookiett += f'{x}='+self.cookie.split(f'{x}=')[1].split(';')[0]+';'
            cookie = cookiett.replace(" ", "").split(';')
            for i in cookie:
                if i:
                    ck = i.split("=")
                    self.driver.add_cookie({"name": ck[0], "value": ck[1], "domain": ".tiktok.com"})
            self.driver.refresh()
            sleep(3)
        except Exception as e:
            print(f"Error during login: {e}")
    def follow(self, link):
        try:
            self.driver.get(link)
            sleep(10)
            follow_button = self.driver.find_element(By.XPATH, '//*[@id="main-content-others_homepage"]/div/div[1]/div[1]/div[2]/div/div[1]/button')
            follow_button.click()
        except Exception as e:
            print(f"Error during follow: {e}")
    def like(self, link):
        try:
            self.driver.get(link)
            sleep(10)
            like_button = self.driver.find_element(By.XPATH, '//*[@id="main-content-video_detail"]/div/div[2]/div/div[1]/div[1]/div[4]/div/button[1]')
            like_button.click()
        except Exception as e:
            print(f"Error during like: {e}")
    def comment(self, link, content):
        try:
            self.driver.get(link)
            sleep(10)
            comment_box = self.driver.find_element(By.CSS_SELECTOR, '#main-content-video_detail > div > div.css-12kupwv-DivContentContainer.ege8lhx2 > div > div.css-x4xlc7-DivCommentContainer.e1a7v7ak0 > div.css-1bg47i4-DivCommentBarContainer.e1a7v7ak2 > div > div > div.css-1vplah5-DivLayoutContainer.e1rzzhjk1 > div > div.css-4p7h1x-DivInputEditorContainer.e1rzzhjk3 > div > div > div.DraftEditor-editorContainer > div')
            comment_box.send_keys(content)
            comment_box.send_keys(Keys.ENTER)
        except Exception as e:
            print(f"Error during comment: {e}")

Clear()
Banner()

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
def enter_token():
    while True:
        try:
            token = input("Nhập Token Trao Đổi Sub: ")
            response = send_request(f"https://traodoisub.com/api/?fields=profile&access_token={token}")
            if response and response.get('success') == 200:
                print(f"Get Info TraoDoiSub Success >>> User: {response['data']['user']} | Xu: {response['data']['xu']} | XuDie: {response['data']['xudie']}")
                if input("Bạn Có Muốn Lưu Token (y/n): ").strip().upper() == 'Y':
                    save_file(os.path.join("TraoDoiSub", "token_traodoisub.txt"), token)
                break
            else:
                print("Token Sai Vui Lòng Nhập Lại")
        except Exception as e:
            print(f"Lỗi: {e}")
def enter_cookie(token):
    while True:
        try:
            cookie = input("Nhập Cookie Tiktok: ")
            tiktok = Config_Tiktok(cookie)
            tiktok.login()
            user_id = tiktok.info()
            tiktok.outchrome()
            response = send_request(f"https://traodoisub.com/api/?fields=tiktok_run&id={user_id}&access_token={token}")
            if response and response.get('success') == 200:
                print(f"Get Info Tiktok Success >>> User: {response['data']['uniqueID']} | Id {response['data']['id']}")
                if input("Bạn Có Muốn Lưu Cookie (y/n): ").strip().upper() == 'Y':
                    save_file(os.path.join("TraoDoiSub", "cookie_tiktok.txt"), cookie)
                break
            else:
                print("Cookie Die Vui Lòng Nhập Cookie Khác!!!")
        except Exception as e:
            try:
                tiktok.outchrome()
            except Exception:
                pass
            print(f"Lỗi: {e}")           
def enter_settings():
    while True:
        try:
            mission = input("Nhập nhiệm vụ (follow/like): ").strip()
            if mission not in ['follow', 'like']:
                print("Sai lựa chọn")
                continue
            delay = input("Nhập delay: ").strip()
            if not delay.isdigit():
                print("Vui lòng chỉ nhập số")
                continue
            if input("Bạn có muốn lưu settings (y/n): ").strip().upper() == 'Y':
                settings = {'mission': mission, 'delay': delay}
                save_file(os.path.join("TraoDoiSub", "settings.txt"), json.dumps(settings))
            break
        except Exception as e:
            print(f"Lỗi: {e}")
def handle_token():
    if not os.path.exists(os.path.join("TraoDoiSub", "token_traodoisub.txt")):
        enter_token()
    else:
        if input("Bạn Có Muốn Sử Dụng Token Đã Lưu (y/n): ").strip().upper() == 'Y':
            try:
                token = open_file(os.path.join("TraoDoiSub", "token_traodoisub.txt")).strip()
                response = send_request(f"https://traodoisub.com/api/?fields=profile&access_token={token}")
                if response and response.get('success') == 200:
                    print(f"Get Info TraoDoiSub Success >>> User: {response['data']['user']} | Xu: {response['data']['xu']} | XuDie: {response['data']['xudie']}")
                else:
                    print("Token Sai Vui Lòng Nhập Lại")
                    enter_token()
            except Exception as e:
                print(f"Lỗi: {e}")
                enter_token()
        else:
            enter_token()
def handle_cookie(token):
    if not os.path.exists(os.path.join("TraoDoiSub", "cookie_tiktok.txt")):
        enter_cookie(token)
    else:
        try:
            cookie = open_file(os.path.join("TraoDoiSub", "cookie_tiktok.txt")).strip()
            tiktok = Config_Tiktok(cookie)
            tiktok.login()
            user_id = tiktok.info()
            tiktok.outchrome()
            response = send_request(f"https://traodoisub.com/api/?fields=tiktok_run&id={user_id}&access_token={token}")
            if response and response.get('success') == 200:
                print(f"Get Info Tiktok Success >>> User: {response['data']['uniqueID']} | Id {response['data']['id']}")
            else:
                print("Cookie Die Vui Lòng Nhập Cookie Khác!!!")
                enter_cookie(token)
        except Exception as e:
            try:
                tiktok.outchrome()
            except Exception:
                pass
            print(f"Lỗi: {e}")
            enter_cookie(token)
def handle_settings():
    if not os.path.exists(os.path.join("TraoDoiSub", "settings.txt")):
        enter_settings()
    else:
        try:
            settings = json.loads(open_file(os.path.join("TraoDoiSub", "settings.txt")))
            mission = settings.get('mission')
            delay = settings.get('delay')
            if mission not in ['follow', 'like']:
                enter_settings()
            if not delay.isdigit():
                enter_settings()
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Lỗi: {e}")
            enter_settings()
ensure_directory("TraoDoiSub")
if not os.path.exists(os.path.join("TraoDoiSub", "information_tool.txt")):
    save_file(os.path.join("TraoDoiSub", "information_tool.txt"), """
>>> TOOL ĐƯỢC CODE BỞI TUNGUYEN2712
>>> TOOL ĐƯỢC CODE DỰA TRÊN TOOL GOLIKE TIKTOK AUTO CỦA LÝ QUANG TOẠI (DLOW)
>>> VERSION : 1.0
>>> NGÀY BẮT ĐẦU CODE 14/8 | NGÀY KẾT THÚC CODE 20/8
""")
handle_token()
token = open_file(os.path.join("TraoDoiSub", "token_traodoisub.txt")).strip()
handle_cookie(token)
handle_settings()
def execute_mission(mission, token, cookie):
    job = 0
    dem = 0
    if mission == 'follow':
        try:
            response = send_request(f"https://traodoisub.com/api/?fields=tiktok_follow&access_token={token}")
            if 'error' in response:
                if response['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                    print(f'Đang Get Nhiệm Vụ Follow {round(response.get("countdown", 0), 3)}', end='\r')
                    time.sleep(2)
                else:
                    print(response['error'], end='\r')
            else:
                if len(response['data']) == 0:
                    print("Hết Nhiệm Vụ Follow", end='\r')
                for i in response['data']:
                    link = i['link']
                    id_job = i['id']
                    try:
                        tiktok = Config_Tiktok(cookie)
                        tiktok.login()
                        tiktok.follow(link)
                        tiktok.outchrome()
                    except Exception as e:
                        try:
                            tiktok.outchrome()
                        except Exception:
                            pass
                        print(f"Lỗi: {e}")
                    response = send_request(f"https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW_CACHE&id={id_job}&access_token={token}")
                    tg = datetime.datetime.now().strftime('%H:%M:%S')
                    job += 1
                    dem += 1
                    if 'error' in response:
                        print(f"[{int(dem)}][FOLLOW][UNSUCCESS][{tg}][{id_job}]")
                    else:
                        print(f"[{int(dem)}][FOLLOW][SUCCESS][{tg}][{id_job}]")
                    custom_delay(delay)
                    if job == 10:
                        try:
                            response = send_request(f"https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW_API&id={id_job}&access_token={token}")
                            if response and response.get('success') == 200:
                                print(f"[NHẬN THÀNH CÔNG {response['data']['job_success']} NHIỆM VỤ][TUTORIAL {response['data']['xu_them']} XU][XU {response['data']['xu']}]")
                                job = 0
                            else:
                                print("[NHẬN XU KHÔNG THÀNH CÔNG]")
                        except Exception as e:
                            print(f"Lỗi: {e}")
        except Exception as e:
            print(f"Lỗi: {e}")
    if mission == 'like':
        try:
            response = send_request(f"https://traodoisub.com/api/?fields=tiktok_like&access_token={token}")
            if 'error' in response:
                if response['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
                    print(f'Đang Get Nhiệm Vụ Like {round(response.get("countdown", 0), 3)}', end='\r')
                    time.sleep(2)
                else:
                    print(response['error'], end='\r')
            else:
                if len(response['data']) == 0:
                    print("Hết Nhiệm Vụ Like", end='\r')
                for i in response['data']:
                    link = i['link']
                    id_job = i['id']
                    try:
                        tiktok = Config_Tiktok(cookie)
                        tiktok.login()
                        tiktok.like(link)
                        tiktok.outchrome()
                    except Exception as e:
                        try:
                            tiktok.outchrome()
                        except Exception:
                            pass
                        print(f"Lỗi: {e}")
                    response = send_request(f"https://traodoisub.com/api/coin/?type=TIKTOK_LIKE_CACHE&id={id_job}&access_token={token}")
                    tg = datetime.datetime.now().strftime('%H:%M:%S')
                    job += 1
                    dem += 1
                    if 'error' in response:
                        print(f"[{int(dem)}][LIKE][UNSUCCESS][{tg}][{id_job}]")
                    else:
                        print(f"[{int(dem)}][LIKE][SUCCESS][{tg}][{id_job}]")
                    custom_delay(delay)
                    if job == 10:
                        try:
                            response = send_request(f"https://traodoisub.com/api/coin/?type=TIKTOK_LIKE_API&id={id_job}&access_token={token}")
                            if response and response.get('success') == 200:
                                print(f"[NHẬN THÀNH CÔNG {response['data']['job_success']} NHIỆM VỤ][TUTORIAL {response['data']['xu_them']} XU][XU {response['data']['xu']}]")
                                job = 0
                            else:
                                print("[NHẬN XU KHÔNG THÀNH CÔNG]")
                        except Exception as e:
                            print(f"Lỗi: {e}")
        except Exception as e:
            print(f"Lỗi: {e}")
execute_mission(mission, token, cookie)