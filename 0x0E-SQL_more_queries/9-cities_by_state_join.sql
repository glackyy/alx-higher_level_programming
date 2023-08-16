-- Listing all cities contained in the db hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.states_id ORDER Y cities.id;
