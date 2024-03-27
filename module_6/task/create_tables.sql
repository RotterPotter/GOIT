drop table students cascade;
drop table teachers cascade;
drop table subjects cascade;
drop table scores cascade;
drop table groups cascade;

create table students(
    id serial primary key,
    name varchar(30)
);

create table teachers(
    id serial primary key,
    name varchar(30)
);

create table subjects(
    id serial primary key,
    name varchar(30),
    teachers_id int references teachers(id) on delete set null
);


create table groups(
    student_id int references students(id) on delete cascade,
    number_of_group int,
    primary key (student_id)
);

create table scores(
    student_id int references students(id) on delete cascade,
    subject_id int references subjects(id) on delete cascade,
    score int,
    created_at timestamp default current_timestamp
);  