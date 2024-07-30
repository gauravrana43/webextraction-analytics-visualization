import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('book_data.csv')

# Ensure 'book_price' and 'star_rating' are numeric
df['book_price'] = pd.to_numeric(df['book_price'], errors='coerce')
df['star_rating'] = pd.to_numeric(df['star_rating'], errors='coerce')

# Compute correlation matrix
corr_matrix = df[['book_price', 'star_rating']].corr()

# Create a heatmap of feature correlations
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Heatmap of Feature Correlations')
plt.show()

# Create a crosstab of category and star_rating
category_counts = pd.crosstab(df['category'], df['star_rating'])

# Create a heatmap of counts
plt.figure(figsize=(10, 8))
sns.heatmap(category_counts, annot=True, cmap='YlGnBu', fmt='d', linewidths=0.5)
plt.title('Heatmap of Category Counts by Star Rating')
plt.show()
