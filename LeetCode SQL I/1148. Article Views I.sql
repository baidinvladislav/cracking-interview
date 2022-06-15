# distinct and the same value in author_id and viewer_id
# finally sorted by in ascending order


SELECT DISTINCT author_id as id
FROM Views
WHERE Views.author_id = Views.viewer_id
ORDER BY id;
