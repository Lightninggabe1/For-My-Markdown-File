import matplotlib.pyplot as plt

# Data
categories = ['Codecademy', 'Nonsense', 'Games']
values = [13, 2, 4]

# Create the bar chart
plt.bar(categories, values, color=['blue', 'red', 'green'])

# Adding title and labels
plt.title('Length of Categories')
plt.xlabel('Category')
plt.ylabel('Length')

# Save the plot as an image
plt.savefig('graph.png')

# Display the plot (optional)
plt.show()
