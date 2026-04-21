-- Q1 -> create a database for your collage. Create a table named teacher to store (id,name,subject,salary)  
CREATE DATABASE IF NOT EXISTS university;
use university;
CREATE TABLE teacher(
	id INT,
    name VARCHAR(30),
    subject VARCHAR(30),
	salary INT 
);
ALTER TABLE teacher
MODIFY COLUMN CTC FLOAT;
DROP TABLE university;
INSERT INTO teacher (id,name,subject,salary)
VALUES 
("1","Rahul","Python",10000),
("2","Ruhi","WEB DEB",10000),
("3","Anki","CPP",10000),
("4","Ritu","DSA",1000);

SET SQL_SAFE_UPDATES = 0;
SELECT name,salary FROM teacher 
WHERE salary >= 10000;

ALTER TABLE teacher
RENAME COLUMN salary TO CTC;

UPDATE teacher
SET CTC = CTC+  CTC * .25;
SELECT * FROM teacher;

ALTER TABLE teacher
ADD COLUMN city VARCHAR(30) DEFAULT "NOT DEFINED";

UPDATE teacher
SET CITY = "DELHI"
WHERE city = "NOT DEFINED";

ALTER TABLE teacher 
DROP CTC;

-- PROBLEM 2 STUDENT INFO  
USE university;
CREATE TABLE student(
	roll INT,
    name VARCHAR(30),
    city VARCHAR(30),
    marks INT
);
INSERT INTO student (roll,name,city,marks)
VALUES
	("1","Harsh","Delhi",70),
    ("2","Ruham","Banglore",55),
    ("3","Aruhi","Mumbai",90),
    ("4","Arti","Pune",40);
    
SELECT * FROM student;

SELECT name,marks FROM student
WHERE marks >= 70;

SELECT city FROM student;

SELECT city,max(marks) FROM student
GROUP BY city;

SELECT avg(marks) FROM student;

ALTER TABLE student
ADD COLUMN grade VARCHAR(5) DEFAULT "NAN";
UPDATE student
SET grade = "O"
WHERE marks >= 80;

UPDATE student
SET grade = "A"
WHERE marks >= 70 AND marks < 80;

UPDATE student
SET grade = "B"
WHERE marks >= 60 AND marks < 70;

UPDATE student
SET grade = "C"
WHERE marks >= 50 AND marks < 60;

UPDATE student
SET grade = "D"
WHERE marks >= 40 AND marks < 50;

SELECT * FROM student;
