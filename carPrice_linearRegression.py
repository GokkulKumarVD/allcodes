import pandas as pd
import numpy as np
# Import Linear Regression machine learning library
from sklearn.linear_model import LinearRegression
car_df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data",names = ['symboling','normalized_losses','make','fuel_type','aspiration','num_of_doors','body_style','drive_wheels','engine_location','wheel_base','length','width','height','curb_weight','engine_type','num_of_cylinders','engine_size','fuel_system','bore','stroke','compression_ratio','horsepower','peak_rpm','city_mpg','highway_mpg','price'])

car_df.head(2).transpose()

car_df = car_df.drop('make', axis=1)  # dropping make here but in real project, may separate data based on make.
#The different makes in same data set may not be a good idea

# dropping following columns due to low variance filter. i.e an attribute which is mostly one type of data is not a good dimension
car_df = car_df.drop('fuel_type', axis=1)
car_df = car_df.drop('engine_location', axis=1)
car_df = car_df.drop('num_of_doors', axis=1)
car_df = car_df.drop('body_style' , axis=1)
car_df = car_df.drop('drive_wheels', axis=1)
car_df = car_df.drop('engine_type', axis=1) # need more info on this column
car_df = car_df.drop('fuel_system', axis=1)
car_df = car_df.drop('aspiration', axis=1)
car_df = car_df.drop('normalized_losses', axis=1)

# Replace the string numbers into numerical values for number of cylinders
car_df['cylinder'] = car_df['num_of_cylinders'].replace({'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five':5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12})


car_df = car_df.replace('?', np.nan)  #replace ? with NA which is equivalent of NULL
#car_df[car_df.isnull().any(axis=1)]  # display records with 'NA'

# Change the attribute types from object to float type (generic numeric types)
car_df['bore'] = car_df['bore'].astype('float64')
car_df['stroke']= car_df['stroke'].astype('float64')
car_df['horsepower']= car_df['horsepower'].astype('float64')
car_df['peak_rpm']= car_df['peak_rpm'].astype('float64')
car_df['price'] = car_df['price'].astype('float64')
#car_df['cylinder']= car_df['cylinder'].astype('int64')  # not required
#car_df['normalized_losses']= car_df['normalized_losses'].astype('float64')

# fill up NaN in numeric columns with median values of those columns respectively
car_df['price'] = car_df['price'].fillna(car_df['price'].median())
car_df['bore']= car_df['bore'].fillna(car_df['bore'].median())
car_df['horsepower'] = car_df['horsepower'].fillna(car_df['horsepower'].median())
car_df['peak_rpm'] = car_df['peak_rpm'].fillna(car_df['peak_rpm'].median())
car_df['stroke'] = car_df['stroke'].fillna(car_df['stroke'].median())
car_df['cylinder'] = car_df['cylinder'].fillna(car_df['cylinder'].median())


# Look at the distribution of data on the various attributes. Look for outliers....

car_df.describe().transpose()

#importing seaborn for statistical plots
import seaborn as sns
car_df_attr = car_df.iloc[:,1:16]

sns.pairplot(car_df_attr, diag_kind = 'kde')

# Copy all the predictor variables into X dataframe. Since 'mpg' is dependent variable drop it
X = car_df.drop('price', axis=1)
X = X.drop('num_of_cylinders', axis=1)# Removing this column as we have created another column "cylinder" out of this

# Copy the 'mpg' column alone into the y dataframe. This is the dependent variable
y = car_df[['price']]

#Let us break the X and y dataframes into training set and test set. For this we will use
#Sklearn package's data splitting function which is based on random function

from sklearn.model_selection import train_test_split

# Split X and y into training and test set in 75:25 ratio

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

# invoke the LinearRegression function and find the bestfit model on training data
regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

