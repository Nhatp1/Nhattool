import requests, re, time

def nghingoi(delay):
    for i in range(delay, -1, -1):
        print(f"\rĐợi {i} giây trước khi tiếp tục like bài viết...", end="")
        time.sleep(1)
    print("\r")

class ApiFacebook():
    def __init__(self, COOKIE) -> None:
        cookie = COOKIE.split(';')
        title = []
        value = []
        for i in range(len(cookie) - 1):
            title.append(cookie[i].split('=')[0].strip())
            value.append(cookie[i].split('=')[1].strip())
        self.COOKIE = dict(zip(title, value))
        self.headers = {
            'authority': 'mbasic.facebook.com',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Cache-Control': 'max-age=0',
            'Dpr': '1',
            'Sec-Ch-Prefers-Color-Scheme': 'light',
            'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'Sec-Ch-Ua-Full-Version-List': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.127", "Google Chrome";v="126.0.6478.127"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Model': '""',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Ch-Ua-Platform-Version': '"10.0.0"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'Viewport-Width': '811'
        }
        try:
            self.UID = self.COOKIE['m_page_voice']
        except:
            self.UID = self.COOKIE['c_user']
    
    def get_user(self):
        home = requests.get(f"https://mbasic.facebook.com/{self.UID}/", headers=self.headers, cookies=self.COOKIE).text
        username = home.split('<title>')[1].split('<')[0]
        if "Facebook" in username:
            return False
        else:
            return username
    
    def LikeBaiDeXuat(self, delay, delay_protection):
        home = requests.get("https://mbasic.facebook.com", cookies=self.COOKIE, headers=self.headers).text
        baiviet = re.findall(r'a\/like.php\?(.*?)"', home)
        for bv in baiviet:
            try:
                like = "https://mbasic.facebook.com/a/like.php?"+bv.replace("amp;","")
                requests.get(like, cookies=self.COOKIE, headers=self.headers)
                success.append(like)
                print(len(success),"Thành công like bài viết!")
            except:
                print(len(success),"Thất bại like bài viết!", end="")
            nghingoi(delay)
        if len(baiviet) > 0:
            print("Đã like tất cả bài viết đề xuất tool sẽ off Facebook và vài giây nữa vào lại!")
        else:
            print("Không tìm thấy bài viết đề xuất! tool sẽ off Facebook và vài giây nữa vào lại!")
        nghingoi(delay_protection)
        print("Bắt đầu truy cập facebook và làm tiếp!")

success = []
cookie = input("Nhập cookie acc cần đi auto like bài viết dạo: ")
delay = int(input("Nhập delay mỗi lần like: "))
chongblock = int(input("Nhập delay nghĩ cao khi hết bài viết đề xuất sẽ nghĩ(Lưu ý thời gian cao để tránh block): "))
FB = ApiFacebook(cookie)
user = FB.get_user()
if user:
    print(user)
    while True:
        FB.LikeBaiDeXuat(delay, chongblock)
else:
    exit("Cookie die hoặc acc bạn bị cấm dùng mbasic!")
