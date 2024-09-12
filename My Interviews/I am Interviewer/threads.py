# чему будет равно значение переменной count после исполнения кода?


count = 0


def inc():
    global count
    sleep(1) # follow-up
    count += 1


threads = []
for i in range(100):
    thread = Thread(inc)
    threads.append(thread)


for t in threads:
    t.join()    


print(count)
