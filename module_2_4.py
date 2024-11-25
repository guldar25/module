numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for elem in numbers:
    if elem < 2:
        continue
    is_prime = True
    for a in range(2, elem):
        if elem % a == 0:
            not_primes.append(elem)
            is_prime = False
            break
    if is_prime:
        primes.append(elem)
print(primes)
print(not_primes)



