# Write your MySQL query statement below

DELETE p1 
FROM Person p1
JOIN Person p2 ON p1.email = p2.email
WHERE p1.id > p2.id

-- DELETE FROM Person 
-- WHERE id NOT IN (
--     SELECT MIN(id)
--     FROM Person 
--     GROUP BY email
-- )