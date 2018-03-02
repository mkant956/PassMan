-- creating databases scripts
create database if not exists passman;
use passman;

create table if not exists user_pass(id int(11) NOT NULL AUTO_INCREMENT,username varchar(80),password varchar(200),update_date DATE,PRIMARY KEY (id));

create table if not exists masterpass(masterpassword varchar(128) not null);
