-- Find max where value is not equals to max salary (subquery)
-- https://leetcode.com/problems/second-highest-salary/solution/

SELECT max(salary) AS SecondHighestSalary
FROM Employee
WHERE salary NOT IN (SELECT max(salary) FROM Employee);
