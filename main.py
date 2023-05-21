import numpy as np
import matplotlib.pyplot as plt

Math = [100, 90]
English = [90, 80]
Physics = [80, 80]
Computer = [80, 90]
x = np.arange(2) 
width = 0.15
labels = ['Math', 'English', 'Physics', 'Computer']
names = ['Bill', 'Mary']

# ******************************
# Make your code
# ******************************
fig, ax = plt.subplots()

bar1 = ax.bar(x - width/2, Math, width, label='Math')
bar2 = ax.bar(x + width/2, English, width, label='English')
bar3 = ax.bar(x + 3*width/2, Physics, width, label='Physics')
bar4 = ax.bar(x + 5*width/2, Computer, width, label='Computer')

ax.set_ylabel('Scores')
ax.set_title('Grouped graph for scores')
ax.bar_label(bar1, Math)
ax.bar_label(bar2, English)
ax.bar_label(bar3, Physics)
ax.bar_label(bar4, Computer)
ax.set_xticks(x + width)
ax.set_xticklabels(names)
ax.legend()


fig.savefig('A11.png')
