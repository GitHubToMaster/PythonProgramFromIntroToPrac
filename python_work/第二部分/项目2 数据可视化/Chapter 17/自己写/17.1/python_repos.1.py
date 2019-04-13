# 处理响应字典
import requests

# 执行API调用并存储响应
url = "http://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url) # API返回JSON格式的信息
print("Status Code:", r.status_code)

# 将API响应存储到一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# 研究第1个仓库
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)