import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

hour = range(24)

viewers_hour = [30, 17, 34, 99, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

plt.title("Pizza orders")

plt.xlabel("pizzas")
plt.ylabel("number")

plt.plot(hour, viewers_hour)

plt.legend(['2024-06-30'])

ax = plt.subplot()

ax.set_facecolor('#FFE5B1')

ax.set_xticks(hour)
ax.set_yticks([0, 20, 40, 60, 80, 100, 120, 140])

y_upper = [i + (i*0.15) for i in viewers_hour]
y_lower = [i - (i*0.15) for i in viewers_hour]

plt.fill_between(hour, y_lower, y_upper, alpha=0.3)

# Add the code here:
plt.show()
