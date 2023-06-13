# user:
#   id: int
#   name: str

# book:
#   id: int
#   user_id: int

# author:
#   id: int
#   book_id: int

# 1 ===
# book id = 1
# user_id = ?
# select user_id from book where book.id = 1;

# 2 ===
# book id = 1
# author_id - ?
# select author.id from author where book_id = 1;

# 3 ===
# book id = 1
# user.name - ?
# select user.name, book.id from book left join user on book.user_id = user.id where book.id = 1;
