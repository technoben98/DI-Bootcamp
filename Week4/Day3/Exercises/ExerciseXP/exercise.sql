-- -- 1)
-- select * from language;

-- -- 2)
-- select f.title, f.description, l.name 
-- from film as f
-- join language as l
-- on f.language_id = l.language_id;

-- -- 3)
-- select f.title, f.description, l.name 
-- from language as l
-- left join film as f
-- on f.language_id = l.language_id;

-- -- 4)
-- create table new_film ( 
-- 	id serial primary key, 
-- 	name varchar(100) 
-- );
-- insert into new_film (name) 
-- values
-- 	('Matrix'), 
-- 	('Harry Potter'),
-- 	('Ogniem i Mechem');

-- -- 5)
-- create table customer_review ( 
-- 	review_id serial primary key, 
-- 	film_id int, 
-- 	language_id int, 
-- 	title varchar(100), 
-- 	score int, 
-- 	review_text text, 
-- 	last_update date, 
	
-- 	foreign key (film_id) references new_film(id) on delete cascade, 
-- 	foreign key (language_id) references language(language_id) 
-- );

-- -- 6)
-- insert into customer_review (film_id, language_id, title, score, review_text, last_update) 
-- VALUES 
-- (
-- 	(select id from new_film where name = 'Matrix'), 
-- 	(select language_id from language where name = 'English'), 
-- 	'Matrix review', 10, 'Best movie EVER!', current_timestamp
-- ),(
-- 	(select id from new_film where name = 'Harry Potter'), 
-- 	(select language_id from language where name = 'English'), 
-- 	'Harry Potter review', 8, 'Movie about boy who survieved!', current_timestamp
-- ),(
-- 	(select id from new_film where name = 'Ogniem i Mechem'), 
-- 	(select language_id from language where name = 'Polish'),  
-- 	'Review Ogniem i Mechem', 8, 'This film about Rzech Pospolita', current_timestamp
-- );

-- -- 7)
-- delete from new_film where name = 'Harry Potter';

-- Exercise 2

-- 1) Doing 'English' language where another language
-- update film
-- set language_id = (SELECT language_id FROM language WHERE name = 'English') 
-- where language_id != (SELECT language_id FROM language WHERE name = 'English');

-- 2)
-- The foreign keys (references) defined for the customer table are:
-- 1. store_id - references the store table
-- 2. address_id - references the address table

-- 3)
-- drop table customer_review;

--4)
-- select count(*) as outstanding_rentals
-- from rental
-- where return_date is NULL;

-- 5)
-- select film.title, inventory.inventory_id, rental.rental_date, rental.return_date, payment.amount
-- from film
-- join inventory on film.film_id = inventory.film_id
-- join rental on inventory.inventory_id = rental.inventory_id
-- join payment on rental.rental_id = payment.rental_id
-- where rental.return_date is NULL
-- order by payment.amount desc
-- limit 30;

-- 6)
-- select film.title
-- from film
-- join film_actor on film.film_id = film_actor.film_id
-- join actor on film_actor.actor_id = actor.actor_id
-- where film.description like '%sumo wrestler%'
--   and actor.first_name = 'Penelope'
--   and actor.last_name = 'Monroe'
--   limit 1;

-- select film.title
-- from film
-- where film.length < 60
-- and film.rating = 'R'
-- limit 1;

-- select film.title
-- from film
-- join inventory on film.film_id = inventory.film_id
-- join rental on inventory.inventory_id = rental.inventory_id
-- join customer on rental.customer_id = customer.customer_id
-- join payment on rental.rental_id = payment.rental_id
-- where customer.first_name = 'Matthew'
--   and customer.last_name = 'Mahan'
--   and payment.amount > 4
--   and rental.return_date >= '2005-07-28' and rental.return_date <= '2005-08-01'
-- limit 1;

-- select film.title
-- from film
-- join inventory on film.film_id = inventory.film_id
-- join rental on inventory.inventory_id = rental.inventory_id
-- join customer on rental.customer_id = customer.customer_id
-- join payment on rental.rental_id = payment.rental_id
-- where customer.first_name = 'Matthew'
--   and customer.last_name = 'Mahan'
--   and (film.title like '%boat%' or film.description like '%boat%')
--   and film.replacement_cost > 4
-- limit 1;