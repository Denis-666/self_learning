IP = [192,168,10,32]
Subnet_Mask = ["11111111","11111111","11111111","11000000"]

def Transformation_IP_to_binary(IP):
    IP_binary = []
    for i in IP:
        IP_binary.append('{0:08b}'.format(i))# 指定长度为8,转换二进制
        
    print(IP_binary)
    return IP_binary



def get_CIDR_form_Subnet_Mask(Subnet_Mask):
    print(f'Subnet_Mask:',int(Subnet_Mask[0],2),int(Subnet_Mask[1],2),int(Subnet_Mask[2],2),int(Subnet_Mask[3],2))

    Mask_number = 0

    CIDR = 0

    for i in range(4):
        for i in Subnet_Mask[Mask_number]:
            if i == '1':
                CIDR +=1
                # print(CIDR)
            
        Mask_number += 1


    print(f'CIDR:{CIDR}')
    return CIDR




CIDR = get_CIDR_form_Subnet_Mask(Subnet_Mask)
print(f'IP:{IP[0]},{IP[1]},{IP[2]},{IP[3]}/{CIDR}')


'''
C类：
    地址范围：192.0.1.1-223.255.255.254

    网络号段范围：192.0.1 ~ 223.255.255

    子网掩码：255.255.255.0 或  0xFFFFFF00 (十六进制)

        私有号段：192.168.0.0-192.168.255.255

        前3个字节(24位)为网络号，后1个字节(8位)为主机号。

        前3位固定为110。

        最大网络数：2^21 - 1

        最大主机数：2^8 - 2

    一般用于小型网络。=

'''

'''

2^8 = 256 
但计算机是从0 开始数的，所以 最大为 255
2是 0和1 两种组合的意思
8是 8个位

'''