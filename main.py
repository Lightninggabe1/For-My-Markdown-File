import matplotlib.pyplot as plt
import os

# Data
categories = ['Codecademy', 'Nonsense', 'Games']
values = [13, 2, 4]

# Ensure the 'images' directory exists, or create it
output_dir = 'images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create figure with golden ratio cut in half (aspect ratio ~ 1:0.809)
plt.figure(figsize=(8, 6.47), facecolor='#2E2E2E')  # Golden ratio cut in half

# Create a bar chart with a single color for all bars
bars = plt.bar(categories, values, color='#4E73DF', width=0.4)  # Professional muted blue

# Set background color for the axes (lighter gray for contrast)
plt.gca().set_facecolor('#2A2A2A')  # Darker gray for the plot area

# Title font adjustments (centered and clean)
title_font = {'family': 'Arial', 'weight': 'bold', 'size': 18, 'color': 'white'}
plt.title('Different Categories of Repositories', **title_font, ha='center')

# Axis label font adjustments (clean and modern)
label_font = {'family': 'Calibri', 'weight': 'normal', 'size': 14, 'color': 'white'}
plt.xlabel('Categories', **label_font)
plt.ylabel('Number of Repositories', **label_font)

# Tick label font adjustments (subtle and clear)
tick_font = {'family': 'Arial', 'size': 12, 'color': 'white'}
plt.tick_params(axis='both', labelcolor='white', labelsize=12)

# Clean grid with minimal lines (only horizontal lines)
plt.grid(True, axis='y', linestyle='--', color='gray', alpha=0.3)  # Subtle horizontal grid lines
plt.gca().spines['top'].set_visible(False)  # Remove top spine
plt.gca().spines['right'].set_visible(False)  # Remove right spine

# Add data labels on top of the bars for clarity
data_label_font = {'family': 'Arial', 'weight': 'normal', 'size': 12, 'color': 'white'}
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 2), ha='center', **data_label_font)

# Save the plot as an image in the 'images' directory
plt.savefig(os.path.join(output_dir, 'graph.png'), bbox_inches='tight')

# Optionally display the plot
plt.show()
