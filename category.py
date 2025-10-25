# Create a Series, with default dtype
series1 = pd.Series(data=list_of_occupations)

# Print out the data type and number of bytes for series1
print("series1 data type:", series1.dtype)
print("series1 number of bytes:", series1.nbytes)

# Create a Series, "category" dtype
series2 = pd.Series(data=list_of_occupations, dtype='category')

# Print out the data type and number of bytes for series2
print("series2 data type:", series2.dtype)
print("series2 number of bytes:", series2.nbytes)

# Create a categorical Series and specify the categories (let pandas know the order matters!)
medals = pd.Categorical(medals_won, categories=['Bronze', 'Silver', 'Gold'], ordered=True)
print(medals)


# Create a dictionary with column names as keys and "category" as values
adult_dtypes = {
   "Workclass": "category",
   "Education": "category",
   "Relationship": "category",
   "Above/Below 50k": "category" 
}

# Read in the CSV using the dtypes parameter
adult2 = pd.read_csv(
  "adult.csv",
 dtype=adult_dtypes
)
print(adult2.dtypes)


## updating data and converting data to categorical data
# Create the update_coats dictionary
update_coats = {
    'wirehaired':'medium',
    'medium-long': 'medium'
}

# Create a new column, coat_collapsed
dogs["coat_collapsed"] = dogs['coat'].replace(update_coats)

# Convert the column to categorical
dogs['coat_collapsed'] = dogs['coat_collapsed'].astype('category')

# Print the frequency table
print(dogs['coat_collapsed'].value_counts())
