-- Find the first_name and last_name of all actors who have never been in a Sci-Fi film.
-- Order by the actor_id in ascending order.

-- Put your query for q4 here
SELECT actor.actor_id, actor.first_name, actor.last_name
FROM actor
WHERE actor.actor_id NOT IN (
	SELECT actor.actor_id
	FROM actor
	JOIN film_actor ON actor.actor_id = film_actor.actor_id
	JOIN film_category ON film_actor.film_id = film_category.film_id
	JOIN category ON film_category.category_id = category.category_id
	JOIN film ON film_actor.film_id = film.film_id
	AND category.category_id = 14
)
GROUP BY actor.actor_id ASC;