# Just is a left join
# https://leetcode.com/problems/combine-two-tables/


SELECT firstName, lastName, city, state
FROM Person LEFT JOIN Address
ON Person.personId = Address.personId;
