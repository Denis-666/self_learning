class A():
    age = 10


obj2 = A()
obj3 = A()

def 情形1():
    print(obj2.age, obj3.age, A.age)

    # 10,10,10

def 情形2():
    obj2.age+=2
    print(obj2.age, obj3.age, A.age)
    # 12,10,10


def 情形3():
    A.age+=3
    print(obj2.age, obj3.age, A.age)
    # 13 13 13 


情形1()

