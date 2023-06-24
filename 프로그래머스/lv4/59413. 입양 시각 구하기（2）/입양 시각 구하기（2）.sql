with recursive time as (
    select 0 as hour
    union all
    select hour+1 from time
    where hour<23
)

# select * from time

SELECT 
    time.hour as hour,
    case when time.hour in (select date_format(a.datetime, "%H") from animal_outs) then count(*)
    else 0 end as count
from animal_outs as a
right join time on time.hour = date_format(a.datetime, "%H")
group by time.hour
order by time.hour;
