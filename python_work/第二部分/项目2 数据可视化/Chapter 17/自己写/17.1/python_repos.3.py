# 概述最受欢迎的仓库
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

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    # 打印项目的名称
    print("Name:", repo_dict['name'])  
    # 项目所有者是一个用字典表示的，因此使用键owner来访问表示所有者的字典，
    # 继续获得所有者的登录名
    print("Owner:", repo_dict['owner']['login'])
    # 打印项目获得了多少个星的评级
    print("Stars:", repo_dict['stargazers_count'])
    # 打印项目在GitHub仓库的URL
    print("Repository:", repo_dict['html_url'])
    # 打印项目的创建时间
    print("Created:", repo_dict['created_at'])
    # 打印项目的最后更新时间
    print("Updated:", repo_dict['updated_at'])
    # 打印项目的描述
    print("Description", repo_dict['description'])