-- Find the first_name, last_name and total_combined_film_length of Sci-Fi films for every actor.
-- That is the result should list the names of all of the actors(even if an actor has not been in any Sci-Fi films) and the total length of Sci-Fi films they have been in.
-- Look at the category table to figure out how to filter data for Sci-Fi films.
-- Order your results by the actor_id in descending order.
-- Put query for Q3 here

SELECT actor.actor_id AS actor_id, actor.first_name AS first_name, actor.last_name AS last_name,
	COALESCE(SUM(film.length),0) as total_combined_film_length
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
LEFT JOIN film_category ON film_actor.film_id = film_category.film_id
LEFT JOIN category ON film_category.category_id = category.category_id
LEFT JOIN film ON film_actor.film_id = film.film_id
AND category.category_id = 14
GROUP BY actor.actor_id DESC;