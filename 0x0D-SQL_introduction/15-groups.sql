-- Listing the num of records with the same score in the tab second_table
-- Ordered by DESC count
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
