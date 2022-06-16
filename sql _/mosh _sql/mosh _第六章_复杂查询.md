
subqueries 子查询:

    下面例子中 ()里面写的就是sub queries 子查询
    例子:

        找到 比 lettuce(id=3)还贵的全部商品

        select * 
        from products
        where unit_price > (
            select unit_price
            from products
            where product_id = 3
        )

    例子：

        在sql_hr 里面 找到 员工 薪酬是比 平均高

        select *
        from employees
        where salary > (
            select avg(salary)
            from employees
        )

the in operator  in运算符:

    这里做个批准 distinct是唯一的意思，如果搜寻结果重复的 ，只会出现一次


    not in 不在这里面:

    例子:
    在products里面 找出来 没被 order_items 里面出现的 id
    翻译就是，在库存里面找出 从来没被下单的 商品

    select *
    from products
    where product_id not in(
        select distinct product_id
        from order_items)


subqueries vs joins  子查询 vs 连接 ：

        