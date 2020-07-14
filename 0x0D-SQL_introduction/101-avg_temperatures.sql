-- displays the average temperature
-- (Fahrenheit) by city ordered by temperature (descending).

-- first create a database to hold the tables
CREATE DATABASE IF NOT EXISTS hbtn_0;
USE hbtn_0;
SOURCE database/temperatures.sql;

-- manipulate the data
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY 1 ORDER BY 2 DESC;



