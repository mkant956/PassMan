-- creating databases scripts
create database if not exists passman;
use passman;

create table if not exists Users(userid int(11) NOT NULL AUTO_INCREMENT,username varchar(80),password varchar(200),PRIMARY KEY (userid));

-- create table if not exists masterpass(masterpassword varchar(128) not null);
