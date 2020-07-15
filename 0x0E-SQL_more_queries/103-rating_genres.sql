--  lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT genres.name, SUM(ratings.rate) AS rating
FROM tv_show_ratings AS ratings
JOIN tv_show_genres
     ON ratings.show_id = tv_show_genres.show_id
JOIN tv_genres AS genres
     ON genres.id = tv_show_genres.genre_id
GROUP BY 1 ORDER BY 2 DESC;
