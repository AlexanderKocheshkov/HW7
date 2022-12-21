import random

print("Задайте размер первого и второго списка:", end="")
n, m = input().split(" ")
n, m = int(n), int(m)

x = 0
s1, s2 = [], []
while x < n:
    s1.append(random.randint(0, 10))
    x += 1

x = 0
while x < m:
    s2.append(random.randint(0, 10))
    x += 1

s1 = set(s1)
s2 = set(s2)

print("Первый набор: ", s1)
print("Второй набор: ", s2)
print("Входит одновременно в оба набора: ", s1.intersection(s2))
print("Входит только в первое, но не входят во второе: ", s1.difference(s2))
print("Входят только во второе, но не входят в первое: ", s2.difference(s1))
print("Входит в первое или во второе, но не в оба из них одновременно: ", 
		s1.symmetric_difference(s2))
