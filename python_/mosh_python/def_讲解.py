



def save_user(**user):
    print(user)
    # ** 传送变量 会变 字典
    return user
    
    
# aaa = save_user(id=1,name='jhon',age=22)
 
# print(aaa)

def multiply(*numbers):
    # * 传送元组
    total = 1
    for number in numbers:
        print(total)
        total *= number
    return total
        
        
bbb = multiply(2,3,4,5)
print(bbb)




'''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''


# 关于全局变量，和 局部变量
# 这里教你 如何 用 def 改变 全局变量，但这种方法不可取，尽量不用，因为多个def 一起改 就天下大乱


message = 'aa'

def greet(name):
    global message
    message = 'b'
    
    
# greet('ccc')

# print(message)


