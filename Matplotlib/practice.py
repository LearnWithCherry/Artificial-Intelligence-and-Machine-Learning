import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5, 6]

python     = [5, 6, 7, 8, 9, 11]
javascript = [8, 9, 10, 10, 11, 13]
java       = [4, 3, 4, 3, 3, 3]

plt.stackplot(months, python, javascript, java)
plt.title("Language Popularity Over Time")
plt.xlabel("Month")
plt.ylabel("Usage")
plt.show()

plt.stackplot(months, python, javascript, java,
             labels=["Python", "JavaScript", "Java"],
             baseline="zero")    # default — stack from y=0 upward

plt.stackplot(months, python, javascript, java,
             labels=["Python", "JavaScript", "Java"],
             baseline="sym")     # symmetric — centered around 0

plt.stackplot(months, python, javascript, java,
             labels=["Python", "JavaScript", "Java"],
             baseline="wiggle")  # minimises slope — streamgraph style
