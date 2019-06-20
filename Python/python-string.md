



### String

















思考题：

```python
begin =time.perf_counter()
s = ''
for n in range(0, 100000):
    s += str(n)
end = time.perf_counter()
print('第一种方法时间是{}'.format(end - begin ))


begin =time.perf_counter()
l = []
for n in range(0, 100000):
    l.append(str(n))
end1 = time.perf_counter()
s = ' '.join(l)
end = time.perf_counter()
print('第二种方法时间是{},{}'.format(end1 - begin, end -end1))


begin =time.perf_counter()
s = " ".join(map(str, range(0, 10000)))
end = time.perf_counter()
print('第三种方法时间是{}'.format(end - begin ))


第一种方法时间是0.03266749999999996
第二种方法时间是0.022658500000000026, 0.00102629999999998
第三种方法时间是0.001526599999999989
```

