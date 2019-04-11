# import pygal
import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = 'North, Central, and South America'
# 每次调用add方法每次都将为指定的国家显示一种新颜色
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy',
                         'pe', 'py', 'py', 'sr', 'uy', 've'])

# 将渲染出来的图保存到文件中
wm.render_to_file('americas.svg')