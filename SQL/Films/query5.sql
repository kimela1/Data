-- Find the film_title of all films which feature both KIRSTEN PALTROW and WARREN NOLTE
-- Order the results by film_title in descending order.
--  Warning: this is a tricky one and while the syntax is all things you know, you have to think a bit oustide the box to figure out how to get a table that shows pairs of actors in movies.
-- Put your query for q5 here.
SELECT kp.title AS film_title FROM (
    SELECT film.film_id, film.title
    FROM film
	JOIN film_actor ON film.film_id = film_actor.film_id
	JOIN actor ON film_actor.actor_id = actor.actor_id
	WHERE actor.first_name = 'KIRSTEN' and actor.last_name = 'PALTROW'
) AS kp
JOIN (
    SELECT film.film_id, film.title
    FROM film
	JOIN film_actor ON film.film_id = film_actor.film_id
	JOIN actor ON film_actor.actor_id = actor.actor_id
	WHERE actor.first_name = 'WARREN' and actor.last_name = 'NOLTE'
) AS wn
WHERE kp.film_id = wn.film_id
ORDER BY kp.title DESC;