# create_chart.py
#
# This script reads portfolio data from a CSV file and generates a
# Circle Packing chart to visualize the investment allocation.

import pandas as pd
import circlify
import matplotlib.pyplot as plt

# Read the data from the CSV file
try:
    df = pd.read_csv('portfolio.csv')
except FileNotFoundError:
    print("Error: portfolio.csv not found. Please make sure the CSV file is in the same directory.")
    exit()

# Prepare the data for circlify.
# We need a list of dictionaries with 'id', 'datum' (value), and 'children'.
# In this case, we have a two-level hierarchy: sectors and assets.
data = []
for sector, group in df.groupby('sector'):
    children = [
        {'id': row['asset'], 'datum': row['investment']}
        for index, row in group.iterrows()
    ]
    data.append({
        'id': sector,
        'datum': group['investment'].sum(),
        'children': children
    })

# Compute the circle packing layout.
# The `enclosure` function returns a list of circles, each with its x, y, and r.
circles = circlify.circlify(
    data,
    show_enclosure=True,
    target_enclosure=circlify.Circle(x=0, y=0, r=1)
)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_title('Investment Portfolio Allocation')
ax.axis('off')

# Find the enclosing circle for normalization
lim = max(
    max(
        abs(c.x) + c.r,
        abs(c.y) + c.r,
    )
    for c in circles
)
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)

# Plot the circles
for circle in circles:
    if circle.ex is None:
        continue
    if circle.level == 1:  # Sector level
        x, y, r = circle.x, circle.y, circle.r
        ax.add_patch(plt.Circle((x, y), r, alpha=0.2, linewidth=2, facecolor="gray", edgecolor="black"))
    elif circle.level == 2:  # Asset level
        x, y, r = circle.x, circle.y, circle.r
        ax.add_patch(plt.Circle((x, y), r, alpha=0.7, linewidth=2, edgecolor="black"))
        plt.annotate(
            f"{circle.ex['id']}\\n${circle.ex['datum']/1e6:.1f}M",
            (x, y),
            va='center',
            ha='center',
            fontsize=8,
            color="black"
        )

# Add sector labels
for circle in circles:
    if circle.ex is None:
        continue
    if circle.level == 1:
        x, y, r = circle.x, circle.y, circle.r
        plt.annotate(
            circle.ex['id'],
            (x, y + r * 0.8),
            va='center',
            ha='center',
            fontsize=12,
            fontweight='bold',
            color="black"
        )

plt.savefig('chart.png', dpi=72, bbox_inches='tight')
print("Chart saved as chart.png")
