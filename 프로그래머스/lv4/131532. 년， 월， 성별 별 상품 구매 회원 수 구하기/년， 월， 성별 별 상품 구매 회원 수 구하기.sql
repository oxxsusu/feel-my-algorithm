select date_format(sales_date, "%Y") as year,
    date_format(sales_date, "%m") as month,
    gender,
    count(distinct info.user_id) as users
from user_info as info
join online_sale as sale
on info.user_id = sale.user_id
where info.gender in (0, 1) 
group by year, month, gender
order by year, month, gender