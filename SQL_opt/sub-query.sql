-- Uncorrelated sub-query
-- A sub-query is another query within a query.
-- The sub-query returns its results to an outer query to be processed.

SELECT UNStatisticalRegion,
       CountryName
FROM Nations
WHERE Code2 -- Country code for outer query
         IN (SELECT Country -- Country code for sub-query
             FROM Earthquakes
             WHERE depth >= 400 ) -- Depth filter
ORDER BY UNStatisticalRegion;

-- Correlated sub-query
-- Sub-queries are used to retrieve information from
-- another table, or query, that is separate to the main query.

-- TODO: This is an almost little slowly

SELECT UNContinentRegion,
       CountryName,
        (SELECT AVG(magnitude) -- Add average magnitude
        FROM Earthquakes e
         	  -- Add country code reference
        WHERE n.Code2 = e.Country) AS AverageMagnitude
FROM Nations n
ORDER BY UNContinentRegion DESC,
         AverageMagnitude DESC;


--  In correlated sub-queries, the outer query
-- is referenced in the sub-query. I

-- Often the results from a correlated sub-query can be
-- replicated using an INNER JOIN. Depending on what your
--  requirements are, using an INNER JOIN may be more efficient
--  because it only makes one pass through the data whereas
--  the correlated sub-query must execute for each row in the outer query.

SELECT n.CountryName,
       c.BiggestCity
FROM Nations AS n
INNER JOIN -- Join the Nations table and sub-query
    (SELECT CountryCode,
     MAX(Pop2017) AS BiggestCity
     FROM Cities
     GROUP BY CountryCode) AS c
ON n.Code2 = c.CountryCode; -- Add the joining columns


-- Great work! Sub-queries and INNER JOIN's can be used to
-- return the same results. However, in practice large, comp
-- lex queries may contain lots of sub-queries, many of which
--  could be re-written as INNER JOIN's to improve performance.


-- INTERSECT is one of the easier and more intuitive methods used
-- to check if data in one table is present in another.


SELECT Capital
FROM Nations -- Table with capital cities

INTERSECT -- Add the operator to compare the two queries

SELECT NearestPop -- Add the city name column
FROM Earthquakes;
--  It also removes duplicate rows from the results.


-- EXCEPT does the opposite of INTERSECT.
-- It is used to check if data, present in one table, is absent in another.

SELECT Code2 -- Add the country code column
FROM Nations

EXCEPT -- Add the operator to compare the two queries


SELECT Country
FROM Earthquakes; -- Table with country codes


SELECT CountryName
FROM Earthquakes -- Table from Earthquakes database

INTERSECT -- Operator for the intersect between tables

SELECT Country
FROM Nations; -- Table from NBA Season 2017-2018 database

-- Second attempt
SELECT CountryName,
	   Capital,
       	Pop2016, -- 2016 country population
       WorldBankRegion
FROM Nations AS n
WHERE EXISTS -- Add the operator to compare queries
	  (SELECT 1
	   FROM Earthquakes AS e
	   WHERE n.Capital = e.NearestPop); -- Columns being compared


-- IN and EXISTS are the appropriate operators to use here. Their advantage
-- over INTERSECT is that the results can contain any column from the outer
-- query in any order, the population column appears after the capital city column now.


SELECT WorldBankRegion,
       CountryName
FROM Nations
WHERE Code2 NOT IN -- Add the operator to compare queries
	(SELECT CountryCode -- Country code column
	 FROM Cities);


SELECT WorldBankRegion,
       CountryName,
	   Code2,
       Capital, -- Country capital column
	   Pop2017
FROM Nations AS n
WHERE NOT EXISTS -- Add the operator to compare queries
	(SELECT 1
	 FROM Cities AS c
	 WHERE n.Code2 = c.CountryCode); -- Columns being compared

-- NOT IN and NOT EXISTS are used to check if the data present in one table is absent in another.

SELECT WorldBankRegion,
       CountryName,
       Capital
FROM Nations
WHERE Capital NOT IN
	(SELECT NearestPop
     FROM Earthquakes
     WHERE 	NearestPop IS NOT NULL); -- filter condition

-- One major issue with using NOT IN is the way it handles
-- NULL values. If the columns in the sub-query being evaluated
-- for a non-match contain NULL values, no results are returned.
-- A workaround to get the query working correctly is to use
-- IS NOT NULL in a WHERE filter condition in the sub-query.


-- Second query
SELECT t.TeamName,
       t.TeamCode,
	   t.City,
	   e.Date,
	   e.place, -- Place description
	   e.Country -- Country code
FROM Teams AS t
INNER JOIN Earthquakes AS e -- Operator to compare tables
	  ON t.City = e.NearestPop


-- An exclusive LEFT OUTER JOIN can be used to check
-- for the presence of data in one table that is absent
-- in another table. To create an exclusive LEFT OUTER JOIN
-- the right query requires an IS NULL filter condition on the joining column.

-- First attempt
SELECT c.CustomerID,
       c.CompanyName,
	   c.ContactName,
	   c.ContactTitle,
	   c.Phone
FROM Customers c
LEFT OUTER JOIN Orders o -- Joining operator
	ON c.CustomerID = o.CustomerID -- Joining columns
WHERE c.Country = 'France';


-- Second attempt
SELECT c.CustomerID,
       c.CompanyName,
	   c.ContactName,
	   c.ContactTitle,
	   c.Phone
FROM Customers c
LEFT OUTER JOIN Orders o
	ON c.CustomerID = o.CustomerID
WHERE c.Country = 'France'
	AND o.CustomerID IS NULL; -- Filter condition

-- Great! An inclusive LEFT OUTER JOIN
-- returns all the rows in the left query,
-- whereas an exclusive LEFT OUTER JOIN returns
-- only rows in the left query that are absent in the right query.



--  An exclusive LEFT OUTER JOIN checks
--   for data in one table that is absent in
--   a related table. It does this by using
--   IS NULL in a WHERE filter condition of
--   the right query to restrict it to rows that do not match in the left query.

-- Query 1
SELECT *
FROM Teams
-- Sub-query 1
WHERE City IN -- Sub-query filter operator
      (SELECT CityName
       FROM Cities) -- Table from Earthquakes database
-- Sub-query 2
   AND City IN -- Sub-query filter operator
	   (SELECT CityName
	    FROM Cities
		WHERE CountryCode IN ('US','CA'))
-- Sub-query 3
    AND City IN -- Sub-query filter operator
        (SELECT CityName
         FROM Cities
	     WHERE Pop2017 >2000000);

-- Query 2
SELECT *
FROM Teams AS t
WHERE EXISTS -- Sub-query filter operator
	(SELECT 1
     FROM Cities AS c
     WHERE t.City = c.CityName -- Columns being compared
        AND c.CountryCode IN ('US','CA')
          AND c.Pop2017 > 2000000);