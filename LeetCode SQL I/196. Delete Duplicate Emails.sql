# like two pointers
# https://leetcode.com/problems/delete-duplicate-emails/


DELETE p1
FROM Person p1, Person p2
WHERE p1.Email = p2.Email and p1.Id > p2.Id;
