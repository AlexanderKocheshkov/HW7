print("Введите значения списка через пробел:", end=" ")
l = list(input().split(" "))

def bubbletime(l):
	"""Sorting list using bubble method."""
    n = 1
    while n <= len(l):
        for i in range(len(l)-n):
            if int(l[i]) > int(l[i+1]):
                l[i], l[i+1] = l[i+1], l[i]
        n +=1
    return (l)

print(bubbletime(l))
