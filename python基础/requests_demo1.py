import requests
from dbutils import query
url ="http://opendata.baidu.com/api.php?query=172.20.10.11&co=&resource_id=6006&oe=utf8"
res =requests.get(url)
print(res.text)     #接口返回值


#断言：
assert res.status_code == 200 #http状态码
assert res.json()["status"]==0 #把结果转为json格式

#查询数据库
res=query('sql语句')
assert len(res)==1
print('测试用例执行成功')