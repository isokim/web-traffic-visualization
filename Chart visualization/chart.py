import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['07/2019', '08/2019', '09/2019', '10/2019', '11/2019']
searches = [50, 53, 59, 56, 62]
direct = [39, 47, 42, 51, 51]
social = [70, 80, 90, 87, 92]

x = np.arange(len(months))
width = 0.25

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar(x - width, searches, width, label='Searches', color='cornflowerblue')
bars2 = ax.bar(x, direct, width, label='Direct', color='palevioletred')
bars3 = ax.bar(x + width, social, width, label='Social Media', color='gold')

# Axis labels and title
ax.set_ylabel('visitors\nin thousands')
ax.set_xlabel('months')
ax.set_title('Visitors by web traffic sources')
ax.set_xticks(x)
ax.set_xticklabels(months)

# Place legend at bottom
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)

# Annotate bar values
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

# Layout
plt.tight_layout()
plt.show()
