# 添加自定义工具提示
import pygal
from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(my_style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Python Projects"
chart.x_labels = ['httpie', 'django', 'flask']

# 根据与键value相关联的数字来确定条形的高度，并使用"label"相关联的字符串给条形创建工具提示
plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie.'},
    {'value': 15028, 'label': 'Description of django.'},
    {'value': 14798, 'label': 'Description of flask.'},
]

chart.add('', plot_dicts)
chart.render_to_file('bar_description.svg')