Inseting a row 插入单行:

    Values(default)--这里用default,而不写死一个值是因为 客户id 有可能重复。不如让系统自己决定 值为多少

    Insert into customers (
    first_name,
    last_name,
    birth_date,
    address,
    city,
    state)
    Values(
    'denis',
    'hu',
    '1990-1-1',
    'address',
    'LA',
    'CA'
    )

    其实这里的Vlues () 多写几个() 就能多行插入

Inserting Multiple Rows 插入多行:

    insert into shippers (name)
    values('Shipper1'),
          ('Shipper2'),
          ('Shipper3')

Inserting Hierarchical Rows 插入分层行:
因为表格有字母表关系，所以要同步插入数据
如何 查看 最近 新增主 key ？
就要用到 Last_insert_id

    Insert Into orders (customer_id,order_date,status)
    Values(1,'2019-01-02',1);

    insert Into order_items
    Values
        (Last_Insert_id(),1,1,2.95),
        (Last_Insert_id(),2,1,3.95)

Creating a Copy of a Table 创建表格的复制:
就是从一张表格 复制出 另外一张新表格
但新的表格 没有主 key 和 没有自动 加长功能，要记得钩上
create table [新表格名字] as
[旧表格名字]

    create table orders_archived as
    select * from orders

    只Insert 一部分去新表格

    Insert into orders_archived
    select *
    From orders
    where order_date < '2018-01-1'

    这里Insert 可以换成create table ，这样把查到的内容创建新的表格上面

Updating a Single Row 更新单行:
update [需要更新的表]
set [需要更新的列] = [数额为],可加多列
where [定位在列] = [数值为]

    例子:
    use sql_invoicing;

    update invoices
    set
        payment_total = 10,
        payment_date = '2019-03-01'
    where invoice_id = 1

Updating Multple Rows 更新多行:
update invoices
set
payment_total = invoice_total \* 0.5,
payment_date = due_date
where client_id = 3

    use sql_store;
    update customers
    set points = points + 50
    where birth_date < '1990-01-01'

Using Subqueries in Updates 在 Updates 中使用子查询:

    update invoices
    set
        payment_total =  invoice_total * 0.5,
        payment_date = due_date
    where client_id = (
    select client_id
    from clients
    where name = 'Myworks')

    这里的where name in（[可以放多个]，[多个]））
    用in （‘123’，‘321’） 这样格式


    例子：把 customers 表里面 potints > 3000的客户
        在orders 表里面 comments改为 'Golden Customers'

    use sql_store;

    update orders o
    set comments = 'Golden customers!!'
    where customer_id in (
        select c.customer_id
        from customers c
        where points > 3000)


    分析一下步骤：
        第一步：update 表格 orders
        第二步：是基于 orders 里面的 customer_id 去修改的
        第三步： 这个customer_id 搜寻条件 是（）括号里面的
        第四步: （）里面是多个结果，所以要用in

Deleting Rows 删除行:
如果不加 where 会整张表清空
例子:
dellete frome invoices
where invoice_id = 1

Restoring the Databases 恢复数据库:
