import pandas as pd 
import matplotlib.pyplot as plt
plt.style.use('dark_background')

df = pd.read_csv("output2.csv")

for i in range(df.shape[0]):
	print(f"plotting: {i}", end="\r")
	plt.figure(figsize=(16,9))
	plt.scatter(df["primes"].iloc[: i], df["output"].iloc[: i], s=1, c="c")
	plt.title(f"Iteration: {i}")
	plt.savefig(f"./images/{i}.png", dpi=120)
	plt.close()
