-- lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT shows.title, SUM(ratings.rate) AS rating
FROM  tv_show_ratings AS ratings
JOIN tv_shows AS shows
     ON ratings.show_id = shows.id
GROUP BY 1 ORDER BY 2 DESC;
