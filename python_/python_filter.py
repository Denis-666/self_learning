'''
filter()函数用于过滤序列，过滤掉不符合条件的元素，返回符合条件的元素组成新列表。

filter(function,iterable)

function -- 判断函数。
iterable -- 可迭代对象


'''


def example_0():

    def func(x):
        if x in ['a','e','i','o','u']:
            return True
        else:
            return False
        
    msg_0 = ['z','b','p','k','o']
        
    msg_1 = ['h','e','l','k','o']

    print(list(filter(func,msg_1)))
    
    
def example_1():
    def is_odd(n):
        return n%2 == 1


    list_0 = filter(is_odd,[1,2,3,4,5,6,7,8,9,10])
    # 判断 
 
    print(list(list_0))


example_1()


