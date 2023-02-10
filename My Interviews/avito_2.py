recom_ids = [2, 3, 1]
seen_ids = [3, 10, 20]


# filtered -> [2, 1]

# 1. надо составить новый список айдишников
# 2. в том же порядке что recom_ids
# 3. НЕ содержит seen_ids

#  0      3  ...
# [... , (), ...]
# [('w', 89), ('r', 5678)]

# d['w'] -> 89
# d['r'] -> 5678


# Time Complexity: O(N), N=len(recom_ids)
# Space Complexity: O(N), N=len(recom_ids)
def solution(recom_ids, seen_ids):
    seen_ids = set(seen_ids)

    result = []
    for id_ in recom_ids:
        if id_ not in seen_ids:
            result.append(id_)

    return result


def hash_func():
    hash = get_hash()
    while hash not in db:
        hash = resolve()
    return hash_func


for key, val in dict:
    pass


# Написать декоратор, который выполняет функцию N раз и выводит общее время выполнения.
def timer(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_start = time.time.now()

            for _ in range(n):
                func()

            result_time = time.time.now() - time_start

            print(result_time)

            return result

        return wrapper

    return decorator

# func = decorator(10) -> timer(func) -> wrapper(*args, **kwargs)


@timer(10)
def func(a, b):
    sleep(1)
    return a + b


# Условие задачи
# дан список из 1 миллиона url, которые нужно опросить
# из каждого url получить из несколько item id и опросить 3 сервиса независимых c этими данными
# для из данных всех 3х сервисов собрать итоговый и ответ и сохранить результат в список
# результаты сохранить в список


from typing import List


url = 'http://some-service/getItems/'  # 5ms

data = [
    {'user_id': 101},  # -> 'sbhfgbshjfbghsdbfj'
    {'user_id': 102},
    {'user_id': 103},
    ...
]

service_1_url = 'http://service1/fillItems/'  # 50ms
service_2_url = 'http://service2/scoreItems/'  # 1ms
service_3_url = 'http://service3/logItems/'  # 8ms


def business_logic(service1_response, service2_response, service3_response):
    # эта функция не делает сетевых вызовов, только обрабатывает ответы
    # считайте, что она уже написана
    return {}


'''
# схема
1. ('http://some-service/getItems/', {'user_id': 100}) -> # вернет item_ids: [1, 2, 3]
2. в любом порядке и независимо опрашиваем service_1-2-3_url с item_ids
3. собираем результат при помощи business_logic
4. вы великолепны! повторить миллион раз.
'''


def gather_data(requests: List[str]) -> List[dict]:
    # YOU CODE HERE
    pass
