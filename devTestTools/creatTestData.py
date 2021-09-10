import random
import string

def get_str():
    # 26个字母的大小写
    str = string.ascii_letters
    # 26个字母大写
    str = string.ascii_uppercase
    # 26个字母小写
    str = string.ascii_lowercase
    # 符号
    str = string.punctuation
    # 0-9数字
    str = string.digits

    return str


def get_random_Email(min,max,number):
    str = get_str()
    email_list = []
    for i in range(0,number):
        # 获取x-y中的随机整数
        a = random.randint(min,max)
        b = random.randint(2,8)
        A = []
        for i in range(1,a+1):
            # 在指定的字符串中随机取x个字符
            num = random.sample(str,1)
            A = A + num
        B = random.sample(string.ascii_lowercase,b)
        email = ''.join(A)+'@'+''.join(B)+'.com'
        email_list.append(email)
    return email_list