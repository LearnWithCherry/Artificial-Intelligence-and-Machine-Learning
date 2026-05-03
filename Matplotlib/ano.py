import matplotlib.pyplot as plt
x    = [5, 7, 8, 2, 9]
y    = [99, 86, 87, 60, 103]
plt.scatter(x, y)

plt.annotate("Outlier",           # text label
             xy=(9, 103),          # point to annotate
             xytext=(7, 108),       # where to place text
             arrowprops=dict(
                 arrowstyle="->",
                 color="red"
             ),
             fontsize=10,
             color="red")
plt.show()