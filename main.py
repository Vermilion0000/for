numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    if num <= 1:
        not_primes.append(num)  # 1 не является простым числом
    else:
        is_prime = True
        # Проверяем, является ли число num простым
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)
        else:
            not_primes.append(num)

print("Список простых чисел (primes):", primes)
print("Список не простых чисел (not_primes):", not_primes)