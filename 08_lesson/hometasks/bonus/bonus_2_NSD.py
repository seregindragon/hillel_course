def find_gcd(a: int, b: int) -> int:
    set_a = []
    set_b = []
    for i in range(1, a + 1):
        if a % i == 0:
            set_a.append(i)

    for j in range(1, b + 1):
        if b % j == 0:
            set_b.append(j)

    return max(set(set_a).intersection(set(set_b)))
