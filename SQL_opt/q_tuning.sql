-- Generally, elapsed time is the best measure to compare query
-- times because it reports the total
-- duration of the query, from execution to returning the complete results.
-- CPU time measures the time the database server processors spent on the query only.
STATISTICS TIME

-- logical reads for the Orders table indicates that thirty-two data pages
-- were read from memory to complete the query.
STATISTICS IO
