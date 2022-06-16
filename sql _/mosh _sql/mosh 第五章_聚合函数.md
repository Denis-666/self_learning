Aggregate Functions 聚合函数:

    Select
        max(invoice_total) as highest,
        min(invoice_total) as lowest,
        avg(invoice_total) as average,
        sum(invoice_total * 1.1) as total,
        count(*) as total_records
    From invoices
    where invoice_date >= '2018-07-01'

    distinct 唯一 就是重复的id 不再统计:
        Select
            max(invoice_total) as highest,
            min(invoice_total) as lowest,
            avg(invoice_total) as average,
            sum(invoice_total * 1.1) as total,
            count(distinct client_id) as total_records
        From invoices
        where invoice_date >= '2018-07-01'
        

The group by clause (就是进行多列的数据分组，比如 按单个客人 总共下单金额):

    select 
        client_id,
        sum(invoice_total) as total_sales
    from invoices
    group by client_id


    select 
        date,
        pm.name as payment_method,
        sum(amount) as total_payments
    from payments p
    join payment_methods pm
        on p.payment_method = pm.payment_method_id
    group by date,payment_method
    order by date


Having  分组之后 再筛选数据:
    筛选以后不能用where 过滤
    注意点：
        1:Having 里面的条件 必须在select 里面出现,反观where 不需要
         
    单个筛选
    select 
        client_id,
        sum(invoice_total) as total_sales
    from invoices
    Group by client_id
    Having total_sales > 500

    多个筛选
    select 
        client_id,
        sum(invoice_total) as total_sales,
        count(*) as number_of_invoices
    from invoices
    Group by client_id
    Having total_sales > 500 and number_of_invoices > 5



The Rollup Operator    Rollup运算符:
    就是 在数据下面加一个 总和

    select 
        state,
        city,
        sum(invoice_total) as total_sales
    from invoices i 
    join clients c using(client_id)
    group by state,city with rollup


