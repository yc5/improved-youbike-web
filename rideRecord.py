import requests
import json

def str_to_datetime(s):
  tmp = ''
  for y in range(int(len(s)/2)):
    tmp += s[2*y:2*y+2] + ' '

  tmp = tmp.rstrip()
  tmp = tmp.split(' ')
  return tmp[0]+tmp[1]+'/'+tmp[2]+'/'+tmp[3]+' '+tmp[4]+':'+tmp[5]+':'+tmp[6]

def get_token(phone,password):
  my_data = {
    "phone": phone,
    "password": password,
    "lang": "tw",
    "login_from": "web"
  }
  r = requests.post('https://apis.youbike.com.tw/tw1/login', data = my_data)
  r = r.json()
  return r['retVal']['token']

def print_card_history(card_no,token):
  my_headers = {    
      'Authorization': 'Bearer ' + token
  }
  r = requests.get('https://apis.youbike.com.tw/tw1/rideRecord?card_no='+card_no, headers = my_headers)
  r = r.json()

  print('//card_no:'+card_no)
  for x in r['retVal']:
    rdat = str_to_datetime(x['rdat'])
    tdat = str_to_datetime(x['tdat'])  
    print(rdat+','+x['rsna']+','+tdat+','+x['sna']+','+x['bno']+','+x['ramt'])



token = get_token('PHONE_NUMBER','PASSWORD')
print_card_history('CARD_NUMBER', token)
