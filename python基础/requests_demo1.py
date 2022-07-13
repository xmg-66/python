import requests
url ="https://fanyi-api.baidu.com/api/trans/vip/translate?q=我的名字是徐明高&from=zh&to=en&appid=20220309001118111&salt=20001007&sign=e32badc0f992945f3eea91b176dd3d6d"
res =requests.get(url)
print(res.text)