-- Listing all cities contained in the db hbtn_0d_usa
SELECT ct.id, ct.name, st.name FROM cities c JOIN states st  ON st.id = ct.states_id ORDER BY ct.id ASC;
