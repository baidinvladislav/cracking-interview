|   ID   |   Name   |          Email          |
|--------|----------|-------------------------|
|   1    |  John    | john@example.com        |
|   2    |  Sarah   | sarah@example.com       |
|   3    |  Mike    | mike@example.com        |
|   4    |  Emily   | sarah@example.com       |


SELECT name, COUNT(email)
 FROM users
 GROUP BY email
 HAVING COUNT(email) > 1
