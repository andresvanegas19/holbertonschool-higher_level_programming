--  the top 3 of cities temperature during July and August ordered by temperature
-- first create a database to hold the tables
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
USE hbtn_0c_0;
SOURCE database/temperatures.sql;

SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month > 6 AND month < 9
GROUP BY 1 ORDER BY 2 DESC
LIMIT 3;

