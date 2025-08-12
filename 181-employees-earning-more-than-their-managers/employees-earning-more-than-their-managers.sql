-- # Write your MySQL query statement below
-- SELECT a.name As Employee FROM Employee AS a, Employee AS b
-- WHERE a.managerId = b.id AND a.salary > b.salary;

SELECT a.name as Employee FROM Employee AS a Join Employee as b on a.managerID = b.id where a.salary>b.salary;