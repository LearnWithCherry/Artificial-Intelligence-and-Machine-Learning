CREATE DATABASE IF NOT EXISTS customers;
USE customers;
CREATE TABLE IF NOT EXISTS customers(
	customer_id INT PRIMARY KEY,
    name VARCHAR(30),
    city VARCHAR(30)
);
INSERT INTO customers VALUES
(1,"Alice","Mumbai"),
(2,"Charlie","Delhi"),
(3,"Bob","Bangalore"),
(4,"David","Pune");

CREATE TABLE IF NOT EXISTS orders(
	order_id INT PRIMARY KEY,
    customer_id INT,
    amount INT
);
DROP TABLE orders;
INSERT INTO orders VALUES
(101,1,500),
(102,1,900),
(103,2,300),
(104,5,700);

SELECT * FROM customers;
SELECT * FROM orders;

-- Inner join

SELECT * FROM customers c INNER JOIN orders o
ON c.customer_id = o.customer_id;

-- Left join 
SELECT * FROM customers c LEFT JOIN orders o
ON c.customer_id = o.customer_id;

-- Right join 
SELECT * FROM customers c RIGHT JOIN orders o
ON c.customer_id = o.customer_id;

-- Outer join 
SELECT * FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
UNION
SELECT * FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;

-- Cross join
SELECT * FROM customers
CROSS JOIN orders;

-- Self join
SELECT * FROM customers AS a
JOIN customers AS b
ON a.customer_id = b.customer_id;

-- Problem - WAQ to display the exelusive joins:
-- Left exelusive.
SELECT * FROM customers AS a
LEFT JOIN orders AS b
ON a.customer_id = b.customer_id
Where b.customer_id IS NULL;

-- Right execlusive.
SELECT * FROM customers AS a
RIGHT JOIN orders AS b
ON a.customer_id = b.customer_id
Where a.customer_id IS NULL;