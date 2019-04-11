alien_0 = {'color' : 'green', 'points' : 5}
print(type(alien_0))
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print(alien_0['x_position'])
print(alien_0['y_position'])

del alien_0['x_position']
print(alien_0)


favorite_languages = {
    'jen': 'pyhton',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print(favorite_languages)
print("Sarah's favorite language is " + favorite_languages['sarah'].title())