-- create table countries(
-- id serial primary key,
-- name varchar (50)
-- );
-- select * from countries;
-- insert into countries (name)
-- values
-- ('USA'),
-- ('UK');

-- create table movies(
-- 	movies_id serial primary key,
-- 	movie_title varchar(50),
-- 	movie_story text,
-- 	country_id integer,
	
-- 	foreign key(country_id)references countries(id)

-- );

-- insert into movies(movie_title, movie_story, country_id)
-- values(
-- 	'Phantomas',
-- 	'Movie about phantomas',
-- 	(select id from countries where name = 'France')
-- );

-- select m.movie_title, c.name
-- from movies as m
-- join countries as c
-- on m.country_id = c.id

-- create table producers(
-- 	id serial primary key,
-- 	first_name varchar(30),
-- 	last_name varchar(30),
-- 	movie_id integer,
	
-- 	foreign key(movie_id) references movies(movies_id)
-- );

-- insert into movies(first_name, last_name, movie_id)
-- values(
-- 	'Lana',
-- 	'Waczowski',
-- 	(select id from movies where movie_name = 'Matrix')
-- 	),
-- 	(
-- 	'Lily',
-- 	'Waczowski',
-- 	(select id from movies where movie_name = 'Matrix')
-- 	),
-- 	(
-- 	'Charles', 'Roven', (select id from movies where movie_name = 'Oppenhaimer')
-- 	)
-- ;

