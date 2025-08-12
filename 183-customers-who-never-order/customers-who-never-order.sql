# Write your MySQL query statement below
SELECT c.name as Customers 
FROM Customers as c 
left join Orders as o on c.id = o.customerId 
where o.customerID IS NULL