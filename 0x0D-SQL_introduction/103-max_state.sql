--  the top 3 of cities temperature during July and August ordered by temperature
-- first create a database to hold the tables
SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY 1 ORDER BY 1 LIMIT 3;
