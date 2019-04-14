# 重构后的代码2
import json

# 如果以前存储了用户名，就加载它
#   否则，就提示用户输入用户名并存储它

def get_sorted_username():
    """
    如果存储了用户名，就获取它
    """
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """
    问候用户，并指出其名字
    """
    username = get_sorted_username()
    if username:
        print("Welcome back, " + username)
    else:
        username = input("What is your name？")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remermber you when you come back, " + username + "!")

greet_user()