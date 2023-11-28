import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os

# Read the CSV file into a DataFrame
data = pd.read_csv('https://raw.githubusercontent.com/Sangeetha-007/DiwaliSales/main/Diwali%20Sales%20Data.csv', encoding='latin-1')

# Set the environment variable to restore or create the missing .shx file
os.environ['SHAPE_RESTORE_SHX'] = 'YES'

# Load the GeoJSON or Shapefile data using geopandas
map_data = gpd.read_file('/Users/Sangeetha/Downloads/archive (6)/Indian_States.dbf')  

#print(map_data)

#Merge CSV data with the geographical data
merged_data = map_data.merge(data, how='left', left_on='st_nm', right_on='State')


# Plot the choropleth map
merged_data.plot(column='State', cmap='Purples', linewidth=0.8, legend=True)
plt.title('Diwali Sales Per State')
plt.show()  # Display the map
