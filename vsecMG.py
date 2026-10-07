import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Random array with values between 0 and 1
rand_arr = np.random.rand(5)
print("Random array (uniform 0-1):", rand_arr)

# Random integers between 10 and 49
rand_int = np.random.randint(10, 50, size=6)
print("Random integers:", rand_int)

# Random values from standard normal distribution
rand_normal = np.random.randn(5)
print("Random normal (standard):", rand_normal)

# Normal distribution with mean = 50 and standard deviation = 5
normal_dist = np.random.normal(loc=50, scale=5, size=10)
print("Normal distribution (mean=50, std=5):", normal_dist)

# Statistical measures
print("Mean =", np.mean(normal_dist))
print("Median =", np.median(normal_dist))
print("Standard Deviation =", np.std(normal_dist))
print("Variance =", np.var(normal_dist))
print("Min =", np.min(normal_dist))
print("Max =", np.max(normal_dist))

