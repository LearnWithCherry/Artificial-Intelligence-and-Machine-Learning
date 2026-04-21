CREATE DATABASE IF NOT EXISTS instagram;

USE instagram;
DROP TABLE user;
CREATE TABLE user(
    id INT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(50) UNIQUE,
    followers INT DEFAULT 0,
    following INT DEFAULT 0,
    post INT DEFAULT 0,
    age INT,
    address VARCHAR(30)
);
INSERT INTO user(id,name,email,age,followers,following,post,address )
VALUES 
(1,"Rajat","Rajat1234@gmail.com",19,250,230,10,"INDIA"),
(2,"Ruhi","Ruhi223@gmail.com",20,120,30,2,"USA"),
(3,"Abi","A1122@gmail.com",30,120,100,35,"GERMANY");

INSERT INTO user(id,name,email,age,followers,following,post,address)
VALUES
("4","Ansh","ansh233@gmail.com",26,1000,500,31,"UK"),
("5","Rahul","Rahul23@gmail.com",20,456,31,1,"UAE"),
("6","Anshu","anu456@outlook.com",40,70,13,0,"INDIA");
INSERT INTO user(id,name,email,following,post,address)
VALUES
("7","EVE","eve12@outlook.com",123,3,"SPAIN");

SELECT id,name,age FROM user; -- to show selected values

SELECT * FROM user; -- to show all (*) means all

SELECT DISTINCT address FROM user; -- print unique values 

SELECT name,followers FROM user
WHERE followers >= 150 AND age >= 19;

-- SELECT name,age,email,followers FROM user
-- WHERE age + 1 = 21;
-- WHERE age > 15 AND followers > 200;
-- WHERE age > 15 OR followers > 200;
-- WHERE age BETWEEN 20 AND 29;
-- WHERE age IN (20,40);

-- limit clause
-- WHERE age > 15 
-- LIMIT 2;

-- ORDER BY followers ASC;
-- ORDER BY followers DESC;

-- AGGREGATE FUNCTION 
SELECT max(age) FROM user;
SELECT count(age) FROM user
WHERE age = 20;
SELECT min(age) FROM user;
SELECT sum(followers) FROM user;

-- GROUP BY CLAUSE

SELECT age, count(id) FROM user
GROUP BY age;

SELECT name, age, max(followers) FROM user
GROUP BY age,name;

SELECT age, max(followers) FROM user
GROUP BY age
HAVING max(followers) > 200
ORDER BY age DESC;

UPDATE user
SET city = "Not Defined"
WHERE city = "Delhi";

SET SQL_SAFE_UPDATES = 0;

DELETE FROM user
WHERE age <= 14;
ALTER TABLE user 
ADD COLUMN city VARCHAR(30) DEFAULT "Not Defined";
SELECT * FROM user;

ALTER TABLE user
DROP COLUMN age;
SELECT * FROM user;
ALTER TABLE user
RENAME TO insta_user;

ALTER TABLE insta_user
RENAME TO user;

ALTER TABLE user
CHANGE COLUMN followers subs INT DEFAULT 0;
SELECT * FROM user;
ALTER TABLE user
MODIFY subs INT DEFAULT 5;
SELECT * FROM user;

TRUNCATE TABLE user 

-- General order
 

-- Constrains -> Rules for data in the table 

-- NOT NULL    =  Column cannot be empty 
-- UNIQUE      =  All the value in colums are different 
-- DEFAULT     =  Set a default value of a column
-- CHECK       =  It can limit the values allowed in a column
-- PRIMARY KEY =  makes a column unique & not null but used only for one
-- FOREIGN KEY =  prevent action that would destory links between tables  

--  TABLES QUERIES -- 
-- CREATE, INSERT, UPDATE, ALTER, TRUNCATE, DELETE

-- KEYS - Special colums in the table (Primary & Foreign Key) from
-- Only one primary is allowed 
