# 导入模块requests
import requests

# 执行API调用并存储响应
url = "http://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)

# status_code 可以让我们知道请求是否成功，状态码200表示请求成功
print("Status code: " + str(r.status_code))
print("Response text: " + r.text)


# 将API响应存储到一个变量中，由于api返回json数据格式，我们调用json方法转换为Python字典
respose_dict = r.json()


# 处理结果
print(respose_dict.keys())