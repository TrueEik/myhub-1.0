num = []
for i in range(2, 100):
    for j in range(2, i):
        x = i%j
        if (x==0):
            break
        else:
            num.append(i)
print(num)
