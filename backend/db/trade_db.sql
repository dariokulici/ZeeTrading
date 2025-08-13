drop database if exists zeetrading_trade;
create database zeetrading_trade;
use zeetrading_trade;


create table tbl_inventory(
    inventory_id int auto_increment primary key
);

create table tbl_item(
    item_id bigint auto_increment primary key,
    item_name varchar(255) not null,
    item_created_at datetime not null default now(),
    item_rarity varchar(255)
);

create table inventory_has_item(
    id int auto_increment primary key,
    inventory_id int not null,
    item_id bigint not null,
    foreign key(inventory_id) references tbl_inventory(inventory_id),
    foreign key(item_id) references tbl_item(item_id)
);

