-- We want to find out how many of each category of film ED CHASE has starred in.

-- So return a table with category_name and the count of the number_of_films that ED was in that category.

-- Your query should return every category even if ED has been in no films in that category

-- Order by the category name in ascending order.
-- Source: https://dba.stackexchange.com/questions/110850/count-rows-with-inner-joined-tables


SELECT t1.name AS category_name,
    IFNULL(t2.number_of_films, '0') AS number_of_films
FROM (
	SELECT category.name
    FROM category
) AS t1
LEFT JOIN (
	SELECT category.name, COUNT(category.name) AS number_of_films
    FROM category
	JOIN film_category ON category.category_id = film_category.category_id
	JOIN film ON film_category.film_id = film.film_id
	JOIN film_actor ON film.film_id = film_actor.film_id
	JOIN actor ON film_actor.actor_id = actor.actor_id
	WHERE actor.first_name = 'ED' AND actor.last_name = 'CHASE'
	GROUP BY category.name
) AS t2
ON t1.name = t2.name;
