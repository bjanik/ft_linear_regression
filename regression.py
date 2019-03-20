import numpy as np
import pandas
import matplotlib.pyplot as plt

# from hypo import predict_price

def predict_price(mileage, theta):
	return theta[0] + theta[1] * mileage

def fit(X, y, theta, alpha, num_iters):
	m = len(X)
	for i in range(num_iters):
		sigma0 = sum(predict_price(X, theta) - y)
		sigma1 = sum((predict_price(X, theta) - y) * X)
		theta[0] = theta[0] - alpha * sigma0 / m
		theta[1] = theta[1] - alpha * sigma1 / m
		print(theta)
	return theta

def plot_regression(X, y, theta):
	plt.xlabel("mileage")
	plt.ylabel("price")
	plt.scatter(X, y, c='r', marker='o')
	plt.plot(X, predict_price(X, theta), c='g')
	plt.show()

# def cost(X, y, theta):
	# return sum((predict(X, theta) - y) ** 2) / (2 * len(X))


def main():
	data = pandas.read_csv("data.csv")
	theta = np.zeros(2)
	X = np.array(data['km'])
	y = np.array(data['price'])
	theta = np.zeros(2)
	theta = fit(X, y, theta, 0.0000000001, 500)
	print("Theta[0] is {} and theta[1] is {}".format(theta[0], theta[1]))
	plot_regression(X, y, theta)

if __name__ == "__main__":
	main()
