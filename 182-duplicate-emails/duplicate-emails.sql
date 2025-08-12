# Write your MySQL query statement below

SELECT email 
From Person 
GROUP BY Email 
HAVING COUNT(email) > 1