-- SQL command to list all records with a score >= 10 in the table of the database, displaying both score and name, ordered by score (top first)

-- SQL query to select records with score >= 10 from the table, ordering by score (top first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
