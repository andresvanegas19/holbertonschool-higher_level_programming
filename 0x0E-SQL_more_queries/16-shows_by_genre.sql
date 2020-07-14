-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- tv_shows.title - tv_genres.name

SELECT shows.title, genres.name
FROM tv_show_genres
RIGHT JOIN tv_shows AS shows
     ON tv_show_genres.show_id = shows.id
LEFT JOIN tv_genres AS genres
     ON tv_show_genres.genre_id = genres.id
ORDER BY 1;

