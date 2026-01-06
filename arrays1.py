l = [1, 2, 4, 7, 7, 5]
second_l = 0
largest = l[0]
second_s = max(l)
smallest = l[0]

for i in range(1,len(l)):
    c = l[i]
    if c > largest:
        second_l = largest
        largest = c

    elif c > second_l and c < largest:
        second_l = c
    if c <second_s and c<smallest:
        smallest = c
    elif c < second_s:
        second_s = c
print(second_l)
print(second_s)