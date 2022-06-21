# create dynamic field with CASE
# https://leetcode.com/problems/calculate-special-bonus/


SELECT
employee_id,
CASE
    WHEN employee_id % 2 = 0 OR name LIKE 'M%' THEN 0
    ELSE salary
END
AS bonus
FROM Employees
ORDER BY employee_id;
