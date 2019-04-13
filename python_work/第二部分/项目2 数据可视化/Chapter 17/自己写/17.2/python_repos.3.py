# 概述最受欢迎的仓库
import requests
import pygal
# 导入要应用于pygal图表的样式
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 执行API调用并存储响应
URL = "http://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(URL) # API返回JSON格式的信息
print("Status Code:", r.status_code)

# 将API响应存储到一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化

## 使用LightenStyle类定义一种样式，并将基色设置为深蓝色，同时还传递了实参base_style
my_style = LS('#333366', base_style=LCS)
# x_label_rotation让标签绕x轴旋转45度
# show_legend隐藏了图例
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')