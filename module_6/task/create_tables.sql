drop table students;
drop table teachers ;
drop table subjects ;
drop table scores ;
drop table groups;

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
    subject_id int references subjects(id) on delete cascade,
    student_id int references students(id) on delete cascade,
    score int
);  