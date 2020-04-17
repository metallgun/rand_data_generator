
with cross_join as
(
	select s.*, m.name as month, m.start_date as month_start, m.end_date as month_end from subscriptions s
	cross join months m
),

table1 as 
(
	select 
		id,
		case
			when start_date < month_start and end_date > month_start then 1 else 0
		end as old_users,
		case
			when start_date between month_start and month_end then 1 else 0
		end as new_users,
		case
			when end_date between month_start and month_end then 1 else 0
		end as is_deactivated,
		month_start,
		cohort
	from cross_join cj
),

table2 as 
(
	select
		month_start,
		sum(old_users) as old_users,
		sum(new_users) as new_users,
		sum(is_deactivated) as users_deactivated,
		1.0 * sum(is_deactivated) / sum(old_users) as churn_rate
		/*
		sum(is_active_2) as active_users_2,
		sum(is_deactivated_2) as users_deactivated_2,
	
		sum(is_active_3) as active_users_3,
		sum(is_deactivated_3) as users_deactivated_3,
	
		sum(is_active_4) as active_users_4,
		sum(is_deactivated_4) as users_deactivated_4
		*/

	from table1
	where month_start not in ('2020-01-01', '2020-05-01')
	group by month_start
)

select
	month_start,
	old_users,
	users_deactivated,
	churn_rate,
	new_users,
	lag (new_users) over (order by month_start asc) as new_user_from_prev_month,
	1.0 * new_users / lag (new_users) over (order by month_start asc) - 1 as new_users_delta
from table2
order by month_start
;

---Проанализировать оттоковых пользователей: сколько месяцев живут в среднем до ухода