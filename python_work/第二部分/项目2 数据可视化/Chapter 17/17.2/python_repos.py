import requests
# 首先导入pygal以及要应用于图表的Pygal样式
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
URL = "http://api.github.com/search/repositories?q=language:python&sort=stars"
response = requests.get(URL)
print("Status Code: ", response.status_code)


# 将API响应存储到一个变量中
response_dict = response.json()
print("Total repositories: ", response_dict['total_count'])


# 研究有关仓库的信息
repo_dicts = response_dict['items']

names, stars = [], []
for rep_dict in repo_dicts:
    names.append(rep_dict['name'])
    stars.append(rep_dict['stargazers_count'])


# 可视化
my_style = LS('#333366', base_style=LCS)


## 创建一个简单的条形图，第2个参数是让标签绕X轴旋转45度，并隐藏图例
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names
# 由于我们不需要给这个数据系列添加标签，因此在添加数据的时候，将标签设置成空字符串
chart.add('', stars)
chart.render_to_file('python_repos.svg')