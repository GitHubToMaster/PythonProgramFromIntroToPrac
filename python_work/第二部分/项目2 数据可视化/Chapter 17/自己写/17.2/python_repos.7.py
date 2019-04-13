# 在图表中添加可以单击的链接
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

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    print(type(repo_dict['description']))
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        # Python根据与键'xlink'相关联的URL将每个条形都转换为活跃的链接
        # 单击图表中的任何条形都会在浏览器中打开一个新的标签页
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)

# 创建一个Pygal类Config的实例，并将其命名为my_config
# 通过修改my_config可以定制图表的外观
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
# 设置图表的标题字体，副标签字体大小，主标签字体大小
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
# 将较长的项目名称缩短为15个字符
my_config.truncate_label = 15
# 隐藏图中的水平线
my_config.show_y_guides = False
# 自定义宽度，让图表可以更充分利用浏览器中的空间
my_config.width = 1000


chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos3.svg')