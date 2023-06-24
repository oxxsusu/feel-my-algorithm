-- 코드를 입력하세요
select date_format(start_date, "%m") as MONTH, 
    CAR_ID,
    count(*) as RECORDS
from car_rental_company_rental_history
where car_id in (select car_id from car_rental_company_rental_history
     where date_format(start_date, "%Y-%m-%d") between "2022-08-01" and "2022-10-31"
     group by car_id having count(history_id) >= 5 and date_format(start_date, "%Y-%m-%d") between "2022-08-01" and "2022-10-31")
group by car_id, month
having records > 0
order by month, car_id desc;