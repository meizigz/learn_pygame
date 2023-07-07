'''
先产生一个整型随机数n；
循环
获取用户输入i并转为整数；
如果i>n那么就输出过大；
如果i<n那么就输出过小；
如果i=n就输出你猜中了，终止循环；
'''

import random

n = random.randint(1,20)

while True:
    x = int(input('Please input your answer:'))
    if x == n:
        print('答对了！')
        break
    elif x > n:
        print('Your input is bigger than the answer.')
    else:
        print('Your input is smaller than the answer.')
