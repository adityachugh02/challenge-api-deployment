import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.datasets import make_regression

def predict(preprocessed_data):

	df = pd.read_csv('predict/dataset-cleaned.csv')

	column_names = {

	"area": "surface",
    "property_type": "proprety_type",
    "rooms_number": "bedrooms",
    "zip_code": "commune_code",
    "land_area": "surface_plot",
    "garden": "garden",
    "garden_area": "garden_area",
    "equipped_kitchen": "equipped_kitchen",
    "swimming_pool": "swimming_pool",
    "furnished": "furnished",
    "open_fire": "open_fire",
    "terrace": "terrace",
    "terrace_area": "terrace_area",
    "facades_number": "facades",
    "building_state": "state"

	}



	for elem in column_names:
		if elem not in preprocessed_data:
			df = df.drop(columns=[column_names[elem]])

	df = df.drop(columns=['locality'])

	X = np.array(df.drop(columns=['price']))
	y = np.array(df['price']).reshape(-1, 1)

	inverted_column_names = {v: k for k, v in column_names.items()}

	available_data = []

	for elem in df.drop(columns=['price']):
		available_data.append(preprocessed_data[inverted_column_names[elem]])

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
	regressor = LinearRegression()
	regressor.fit(X_train, y_train)
	#print(regressor.score(X_train, y_train))
	#print(regressor.score(X_test, y_test))

	available_data = np.array(available_data).reshape(1, -1)

	return float(regressor.predict(available_data)), float(mean_squared_error(y_train, regressor.predict(X_train)))
	