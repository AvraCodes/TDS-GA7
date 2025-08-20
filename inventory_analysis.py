# inventory_analysis.py
# Author: Jules
# Contact: 24f1002255@ds.study.iitm.ac.in
#
# This script analyzes the quarterly inventory turnover ratio,
# visualizes the data, and compares it against the industry benchmark.

import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
turnover_ratios = [5.71, 1.0, 6.2, 9.71]
industry_target = 8
average_turnover = np.mean(turnover_ratios)

# Create the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(quarters, turnover_ratios, color=['#76b7b2', '#e15759', '#59a14f', '#edc948'])

# Add the industry target line
plt.axhline(y=industry_target, color='r', linestyle='--', label=f'Industry Target: {industry_target}')

# Add the average line
plt.axhline(y=average_turnover, color='b', linestyle=':', label=f'Average: {average_turnover:.2f}')

# Add data labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.2f}', va='bottom', ha='center')

# Add titles and labels
plt.title('2024 Quarterly Inventory Turnover Ratio')
plt.xlabel('Quarter')
plt.ylabel('Turnover Ratio')
plt.legend()
plt.ylim(0, max(turnover_ratios + [industry_target]) * 1.2)

# Save the figure
plt.savefig('inventory_turnover_chart.png')

print("Chart saved as inventory_turnover_chart.png")
print(f"Average Turnover: {average_turnover:.2f}")
