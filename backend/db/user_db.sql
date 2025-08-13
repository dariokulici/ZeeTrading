drop database if exists zeetrading_user;
create database zeetrading_user;
use zeetrading_user;

create table tbl_role(
    role_id int auto_increment primary key,
    role_name varchar(255) not null unique
);

create table tbl_user(
    user_uuid char(36) primary key not null unique,
    user_name varchar(255) not null unique,
    user_password varchar(255) not null,
    user_created_at datetime not null default now()
);

create table role_has_user(
    id int auto_increment primary key,
    user_uuid char(36) not null,
    role_id int not null,
    foreign key (user_uuid) references tbl_user(user_uuid),
    foreign key (role_id) references tbl_role(role_id)
);

create table tbl_session(
    token char(22) primary key unique,
    session_created_at datetime not null default now(),
    session_expires_at datetime not null,
    fk_user_uuid char(36) not null,
    foreign key (fk_user_uuid) references tbl_user(user_uuid)
);

create index idx_user on tbl_user(user_uuid, user_name);