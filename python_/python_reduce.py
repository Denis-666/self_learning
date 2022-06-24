from functools import reduce

def add (x,y):
    return x + y

b_list = [1,2,3,4]

answer = reduce(add,b_list)

print(answer)# 1 + 2 = 3 , 3 + 3 = 6 , 6 + 4 = 10

# 所以最后是10

