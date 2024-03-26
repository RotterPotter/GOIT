-- create table genders(
--     id int primary key,
--     name varchar(30),
--     created_at timestamp default current_timestamp
-- );

-- create table users(
--     id int primary key,
--     name varchar(30),
--     email varchar(30),
--     password varchar(30),
--     age int,
--     gender_id int,
--     created_at timestamp default current_timestamp,
--     foreign key (gender_id) references genders(id)
--         on delete set null
--         on update cascade
-- );

-- insert into genders (id, name)
-- values (1, 'male'), (2, 'female')

-- CREATE TABLE contacts (
--   id INT PRIMARY KEY,
--   name VARCHAR(30),
--   email VARCHAR(30),
--   phone VARCHAR(30),
--   favorite int,
--   user_id INT,
--   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--   FOREIGN KEY (user_id) REFERENCES users (id)
--         ON DELETE CASCADE
--         ON UPDATE CASCADE
-- );

-- insert into users (id, name, email, password, age, gender_id)
-- values (1, 'Boris', 'boris@test.com', 'password', 23, 1),
-- (2, 'Alina', 'alina@test.com', 'password', 32, 2),
-- (3, 'Maksim', 'maksim@test.com', 'password', 40, 1);

-- insert into contacts (id, name, email, phone, favorite, user_id)
-- values (1, 'Allen Raymond', 'nulla.ante@vestibul.co.uk', '(992) 914-3792', 0, 1),
-- (2, 'Chaim Lewis', 'dui.in@egetlacus.ca', '(294) 840-6685', 1, 1),
-- (3, 'Kennedy Lane', 'mattis.Cras@nonenimMauris.net', '(542) 451-7038', 1, 2),
-- (4, 'Wylie Pope', 'est@utquamvel.net', '(692) 802-2949', 0, 2),
-- (5, 'Cyrus Jackson', 'nibh@semsempererat.com', '(501) 472-5218', 0, null);