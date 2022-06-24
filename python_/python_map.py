def square(number):
    return number**2

a_list = [3,2,5,7,8,9,0,5,4,2]

print(list(map(square,a_list))) # 把 a_list 里面每一个都放进去 square 运算

