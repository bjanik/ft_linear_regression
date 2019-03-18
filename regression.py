import numpy as np
import pandas

def predict(mileage, theta):
	return theta[0] + theta[1] * mileage

def fit(X, y, theta, alpha, num_iters):
	m = len(X)
	for i in range(num_iters):
		sigma0 = sum(predict(X, theta) - y)
		sigma1 = sum((predict(X, theta) - y) * X)
		# print(sigma0, sigma1)
		theta[0] = theta[0] - alpha * sigma0 / m
		theta[1] = theta[1] - alpha * sigma1 / m
		# print(theta)
	return theta

def cost(X, y, theta):
	return sum((predict(X, theta) - y) ** 2) / (2 * len(X))

# data = pandas.read_csv("ex1data1.csv")
data = pandas.read_csv("data.csv")
# data.plot.scatter('km', 'price')
theta = np.zeros(2)
# X = np.array(data['population'])
# y = np.array(data['profit'])
X = np.array(data['km'])
y = np.array(data['price'])
# print(predict(X[0], theta) - y[0])
theta[0] = 0
theta[1] = 0
theta = fit(X, y, theta, 0.0000000001, 7500)
print(theta)
print(predict(120000, theta))
# print(data)