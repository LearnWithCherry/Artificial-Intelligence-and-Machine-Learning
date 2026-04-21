SELECT * FROM customers;
SELECT * FROM orders;

-- WHERE CONDITION(find greater then values)
SELECT * FROM orders
WHERE amount > 500;

-- AVERAGE AMOUNT 
SELECT * FROM orders
WHERE amount > (SELECT AVG (amount) FROM orders);

-- WITH SELECT
SELECT name ,
	(
		SELECT COUNT(*)
		FROM orders o
		WHERE o.customer_id = c.customer_id
	) AS order_count
FROM customers c;