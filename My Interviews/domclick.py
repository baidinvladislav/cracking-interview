"""
Кеширующий декоратор без параметров, 
который кеширует по параметрам функции результат выполнения
"""


def cache_decorator(func):
    memo = {}

    def wrapper(*args, **kwargs):
        a = str(args)
        b = str(kwargs)

        result_in_cache = memo.get(a) or memo.get(b)

        if result_in_cache:
            return memo[result_in_cache]

        result = wrapper(*args, **kwargs)
        memo[args] = result
        return result

    return wrapper


@cache_decorator
def sum(a: int, b: int):
    return a + b


print(sum(2, 3))

####
import asyncio


async def sleep(value: float):
    await asyncio.sleep(value)


async def task():
    await sleep(1)
    await sleep(2)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task())

"""
сделать код ревью
"""


@router.get('/users/')
def func(request) -> Optional[user]:
    id = request.args.get("id")
    if id:
        result = Users.query.filter({"id": int(id)})  # get()
        return result

    return None


# TABLE
# Users
# -------------------------------------------------
# ID | Name | User_group_id |
# 1001 | Иван
# Макаров | 1 |
# 1002 | Екатерина
# Мирошниченко | 1 |
# 1003 | Кирилл
# Лебедев | null |
# 1004 | Александр
# Черепанов | 3 |
# 1005 | Мария
# Рукалова | 4 |
# 1006 | Георгий
# Вирунов | 4 |

# TABLE
# User_group
# -------------------------------------------------
# ID | Group_name |
# 1 | User |
# 2 | Power
# user |
# 3 | Admin |
# 4 | Cybersec |
# 5 | DevOps |


# Найти количество неиспользуемых групп пользователей (к которым не привязан ни один из пользователей)
# select COUNT(*) from user_group
# where user_group.id not in (select user_group_id from users);

# select id from user_group
# left join Users on user_group.id = user.User_group_id
# where User_group_id is NULL
