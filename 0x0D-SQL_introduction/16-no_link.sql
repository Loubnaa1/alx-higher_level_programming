-- Lists all records of the table second_table.
SELECT score, name FROM second_table WHERE name IS NOT NULL AND  LENGTH(name) > 0 ORDER BY score DESC;
