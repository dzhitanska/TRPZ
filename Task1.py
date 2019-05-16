import random

ALPHA = []
for x in range(150):
    ALPHA.append(random.randint(1, 200))

BETA = list(sorted(ALPHA, reverse=True)[:15])

f = open('text.txt', 'w')
for i in BETA:
    f.write(str(i) + '\n')

print(ALPHA)
print(BETA)