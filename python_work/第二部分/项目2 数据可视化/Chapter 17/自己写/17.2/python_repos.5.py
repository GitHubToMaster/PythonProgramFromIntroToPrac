# 自定义工具提示
import pygal
# 导入要应用于pygal图表的样式
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 可视化
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Python Projects"
chart.x_labels = ['httpie', 'django', 'flask']


# Python根据与键'value'相关联的数字来确定条形高度，
# 并使用与'label'相关联的字符串给条形工具创建提示
plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie.'},
    {'value': 15028, 'label': 'Description of django.'},
    {'value': 14798, 'label': 'Description of flask.'}
]

# add()方法接收一个字符串和列表
chart.add('', plot_dicts)
chart.render_to_file('bar_description.svg')