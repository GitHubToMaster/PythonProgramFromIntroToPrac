import requests

# 执行API调用并存储响应
url = "http://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url) # API返回JSON格式的信息
print("Status Code:", r.status_code)
# 将API响应存储到一个变量中
response_dict = r.json()
print(response_dict.keys())