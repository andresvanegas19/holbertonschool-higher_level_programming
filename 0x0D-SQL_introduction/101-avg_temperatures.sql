-- displays the average temperature
-- (Fahrenheit) by city ordered by temperature (descending).
-- manipulate the data
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY 1 ORDER BY 2 DESC;



