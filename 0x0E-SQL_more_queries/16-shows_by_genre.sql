-- lists all tv_shows, and all genres linked to that show, from the database hbtn_0d_tvtv_shows.
-- tv_tv_shows.title - tv_genres.name

SELECT tv_shows.title, tv_genres.name
FROM tv_show_genres
RIGHT JOIN tv_shows
     ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres
     ON tv_show_genres.genre_id = tv_genres.id
ORDER BY 1, 2;

