import json
import requests

url = 'https://api.github.com/some/endpoint'
payload = {'some':'data'}
headers = {'Content-Type':'application/json', 'Authorization':'some token'}

r = requests.post(url, data=json.dumps(payload), headers=headers)

r = requests.get('http://google.com')
r.status_code == requests.codes.ok

r.headers
r.header['Conent-Type']

url = 'http://somewebsite/some/cookie/setting/url'
r = requests.get(url)
r.cookies['some_cookie_name']

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
r.text -- '{"cookies": {"cookies_are":"working"}}'

r = requests.get('http://google.com')
r.url
r.status_code
r.history

requests.get('http://google.com', timeout=0.03)