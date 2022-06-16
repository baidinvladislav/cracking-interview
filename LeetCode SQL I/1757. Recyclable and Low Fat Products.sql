# simple WHERE filtering
# https://leetcode.com/problems/recyclable-and-low-fat-products/submissions/


SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y'
