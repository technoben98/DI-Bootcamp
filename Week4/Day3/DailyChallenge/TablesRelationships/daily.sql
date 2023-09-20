-- PART 1

-- create table customer(
-- 	id serial primary key,
-- 	first_name varchar(30),
-- 	last_name varchar(30) not null unique
-- );

-- create table customer_profile(
-- 	id serial primary key,
-- 	is_logged_in boolean default false,
-- 	customer_id int,
	
-- 	foreign key (customer_id) references customer(id) 
-- );

-- insert into customer(first_name, last_name) values('John', 'Doe');
-- insert into customer(first_name, last_name) values('Jerome', 'Lalu');
-- insert into customer(first_name, last_name) values('Lea', 'Rive');
-- insert into customer_profile (is_logged_in, customer_id)
-- values(
-- 	true,
-- 	(select id from customer where last_name = 'Doe')
-- );
-- insert into customer_profile (is_logged_in, customer_id)
-- values(
-- 	false,
-- 	(select id from customer where last_name = 'Lalu')
-- );

-- select c.first_name
-- from customer as c
-- join customer_profile as cp
-- on c.id = cp.customer_id where cp.is_logged_in = true;

-- select c.first_name, cp.is_logged_in
-- from customer as c
-- left join customer_profile as cp
-- on c.id = cp.customer_id;

-- select count(c.id)
-- from customer as c
-- right join customer_profile as cp
-- on c.id = cp.customer_id where cp.is_logged_in = false;

-- PART 2

-- create table book (
-- 	book_id serial primary key,
-- 	title varchar (100) not null,
-- 	author varchar(100) not null
-- );

-- insert into book (title, author) 
-- values
--     ('Alice In Wonderland', 'Lewis Carroll'),
--     ('Harry Potter', 'J.K Rowling'),
--     ('To kill a mockingbird', 'Harper Lee');

-- create table student (
-- 	student_id serial primary key,
-- 	name varchar(100) not null unique,
-- 	age int check (age<=15)
-- );

-- insert into student (name, age) 
-- values
--     ('John', 12),
--     ('Lera', 11),
--     ('Patrick', 10),
--     ('Bob', 14);
	
-- create table library (
--     book_fk_id int,
--     student_fk_id int,
--     borrowed_date date,
--     foreign key (book_fk_id) references book (book_id) on delete cascade on update cascade,
--     foreign key (student_fk_id) references student (student_id) on delete cascade on update cascade,
--     primary key (book_fk_id, student_fk_id)
-- );

-- insert into library (book_fk_id, student_fk_id, borrowed_date)
-- values (
--     (select book_id from book where title = 'Alice In Wonderland'),
--     (select student_id from student where name = 'John'),
--     '2022-02-15'
-- ), (
--     (select book_id from book where title = 'To kill a mockingbird'),
--     (select student_id from student where name = 'Bob'),
--     '2021-03-03'
-- ), (
--     (select book_id from book where title = 'Alice In Wonderland'),
--     (select student_id from student where name = 'Lera'),
--     '2021-05-23'
-- ), (
--     (select book_id from book where title = 'Harry Potter'),
--     (select student_id from student where name = 'Bob'),
--     '2021-08-12'
-- );

select * from library;

select s.name, b.title from library l
join student s on s.student_id = l.student_fk_id
join book b on b.book_id = l.book_fk_id;

select avg(s.age) from library l
join student s on s.student_id = l.student_fk_id
join book b on b.book_id = l.book_fk_id
where b.title = 'Alice In Wonderland';

delete from student where name = 'John';
select * from library;