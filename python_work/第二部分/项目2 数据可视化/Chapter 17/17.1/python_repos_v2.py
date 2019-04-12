import requests


# 执行API调用并存储响应
url = "http://api.github.com/search/repositories?q=language:python&sort=stars"
resp = requests.get(url)

# status_code 可以让我们知道请求是否成功，状态码200表示请求成功
print("Status Code: " + str(resp.status_code))


# 将API响应存储在一个变量中
response_dict = resp.json()
print("Total repositories : ", response_dict['total_count'])


# 探索有关仓库的信息
repo_dicts = response_dict['items']
print(type(repo_dicts))
print("Repositories returned:", len(repo_dicts))
print(repo_dicts)


# 研究第一个仓库
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
print(repo_dict)
for key in sorted(repo_dict.keys()):
    print(key)