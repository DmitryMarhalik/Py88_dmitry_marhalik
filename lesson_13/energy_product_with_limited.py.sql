create database lesson13;
create table person (id integer primary key , name text NOT NULL, CHECK(id > 0));
--"""ключ это и есть уникальный номер и not null, поэтому сделал проверку на что-то другое,имя 
-- проверяется на not null"""
create table product (id integer primary key , title text NOT NULL, CHECK(id > 0));
--"""аналогично первой таблице"""
create table eating (person_id integer references person(id), product_id integer references product(id),
datetime timestamp default current_timestamp NOT NULL);
--"""два первыx столбца это ссылки на id в других таблицах, проверка timestamp не придумал(.
--Пробовал на больше- меньше определенной даты - ошибка."""
INSERT INTO person VALUES (1, 'Arkady');
INSERT INTO person VALUES (2, 'Violetta');
INSERT INTO person VALUES (3, 'Evlampiy');
INSERT INTO person VALUES (4, 'Ognezhka');
INSERT INTO product VALUES (1, 'meat');
INSERT INTO product VALUES (2, 'spagetti');
INSERT INTO product VALUES (3, 'apple');
INSERT INTO product VALUES (4, 'potato');
INSERT INTO eating VALUES (1,1);
INSERT INTO eating VALUES (1,2);
INSERT INTO eating VALUES (1,3);
INSERT INTO eating VALUES (1,4);
INSERT INTO eating VALUES (2,1);
INSERT INTO eating VALUES (2,2);
INSERT INTO eating VALUES (2,3);
INSERT INTO eating VALUES (2,4);
INSERT INTO eating VALUES (3,1);
INSERT INTO eating VALUES (3,2);
INSERT INTO eating VALUES (3,3);
INSERT INTO eating VALUES (3,4);
INSERT INTO eating VALUES (4,1);
INSERT INTO eating VALUES (4,2);
INSERT INTO eating VALUES (4,3);
INSERT INTO eating VALUES (4,4);

