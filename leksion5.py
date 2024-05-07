import pandas as pd
import matplotlib.pyplot as plt



#Read the file with pandas into a dataframe called "df", and specify encoding style
df = pd.read_csv(r'recipeData.csv', encoding='latin-1')

#Print titles of the columns
print("Columns in DataFrame:", df.columns.tolist())

#Remove missing values, using .dropna
df = df.dropna()

#Plot numerical data
x = df['BeerID']  # Assuming BeerID is your x-axis
y = df['StyleID']  # Assuming StyleID is your y-axis

plt.figure(figsize=(10, 5))  # Set the figure size for better readability
plt.scatter(x, y, alpha=0.5)  # Create a scatter plot
plt.title('BeerID vs StyleID')  # Set a title for the plot
plt.xlabel('BeerID')  # Label x-axis
plt.ylabel('StyleID')  # Label y-axis
plt.grid(True)  # Enable grid for easier readability
plt.show()
