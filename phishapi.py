import requests, json


def check(target):
	url = "http://checkurl.phishtank.com/checkurl/"
	payload = {}
	payload['url'] = target
	payload['format'] = "json"
	payload['app_key'] = "d6ca7d8d845d2b4fd5ec9be70f78ed6c532269caad66c54a16cf4e1cd086e927"
	r = requests.post(url = url,data=payload)
	js = json.loads(r.text)
	try:
		if js['results']['valid'] == True:
			print target
	except:
		pass


f = open("web.json")
js = json.load(f)
f.close()
for i in js:
	check(str(i['url']))

