查...

按顺序输入

use : 是 use 那一个数据库，use 后面填 数据库

select : 选取你需要的列，因为一些数据库有几百万行，所以一般 声明出来具体哪一列，而不是\*，

    as ： 把列表 比如 age，可以 age+100 as 'age_plus'，这样 age就会变 +100 后，名字改为 'age_plus'

    Distinct : 这里的用法是 独特的意思，， 比如说 有一堆客户 27岁 28 岁 29岁，各有 5个人，但输入        Distinct 后 只会显示 27.28.29

    From : From 数据库里面的那一张表

    where : 条件语句,比如 age>25,(当年我这么多号，就是一句where给搞死了！tm的！)(> ,< ,=,>=,<=, !=,<> 最后两个都是不等于)

        运算等级：* / 的运算等级高于 + -
            可以用（）改变运算顺序

        AND , OR ,NOT ：也能写进去 条件语句里面
            例子: where age > 10 and age <30

        IN ：是吧条件写在里面，在IN 里面寻找
            例子: where age IN ('22','23','24','25')

        NOT IN ： 跟上面的翻着来

        BETWEEN ：在这之间,用and隔开
            例子: where age between 10 and 30
            其实等于 where age > 10 and age < 30

        小提示: 日期可用 '1990-01-01' 这种格式表示
            例子 ： where days between '1990-01-01' and '20200-01-01'


        LIKE ：配对功能
            要求 找 first_name 里面 a 开头的，用到正则表达式
            where First_name like 'a%'

            正则表达式，这东西必修，我也很无奈，，，

            a 开头 后面 无限跟 ： a%
            无限开头 a结尾 :     %a
            字段包含ufo : %ufo%
            字段 不！包含ufo ： not like "%ufo%" (上面是like，做比较)
            两个字母 后面字母结尾a: _a
            三个字母 最后字母为a : __a （如此类推）
            4个字母 b开头 a结尾 :b__a （如此类推）


        REGEXP：regular expression 的缩写 加强版的like
            找单个匹配：
            字段包含ufo : where First_name REGEXP 'ufo'
            字段前开始为 ufo：'^ufo'
            字段结尾为 ufo: 'ufo$'
            找多个匹配：where First_name REGEXP 'ufo|rose|jack'
            可以把单个寻找条件，放进去多个里面 : where First_name REGEXP '^ufo|rose$|jack'
            同时寻找 gm,im,om ，前面不一样后面连个M 用[]: where First_name REGEXP '[gio]m'
            同样可以调转 'm[gio]' 得到 mg,mi,mo
            []里面还能放连续字母 比如，ABCD 表达为 : '[a-d]
            1.^ beginning
            2.$ end
            3.| logical or
            4.[abcd] （可以不连贯)
            5.[a-d]


        IS NULL:判空
            就是判断是否空，没啥好讲
            例子: where age IS NULL


        Order by:排序
            例子：Order by age（默认升序)
            DESC ：descending 缩写 下降
            例子：Order by age DESC


        Limit clause:限制输出
            例子: Limit 3（前三个，放在最后的地方）
            求，emplotyees 里面 年纪最大的三个:
            解：select * From emplotyees
                Order by age DESC
                Limit 3

        JOIN: 结合两列 作为一体 JOIN ON

            例子: (这里例子是同一个db)
                select *
                from orders
                Join customers
                    ON orders.customer_id = customers.customer_id

                    就是 orders 里面的 customer_id，和 customers里面的 customer_id 相同


        缩写：把表的名字缩写
            缩写是从From哪里开始的，不像 vbs，python ，从头开始，我感觉执行层面就是From开始读取。
            写好from缩写后，可以把select的改了。

            例子:
                select *
                from orders
                Join customers
                    ON orders.customer_id = customers.customer_id

            缩写后：
                select *
                from orders o
                Join customers c
                    ON o.customer_id = c.customer_id


        跨数据库查询:
            就是在表前面加上 数据库名字， 这意味着如果不写数据库名字，在不同 指针在不同数据库中，表的名字不同。
            就是说，如果没指定，在目前数据库 找不到这张表。而必须用use 数据库。但跨数据库查询 不能use 两次，，use一般用于写入.

                例子：数据库名字叫 db1
                select * from db1.orders


        Self join:
            单表连接
            同一张表中，关联，这里例子的e表和m表 其实是同一张表
            这张表里面的员工 归属同一个经理管
            select
                e.employee_id, //只显示employee_id
                e.first_name, //只显示first_name
                m.first_name as manager //只显示 m的first_name，就是经理的名字
            from employees e //从 employees as e 里面
            join employees m // 关联表格 employees as m
                on e.reports_to = m.employee_id // on 关联在 e表的reports_to，对应 m表的 employee_id

                这样把 m表的 关联后面 全部显示出来，包括 经理的 什么 job_title,salary,office_id。

        Joining Multiple Tables:
            多表连接
            在实际运行中，有可能是 join 10多张表

            use sql_store;

            select
                o.order_id,
                o.order_date,
                c.first_name,
                c.last_name,
                os.name as status
            from orders o
            join customers c
                on o.customer_id = c.customer_id
            join order_statuses os
                on o.status = os.order_status_id



            Compound Join Conditions:
                复合连接条件:
                就是，之前都用一个表里面的一列 比如 order_id  作为 唯一连接 选项
                这次用多个列，粘合在一起，然后作为 和其他表格的连接选项
                需要把 粘合的列 设置为 Primary key 就是主键 ，双主键，或多个

                use sql_store;

                select *
                from order_items oi
                join order_item_notes oin
                    on oi.order_id = oin.order_id
                    and oi.product_id = oin.product_id


            Implicit Join Syntax 隐式连接语法:
                use sql_store;

                select *
                From orders o,customers c
                where o.customer_id = c.customer_id

                这个和 join 上面那个 一样，但 不建议使用，因为如果 忘了打where 就会导致 交叉
                每个表 10 行，如果忘了 where 就会 10 * 10 = 100 行

                每一行 都会和另外一个表里 每一行 join


            outer join 外链接:
                use sql_store;

                select *
                from orders o
                LEFT outer join customers c
                    on c.customer_id = o.custumer_id
                order by c.customer_id

                就是把左边表格 from （表格），全部显示出来，就算右边表格 Left outer join （表格） 没有，也显示出行

                right outer join一样道理，位置倒转



            using 关键字简化连接 查询:
            使用using关键字简化连接时，需要注意以下几点：
            1.使用emp表和dept表中的deptno列进行连接时，在using子句和select子句中，都不能为deptno列指定表名或表别 名。
            2.如果在连接查询时使用了两个表中相同的多个列，那么久可以在using子句中指定多个列名，形式如下：
            '''
                select... from table1 inner join table2

                using(column1,column2)
                                        '''
                相等于
            '''
                select... from table1 inner join table2

                on table1.column1=table2.column2

                and table1.column2=table2.column2;
                                                    '''

            如果对多个表进行检索，就必须多次使用using关键字进行指定，形式如下：
            '''
            select... from table1

            inner join table2 using(column1)

            inner join table3 using(column2);
                                            '''
            相等于
            '''
            select... from table1,table2,table3

            where table1.column1=table2.column1

            and table2.column2=table3.table2;
                                            '''


            Natural Join 自然连击:
                就是用算法，把两个表自己链接起来

                use sql_store;

                select
                    o.order_id,
                    c.first_name
                from orders o
                Natural join customers c

                因为很大可能出错，所以 不推荐使用


            Cross join 交叉连接：
                之前上面有讲过，from 两个表，也是这个效果
                把两个表的每一行 都和 另外一个表 每一行 连接

                use sql_store;

                select
                    o.order_id,
                    c.first_name
                from orders o
                Cross join customers c


            Unions 联合:
                把不同查询条件 联合 起来 显示在同一张表上

                select
                    order_id,
                    order_date,
                    'inActive' As status
                From orders
                Where order_date < '2018-01-01'
                Union
                select
                    order_id,
                    order_date,
                    'Active' As status
                From orders
                Where order_date >= '2018-01-01'

            这里意思是，2018年前的订单 显示为 inactive




































改....

例：UPDATE `py_testing_db1`.`employees` SET `MARITAL_STAT` = 'Single' WHERE (`EMP_ID` = '1003');

UPDATE 更新 数据库.表名 set：修改内容 把 `MARITAL_STAT` 改为 'Single'，定位在 `EMP_ID` 里面的 '1003' 中
这里的 EMP_ID 是主 KEY，每一个客户都唯一一个 ID
