import requests,re,random,time,os

def Email():
	rand = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	email = str(''.join(random.choice(rand) for i in range(int(random.randint(6,9)))))+random.choice(["@gmail.com","@hotmail.com","@yahoo.com","@live.com"])
	return email
message = input("Enter Message - دخـل الكلـيشه :")
phone = input("Enter phone - دخـل الرقـم :")
cookies = {
    'stel_ssid': 'cd2917a1af2f1b01b8_603937409023394492',
}

headers = {
    'authority': 'telegram.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'stel_ssid=cd2917a1af2f1b01b8_603937409023394492',
    'origin': 'https://telegram.org',
    'referer': 'https://telegram.org/support',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

data = {
    f'message': {message},
    f'email': '{}'.format(Email()),
    f'phone': {phone},
    'setln': 'ar',
}
while True:
	req = requests.post('https://telegram.org/support', cookies=cookies, headers=headers, data=data).text
	res_get = re.compile(r'<div class="alert alert-success"><b>(.*?)</b><br/>(.*?)</div>', re.DOTALL)
	match = res_get.search(req)
	if match:
		  responses = match.group(1) + " " + match.group(2)
		  if "شكرًا على بلاغك&#33; سنحاول الرّد بأسرع ما يمكن." in responses :
		  	print("""- Done Send Report
.----.     .----.   .----.    
| {}  }   { {__     | {}  }   
| .-. \   .-._} }   | .-. \   
`-' `-'   `----'    `-' `-
Ｄｍｉｔｒｙ　さ謁悦'""")
		  	
