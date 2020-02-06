-- Create a table with the following columns, named bsg_spaceship
--
--    id - an auto-incrementing integer which is also the primary key
--    name - variable-length string with a max of 255 characters, cannot be null
--    separate_saucer_section - a boolean property which specifies whether or not there is a separate saucer section on the spaceship. This defaults to No.
--    length - integer, cannot be null
--
-- Once you have created the table, run the query "DESCRIBE bsg_spaceship;"
CREATE TABLE bsg_spaceship(
id int(11) NOT NULL AUTO_INCREMENT,
name varchar(255) NOT NULL,
separate_saucer_section boolean not null default 0,
length int(11) NOT NULL,
PRIMARY KEY (id)
);

-- Write your queries BELOW this line
DESCRIBE bsg_spaceship;




