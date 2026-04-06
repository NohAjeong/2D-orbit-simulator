import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
math = [2, 3, 4, 3, 5]
english = [1, 2, 2, 3, 4]

plt.plot(days, math, label="math", color='orange', marker='o')
plt.plot(days, english, label="english", color='skyblue', marker='x')

avg = (sum(math) / len(math))
plt.axhline(avg, linestyle = '--', label="Math avg", color='red')
plt.title("Study Title")
plt.xlabel("Day")
plt.ylabel("Hours")
plt.legend(loc='upper right')
plt.grid(color='gray', linestyle=':', linewidth=0.5)
plt.show()
