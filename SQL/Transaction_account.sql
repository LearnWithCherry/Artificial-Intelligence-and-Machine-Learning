-- 1. Setup the Database
CREATE DATABASE IF NOT EXISTS bank;
USE bank;

-- 2. Clean up and Create Table
DROP TABLE IF EXISTS account;

CREATE TABLE account(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    balance DECIMAL(10,2)
);

-- 3. Insert initial data (Using numbers for IDs, not strings)
INSERT INTO account(id, name, balance) VALUES
(1, 'Adam', 500.00),
(2, 'Bob', 300.00),
(3, 'Charlie', 100.00);

-- 4. Check initial state
SELECT * FROM account;

-- ---------------------------------------------------------
-- TRANSACTION BLOCK
-- ---------------------------------------------------------

-- Disable autocommit to manually control the transaction
SET autocommit = 0;

START TRANSACTION;

-- Task: Transfer 50 from Adam to Bob
UPDATE account SET balance = balance + 5000 WHERE id = 1;
SAVEPOINT after_topup;

UPDATE account SET balance = balance + 10 WHERE id = 2;
ROLLBACK TO after_topup;

COMMIT;

-- At this point, if you run a SELECT in a DIFFERENT tab, 
-- you won't see the changes yet.

-- 5. Save changes permanently
COMMIT;

-- 5.1 If payment was not successful then Rollback(uncommited changes will affected)
ROLLBACK;

-- 5.2 Savepoint
SAVEPOINT;

-- 6. Verify the final result
SELECT * FROM account;


-- Re-enable autocommit (standard default setting)
SET autocommit = 1;