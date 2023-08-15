-- Listing all records of the tab second_table having a name value
-- Ordered by DESC score
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
