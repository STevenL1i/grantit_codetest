create database grantit_codetest;
use grantit_codetest;

create table book
(
    bookname     varchar(500)  not null
        primary key,
    writer       varchar(500)  not null,
    publisher    varchar(100)  null,
    publish_date varchar(10)   null,
    price        decimal(5, 2) null,
    rating       decimal(2, 1) null,
    comments     int           null,
    lastupdate   datetime      not null
);