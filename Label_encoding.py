# Convert to categorical and print the frequency table
used_cars["color"] = used_cars["color"].astype("category")
print(used_cars["color"].value_counts())

# Create a label encoding
used_cars["color_code"] = used_cars["color"].cat.codes

# Create codes and categories objects
codes = used_cars["color"].cat.codes
categories = used_cars["color"]
color_map = dict(zip(codes, categories))

# Print the map
print(used_cars['color'].map(color_map))


#REVERTING TO PREVIOUS VALUES USING THE MAP FN
# Update the color column using the color_map
used_cars_updated["color"] = used_cars_updated['color'].map(color_map)
# Update the engine fuel column using the fuel_map
used_cars_updated["engine_fuel"] = used_cars_updated['engine_fuel'].map(fuel_map)
# Update the transmission column using the transmission_map
used_cars_updated["transmission"] = used_cars_updated['transmission'].map(transmission_map)

# Print the info statement
print(used_cars_updated.info())



# Print the "manufacturer_name" frequency table.
print(used_cars["manufacturer_name"].value_counts())

# Create a Boolean column for the most common manufacturer name
used_cars["is_volkswagen"] = np.where(
  used_cars["manufacturer_name"].str.contains("Volkswagen", regex=False), 1, 0
)
  
# Check the final frequency table
print(used_cars['is_volkswagen'].value_counts())
