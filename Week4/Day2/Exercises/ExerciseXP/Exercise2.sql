-- 1)
select * from customer;
-- 2)
select (first_name, last_name) as full_name from customer;
-- 3)
select create_date from customer group by create_date;
-- 4)
select * from customer order by first_name desc;
-- 5)
select film_id, title, description, release_year, rental_rate from film order by rental_rate;
-- 6)
select address, phone from address where district = 'Texas';
-- 7)
select * from film where film_id in(15, 150);
-- 8)
select * from film where title = 'Matrix';
-- 9)
select film_id, title, description, length, rental_rate from film where title like 'Ma%';
-- 10)
select * from film order by replacement_cost limit 10;
-- 11)
select * from film order by replacement_cost offset 10 limit 10;
-- 12)
select c.first_name, c.last_name, p.amount, p.payment_date
from customer as c
join payment as p
on c.customer_id = p.customer_id
order by c.customer_id;
-- 13)
select * from film 
join inventory
on film.film_id = inventory.film_id;
-- 14)
select city.city, country.country
from city
join country
on city.country_id = country.country_id;
