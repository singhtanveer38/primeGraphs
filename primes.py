import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def reverseNumber(num):
	rev_num = 0;
	while (num > 0):
		rev_num = rev_num * 10 + num % 10
		num = num // 10
	return rev_num

output = []

primes = []

for i in range(2,100000):
	print(f"iteration: {i}", end="\r")
	count = 0
	for j in range(2,i):
		if i%j == 0:
			count += 1
	if count == 0:
		primes.append(i)
	count = 0	

for i in primes:
	print(f"calculating for {i}", end="\r")
	binary = int(np.binary_repr(i))
	reverse = reverseNumber(binary)
	decimal = int(str(reverse), 2)
	output.append(i-decimal)


pd.DataFrame({"primes": primes, "output": output}).to_csv("output2.csv", index=None)
plt.scatter(primes, output, s=1)
plt.show()
