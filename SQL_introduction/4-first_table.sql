-- a script that creates a table called first_table in the current database in MySQL server
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

-- Inserting the data
INSERT INTO first_table (id, name, score) VALUES
(1, 'A', 12),
(2, 'B', 2),
(3, 'Bob', 10),  -- Corrected score
(4, 'D', 89),
(5, 'E', 0),
(6, 'F', 23),
(7, 'G', 5),
(8, 'H', 6),
(9, 'I', -9),
(10, 'J', 3)
ON DUPLICATE KEY UPDATE
    name = VALUES(name),
    score = VALUES(score);
