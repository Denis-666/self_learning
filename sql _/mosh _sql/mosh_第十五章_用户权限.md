


Creating a User 创建用户：
    Create user [name]@[ip address]
    Create user [name] Identified by '[密码]'

    ip address : @ 后面加下列
                196.0.0.1 本机ip
                localhost
                codewithmosh.com  从网站链接
                '%.codewithmosh.com'  从这网站的子网域链接

    Identified by :
                    '[密码]'

    Create user john Identified by '12345'



viewing user 查看用户:
    在一个叫mysql的数据库里面有 表 叫 user
    我在mysql workBench 居然肉眼找不到

    select * from mysql.user;

    原来左上角 有 Administration ，里面可以看user=，= 我用了这么久才知道


Dropping users 删除用户:

    drop user john


Changing passwords 更改密码:

    set password for [用户名] = [要改的密码]


Granting Privileges 给予权限:

    例：
    给 用户叫 moon_app 的，增删改查，运行，的权利，仅仅在 数据库 sql_store里面

     Grant select,insert,update,delete,execute
     on sql_store.*
     to moon_app

     例子： 
        给用户全部的权限,仅仅在 数据库 sql_store里面
        grant all
        on sql_store.*


viewing privileges 查看权限 :

    也可以点击，左上角 ，管理员，用户权限，点击用户，schema privileges

    例子:
      show grants for john;


Dropping Privileges 取消权限:

    Revoke

    from

    例子:
        revoke select 
        on sql_store.*
        from moon_app

        




    



