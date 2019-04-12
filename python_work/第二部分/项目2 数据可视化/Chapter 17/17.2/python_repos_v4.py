# 在图表中添加可以单击的链接
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
print("Number of items:", len(repo_dicts))


names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        # pygal根据与键'xlink'相关联的URL将每个条形都转换为活跃的链接
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)


# 可视化
my_style = LS('#333366', base_style=LCS)

# 定制图表的外观
my_config = pygal.Config()
# 设置X轴标签旋转
my_config.x_label_rotation = 45
# 设置
my_config.show_legend = False  #
# 设置图表标题字体大小
my_config.title_font_size = 24
# 设置图表副标签字体大小
my_config.label_font_size = 14
# 设置图表主标签字体大小
my_config.major_label_font_size = 18
# 将图表中较长项目的字体的个数压缩到15个字符，如果将鼠标移动到对应的标签上，将会显示完整的项目名称
my_config.truncate_label = 15
# 隐藏图表中的水平线
my_config.show_y_guides = False
# 自定义图表的宽度，可以让图表更充分的利用浏览器中的可用空间
my_config.width = 1000

## 创建一个简单的条形图，第2个参数是让标签绕X轴旋转45度，并隐藏图例
# 通过第一个实参传递了所有的配置设置，我们可以通过my_config做任意数量的样式和配置修改
chart = pygal.Bar(my_config, style=my_style)
# 设置图表的标题
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names
# 由于我们不需要给这个数据系列添加标签，因此在添加数据的时候，将标签设置成空字符串
chart.add('', plot_dicts)
chart.render_to_file('python_repos4.svg')
