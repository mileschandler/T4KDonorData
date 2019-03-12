import requests
from datetime import datetime, timedelta

url = 'https://nfp.everydayhero.com/api/v1/supporter_page_reports'
token = ''
headers= {'Authorization': 'Token token='+ token, 'Accept-Encoding': 'gzip, deflate, br', 'Host': 'npf.everydayhero.com', 'Origin': 'https://nfp.everydayhero.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36', 'Content-type': 'application/json', 'Accept': '*/*'}


now = datetime.now()
yesterday = (now - timedelta(days=1)).strftime("%Y-%m-%d")
today = now.strftime("%Y-%m-%m")
print (today)
print (yesterday)

payload = {"supporter_page_report":{"start_at":yesterday,"end_at":today,"organisation_id":"7717ddef-6908-4b09-9c3d-498aa4b9c081"}}
#r = requests.post(url, headers=headers, data=payload)
#print(r.text)

