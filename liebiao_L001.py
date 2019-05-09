import time

a = []
t0 = time.perf_counter()
for i in range(1,20000000):
    a.append(i)
tt1 = round((time.perf_counter() - t0),2)
print(tt1, "secends!")

t0 = time.perf_counter()
b = [i for i in range(1,20000000)]
tt2 = round((time.perf_counter() - t0),2)
print(tt2, "secends!")

ttl = tt1 - tt2
percent = round((1 - tt2/tt1) * 100)
print('两种方法相差{}秒!'.format(ttl))
print('方法二比方法一提升{}%'.format(percent))
