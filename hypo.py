import numpy as np

theta = np.zeros(2) # Initialize an array of 2 elements with value 0

def predict_price(theta, mileage):
	return theta[0] + theta[1] * mileage