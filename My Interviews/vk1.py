# ```
# Таблица users
# +----------------
# | id | username |
# +----------------
# | 1  | Эдик     |
# | 2  | Жора     |
# | 3  | Вася     |
# | 4  | Маша     |
# | 5  | Коля     |
# | 6  | Петя     |
# +----------------
#
# Таблица invoices
# +------------------------
# | id | user_id | amount |
# +------------------------
# | 1  | 1       | 100.00 |
# | 2  | 1       | 210.00 |
# | 3  | 3       | 500.00 |
# | 4  | 5       | 300.00 |
# | 5  | 6       | 100.00 |
# | 6  | 6       | 100.00 |
# +------------------------
# ```
#
# **Написать sql-запросы:**
#
# 1. Вывести юзеров без счетов.
# 2. Вывести юзеров, у которых сумма по всем счетам больше 300.
#
#
# select id, username from users
# Join invoices left on username.id = invoices.user_id
# where invoices.amount is NULL;
#
# select id, username from users
# Join invoices left on username.id = invoices.user_id
# GROUP BY user_id
# HAVING SUM(invoices.amount) > 300;


"""Нужно написать реализацию функции flat ,
которая принимает список из Item и возвращает список всех id,
учитывая вложенность item['children'] ."""


from typing import TypedDict, List


class Item(TypedDict):
    id: int
    name: str
    children: List['Item']


def flat(items: List[Item]) -> List[int]:
    result = []

    queue = deque()
    queue.extend([item for item in items]) # add 1st line
    while queue:

        # add the chiildren
        if node.get("children"):
            queue.add(node["children"])

        result.append(node["id"])

    return result


# Пример структуры
items: List[Item] = [
    {
        "id": 1,
        "name": "1",
        "children": [
            {
                "id": 2,
                "name": "2",
                "children": [
                    {"id": 3, "name": "3", "children": []},
                    {"id": 4, "name": "4", "children": []},
                ]

            },
            {"id": 5, "name": "5", "children": []},
        ]
    },
    {"id": 6, "name": "6", "children": []},
]

# Вызов
print(flat(items))
