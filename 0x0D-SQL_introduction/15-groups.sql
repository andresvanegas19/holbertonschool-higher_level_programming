--  number of records with the same score in the
--  table second_table of the database hbtn_0c_0 in MySQL server.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY 1 ORDER BY 1 DESC;
