# take those customers and his times without transactions
# who don't represent into Transaction table (subquery)
# then we group by every customer
# https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/


SELECT customer_id, COUNT(customer_id) AS count_no_trans
FROM Visits
WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)
GROUP BY customer_id;
