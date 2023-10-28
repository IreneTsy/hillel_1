import random

rand_rand = set(random.sample(range(0, 500), 15))
rand_odd = sum({i for i in rand_rand if i%2})
rand_even = sum({i for i in rand_rand if (i%2 == 0)})
print("Yes" if rand_odd > rand_even else "No")
