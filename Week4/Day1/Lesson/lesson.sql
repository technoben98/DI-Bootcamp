-- create table house_expenses(
-- id serial primary key,
-- date_paid date,
-- electricity float,
-- water float,
-- paid_by varchar(50)
-- );

-- insert into house_expenses (date_paid, electricity, water, paid_by)
-- values
-- ('2023-01-01', 55.5, 66.6, 'Adam')
-- insert into house_expenses (date_paid, electricity, water, paid_by)
-- values
-- ('2023-03-01', 55.5, 66.6, 'Adam'),
-- ('2023-05-01', 55.5, 66.6, 'Adam'),
-- ('2023-07-01', 55.5, 66.6, 'Adam'),
-- ('2023-09-01', 55.5, 66.6, 'Adam'),
-- ('2023-11-01', 55.5, 66.6, 'Adam')
-- ;
-- select * from house_expenses;
-- select electricity from house_expenses;
-- select electricity, water from house_expenses;
-- select * from house_expenses where id=1 or id=2;
-- select max(water) from house_expenses;
-- select min(electricity) from house_expenses;
-- select avg(electricity) from house_expenses where paid_by = 'Adam';
-- select paid_by, max(electricity) from house_expenses
-- group by paid_by;
-- select * from house_expenses
-- select paid_by, sum(electricity)as sum_electricity, sum(water) as sum_water, 
-- max(electricity) as max_electricity, max(water) as max_water from house_expenses
-- group by paid_by;
-- update house_expenses
-- set electricity = 0 where paid_by = 'Adam';
-- update house_expenses
-- set paid_by = 'Ben' where id=1;


-- delete from house_expenses where electricity < 50;
delete from house_expenses where date_paid > '2023-09-05';
select * from house_expenses order by id;
