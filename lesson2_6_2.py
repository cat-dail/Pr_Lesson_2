numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
primes = []
not_primes = []
kod_1 = []
uniq_kod_1 = []
kod = {}
for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
for i in primes:
     for j in range(1, i):
         kod_1.append([i, {j, (i - j)}])
# kod_1 = sorted(kod_1)
for i in kod_1:
    if i not in uniq_kod_1:
        uniq_kod_1.append(i)
values = set(map(lambda x: x[0], uniq_kod_1))
uniq_kod_1 = list([y[1] for y in uniq_kod_1 if y[0] == x] for x in values)
kod = dict(zip(primes, uniq_kod_1))
# print('not_primes', not_primes)
print('primes', primes)
# print('uniq_kod_1', uniq_kod_1)
print('kod', kod)
