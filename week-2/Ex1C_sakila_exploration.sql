/*
a) The information included in this table is actor id, first name, last name and last_update.
b) The information included in the film table is film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_feature and last_update.
c) The other table in sakila that contains colums for both actor_id and film_id is film_actor table.
d) The information found in the rental table tab is rental and return dates and time, inventory_id, customer_id, staff_id and last_update. The information is organized in a simple to read way.
e) The information found in the inventory table tab is inventory_id, film_id, store_id and last_update. It is easy to read.
f) The tables I need to use to understand the names of all films that were rented on a spefic date is the title, rental_id and rental_date tables, because they obtain film and rental time infromation.
*/

SELECT TITLE From film;
SELECT film_id From film;
SELECT inventory_id From inventory;
SELECT rental_id From rental;
SELECT rental_date From rental;