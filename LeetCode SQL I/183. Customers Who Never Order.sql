# select customer names who aren't in the subquery
# https://leetcode.com/problems/customers-who-never-order/submissions/


SELECT Customers.name AS 'Customers'
FROM Customers
WHERE Customers.id NOT IN (SELECT customerId FROM Orders);
