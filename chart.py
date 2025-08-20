import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic data for customer spending behavior
np.random.seed(42)
data = {
    'Segment': np.random.choice(['New', 'Regular', 'VIP'], 500),
    'Spending': np.random.normal(100, 40, 500)
}
df = pd.DataFrame(data)

# Adjust spending based on segment
df.loc[df['Segment'] == 'New', 'Spending'] *= 0.5
df.loc[df['Segment'] == 'Regular', 'Spending'] *= 1.0
df.loc[df['Segment'] == 'VIP', 'Spending'] *= 1.5
df['Spending'] = df['Spending'].clip(lower=5)

# Set professional styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Create the boxplot
plt.figure(figsize=(8, 8))
sns.boxplot(x='Segment', y='Spending', data=df, palette='viridis', order=['New', 'Regular', 'VIP'])

# Add titles and labels for clarity
plt.title('Customer Spending by Segment', fontsize=20)
plt.xlabel('Customer Segment', fontsize=16)
plt.ylabel('Spending ($)', fontsize=16)

# Adjust layout to prevent labels from being cut off
plt.tight_layout()

# Save the chart with specified dimensions
plt.savefig('chart.png', dpi=64)

# Optional: Display the plot if running locally
# plt.show()
