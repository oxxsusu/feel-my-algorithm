-- 코드를 입력하세요
SELECT distinct car.car_id
from car_rental_company_car as car
join car_rental_company_rental_history as history on car.car_id=history.car_id
where car.car_type in ("세단")
and date_format(history.start_date, "%m") in ("10")
order by 1 desc