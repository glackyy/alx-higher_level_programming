-- Listing all cities contained in the db hbtn_0d_usa
SELECT ct.id, ct.name, st.name FROM cities ct JOIN states st ON ct.states_id = st.id ORDER BY ct.id ASC;
